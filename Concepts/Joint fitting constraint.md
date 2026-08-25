---
title: Joint fitting constraint
tags: [concept, method]
aliases: ["joint fitting", "joint fit"]
---

# The joint fitting constraint

Back to [[00-Concepts]].

## The rule

**All runs must be fitted together as multiple trajectories. Never one
at a time.**

## Why

Cmu is **constant within each run**. If you fit a single run, the
blowing term is a constant, and a constant is indistinguishable from the
bias term — they are collinear.

The fit will still converge. It will still report coefficients. Those
coefficients will be meaningless, because the optimiser has no way to
tell how much of the offset came from blowing and how much from the
baseline.

Fitting one at a time yields **confident garbage** — the worst kind of
result, because nothing looks wrong.

## What makes it work

Fitting all runs together means Cmu actually varies across the dataset,
so its effect becomes separable from the bias.

## Related trap: conditioning

Alpha spans only 0.19 to 0.44 radians. Over that narrow band, alpha
squared is 95.6 percent reproducible as a straight line in alpha. An
uncentred fit returned cancelling coefficients in the hundreds of
thousands — predictions fine, individual coefficients meaningless.

**Centre every variable.** This drops the alpha/alpha-squared
correlation to exactly zero.

(For SINDy this was fatal, since its entire output *is* the coefficient
list. For G-K it matters less — only two parameters, both physically
meaningful in seconds — but the habit is worth keeping.)
