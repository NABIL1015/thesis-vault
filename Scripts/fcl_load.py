"""
fcl_load.py  --  loader for the FlowControlLab (Technion) measurement files.

File format
-----------
Line 1 : title / metadata,  e.g.
         "measurement #3956,  dynamic pitch,  k=0.09,  Re=300000,  AoA=18deg+7deg*sin(phi)"
Line 2 : column header,  tab separated,  e.g.
         "time_[s]  phase_angle_[deg]  AoA_[deg]  U_infty_[m/s]  q_[Pa]  Cl  Cd  Cm  Cmu_[%]"
Line 3+: numeric data, tab separated.
Line endings are Windows (CRLF).

The loader does NOT assume a fixed column set.  It reads whatever the header
line says, so the same code works for the dynamic-pitch files (99920/99922/
99924/...) and for the quasi-steady polars (99900/99901) even though those have
different columns.

Typical use
-----------
    from fcl_load import load_run, load_dataset

    run = load_run("~/thesis/FCL_pressure_data/99924/data_#3956.txt")
    print(run)                      # summary
    print(run.meta["k"], run.cmu)   # 0.09, 1.43
    a, cl = run["aoa"], run["cl"]

    runs = load_dataset("~/thesis/FCL_pressure_data/99924")   # all files, sorted by Cmu
    for r in runs:
        print(r.name, r.cmu, r.n)

Only numpy is required.
"""

from __future__ import annotations

import os
import re
import glob
import numpy as np

__all__ = ["Run", "load_run", "load_dataset", "spectral_derivative"]

DATA_ROOT = os.path.expanduser("~/thesis/FCL_pressure_data")


# --------------------------------------------------------------------------
# column-name handling
# --------------------------------------------------------------------------

_UNIT_RE = re.compile(r"_?\[(.*?)\]\s*$")

# canonical short names for the columns we actually use by name
_ALIASES = {
    "time": "time",
    "phase_angle": "phase",
    "phase": "phase",
    "aoa": "aoa",
    "alpha": "aoa",
    "u_infty": "u",
    "u": "u",
    "q": "q",
    "cl": "cl",
    "cd": "cd",
    "cm": "cm",
    "cmu": "cmu",
}


def _clean_column(raw: str):
    """'AoA_[deg]' -> ('aoa', 'deg').  Unknown names pass through lower-cased."""
    raw = raw.strip()
    unit = None
    m = _UNIT_RE.search(raw)
    if m:
        unit = m.group(1)
        raw = _UNIT_RE.sub("", raw)
    key = raw.strip().strip("_").lower()
    key = _ALIASES.get(key, key)
    return key, unit


# --------------------------------------------------------------------------
# title-line handling
# --------------------------------------------------------------------------

def _parse_title(line: str) -> dict:
    """
    Pull key=value pairs out of the title line and keep the rest as free tags.
    Numeric values are converted to float where possible.
    """
    meta = {"title": line.strip(), "tags": []}
    for field in line.split(","):
        field = field.strip()
        if not field:
            continue
        if "=" in field:
            key, val = field.split("=", 1)
            key, val = key.strip(), val.strip()
            # strip a trailing unit word like 'deg' from a bare number
            m = re.fullmatch(r"([-+0-9.eE]+)\s*([A-Za-z%]*)", val)
            if m:
                try:
                    meta[key] = float(m.group(1))
                    if m.group(2):
                        meta[key + "_unit"] = m.group(2)
                    continue
                except ValueError:
                    pass
            meta[key] = val
        else:
            m = re.fullmatch(r"measurement\s*#?\s*(\d+)", field, re.I)
            if m:
                meta["measurement"] = int(m.group(1))
            else:
                meta["tags"].append(field)
    return meta


# --------------------------------------------------------------------------
# the Run container
# --------------------------------------------------------------------------

class Run:
    """One measurement file: metadata plus columns as 1-D numpy arrays."""

    def __init__(self, path, meta, columns, units, order):
        self.path = path
        self.name = os.path.basename(path)
        self.meta = meta
        self.cols = columns          # dict: name -> np.ndarray
        self.units = units           # dict: name -> unit string or None
        self.order = order           # column names in file order

    # ---- access -----------------------------------------------------------
    def __getitem__(self, key):
        return self.cols[key]

    def __contains__(self, key):
        return key in self.cols

    def get(self, key, default=None):
        return self.cols.get(key, default)

    def __len__(self):
        return self.n

    @property
    def n(self):
        return len(next(iter(self.cols.values())))

    def array(self, *names):
        """Stack several columns into an (n, len(names)) array."""
        return np.column_stack([self.cols[nm] for nm in names])

    # ---- convenience ------------------------------------------------------
    @property
    def cmu(self):
        """Nominal momentum coefficient in percent (mean of the Cmu column)."""
        if "cmu" in self.cols:
            return float(np.mean(self.cols["cmu"]))
        return self.meta.get("Cmu", np.nan)

    @property
    def k(self):
        return self.meta.get("k", np.nan)

    @property
    def re(self):
        return self.meta.get("Re", np.nan)

    @property
    def period(self):
        """Cycle period T in seconds, from the phase column if present."""
        if "time" not in self.cols or "phase" not in self.cols:
            return np.nan
        t, ph = self.cols["time"], self.cols["phase"]
        dphi = float(np.mean(np.diff(ph)))
        dt = float(np.mean(np.diff(t)))
        return 360.0 * dt / dphi

    @property
    def is_periodic(self):
        """True if the phase column covers one full cycle at uniform spacing."""
        if "phase" not in self.cols:
            return False
        ph = self.cols["phase"]
        d = np.diff(ph)
        return bool(np.all(d > 0) and np.ptp(d) < 1e-6 * max(1.0, np.mean(d)) + 1e-3
                    and abs(ph[-1] - ph[0] + d.mean() - 360.0) < 1.0)

    def alpha_dot(self, n_harmonics=25):
        """d(AoA)/dt in deg/s, spectrally for periodic runs."""
        if not self.is_periodic:
            raise ValueError(f"{self.name}: not a full uniform cycle; "
                             "use np.gradient instead")
        return spectral_derivative(self.cols["aoa"], self.period, n_harmonics)

    def ddt(self, name, n_harmonics=25):
        """Spectral time derivative of any column, per second."""
        return spectral_derivative(self.cols[name], self.period, n_harmonics)

    def __repr__(self):
        bits = [f"Run({self.name}", f"n={self.n}"]
        if "measurement" in self.meta:
            bits.append(f"#{self.meta['measurement']}")
        if not np.isnan(self.k):
            bits.append(f"k={self.k:g}")
        if not np.isnan(self.re):
            bits.append(f"Re={self.re:g}")
        c = self.cmu
        if c == c:  # not nan
            bits.append(f"Cmu={c:.3f}%")
        bits.append("cols=" + ",".join(self.order))
        return ", ".join(bits) + ")"


