---
title: Glossary
tags: [reference]
---

# Glossary

Everything defined in plain words. No entry uses a term that isn't
defined somewhere else in this file.

---

## 1. The physical setup

**Airfoil** — the cross-section shape of a wing. If you sliced a wing
and looked at the cut face, that shape is the airfoil.

**NACA 0018** — the specific airfoil shape used in your experiments.
The name is a code: the "00" means symmetric (top and bottom are mirror
images), the "18" means its thickest point is 18% of its length. A
fairly thick airfoil.

**Chord (c)** — the length of the airfoil from front to back. Yours is
0.348 metres.

**Span (s)** — how wide the wing is, side to side. Yours is 0.610 metres.

**Leading edge** — the front of the airfoil, the part that meets the air
first.

**Trailing edge** — the back, where the air leaves.

**Angle of attack (α, "alpha")** — the angle between the airfoil and the
oncoming air. Tilt the wing nose-up and alpha increases. Measured in
degrees.

**Pitching** — rotating the airfoil so that alpha changes over time. Your
experiments pitch the airfoil back and forth continuously.

**Freestream velocity (U∞, "U infinity")** — the speed of the air coming
at the airfoil, far enough upstream that the airfoil hasn't disturbed it
yet. Around 13 m/s in your runs.

**Pressure port (or tap)** — a small hole in the airfoil surface
connected to a pressure sensor. Your model has 40 of them along the
mid-span.

---

## 2. The forces

**Lift** — the force pushing the wing perpendicular to the oncoming air.
The useful one. This is what keeps aircraft up.

**Drag** — the force pushing the wing backwards, along the flow. The
wasteful one.

**Moment** — a twisting force. Tends to rotate the airfoil nose-up or
nose-down.

**Coefficient** — a version of a force with the size and speed divided
out, so you can compare a small slow wing to a big fast one directly.
Dimensionless (no units).

**Cl** — lift coefficient. The main quantity you measure and model.

**Cm** — moment coefficient.

**Cd** — drag coefficient.

---

## 3. How the flow behaves

**Attached flow** — the air follows the curve of the airfoil surface
smoothly, all the way to the trailing edge. This is the well-behaved
case and it produces good lift.

**Separation** — the air stops following the surface and peels away,
leaving a churning, low-pressure region behind. Lift drops.

**Separation point** — the exact location along the airfoil where the
air peels off. It moves depending on conditions. This is the single
most important idea in your whole project.

**Stall** — what happens when separation becomes severe enough that lift
collapses. Happens when alpha gets too large.

**Static stall** — stall measured while holding the airfoil still (or
moving it very slowly) at each angle.

**Dynamic stall** — stall while the airfoil is pitching rapidly. Behaves
very differently from static stall: lift can climb far higher before
collapsing, then collapse harder. This is your thesis topic.

**Hysteresis** — when the answer depends on which direction you came
from. Pitching up through 20 degrees gives a different lift than pitching
down through 20 degrees, even though alpha is identical. Plotted, this
makes a loop rather than a line.

**Leading-edge vortex (LEV)**, also called the **dynamic stall vortex
(DSV)** — a large spinning mass of air that forms near the leading edge
during dynamic stall, travels backwards along the airfoil, and then
sheds off. While it sits on the wing it generates a lot of extra lift;
when it leaves, lift collapses.

---

## 4. Numbers that describe the experiment

**Reynolds number (Re)** — a single number summarising how fast and how
big the flow is, relative to the stickiness of air. Two experiments with
the same Re behave similarly even at different scales. Yours is 300,000,
usually written 300k.

**Reduced frequency (k)** — how fast the airfoil is pitching, compared
with how fast air travels past it. Small k means slow pitching (the flow
has time to keep up); large k means fast pitching (the flow lags
behind). Defined as k = πfc/U∞. Yours are mostly 0.06 to 0.09.

**Strouhal number (St)** — another dimensionless frequency, similar in
spirit to k, more commonly used when talking about vortex shedding and
pulsed actuation. Your target band for pulsed blowing is St = 0.07 to
0.16.

**Phase angle (φ, "phi")** — where you are in one pitching cycle,
measured 0 to 360 degrees. φ = 0 at the start, 360 back at the start
again. Your data has 180 points per cycle, one every 2 degrees.

**Period (T)** — the time for one complete pitching cycle. 0.900 seconds
in dataset 99924.

**Phase averaging** — running the experiment for hundreds of cycles and
averaging all the cycles together, point by point, to cancel out random
noise. Your data has already had this done, over at least 300 cycles.

---

## 5. Flow control (the thing you're trying to do)

**Flow control** — deliberately interfering with the air to change how
it behaves. Here, the goal is to stop or soften dynamic stall.

**Blowing** — injecting a jet of air through a narrow slot in the
airfoil surface, to re-energise the flow and delay separation.

**Slot** — the opening the air comes out of. Yours is at 5% chord, near
the leading edge.

**Momentum coefficient (Cμ, "C mu")** — how strong the blowing is,
expressed as a dimensionless number. Cμ = 0 means no blowing. Your
datasets go up to about 6 or 7%.

**Steady blowing** — the jet is on constantly at a fixed strength for a
whole run. This is what most of your data uses.

**Pulsed / modulated blowing** — the jet is switched on and off, or
varied in strength, over time. This is what your thesis is ultimately
aiming at.

**Adaptive blowing** — the jet strength is adjusted based on what the
flow is doing. Some of your datasets (99940, 99950, 99952, 99964,
99966) use this.

