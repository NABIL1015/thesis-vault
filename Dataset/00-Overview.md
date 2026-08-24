---
title: Dataset Overview
---

# FCL Dataset Overview

Rig constants (all datasets): NACA 0018, chord c = 0.348 m, span s = 0.610 m,
pitch axis at 25% chord, 40 mid-span pressure ports, leading-edge blowing
slot at 5% chord (open), mid-chord slot at 50% chord (sealed with tape).
Re = U-infinity * c / nu. k = pi * f * c / U-infinity.
Source: FCL_data_documentation.pdf (flowcontrollab.com).

**Known documentation error:** individual per-dataset pages for 99922 and
99924 both list k = 0.06; the overview table and file headers say k = 0.09.
Trust 0.09 for both.

| Dataset | Category | Inflow | Re | AoA | k | PIV |
|---|---|---|---|---|---|---|
| [[99900]] | baseline | quasi-steady pitch | various (1.5e5-5.0e5) | -2 to 32 deg | 0 |  |
| [[99930]] | baseline | dynamic pitch | various | 10+10sin(phi) | various | yes |
| [[99932]] | baseline | dynamic pitch & surge | 250k*[1+0.5sin(phi-tau)] | 10+10sin(phi) | 0.074 | yes |
| [[99901]] | steady-blowing | quasi-steady pitch | 300k | -2 to 32 deg | 0 |  |
| [[99910]] | steady-blowing | surge | 300k*[1+0.2sin(phi)] | 15 deg | 0.05 |  |
| [[99920]] | steady-blowing | dynamic pitch | 300k | 18+7sin(phi) | 0.06 |  |
| [[99922]] | steady-blowing | dynamic pitch | 300k | 18+7sin(phi) | 0.09 |  |
| [[99924]] | steady-blowing | dynamic pitch | 300k | 18+7sin(phi) | 0.09 |  |
| [[99926]] | steady-blowing | dynamic pitch | 300k | 14.5+3sin(phi) | 0.041 |  |
| [[99928]] | steady-blowing | dynamic pitch | 300k | 14.5+3sin(phi) | 0.082 |  |
| [[99936]] | steady-blowing | dynamic pitch | 250k | 15+10sin(phi) | 0.074 | yes |
| [[99940]] | adaptive-blowing | surge | 300k*[1+0.2sin(phi)] | 15 deg | 0.05 |  |
| [[99950]] | adaptive-blowing | dynamic pitch | 300k | 18+7sin(phi) | 0.01, 0.06, 0.09 |  |
| [[99952]] | adaptive-blowing | dynamic pitch | 300k | 18+7sin(phi) | 0.06 |  |
| [[99964]] | adaptive-blowing | dynamic pitch & surge | 300k*[1+0.2sin(phi)] | 18+7sin(phi) | 0.06 |  |
| [[99966]] | adaptive-blowing | dynamic pitch & surge | 300k*[1+0.2sin(phi-180)] | 18+7sin(phi) | 0.06 |  |

## Data location

Raw FCL data (all 16 datasets, one folder each) lives on disk at:
`/home/nabil/Downloads/FCL_pressure_data/`

Not inside the vault — this is data, not notes. Each subfolder is named
by dataset ID (e.g. `99924/`) and matches the notes above 1:1.
