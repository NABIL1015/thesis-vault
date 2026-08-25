---
title: Kirchhoff relation
tags: [concept]
aliases: ["Kirchhoff", "kirchoff", "Kirchhoff lift"]
---

# The Kirchhoff relation

Back to [[00-Concepts]].

## The idea

Model the separated region as a pocket of constant pressure sitting on
the upper surface, from the separation point back to the trailing edge.
Ahead of it, flow behaves normally and makes lift. Behind it, almost
none. Solve that idealised problem and lift comes out as the attached
value times a single shrinking factor depending only on X:

$$C_l = 2\pi \sin\alpha \left(\frac{1+\sqrt{X}}{2}\right)^2$$

## Sanity check at the ends

- X = 1 (attached): factor is 1, recovers ordinary thin-airfoil lift
- X = 0 (fully separated): factor is 1/4, **not zero** — a stalled
  airfoil still carries about a quarter of its attached lift, which is
  roughly what real stalled airfoils do

## The important part: you invert it

You never guess X0(alpha). You take the **measured static lift curve**
and ask, at each angle: what X would Kirchhoff need to produce the lift
actually measured?

$$X_0(\alpha) = \left(2\sqrt{\frac{C_l^{static}(\alpha)}{2\pi\sin\alpha}} - 1\right)^2$$

Feed in the static polar, get out X0 against angle. It is data, not a
fitted function. **This is why G-K has only two free parameters**
([[tau_1]] and [[tau_2]]) instead of two plus an unknown curve.

## The blocker

This requires a **static polar** — and one per blowing level, because
blowing is precisely what moves the static separation point.

**Blowing enters G-K through X0, not through the differential
equation.** That is the architectural insight that makes G-K suitable
here.

Candidate sources: datasets [[99900]] (baseline, various Re) and
[[99901]] (steady blowing, 300k, several Cmu levels), both quasi-steady
pitch, -2 to 32 degrees.
