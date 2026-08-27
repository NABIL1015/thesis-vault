---
title: Reading - Goman-Khrabrov 1994
tags: [reading-note, concept]
aliases: ["reading goman", "GK reading notes", "goman khrabrov reading"]
source: "[[gomanStatespaceRepresentationAerodynamic1994]]"
progress: "airfoil section complete, through Eq. 4"
---

# Reading notes: Goman & Khrabrov 1994

Running summary. Source: [[gomanStatespaceRepresentationAerodynamic1994]].
Equations collected separately in [[gk-equations]].
Limitations collected separately in [[G-K limitations]].

---

## Triage: what to actually read

The paper is about **fighter aircraft** at high angles of attack. Most of
it is not your problem.

| Pages | Content | Relevant? |
|---|---|---|
| 1109-1110 | Introduction, the state-space idea | Yes, briefly |
| 1110-1111 | **Airfoil with trailing-edge separation** | **This is your section** |
| 1111-1113 | Slender delta wing, vortex breakdown | No |
| 1113-1114 | Full aircraft | No |
| 1115 | Concluding remarks | Yes — admits limitations |

You are reading roughly two pages, not seven.

**Warning:** the tau_1 of about 15 c/V in the delta-wing section is a
**vortex breakdown** number, not an airfoil number. Do not cite it as
one. See [[tau_1]].

---

## Note on the letter x

The paper uses lowercase **x** for the separation point throughout. It
never means a graph coordinate. In these notes the separation point is
written **X** to avoid the clash.

---

## Block 1 — The architecture (Eq. 1)

$$\frac{dx}{dt} = f(x, h) \qquad C = g(x, h)$$

- **h** — what you do to the system (angle of attack, pitch rate,
  control deflections)
- **C** — what you measure (forces and moments)
- **X** — an internal variable describing what the flow is doing

First line: X evolves in time by some rule. Second line: forces follow
from X and h together.

**Why bother with X.** At high angles the flow has memory — convection
lags, boundary-layer adjustment, separation developing and recovering.
Forces depend on the motion *and* on where separation currently is. So
you cannot get forces from the motion alone. Something must carry the
history. X is it.

They are explicit that X can be physically real or purely formal. For the
airfoil it is real. For the full aircraft they admit it becomes abstract.

---

## Block 2 — The airfoil, and what X means

### Scope they claim

- Trailing-edge separation
- No spilled vortex effects
- Valid for "relatively slow" changes in incidence
- Airfoil thick enough for separation to develop near the trailing edge

**How your case fits.** NACA 0018 is thick, fine. But your motion is not
slow and deep dynamic stall involves a spilled vortex. You are applying
the model outside its stated comfort zone. See [[G-K limitations]].

### The definition

X runs 0 to 1, giving separation point position on the upper surface.

- **X = 1** — attached, separation at the trailing edge
- **X = 0** — leading-edge separation, whole upper surface separated

X is a fraction of chord measuring how much of the upper surface still
has flow stuck to it. Bigger X, healthier flow.

They claim X is the variable "on which aerodynamic loads depend
essentially" — one number carrying all the memory that matters.

**That is the bet the whole model rests on.**

See [[Separation point X]].

---

## Block 3 — Eq. 2, turning X into lift

$$C_L(\alpha, X) = \frac{\pi}{2}\sin\alpha\left(1+\sqrt{X}\right)^2$$

From assuming the separated region is a pocket of constant pressure
(Kirchhoff).

| X | factor | result |
|---|---|---|
| 1 (attached) | (1+1)² = 4 | C_L = 2π sin α — thin-airfoil theory |
| 0 (separated) | (1+0)² = 1 | C_L = (π/2) sin α — a quarter of attached |

Not zero at full separation, which is correct: a stalled airfoil still
carries some lift.

So: **attached-flow lift times a factor shrinking from 1 to a quarter.**

A moment expression is given alongside, referenced to the **airfoil
nose** (not quarter chord — see [[G-K limitations]]). Fit lift first.

### The key structural point

Eq. 2 has **no time in it**. Instantaneous: give me X now, I give you
lift now. All time dependence lives in Eq. 3. That separation is what
makes the model tractable.

### The inversion — why this matters most

You have a measured steady lift curve. Solve Eq. 2 for X and recover
X_0(alpha) from data:

