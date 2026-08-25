---
title: Collision test
tags: [concept, method]
aliases: ["collision test", "state validity check"]
---

# The collision test

Back to [[00-Concepts]].

## What it checks

Whether a proposed set of variables is a **valid state** — that is,
whether knowing them is enough to determine what happens next.

The rule: if two moments have the same state, they must have the same
future. If they don't, the state is incomplete and no model built on it
can work.

## How to run it

Go through the trajectory. Find pairs of moments where the candidate
state variables are nearly identical. Then compare what happens next at
each. If the futures diverge, the state is invalid.

## The result on this data

Testing (Cl, Cm) as a state:

At phi = 78 degrees and phi = 94 degrees, the trajectory passes within
**1.2 percent of its own range** of itself — essentially the same point.
But dCl/dt is **+9.09 at one and -9.54 at the other**.

Same lift, same moment, opposite futures.

| candidate state | worst future disagreement |
|---|---|
| (Cl, Cm) | 41 % of range |
| (Cl, Cm, dCl/dt) | 2.7 % |
| (Cl, Cm, dCl/dt, dCm/dt) | 2.7 % |

## Why this matters

**The collision test predicted the SINDy failure before it happened.**
If the state does not determine the future, no function of that state
can predict the future — regardless of how clever the fitting method is.

This should be the **first check before any new model attempt**.

G-K resolves the problem by introducing [[Separation point X]] as a
hidden variable. What distinguishes phi = 78 from phi = 94 is where the
separation point is — invisible in Cl and Cm, but real.

See [[SINDy negative result]].
