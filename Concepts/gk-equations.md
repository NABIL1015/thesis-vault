---
title: G-K equations and variables
tags: [reference, concept]
aliases: ["goman khrabrov equations", "GK equations", "tau1 tau2 equations"]
---

# Goman-Khrabrov: every equation with τ₁ or τ₂, and what the symbols mean

Source: Goman & Khrabrov, *J. Aircraft* 31(5), 1994, pp. 1109-1115.
Equation numbers below are the paper's own.

---

## Part A — The variables

### The state variable

**x** — position of the separation point (airfoil) or the vortex
breakdown point (delta wing), measured along the surface.

Range is 0 to 1, and it is **already dimensionless** — it is a fraction
of the chord, not a distance in metres. So it needs no further
normalising.

- x = 1 → fully attached, separation sits at the trailing edge
- x = 0 → fully separated, separation has run to the leading edge

**x₀(α)** — the value x would settle to if you held α fixed and waited.
A whole curve, one value for each α, not a single number. Obtained from
static measurements, not from theory.

### The inputs

**α** — angle of attack, in radians for the equations (degrees only for
plotting).

**α̇** — pitch rate, radians per second.

**q** — pitch rate as a body rate. For pure pitching, q = α̇.

**β, β̇** — sideslip angle and its rate. Delta-wing roll section only.
Ignore for your work.

### The parameters being fitted

**τ₁** — relaxation time, in seconds. How fast x chases x₀.

**τ₂** — delay time, in seconds. Shifts the *argument* of x₀.

**τ₃** — a third time constant, appearing only in the roll-oscillation
equations (Eq. 9, 10) as the sideslip analogue of τ₂. Not relevant to
you.

### Lengths and speeds used for normalising

**c̄** — mean aerodynamic chord (airfoil sections).
**c** — root chord (delta wing sections).
**b** — semispan (roll sections).
**V** — freestream speed.

**c/V** — the convective time: how long air takes to cross one chord.
≈ 0.026 s for your rig (c = 0.348 m, V ≈ 13.2 m/s).

---

## Part B — Every equation containing τ₁ or τ₂

### Eq. 3 — the core equation (airfoil)

$$\tau_1 \frac{dx}{dt} + x = x_0(\alpha - \tau_2\dot{\alpha})$$

This is the one that matters. Everything else in the paper is this
equation rearranged, linearised, or applied to a different shape.

Read as: the separation point chases its steady value, with lag τ₁, and
the thing it chases is evaluated at a shifted angle.

Rearranged to show the chase more plainly:

$$\frac{dx}{dt} = \frac{x_0(\alpha - \tau_2\dot{\alpha}) - x}{\tau_1}$$

Rate of chase = gap ÷ τ₁. Bigger gap, faster chase. Bigger τ₁, slower
chase.

### Eq. 4 — linearised for small sinusoidal oscillations (airfoil)

Two expressions, for the in-phase and out-of-phase parts of the lift
response at oscillation frequency ω:

$$C_{L_\alpha}^{fo} = \frac{\pi}{2}\cos\alpha\left[1+\sqrt{x_0}\right]^2 + \frac{\pi}{2}\sin\alpha\,\frac{1+\sqrt{x_0}}{\sqrt{x_0}}\,\frac{dx_0}{d\alpha}\,\frac{1-\omega^2\tau_1\tau_2}{1+\omega^2\tau_1^2}$$

$$C_{L_{\dot\alpha}}^{fo} = -\frac{\pi}{2}\sin\alpha\,\frac{1+\sqrt{x_0}}{\sqrt{x_0}}\,\frac{dx_0}{d\alpha}\,\frac{\tau_1+\tau_2}{1+\omega^2\tau_1^2}$$

**This is the closest equation in the paper to your experiment**, since
your data is sinusoidal pitching. Three things worth noticing:

1. τ₁ appears as the group **ωτ₁** — frequency times relaxation time.
   That product is what actually controls the behaviour, not τ₁ alone.
2. In the first expression the two times appear as a **product** τ₁τ₂;
   in the second as a **sum** τ₁+τ₂.
3. Both expressions carry the factor dx₀/dα. Where the static curve is
   flat, that derivative is zero and the whole unsteady effect vanishes.
   **The lag only exists where the separation point is actually moving.**

### The ξ equations — small deviation from steady (delta wing, p.1112)

Defining ξ = x(t) − x₀[α(t)], the gap between where the separation
point is and where it wants to be:

$$\tau_1\frac{d\xi}{dt} + \xi = -(\tau_1+\tau_2)\frac{dx_0}{d\alpha}\dot{\alpha}$$

This is the cleanest statement of the lag idea in the whole paper: the
gap itself obeys a first-order equation, and it is **driven by α̇**.
Stop pitching and the forcing disappears and the gap decays to zero.

### Eq. 6 — delta wing longitudinal

$$\tau_1\frac{dx}{dt} + x = x_0(\alpha - \tau_2\dot{\alpha})$$

Identical in form to Eq. 3 — that is the paper's central claim, that the
same lag equation describes two quite different flows. Paired with a
different lift expression (Eq. 5, the Polhamus vortex analogy) rather
than Kirchhoff.

### Eq. 7 — transfer-function form (delta wing)

$$C_L = C_L^{st}(\alpha) + K(\alpha)\frac{s\alpha}{\tau_1 s + 1} + \text{(attached-flow terms)}$$

where s is the Laplace variable and the gain is

$$K(\alpha) = -(\tau_1+\tau_2)\frac{\partial C_L}{\partial x}\frac{dx_0}{d\alpha}$$

