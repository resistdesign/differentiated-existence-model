# DEM Mathematical Models

This directory contains explicit calculational models derived from or motivated by the Differentiated Existence Model.

A model belongs here only when it defines enough mathematics to calculate concrete consequences. Conceptual notes and speculative correspondences belong under `docs/research-notes/` instead.

## Model status vocabulary

- **Toy model** — deliberately simplified construction used to test coherence or recover a known result.
- **Candidate physical model** — supplies dynamics intended to describe some actual physical regime.
- **Recovery model** — reproduces established physics from a proposed deeper structure.
- **Predictive model** — produces a discriminating observable not inserted as an assumption.

None of these labels implies experimental confirmation.

## Current models

### 01 — Clock/Geometry Budget

[`01-clock-geometry-budget/`](01-clock-geometry-budget/)

The first DEM toy model introduces one geometric mode, one physical clock-process mode, an arbitrary bookkeeping parameter, and a positive quadratic mode-norm constraint. It derives

\[
d\tau^2 = dt^2 - \frac{dx^2}{c_*^2}
\]

with

\[
c_*^2 = \frac{g_\kappa}{g_x}.
\]

It therefore recovers special-relativistic time dilation, an effective Lorentzian interval, and an invariant limiting speed from an explicit metric-ratio construction. With the standard free-particle action it also recovers relativistic momentum, energy, dispersion, and the Newtonian limit.

Its primary unresolved burden is equally explicit: **derive the quadratic mode-norm constraint rather than postulate it.**
