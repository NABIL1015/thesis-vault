---
title: Home
tags: [index]
---

# Dynamic stall control — thesis home

Closed-loop hybrid feedforward/feedback control of dynamic stall on a
pitching NACA 0018, using pulsed leading-edge slot blowing in the
Strouhal band St = 0.07-0.16.

## Start here

- [[glossary]] — every term defined in plain words
- [[gk-equations]] — all Goman-Khrabrov equations in one place

## Sections

- [[00-Overview]] — the 16 FCL datasets
- [[00-Literature]] — papers
- [[00-Concepts]] — ideas and reference notes

## Open parameters

- [[tau_1]] — relaxation time. Disputed. Must be settled before fitting.
- [[tau_2]] — delay time.

## Where things stand

SINDy was attempted and is **closed** — it failed at 59% error, and the
cause was diagnosed structurally, not as a tuning problem. See
[[SINDy negative result]].

Current model target: **Goman-Khrabrov**.

## Next steps

1. Extract static polar from datasets [[99900]] and [[99901]] — needed
   for X0(alpha), see [[Kirchhoff relation]]
2. Settle the [[tau_1]] starting value
3. Fit G-K jointly across runs — see [[Joint fitting constraint]]
4. Validate by held-out prediction, then a different k — see
   [[Clock model trap]]
