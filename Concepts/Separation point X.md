---
title: Separation point X
tags: [concept]
aliases: ["X", "separation point", "internal state variable"]
---

# The separation point X

Back to [[00-Concepts]].

## The idea

Air flowing over an airfoil follows the surface for a while, then peels
away. The place where it peels away is the **separation point**. X is
its position, expressed as a fraction of the chord.

- X = 1 → fully attached, separation at the trailing edge
- X = 0 → fully separated, separation at the leading edge

X is already dimensionless. It needs no normalising.

## Why it matters

X is the **hidden state** — the thing that determines lift but that no
sensor in the rig reports. Your data contains Cl and Cm, not X.

This is exactly what was missing when SINDy failed. See
[[Collision test]] and [[SINDy negative result]].

## How it behaves

X does not jump instantly to where it should be. It chases, with a lag
set by [[tau_1]]. The equation is Eq. 3 in
[[gomanStatespaceRepresentationAerodynamic1994]]:

$$\tau_1 \frac{dX}{dt} + X = X_0(\alpha - \tau_2\dot{\alpha})$$

Because alpha is always moving in your experiment, X never arrives. It
spends the whole cycle trailing behind, and **that permanent lag is the
phenomenon** — it is why lift differs between upstroke and downstroke at
the same angle.

## The gap does not accumulate

The chase rate is proportional to the current gap, so a bigger gap means
a stronger pull. Self-correcting. After a cycle or two the motion locks
into a repeating pattern — which is why phase averaging over 300 cycles
works, and why the lab discards the first two cycles.

The gap is constant **from cycle to cycle**, but varies **within** a
cycle: largest where pitching is fastest, smallest at the turnaround
points.

## Getting X0

X0 is not guessed — it is obtained by inverting measured static lift.
See [[Kirchhoff relation]].
