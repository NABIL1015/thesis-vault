---
title: tau_1
tags: [parameter, open-question]
aliases: ["tau1", "tau one", "relaxation time"]
status: unresolved
---

# tau_1 — the relaxation time

Back to [[Home]].

## What it is

How fast the separation point chases its steady value. Appears in every
dynamic equation in G-K. See [[gk-equations]] and [[Separation point X]].

Units: seconds. Usually quoted as a multiple of c/V, the convective
time. For this rig c/V is about 0.026 s.

## Why it is unresolved

Published values disagree. This matters because tau_1 is a **seed** for
the optimiser — a bad starting guess can send a nonlinear fit somewhere
useless.

| Source | Value | In seconds here | Method |
|---|---|---|---|
| G-K 1994, NACA 0015 | 0.52 c/V | 0.014 s | ramp motion |
| G-K 1994, delta wing | 1.5 c/V | 0.039 s | water tunnel visualisation |
| G-K 1994, delta wing | 15 c/V | 0.39 s | forced oscillation |
| Ayancik & Mulleners | 4.24 c/V | 0.11 s | post-stall vortex formation |

## What the disagreement actually is

The apparent eightfold gap partly dissolves on inspection. The 15 c/V
figure is a **delta wing vortex breakdown** value — a different physical
process from trailing-edge separation on an airfoil. Comparing it
against airfoil values is not like-for-like.

Airfoil to airfoil, the gap is narrower: 0.52 c/V versus 4.24 c/V, and
that is explicable by different airfoils, Reynolds numbers, and fitting
methods.

**But** G-K report a tenfold internal disagreement for the *same* delta
wing (1.5 vs 15 c/V) and state plainly they cannot explain it.

## Conclusion so far

tau_1 is **weakly identifiable** — the data does not pin it down
sharply. Structural reason: in the gain function K(alpha) it appears
only as the sum tau_1 + tau_2. See [[gk-equations]].

Practical approach: seed near a physics-based value (4.24 c/V), fit, and
check whether the result is insensitive to that choice within roughly
plus or minus 30 percent. If it is insensitive, report it as fixed
rather than estimated.

## Auto-collected from literature notes

```dataview
TABLE tau1_value AS "tau1", tau1_units AS "units", nondim_convention AS "convention", airfoil
FROM "Literature"
WHERE tau1_value != null AND tau1_value != ""
```