$$X_0(\alpha) = \left(2\sqrt{\frac{C_L^{static}(\alpha)}{2\pi\sin\alpha}} - 1\right)^2$$

This is why the model has **only two unknowns** ([[tau_1]], [[tau_2]])
instead of two plus an unknown curve. See [[Kirchhoff relation]].

---

## Block 4 — Eq. 3, the actual model

$$\tau_1 \frac{dX}{dt} + X = X_0(\alpha - \tau_2\dot{\alpha})$$

Built from **two separate physical claims**, not pulled out of the air.

### Claim 1 — quasi-steady effects, giving tau_2

Circulation lag, boundary-layer convection lag, boundary-layer
improvement. These influence *when* separation happens and recovers.
Their argument: the delay is roughly proportional to alpha-dot. So they
shift the argument — the flow reacts to (alpha − tau_2 · alpha-dot).

They call tau_2 "the total time delay of the above mentioned effects."
**Plural.** It is a lumped parameter from the start.

### Claim 2 — transient adjustment, giving tau_1

Separate idea. Disturb the separated flow and leave the angle alone, and
it still relaxes back toward steady state. A process in its own right,
independent of motion. Simplest description of a relaxation is a
first-order ODE. That is the tau_1 term.

### So the two constants are not two knobs on one effect

They come from different physical stories and enter differently:
tau_1 multiplies the derivative on the left, tau_2 shifts the argument on
the right.

### What the equation says

The separation point is always being pulled toward a target. The left
side is the pull. The right side is the target — and it is not where the
current angle says, it is offset by the pitch rate.

### "Closed"

Eqs. 2 and 3 together "form the closed mathematical model." Closed means
complete — nothing else needed. They add explicitly that spilled vortex
and wake vortex sheet effects are neglected.

The count: **two unknown parameters plus one unknown function X_0(alpha)**,
all from steady and unsteady experimental data. That sentence is your
fitting plan, written in 1994.

---

## Block 5 — Fig. 1, the equation as a picture

The best thing in the paper. Two stacked panels sharing a common
horizontal axis: **angle of attack**.

### Upper panel — the fan

A fan of dotted lines spreading from the origin. Each line is Eq. 2 at
one **fixed** X: top line X = 1, bottom line X = 0, others between.
Since Eq. 2 is sin(alpha) times a constant, each is nearly straight.

The real static lift curve is drawn over the fan and **crosses** it. At
low angles it rides the X = 1 line. As angle rises and separation creeps
forward, it slides down through X = 0.8, 0.6, and lower.

**The static lift curve is a trajectory across the fan.** That is what
X_0(alpha) means geometrically.

### Lower panel — the S-curve

X_0(alpha) directly: flat near 1 at low angles, dropping steeply through
stall, flat near 0 after. The steep middle is where all the action is.

### Connecting the panels

Dashed lines are ramp motions.

- **Pitching up**: X sits *above* the steady curve. Separation has not
  run forward yet, so flow is still attached at an angle where statically
  it would not be. Upper panel: riding a higher fan line than you should
  be, so lift **overshoots**.
- **Pitching down**: X sits *below*. Separation lingers, slow to clear.
  Lower fan line, so lift **undershoots**.

That is dynamic stall in one mechanism. It is also hysteresis: at the
same angle, upstroke and downstroke sit on different fan lines.

### A practical detail worth keeping

The fan lines are packed close near X = 1 and spread far apart near
X = 0. Going from X = 1 to 0.8 barely moves the lift; going from 0.2 to
0 moves it a lot.

**Lift is most sensitive to X when the flow is already badly separated.**
So errors in X_0 at low angles cost little; errors in the stall region
cost a great deal.

---

## Block 6 — Fig. 2 and the fitted numbers

Data is not theirs — from Jumper, Schreck & Dimmick (1987), NACA 0015
pitching at constant rate.

**The experiment:** ramp motions. Pitch up at steady rate, once, low to
high angle. Four different pitch rates. Crosses are measurements, solid
lines the model fit.

**What it shows:** faster ramp, further the lift climbs before collapsing
and the higher the peak. That spread is the stall delay — exactly what
tau_2 produces.

**Fitted by least squares:**

