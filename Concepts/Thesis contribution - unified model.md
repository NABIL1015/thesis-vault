---
title: Thesis contribution - unified model
tags: [thesis-material, plan, concept]
aliases: ["the gap", "contribution", "unified model", "thesis idea"]
status: proposed
---

# The proposed contribution: a unified pitch + time-varying blowing model

Back to [[Home]].

Working statement of the thesis idea, the gap it fills, why it is
achievable, and what role simulation and SINDy play.

---

## 1. What Williams 2019 actually did

The paper builds **two separate models** from **two separate
experiments**.

| | Airfoil | Blowing | Model | Figures |
|---|---|---|---|---|
| **G_d** disturbance model | pitching, 11 to 25 deg, k = 0.09 | **constant** per run (0.6, 2.7, 6.5%) | modified G-K, X_0 made a function of Cmu | Fig. 8 |
| **G_p** plant model | **stationary** at 11, 18, 25 deg | sinusoidal, Cmu = 0.017 + 0.007 sin | first-order time delay | Figs. 9-13 |

In G_d the airfoil moves and the blowing does not. In G_p the blowing
moves and the airfoil does not.

**Neither experiment has both varying at once.**

The two models meet only inside a Simulink block diagram (their Fig. 14),
where G_p is inverted to cancel G_d.

### Two assumptions buried in that arrangement

**Superposition.** The paper states the system output is the
disturbance-produced lift increment added to the lift modified by the
controller. Two nonlinear models, added. Nobody checked whether real
flow superposes.

**Transferability.** G_p was identified at *fixed* angles, then applied
while the airfoil sweeps 11 to 25 degrees. The plant is assumed
unchanged by the motion.

Both are reasonable engineering approximations. Neither is verified.

### The closed-loop result is a simulation

Figs. 15 and 16 come from Simulink, not the wind tunnel. There is no
experimental closed-loop demonstration in the paper.

### Their own data strains the assumption

They report the model works **better at Cmu = 0.6% than at 2.7% or
6.5%**, and explain why: at low blowing the flow is fully separated from
the leading edge throughout the cycle, while at higher blowing you get
"partially separated" leading-edge flow the model cannot represent.

So the character of the flow state changes with **both** alpha and Cmu —
which is exactly what a fixed-alpha plant model cannot capture.

---

## 2. The gap

**No published model takes both alpha(t) and Cmu(t) as simultaneously
time-varying inputs.**

Evidence gathered so far:

- The **JFM 2024** state-space neural network paper (same airfoil,
  NACA 0018) surveys recent G-K enhancements and lists exactly three:
  An et al. 2021 (pressure assimilation), Williams et al. 2019 (slot
  blowing), De Troyer et al. 2022 (plasma). Blowing and plasma appear as
  **separate** extensions. No unified one.
- **An, Williams & Hemati 2020** (Energies) models time-varying
  "burst-type" actuation — explicitly on a **stalled**, i.e. stationary,
  airfoil. Same split as Williams 2019.
- That JFM 2024 paper's own SS-NN maps **angle of attack to lift only**.
  No actuation input at all.
- **Müller-Vahl 2016** adaptive blowing experiments *do* vary Cmu in time
  during pitching, including combined pitch and surge. **No reduced-order
  model appears to have been fitted to them.**

### Datasets that appear unmodelled

| Dataset | Content |
|---|---|
| [[99940]] | surge only, adaptive blowing |
| [[99950]] | dynamic pitch, adaptive, **three k values** (0.01, 0.06, 0.09) |
| [[99952]] | dynamic pitch, adaptive, k = 0.06 |
| [[99964]] | pitch **and** surge, adaptive, in phase |
| [[99966]] | pitch **and** surge, adaptive, 180 deg out of phase |

### Honest limits of this novelty claim

Not exhaustively verified. Before writing "novel" in the thesis:

- Check **Sedky, Jones & Lagor**, lift regulation during transverse gust
  encounters using a modified G-K model. Different actuation, but
  structurally close — time-varying effective alpha with active
  regulation.
- Check the **wind turbine trailing-edge flap** literature (Bergami &
  Gaunaa, Andersen). The equivalent problem — varying inflow plus varying
  actuator state — may already be solved for flaps.
- Do a **citation-forward search** on Williams 2019 and Müller-Vahl 2016.

Absence of evidence from a handful of searches is not proof.

---

## 3. Why it is feasible

This is unusually well set up compared with most undergraduate projects.

**Everything needed is published.**