**Note carefully:** in K(α), τ₁ and τ₂ appear *only as their sum*. If
you fit using this form alone, you cannot separate them — only τ₁+τ₂ is
determined. τ₁ is separately visible only through the (τ₁s + 1)
denominator. This is a direct clue about why τ₁ and τ₂ are hard to pin
down independently.

### Eq. 8 — harmonic oscillation derivatives (delta wing)

$$C_{L_\alpha}^{fo} = C_{L_\alpha}^{st} + K(\alpha)\frac{\omega^2\tau_1}{1+\omega^2\tau_1^2}$$

$$C_{L_{\dot\alpha}}^{fo} = C_{L_{\dot\alpha}}^{att} + C_{L_\alpha}^{att} + \frac{K(\alpha)}{1+\omega^2\tau_1^2}$$

Again everything runs through **ωτ₁**. This is what G-K fitted against
data at three different frequencies to extract τ₁ ≈ 15 c/V.

### Eq. 9, 10 — roll oscillations (delta wing)

$$\tau_1\frac{dx_{l}}{dt} + x_{l} = x_0 + K_\beta(\beta - \tau_3\dot{\beta})$$
$$\tau_1\frac{dx_{r}}{dt} + x_{r} = x_0 - K_\beta(\beta - \tau_3\dot{\beta})$$

$$\tau_1\frac{dC_l^{vor}}{dt} + C_l^{vor} = 2\frac{dC_l^{vor}}{dx}K_\beta(\beta-\tau_3\dot{\beta})$$

Left and right vortices tracked separately. Not relevant to a 2D
airfoil, but note the same τ₁ is reused — the paper's argument that one
relaxation process governs everything.

### Eq. 12 — roll damping fit

$$(C_{l_p} + C_{l_\beta}\sin\alpha)^{fo} = \text{(attached terms)} + \frac{K_p(\alpha)}{1+\omega^2\tau_1^2}$$

The same ωτ₁ group once more.

### Eq. 13 — full aircraft

$$\tau_1\frac{dx}{dt} + x = x_0(\alpha - \tau_2\dot{\alpha}), \qquad |x| \le 1$$

Eq. 3 again, now with x as an abstract internal variable with no
physical meaning attached.

---

## Part C — Nondimensionalisation, summarised

### What is already dimensionless

| Quantity | Why |
|---|---|
| x, x₀ | fraction of chord by construction |
| C_L, C_m, C_d | forces/moments already normalised |
| α, β | angles (radians) |
| k, St | dimensionless by definition |

### What carries units, and how it gets normalised

| Quantity | Units | Normalised form |
|---|---|---|
| τ₁, τ₂ | seconds | τ₁ / (c/V) → "τ₁ = 0.52 c/V" |
| α̇ | rad/s | α̇c/V |
| q | rad/s | qc/V |
| ω | rad/s | ωc/V (or ωb/V for roll) |
| t | seconds | tV/c |

### The dimensionless groups that actually matter

**ωτ₁** — oscillation frequency times relaxation time. This single
product controls all the frequency dependence in Eqs. 4, 7, 8, 12. It
answers: is the flow fast enough to keep up with the motion?

- ωτ₁ ≪ 1 → flow keeps up, quasi-steady, little hysteresis
- ωτ₁ ≈ 1 → maximum lag effect
- ωτ₁ ≫ 1 → flow cannot respond at all, frozen

**τ₂α̇** — has units of angle (seconds × rad/s = rad). Good sanity
check: it must, since it is subtracted from α.

**τ₁ + τ₂** — appears as a pair in the gain K(α). The combination that
is easiest to identify from data.

---

## Part D — The values G-K report

| Case | τ₁ | τ₂ | Method |
|---|---|---|---|
| NACA 0015 airfoil | 0.52 c̄/V | 4.5 c̄/V | ramp motions, least squares |
| Delta wing A=1.5 | 1.5 c/V | 0.5 c/V | water tunnel, flow visualisation |
| Delta wing A=1.5, pitch | ≈15 c/V | — | wind tunnel, forced oscillation |
| Delta wing A=1.5, roll | ≈15 c/V | — | wind tunnel, forced oscillation |

**The unexplained gap:** same delta wing, same physical process, 1.5 c/V
from visualisation versus 15 c/V from forced oscillation — a factor of
ten. The paper states plainly that this cannot be explained from the
available data.

**For your rig** (c/V ≈ 0.026 s), the airfoil values become
τ₁ ≈ 0.014 s, τ₂ ≈ 0.12 s. Compare Ayancik & Mulleners' τ₁ = 4.24 c/V
≈ 0.11 s.

---

## Part E — The short version

- **τ₁ is in every dynamic equation.** It is the one universal parameter.
- **τ₂ only ever appears multiplied by α̇** (or β̇ as τ₃). It exists only
  when the airfoil is moving; it vanishes identically in static tests.
- **Frequency enters only through ωτ₁.** Nothing else.
- **τ₁ and τ₂ often appear only as a sum**, which is why separating them
  from data is hard.
- **Everything is switched off by dx₀/dα.** Where the static separation
  curve is flat, there is no unsteady effect at all. All the action is
  in the stall region where x₀ is changing fast.


---

## Related

- [[Home]] — thesis home
- [[gomanStatespaceRepresentationAerodynamic1994]] — source paper
- [[glossary]] — plain-language definitions
- [[tau_1]] — the disputed relaxation time
- [[tau_2]] — the delay time
- [[Separation point X]] — what x means physically
- [[Kirchhoff relation]] — how x becomes lift
