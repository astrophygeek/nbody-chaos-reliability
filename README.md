# Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics

**Researcher:** Fatima Shahzad

## Overview

Numerical simulations allow us to investigate gravitational systems whose motion cannot generally be expressed through simple analytical solutions. However, these simulations introduce approximation errors that can become especially significant near close gravitational encounters or in dynamically sensitive regions.

This project investigates how numerical integration methods, timestep selection, and solver tolerances influence orbital predictions and finite-time chaos diagnostics.

The study compares Forward Euler, Leapfrog, fourth-order Runge–Kutta (RK4), DOP853, and Radau. Numerical reliability is evaluated through trajectory agreement, finite-time Lyapunov exponents, convergence tests, and conservation diagnostics.

## Research Objectives

- Establish numerical accuracy using analytically understood gravitational benchmarks.
- Compare integration methods and investigate timestep-dependent errors.
- Study close encounters and false numerical orbital escape.
- Calculate finite-time Lyapunov exponents using variational equations.
- Evaluate numerical reliability across an ensemble of restricted three-body configurations.
- Investigate Jacobi conservation and challenging reference trajectories.
- Cross-check selected results using independent adaptive solvers.

## Repository Contents

- `src/` — Reusable numerical simulation code.
- `notebooks/` — Computational experiments and analysis.
- `experiments/` — Experiment configurations and scripts.
- `manuscript/` — Research manuscript and publication figures.
- `results/` — Saved numerical results.
- `data/` — Research datasets and reference outputs.
- `reproducibility/` — Verification records and experimental settings.

## Reproducibility

The repository is being organized for independent reproduction. Some original experiment notebooks and numerical outputs are not yet available locally, so not every published figure can currently be regenerated from the checked-in files.

The manuscript should be treated as a research draft pending a final audit of the numerical results.