- Model form: C_L = f(alpha, Cmu)·X + g(alpha, Cmu)·(1 − X), and
  tau_1 dX/dt + X = X_0(alpha − tau_2·alpha-dot, Cmu)
- All five output constants: dC_L/dalpha|low = 5.63, dC_L/dCmu = 3.55,
  d2C_L/dalpha dCmu = 25, dC_L/dalpha|high = 3.08, alpha_0 = 0.177 rad
- Both time constants: tau_1 = 1.57 t_conv, tau_2 = 1.52 t_conv,
  t_conv = 0.027 s — **confirmed independently by Santra 2020, Table 2**
- X_0(alpha, Cmu) published as their Fig. 7, for seven blowing levels

**The data is on disk.** [[99901]] gives the static polars for X_0.
[[99924]] and [[99922]] give the dynamic reproduction target. The
adaptive sets give the validation.

**The model is small.** Two parameters, both in seconds, both physically
meaningful. Bad fits are visible by inspection — unlike
[[SINDy negative result]] with twenty meaningless coefficients.

**Compute is trivial.** Integrating a first-order ODE. Runs on any laptop.

### The one thing to check first

The exact Cmu values Williams plots (0.6, 2.7, 6.5%) do **not** all
appear in the archive. Nearest available are 0.56% and 6.08%. Close, not
identical. Verify before promising an exact reproduction.

---

## 4. The way — staged

### Stage 1: reproduce

Implement the Williams model with **their** constants and **their**
inputs. Target: their Fig. 8, and Santra's Fig. 4 right panel (same
conditions: 18 + 7 sin, k = 0.09, Re = 3e5).

Using their constants rather than refitting isolates **your
implementation** as the only unknown. This is a checkpoint, not a
contribution. Budget roughly a third of the time.

### Stage 2: unify

Write a **single** state-space model in which alpha(t) and Cmu(t) both
vary. The obvious first form keeps the G-K state equation and lets the
forcing depend on instantaneous Cmu:

  tau_1 dX/dt + X = X_0(alpha − tau_2·alpha-dot, Cmu(t))

**The open question is whether that is enough.** If the flow lags a
*changing* Cmu — which Williams' G_p says it does, with its own tau_1 and
tau_2 — then an additional actuation state is needed, something like
Williams' Y equation folded into the same system rather than kept
separate.

Deciding between those two is the intellectual content of the thesis.

### Stage 3: validate on the unmodelled data

Fit on some adaptive runs, predict held-out ones. [[99964]] and
[[99966]] are the strongest test: pitch, surge and blowing all varying,
and the two differ only by a 180 degree phase shift in the freestream —
a clean pair.

### Stage 4: cross-frequency

[[99950]] contains three k values in one dataset. Fit at one k, predict
another. This is the test that separates a real model from a
[[Clock model trap]].

---

## 5. Where simulation comes in, and why X matters

### The circularity in the current approach

X is **hidden**. Nobody measures it. It is obtained by taking a measured
static lift curve and inverting an output equation for whatever X would
reproduce that lift.

Then the model uses X to predict lift.

So the state is *defined by* lift and then used to *predict* lift. That
is not viciously circular — the dynamics in between are real content —
but it means **the state equation itself has never been tested
independently**. Every validation to date is an input-output check.

### What simulation changes

In a simulation you can see the separation point **directly**: find where
wall shear stress crosses zero along the upper surface, at every
timestep.

That gives X as a **measured** quantity rather than an inferred one.

Which enables the question nobody has asked: **does the real separation
point actually obey tau_1 dX/dt + X = X_0(alpha − tau_2 alpha-dot)?**

- If yes — independent confirmation of a 30-year-old model, by a route
  its authors could not take
- If no — a more interesting result, and a pointer to what is missing

This is the **justification section** for the unified model: evidence
that the state variable means what the thesis claims it means.

### Four caveats, stated plainly

**1. Wall-shear X is not the same quantity as Kirchhoff X.** One is a
geometric fact about the flow field; the other is defined so that an
output equation reproduces measured lift. They are related, not
identical. In separated flow wall shear can cross zero several times, and
choosing "the" separation point involves judgement.

**Check whether the two definitions track each other before building
anything on it.**

**2. URANS separation is turbulence-model dependent.** k-omega SST and
Spalart-Allmaras will not put the separation point in the same place. So
the reference quantity is itself uncertain.

**3. URANS handles the DSV poorly.** But note: **so does G-K.** The
simulation's weakness is matched to the model's weakness, which is a
happier accident than it sounds.

**4. Reynolds number.** 2D URANS at Re = 3e5 is achievable on a desktop.
LES is not — see the hardware note below.

