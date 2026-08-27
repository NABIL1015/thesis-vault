---
title: G-K limitations
tags: [concept, limitation, thesis-material]
aliases: ["GK limitations", "limitations of goman khrabrov", "model assumptions"]
---

# Limitations of the Goman-Khrabrov model

Back to [[00-Concepts]]. Source: [[gomanStatespaceRepresentationAerodynamic1994]].

**This note is thesis material.** It is the "assumptions and validity"
section, and the honest answer to "why not just apply G-K directly."

Three groups below: what the paper states outright, what it concedes in
the concluding remarks, and what is missing for this particular
application.

---

## A. Stated outright in the paper

### A1. No spilled vortex

Twice stated. When setting up the airfoil model they specify flow
"without spilled vortex effects," and after Eq. 3 they repeat that
spilled vortex and wake vortex sheet effects are neglected.

**Why it is structural, not a footnote.** The leading-edge vortex is a
*travelling* low-pressure structure moving along the chord with its own
dynamics. A single number "where is the separation point" cannot
represent something moving across the surface. The model excludes it **by
construction**, not by choice of parameters.

**Consequence for you:** your data is deep dynamic stall, where the LEV
is the dominant event. G-K will capture the lag and the hysteresis. It
will **not** reproduce the sharp lift overshoot as the vortex passes, nor
the fluctuations after it sheds.

### A2. Slow variations of incidence only

They state the model is valid "for relatively slow variations of the
airfoil incidence."

**Consequence:** your reduced frequencies (0.041 to 0.09) with 7 to 10
degree amplitudes are not slow. You are outside the stated range.

### A3. Trailing-edge separation only

The airfoil must be "of sufficient thickness for the development of flow
separation in the vicinity of the trailing edge."

**Consequence:** NACA 0018 is thick, so this one is satisfied — but only
at moderate angles. Once leading-edge separation takes over, the premise
fails. Also noted in the wider literature: G-K is stated not to apply to
flat-plate leading-edge stall.

### A4. Kirchhoff is a steady result used in unsteady flow

Eq. 2 was "obtained for quasisteady flow conditions." It contains no
time. The model assumes the *instantaneous* relationship between X and
lift is the same as the steady one, and puts all the unsteadiness into X.

**This is an assumption, not a derivation.** It could fail if the
pressure distribution over a separated region behaves differently when
the flow is moving.

### A5. Kirchhoff's own assumptions

The separated zone is modelled as a region of **constant pressure**, plus
the standard assumption of linear cavitation theory. Real separated flow
is neither uniform in pressure nor steady.

### A6. Moment is referenced to the airfoil nose

Their moment expression is taken about the nose. **Your data is about the
quarter chord** (pitch axis at 25% chord).

**Consequence:** a coordinate transfer is required before comparing
moments. One more reason to fit lift first.

### A7. First order, so one relaxation process

Eq. 3 is first order. That encodes exactly one relaxation timescale.
Real separated flow has several — boundary layer, shear layer, vortex
formation, wake — on different timescales.

**Consequence:** a first-order model cannot reproduce post-stall
vortex-shedding fluctuations. Confirmed by later work benchmarking G-K on
this same NACA 0018.

---

## B. Conceded in the concluding remarks (p. 1115)

The last page is unusually candid. Four admissions:

### B1. The right-hand side is a simplification

They say Eq. 3's right side "can be written in a more general form"
X_0(alpha, alpha-dot, q, ...). So X_0(alpha − tau_2·alpha-dot) is itself
a convenient reduction, not the general case.

### B2. Static hysteresis needs a different equation

"When the aerodynamic hysteresis occurs," Eq. 3 must be rewritten
nonlinearly as X-dot = F(X, alpha, alpha-dot, q, ...), giving **bistable
solutions** for the internal variable.

**Directly relevant.** A thick airfoil like the NACA 0018 shows static
hysteresis around 16 to 22 degrees. Your mean angle is 18 degrees, so
you are sitting in that band. This is the gap
[[williamsModelingLiftHysteresis2016]] exists to fill, with separate X_0
branches for pitch-up and pitch-down.

### B3. Higher order may be needed

"The order of the differential operator can be increased to describe more
complex flow adjustment processes." An acknowledgement that one
timescale may not be enough.

### B4. Identification methods are immature

They close by saying use of the model "is closely related to the problem
of the identification of its structure and evaluation of unknown
parameters," and that "special efforts are needed to develop the adequate
methods."