---

## 6. Modelling words

**Model** — here, a set of equations that predicts what the lift will do,
given the angle of attack and the blowing. Not a physical model.

**Differential equation (ODE)** — an equation that relates a quantity to
its own rate of change. Instead of saying "the lift is 1.4," it says
"the lift is changing at this rate, right now." Give it a starting value
and let it run forward, and you get the whole curve.

**Rate of change** — how fast something is changing per second. Written
with a dot on top: α̇ ("alpha dot") is the rate of change of alpha.

**State** — the minimum set of numbers you need to know *right now* in
order to predict what happens next. If two moments have the same state,
they must have the same future. This is the concept that killed the
SINDy attempt.

**State variable** — one of those numbers.

**Hidden (or internal) state** — a state variable that matters but that
you cannot measure directly. The separation point is one of these: it
governs the lift, but no sensor in your rig reports it.

**Forcing** — something imposed on the system from outside that you
don't control as part of the model. Alpha is forcing: the rig dictates
it, on a fixed schedule.

**Input** — something you *do* control and can change. Cμ is the input.

---

## 7. The Goman-Khrabrov model specifically

**Goman-Khrabrov (G-K)** — the 1994 model you're adopting. Its core idea:
introduce one hidden state variable representing the separation point,
give it its own differential equation, and compute lift from it.

**X** — the G-K hidden state variable. A number between 0 and 1 giving
where the separation point sits. X = 1 means fully attached (separation
right at the trailing edge). X = 0 means fully separated (separation
right at the leading edge).

**X₀(α)** ("X nought of alpha") — where X would settle if you held the
airfoil still at angle alpha and waited. The steady, no-rush value. Note
this is a whole curve, one X₀ for every alpha, not a single number.

**τ₁ (tau one)** — the relaxation time. How long the flow takes to
settle towards X₀ after being disturbed. Measured in seconds, though
usually quoted in units of c/V (see below).

**τ₂ (tau two)** — the delay time. Accounts for the flow reacting to
where alpha *was* a moment ago rather than where it is now.

**c/V** (or c/U∞) — the "convective time," how long a parcel of air
takes to travel one chord length. About 0.026 seconds for your rig.
Time constants are often quoted as multiples of this, so "τ₁ = 4.24 c/V"
means 4.24 × 0.026 ≈ 0.11 seconds.

**Kirchhoff relation** — an old, simple theory that gives lift directly
from the separation point position: Cl = 2π·sin(α)·((1+√X)/2)². Its use
here is *backwards*: you take measured static lift and invert this
formula to work out X₀(α).

**Static polar** — a plot of lift coefficient against angle of attack,
measured slowly (quasi-statically). Needed to get X₀(α). Datasets 99900
and 99901 are your static polars.

---

## 8. Fitting words

**Fitting** — finding the parameter values (here τ₁ and τ₂) that make
the model's prediction match the measured data as closely as possible.

**Parameter** — a constant in the model whose value you don't know in
advance and have to determine from data.

**Least squares** — the standard way of measuring "how badly does the
model match?": square all the errors and add them up. Fitting means
making that total as small as possible.

**Optimiser** — the algorithm that hunts for the best parameter values.
It tries a guess, checks the error, adjusts, repeats.

**Initial guess (or seed)** — the starting values you hand the optimiser
before it begins hunting. A bad seed can send it somewhere useless,
which is why the τ₁ disagreement in the literature matters.

**Forward integration (or marching)** — starting from a known initial
condition and stepping the differential equation forward in time to
produce a whole predicted curve. This is how you test a G-K fit.

**Held-out validation** — fit the model using six of your seven runs,
then predict the seventh and compare against the real measurement. Since
the model never saw that run, this is an honest test.

**Identifiability** — whether the data actually pins down a parameter.
A parameter is weakly identifiable if wildly different values give
almost equally good fits. τ₁ appears to be weakly identifiable.

**SINDy** — Sparse Identification of Nonlinear Dynamics. The method you
tried first and abandoned. It attempts to discover the governing
equation from data by testing a long menu of candidate terms. It failed
here because Cl and Cm alone are not a valid state.

---

## 9. Control words (for later)

**Controller** — a system that decides what the blowing should do,
moment to moment.

**Open-loop** — the controller follows a pre-planned schedule and
ignores what's actually happening.

**Closed-loop** — the controller measures what's happening and adjusts
in response.

**Feedback** — reacting to what has already happened (the lift dropped,
so blow harder).

**Feedforward** — acting in advance based on what you know is coming
(the airfoil is about to reach a dangerous angle, so start blowing now).

**Hybrid feedforward/feedback** — using both together. This is your
thesis target.

**Plant** — control-engineering jargon for "the thing being controlled."
Here, the airfoil and its flow.

---

## 10. Notation cheat-sheet

| Symbol | Say it | Means |
|---|---|---|
| α | alpha | angle of attack |
| α̇ | alpha dot | rate of change of alpha |
| φ | phi | phase angle within the cycle |
| τ₁, τ₂ | tau one, tau two | the two G-K time constants |
| Cμ | C mu | blowing strength |
| U∞ | U infinity | freestream air speed |
| c | — | chord length |
| k | — | reduced frequency |
| X | — | G-K separation point state |
| X₀ | X nought | steady-state value of X |
| subscript 0 | nought | "the steady value of" |
| dot on top | dot | "rate of change of" |