$$\tau_1 \approx 0.52\,(c/V), \qquad \tau_2 \approx 4.5\,(c/V)$$

### tau_2 is nearly nine times tau_1 here

The delay dominates the relaxation — the opposite of the common
assumption that slow relaxation is the main effect.

**Why they add up.** In a ramp, two effects push X away from the static
curve. The tau_2 effect shifts the target. The tau_1 effect means X
cannot even reach that shifted target, adding roughly tau_1 · alpha-dot
more. Total offset is proportional to **(tau_1 + tau_2)**.

Visible directly in the paper: the xi equation on p.1112 and the gain
K(alpha) in Eq. 7 both carry (tau_1 + tau_2). **The sum is what the data
sees.**

### But tau_1 does something tau_2 cannot

tau_2 is a static shift — give me alpha-dot now, I give you the shift
now. No memory. tau_1 governs *how fast the system responds to change* —
a dynamic property.

This is why frequency enters only through **omega·tau_1** and never
through tau_2.

**tau_2 dominates the size of the offset. tau_1 owns the timing.**

### A likely explanation for the tau_1 disagreement

A ramp is slow and one-directional. It barely exercises the dynamic
behaviour tau_1 controls. So a ramp fit mostly sees the sum and can
hardly separate the two.

G-K's tau_1 = 0.52 c/V may therefore be **poorly constrained by that
experiment** — not wrong, just barely tested. Ayancik & Mulleners
extracted tau_1 from post-stall vortex shedding, a genuinely dynamic
process that actually depends on it.

Treat as a reasonable inference, not a settled conclusion. But it points
the same way as the loop-width argument. See [[tau_1]].

### Relevance to your data

This is a **ramp** fit: one-directional, constant rate. Your data is
sinusoidal, continuously reversing, fixed frequency.

In a ramp, alpha-dot is constant so the tau_2 shift is a fixed offset
throughout. In your case alpha-dot varies through the cycle — largest at
mid-points, zero at turnarounds. So tau_2 produces a *varying* shift and
the model gets tested in a way ramps never test it.

---

## Block 7 — Eq. 4, the oscillatory branch

They switch to small-amplitude sinusoidal oscillation and linearise.
**This is the branch structurally closest to your experiment.**

Output: two expressions, one for the in-phase part of the lift response,
one for the out-of-phase part.

- **In phase** — the piece moving in step with the angle, peaking when
  alpha peaks.
- **Out of phase** — a quarter-cycle offset, peaking when alpha-dot
  peaks.

Any sinusoidal response splits into these two. Together they give the
size and the timing of the response.

### Three things to take from Eq. 4

**1. Frequency enters only as omega·tau_1.** Both expressions have
(1 + omega²·tau_1²) in the denominator. Nothing else depends on
frequency. That single product decides everything.

**2. The two constants appear differently.** In-phase carries the
*product* tau_1·tau_2. Out-of-phase carries the *sum* tau_1 + tau_2. So
with measurements at several frequencies you can pull them apart — a sum
and a product together determine both. That is the identification route
the paper points at.

**3. Everything is gated by dX_0/d(alpha).** That derivative multiplies
the unsteady terms in both expressions. G-K say it outright: unsteady
effects depend strongly on frequency only where separation is developing,
where dX_0/d(alpha) is not zero.

**Where the static separation curve is flat, there is no unsteady effect
at all.** At low angles X_0 is pinned near 1 and barely changes, so the
derivative is zero, so no lag, no hysteresis. All the interesting
behaviour lives in the steep middle of the S-curve.

### Two practical consequences

You need X_0 accurately **in the stall region**. Elsewhere it barely
matters. That sharpens what you need from the static polar.

The identification logic needs **multiple frequencies**. Your data is at
one k per dataset. Across datasets you have several (0.041, 0.06, 0.074,
0.082, 0.09) but at different amplitudes and mean angles, so not a clean
frequency sweep. See [[Clock model trap]].

---

## Where we are

**The airfoil section is complete.** Everything after Eq. 4 in the paper
is delta wings (pp. 1111-1113) and full aircraft (pp. 1113-1114), neither
of which applies to a 2D airfoil.

Worth still reading: the **concluding remarks** (p. 1115), where they
admit what the model cannot do. Those are collected in
[[G-K limitations]].