That is the authors saying, in 1994, that they do not have a reliable way
to get tau_1 and tau_2 out of data.

### B5. Their own unexplained discrepancy

For the same delta wing they obtained tau_1 of about 1.5 c/V from water
tunnel visualisation and about 15 c/V from wind tunnel forced
oscillation — a factor of ten — and state that it "cannot be explained on
the basis of the available experimental information."

**Take this seriously.** It is direct evidence that tau_1 is weakly
identifiable. See [[tau_1]].

---

## C. Missing for this thesis specifically

These are gaps between the 1994 model and what this project needs. None
is a flaw in the paper — it simply was not written for this.

### C1. There is no actuation input at all

The model has alpha as its only input. **Cmu has nowhere to enter.**

The resolution: blowing enters through **X_0, not through the ODE** —
steady blowing changes where the flow separates statically, so it changes
the target curve, leaving tau_1 and tau_2 as flow properties.

This is the route taken in [[williamsFeedForwardDynamicStall2018]], which
makes X_0 a function of Cmu. See [[Kirchhoff relation]].

### C2. A static polar is needed per Cmu level

Follows directly from C1. Inverting Kirchhoff requires measured static
lift **at each blowing level**.

**Status: open blocker.** Candidate sources are [[99900]] (baseline,
various Re) and [[99901]] (steady blowing at 300k, several Cmu levels),
both quasi-steady pitch from -2 to 32 degrees.

### C3. Steady blowing only, but the target is pulsed

The model would be trained entirely on **constant** Cmu. The thesis
targets pulsed blowing in the Strouhal band 0.07 to 0.16.

If the flow's response lags a *changing* Cmu, a model trained on constant
Cmu has never seen that lag and cannot represent it. That would need an
additional actuation state.

**State this as a limitation.** The adaptive-blowing datasets ([[99940]],
[[99950]], [[99952]], [[99964]], [[99966]]) are the natural test.

### C4. Single frequency per dataset

Eq. 4's identification logic needs several frequencies. Each dataset has
one k. Across datasets several exist, but at different amplitudes and
mean angles — not a clean sweep. See [[Clock model trap]].

### C5. tau_1 and tau_2 are hard to separate

Structural, not a data problem: in the gain K(alpha) the two appear only
as the **sum**. A fit can trade one against the other with little change
in result.

**Practical approach:** fix tau_1 at a defensible physical value, fit
tau_2, then check whether moving tau_1 by plus or minus 30 percent
changes anything. If not, report tau_1 as assumed rather than measured.

---

## D. Summary table for the thesis

| Limitation | Source | Severity here | Mitigation |
|---|---|---|---|
| No spilled vortex / LEV | Stated | **High** — LEV dominates your case | State as limitation; blowing suppresses the vortex |
| Slow motion only | Stated | Medium | Outside stated range; later papers do the same |
| Trailing-edge separation only | Stated | Medium | Fails once LE separation takes over |
| Kirchhoff used unsteadily | Stated | Low-medium | Standard practice |
| Moment about the nose | Stated | Low | Coordinate transfer; fit lift first |
| First order, one timescale | Structural | Medium | Cannot capture post-stall fluctuations |
| Static hysteresis unmodelled | Conceded | **High** — NACA 0018, 16-22 deg | Williams 2017 dual-branch X_0 |
| Identification unreliable | Conceded | **High** | Fix tau_1, test sensitivity |
| No Cmu input | Gap | **High** | X_0 as a function of Cmu (Williams 2019) |
| Static polar per Cmu needed | Gap | **Blocker** | Extract from 99900 / 99901 |
| Steady blowing only | Gap | **High** for the endgame | Extra actuation state; test on adaptive datasets |
| Single k per dataset | Gap | Medium | Cross-k validation |

---

## E. The honest framing

G-K is not being used because it is correct for deep dynamic stall on a
blown airfoil. It is being used because:

1. It introduces the hidden state that the data demonstrably requires
2. It has **two** physically meaningful parameters instead of twenty
   meaningless ones, so bad fits are detectable by inspection
3. Blowing has a natural place to enter, through X_0
4. There is direct precedent on **this exact rig**
   ([[williamsFeedForwardDynamicStall2018]])

The limitations above are the price. Stating them plainly is stronger
than pretending they are not there — and several of them (the LEV, the
pulsed-blowing gap) are natural "further work" material.
