---
title: Clock model trap
tags: [concept, method]
aliases: ["clock model", "sinusoid trap"]
---

# The clock model trap

Back to [[00-Concepts]].

## The problem

Alpha is a sine wave repeating every 0.9 seconds. So there is a fixed
relationship between phase and everything else: at phi = 54 degrees the
airfoil is always at the same angle, moving at the same rate, and stall
always happens right about there.

A fitted model can therefore learn one of two very different things:

- **A real model** learns *why* — the flow separates because the angle
  got steep and the separation point had time to run forward. Change
  conditions, it still works.
- **A clock model** learns *when* — lift drops at phi = 54 because that
  is where lift drops. It has memorised the timetable.

**On one dataset at one frequency these are indistinguishable.** Both
fit equally well.

## Why it is fatal here

A controller's whole job is to change what happens at a given moment.
A clock model denies that is possible — it predicts the same collapse
regardless of actuation, because it never learned that blowing causes
anything.

## The specific mechanism for polynomial models

Alpha is a sine, so alpha squared contains the second harmonic, alpha
cubed the third, and so on. A polynomial menu in alpha is secretly a
Fourier series in phase. This is why the [[SINDy negative result]] was
so hard to diagnose from fit quality alone.

## The test

**Change the timetable.** Fit at one reduced frequency, predict another.
A real model survives. A clock model falls apart, because its memorised
schedule no longer applies.

Available k values across the datasets: 0.041 ([[99926]]), 0.06
([[99920]], [[99952]]), 0.074 ([[99936]]), 0.082 ([[99928]]), 0.09
([[99922]], [[99924]]). [[99950]] spans three k values in one dataset.

## Where G-K sits

Better protected than SINDy, because it has physical structure — X
chasing X0 with a lag — and only two free numbers. Hard to accidentally
build a clock with two parameters. But the cross-k test is still what
proves it.
