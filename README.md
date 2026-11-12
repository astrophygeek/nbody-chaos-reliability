# Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics

<!-- BADGES START -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-Scientific_Computing-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![LaTeX](https://img.shields.io/badge/Manuscript-LaTeX-008080?logo=latex&logoColor=white)
![Astrophysics](https://img.shields.io/badge/Field-Computational_Astrophysics-663399)
![Research Status](https://img.shields.io/badge/Status-Research_Project-informational)

[![Last Commit](https://img.shields.io/github/last-commit/astrophygeek/nbody-chaos-reliability)](https://github.com/astrophygeek/nbody-chaos-reliability/commits/main)
[![GitHub Stars](https://img.shields.io/github/stars/astrophygeek/nbody-chaos-reliability)](https://github.com/astrophygeek/nbody-chaos-reliability/stargazers)
<!-- BADGES END -->


**Researcher:** Fatima Shahzad

## Overview

Numerical simulations allow us to investigate gravitational systems whose motion cannot generally be expressed through simple analytical solutions. However, these simulations introduce approximation errors that can become especially significant near close gravitational encounters or in dynamically sensitive regions.

This project investigates how numerical integration methods, timestep selection, and solver tolerances influence orbital predictions and finite-time chaos diagnostics.

The study compares Forward Euler, Leapfrog, fourth-order Runge-Kutta (RK4), DOP853, and Radau. Numerical reliability is evaluated through trajectory agreement, finite-time Lyapunov exponents, convergence tests, and conservation diagnostics.

## Research Objectives

- Establish numerical accuracy using analytically understood gravitational benchmarks.
- Compare integration methods and investigate timestep-dependent errors.
- Study close encounters and false numerical orbital escape.
- Calculate finite-time Lyapunov exponents using variational equations.
- Evaluate numerical reliability across an ensemble of restricted three-body configurations.
- Investigate Jacobi conservation and challenging reference trajectories.
- Cross-check selected results using independent adaptive solvers.

## Repository Contents

- `src/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Reusable numerical simulation code.
- `notebooks/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Computational experiments and analysis.
- `experiments/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Experiment configurations and scripts.
- `manuscript/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Research manuscript and publication figures.
- `results/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Saved numerical results.
- `data/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Research datasets and reference outputs.
- `reproducibility/` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Verification records and experimental settings.

## Reproducibility

The repository is being organized for independent reproduction. Some original experiment notebooks and numerical outputs are not yet available locally, so not every published figure can currently be regenerated from the checked-in files.

The manuscript should be treated as a research draft pending a final audit of the numerical results.

---

## Research overview

**Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics**

**Researcher:** Fatima Shahzad

This computational astrophysics project investigates how numerical integration methods, timestep selection, close encounters, and solver tolerances influence the reliability of chaos diagnostics in gravitational dynamics.

The study examines the distinction between physical orbital instability and numerical artifacts, with an emphasis on convergence testing and independent numerical verification.

### Research objectives

- Investigate numerical accuracy in gravitational simulations.
- Compare fixed-step and adaptive numerical integrators.
- Analyze orbital energy, angular momentum, and Jacobi-constant conservation.
- Examine close encounters and apparent orbital escape.
- Investigate finite-time Lyapunov exponent diagnostics.
- Evaluate trajectory and timestep convergence.
- Compare independent adaptive solver results.
- Develop a reliability-oriented interpretation of numerical experiments.

## Research methodology

The project investigates gravitational dynamics using numerical integration, conservation-law diagnostics, finite-time Lyapunov exponent analysis, convergence studies, and cross-solver comparisons.

Methods discussed in the manuscript include Euler, leapfrog, fourth-order Runge-Kutta, DOP853, and Radau integration.

## Project organization

| Directory | Contents |
|---|---|
| `manuscript/` | Research paper, LaTeX source, and manuscript figures |
| `figures/plots/` | Scientific visualizations |
| `results/numerical/` | Numerical experiment datasets |
| `results/objective_01/` | Objective 1 experiment output |
| `notebooks/` | Available Jupyter notebooks |
| `scripts/` | Available Python experiment scripts |
| `docs/` | File inventory and project documentation |

## Reproducibility

The repository contains numerical results, scientific plots, and available experiment code.

The currently available Python notebook and script cover Objective 1. Complete executable workflows for every subsequent experiment have not yet been consolidated into the repository.

The numerical datasets and manuscript therefore provide research evidence, but the repository should not be interpreted as a fully automated end-to-end reproduction package.

## Manuscript

The research manuscript is available at:

[Read the research paper](manuscript/main.pdf)

The corresponding LaTeX source is available at:

[View the LaTeX manuscript](manuscript/main.tex)

To compile locally, install a LaTeX distribution and run:

```bash
cd manuscript
latexmk -pdf main.tex
```

## Citation

If you use this research, please acknowledge:

**Fatima Shahzad**, *Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics*, independent computational astrophysics research project, 2026.

This citation is descriptive and does not imply peer-reviewed publication.

## License

Original software code in this repository is available under the [MIT License](LICENSE), subject to the rights holder's authorization.

The manuscript, research figures, and datasets are not covered by that MIT software license unless their rights holder separately grants permission.

## Author

**Fatima Shahzad**

Independent Computational Astrophysics Research