# --------------------------------------------------------------------------
# readers
# --------------------------------------------------------------------------

def load_run(path) -> Run:
    """Read one measurement file."""
    path = os.path.expanduser(path)
    # newline='' + utf-8-sig: handles CRLF and a possible BOM without fuss
    with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
        lines = fh.read().replace("\r\n", "\n").replace("\r", "\n").split("\n")

    lines = [ln for ln in lines if ln.strip() != ""]
    if len(lines) < 3:
        raise ValueError(f"{path}: fewer than 3 non-empty lines")

    meta = _parse_title(lines[0])
    raw_header = lines[1].split("\t")
    order, units = [], {}
    for raw in raw_header:
        key, unit = _clean_column(raw)
        order.append(key)
        units[key] = unit

    ncol = len(order)
    rows = []
    for i, ln in enumerate(lines[2:], start=3):
        parts = ln.split("\t")
        if len(parts) != ncol:
            raise ValueError(f"{path}: line {i} has {len(parts)} fields, "
                             f"expected {ncol}")
        try:
            rows.append([float(p) for p in parts])
        except ValueError as e:
            raise ValueError(f"{path}: line {i} is not numeric: {e}") from None

    data = np.asarray(rows, dtype=float)
    columns = {name: np.ascontiguousarray(data[:, j]) for j, name in enumerate(order)}
    meta["n_rows"] = data.shape[0]
    return Run(path, meta, columns, units, order)


def load_dataset(folder, pattern="*.txt", sort_by="cmu"):
    """
    Read every measurement file in a dataset folder.

    folder may be a full path or just the dataset number, e.g. "99924",
    in which case DATA_ROOT is prepended.
    Returns a list of Run objects, sorted by `sort_by` ('cmu', 'k', 'name', None).
    """
    folder = str(folder)
    path = os.path.expanduser(folder)
    if not os.path.isdir(path):
        path = os.path.join(DATA_ROOT, folder)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"no such dataset folder: {folder}")

    files = sorted(glob.glob(os.path.join(path, pattern)))
    if not files:
        raise FileNotFoundError(f"no files matching {pattern} in {path}")

    runs = [load_run(f) for f in files]
    if sort_by == "cmu":
        runs.sort(key=lambda r: (np.nan_to_num(r.cmu, nan=1e9), r.name))
    elif sort_by == "k":
        runs.sort(key=lambda r: (np.nan_to_num(r.k, nan=1e9), r.name))
    elif sort_by == "name":
        runs.sort(key=lambda r: r.name)
    return runs


# --------------------------------------------------------------------------
# spectral derivative (exact for one clean period of a periodic signal)
# --------------------------------------------------------------------------

def spectral_derivative(y, period, n_harmonics=25):
    """
    Time derivative of a periodic signal sampled uniformly over exactly one
    period, obtained by differentiating its truncated Fourier series.

    y            : array of length n, one full cycle, uniform spacing
    period       : cycle duration T in the same time units you want per-unit
    n_harmonics  : harmonics retained; the rest are discarded as noise
    """
    y = np.asarray(y, dtype=float)
    n = y.size
    Y = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(n, d=period / n)      # cycles per unit time
    keep = np.arange(Y.size) <= n_harmonics
    Yd = Y * (2j * np.pi * freqs) * keep
    return np.fft.irfft(Yd, n=n)


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    targets = sys.argv[1:] or [os.path.join(DATA_ROOT, "99924")]
    for tgt in targets:
        tgt = os.path.expanduser(tgt)
        runs = [load_run(tgt)] if os.path.isfile(tgt) else load_dataset(tgt)
        for r in runs:
            print(r)
            if r.is_periodic and "aoa" in r:
                T = r.period
                ad = r.alpha_dot()
                # analytic check for a pure sinusoid: amplitude * 2*pi/T
                amp = 0.5 * np.ptp(r["aoa"])
                print(f"   T = {T:.4f} s   "
                      f"max|alpha_dot| = {np.abs(ad).max():.2f} deg/s   "
                      f"analytic = {amp * 2 * np.pi / T:.2f} deg/s")
