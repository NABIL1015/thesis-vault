---
title: tau_2
tags: [parameter]
aliases: ["tau2", "tau two", "delay time"]
status: open
---

# tau_2 — the delay time

Back to [[Home]].

## What it is

Shifts the *argument* of the steady curve. The separation point chases
not x0(alpha) but x0(alpha - tau_2 * alphadot).

Consequence: when pitching up, alphadot is positive, so the flow behaves
as though the airfoil were at a smaller angle than it really is. **This
is the stall delay** — the reason lift can climb past the static stall
angle before collapsing.

## Key property

tau_2 **only ever appears multiplied by alphadot**. In a static test
alphadot is zero and tau_2 does nothing at all. It is purely a motion
parameter.

Sanity check on units: tau_2 (seconds) times alphadot (rad/s) gives
radians — an angle, as it must be, since it is subtracted from alpha.

## Published values

| Source | Value | In seconds here |
|---|---|---|
| G-K 1994, NACA 0015 | 4.5 c/V | 0.12 s |
| G-K 1994, delta wing | 0.5 c/V | 0.013 s |

Ayancik & Mulleners give a stall-delay power law rather than a single
constant.

## Auto-collected

```dataview
TABLE tau2_value AS "tau2", nondim_convention AS "convention", airfoil
FROM "Literature"
WHERE tau2_value != null AND tau2_value != ""
```
