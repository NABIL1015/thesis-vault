---
title: Literature index
tags: [index]
---

# Literature

Back to [[Home]].

## Read first

- [[gomanStatespaceRepresentationAerodynamic1994]] — the original G-K
  paper. Only pages 1110-1111 matter for a 2D airfoil.
- [[williamsFeedForwardDynamicStall2018]] — same rig as your data
  (NACA 0018, LE slot, Re 300k, k 0.09). Closest precedent that exists.
- [[williamsModelingLiftHysteresis2016]] — modified G-K adding static
  hysteresis.
- [[ayancikAllYouNeed2021]] — physics-based values for tau1 and tau2.

## Reading list by category

1. Foundational G-K formulation
2. Greenblatt-group modified G-K for pitching airfoils
3. tau1 / tau2 parameter identification
4. G-K with active flow control / blowing
5. FCL experiments and dataset provenance
6. Numerical ODE parameter estimation
7. Pulsed blowing in the Strouhal band

```dataview
TABLE year AS "Year", category AS "Cat", tau1_value AS "tau1"
FROM "Literature"
WHERE citekey != null
SORT year ASC
```
