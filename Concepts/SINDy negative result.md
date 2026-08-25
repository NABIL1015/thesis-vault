---
title: SINDy negative result
tags: [concept, result, negative-result]
aliases: ["SINDy", "Cindy", "sindy failure"]
---

# SINDy: the negative result

Back to [[00-Concepts]].

**Status: closed. Do not reopen.** This is a proven structural result,
not a preference or a tuning failure.

## What was attempted

Sparse Identification of Nonlinear Dynamics. Write down a long menu of
candidate terms, fit coefficients by least squares, then repeatedly
delete small coefficients and refit until only a few survive.

Setup: 1260 data points, seven runs fitted **jointly** (see
[[Joint fitting constraint]]), all variables centred, derivatives by
Fourier spectral differentiation at 25 harmonics (0.08 to 0.26 percent
error).

## The result

| degree | terms | condition no. | err dCl | err dCm |
|---|---|---|---|---|
| 2 | 21 | 1.4e6 | **59.2 %** | 72.4 % |
| 3 | 56 | 1.8e8 | 38.7 % | 36.7 % |
| 4 | 126 | 1.8e12 | 20.4 % | 19.1 % |

Error spread evenly across runs (48-74 %), so not one bad run. Degree 4
is memorisation, not modelling.

**Marching the fitted model forward** through one cycle from the true
initial condition, with alpha and Cmu fed in as known: the model tracked
for about 20 degrees, missed the stall entirely, and ended the cycle
predicting **Cl = -0.17** where the measurement was 1.404.

Negative lift at 16 degrees positive incidence is physically impossible.

Note that marching compounds error in a way one-step-ahead statistics
hide — and marching is what a controller needs.

## Why it failed

**The [[Collision test]] predicted this beforehand.** (Cl, Cm) is not a
valid state: the trajectory revisits itself at phi = 78 and phi = 94
while dCl/dt differs by +9.09 versus -9.54.

If the state does not determine the future, no function of that state
can predict the future.

## What it implies

Not a data problem. Not data-starved either — 1260 points against 21
unknowns. The deficiency is **structural**.

More Cmu levels would not have helped. Different *kinds* of data would:
per-port Cp, other k values, adaptive-blowing runs.

This is why the move to G-K, which introduces [[Separation point X]] as
the missing hidden state.

## For the thesis

Write this up honestly as a negative result. It is a real finding with a
clean diagnosis, and it motivates the model choice that follows.