### Hardware reality

2D URANS at Re = 1e5 to 3e5: comfortable. Roughly 100-200k cells, hours
per pitching cycle.

**Wall-resolved LES at Re = 1e5 is not desktop work.** It needs roughly
10-50 million cells and hundreds to thousands of cores. Adding RAM
removes one wall and leaves a bigger one — cores cannot move that mesh in
useful time. LES cost scales roughly as Re^1.8.

**Tell the CFD partner early: output wall shear stress along the
surface.** Trivial to plan, annoying to retrofit.

---

## 6. Where SINDy could return, and why not yet

### The condition under which it becomes legitimate

[[SINDy negative result]] failed because (Cl, Cm) is not a valid state —
proven by the [[Collision test]].

If simulation supplies **measured X**, that objection disappears. You
would then be running SINDy on a state that G-K claims *is* the state.
That is not repeating the failed experiment; it is the controlled version
with the missing variable supplied.

### But do the simple thing first

**SINDy earns its place only when you do not know the equation's form.
Here you do.**

The simpler and more interpretable move: take the measured X, fit tau_1
and tau_2 directly, and **look at the residual**.

- Residual small and unstructured → G-K structure confirmed, done
- Residual **systematic** → something is missing, and *then* SINDy is the
  right tool for asking what

### The trap that has not gone away

Simulated alpha is still sinusoidal at one frequency. A polynomial menu
in alpha is still secretly a Fourier series in phase. **Multiple k values
or non-sinusoidal kinematics are required before any discovered equation
means anything.** See [[Clock model trap]].

---

## 7. Prospects — honest assessment

### What this is not

The simulation-validates-G-K piece **on its own is not a strong paper**.
It is confirmatory — "the model works as advertised" — and reviewers
reward findings that change what people do. Add the methodological
objections (turbulence-model dependence, one airfoil, one Re, 2D) and it
would struggle.

### What could reach a decent venue

The **unified model validated on the adaptive-blowing datasets**. That is
a new capability, not a confirmation. The X-from-simulation work becomes
a supporting section inside it rather than the headline.

Realistic target format: an **AIAA Journal Technical Note**. Santra 2020
is exactly that — five pages, Q1 venue. A far more plausible target than
a full-length JFM paper.

### The blunt part

Undergraduate theses rarely produce Q1 papers, and that is arithmetic
rather than a judgement. PhD students take three or four years with
cluster access and a supervisor's network to get there.

The realistic good outcome: **a thesis strong enough that the supervisor
says "there is a paper in this," followed by a few months of extra work
after submission.** That is how most first papers actually happen.

Aiming at Q1 from the start tends to produce scope creep and an
unfinished thesis.

### The scope warning

Candidate directions currently on the table:

1. Reproduce Williams 2019
2. Unified pitch + time-varying blowing model
3. Ayancik tau_1 generalisation test
4. Simulation validation of X
5. ML / data-driven modelling
6. Other actuators (plasma, control surfaces)

**That is five or six theses.**

Recommended shape: **(1) as a checkpoint, (2) as the contribution, (4) as
its justification section, (3) as a short subsection.** Drop (6)
entirely — breadth is weaker than depth and restarts validation from
zero. Treat (5) as a *method choice within* (2), not a separate
direction — e.g. learning X_0(alpha, Cmu) as a small network while
keeping the state equation physical.

**Theses die from scope, not from difficulty.**

---

## 8. On ML specifically

The JFM 2024 paper already did "neural network instead of G-K for a
pitching NACA 0018," and the SS-NN outperformed G-K. That ground is
taken.

**But it had no actuation input.** So the ML version of this thesis is
the *same gap*, different tool: a data-driven state-space model with two
time-varying inputs.

**The data-volume problem is real.** Phase-averaged data means 180 points
per cycle, one cycle per run — a few thousand points total, smooth and
highly correlated. Free-form networks will memorise. This points toward
**physics-constrained** ML: keep the state equation, learn only
X_0(alpha, Cmu), which is a smooth two-input one-output function with
Williams' Fig. 7 available as a sanity check.

---

## Open questions to resolve

- [ ] Do wall-shear X and Kirchhoff-inverted X track each other?
- [ ] Is instantaneous Cmu in the forcing enough, or is a separate
      actuation state required?
- [ ] Has anyone modelled the adaptive-blowing datasets? (citation-forward
      search)
- [ ] Check Sedky/Jones/Lagor and the wind-turbine flap literature
- [ ] Confirm which Cmu values in [[99901]] correspond to Williams' Fig. 7
