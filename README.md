# Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24158795.svg)](https://doi.org/10.5281/zenodo.24158795)

[![MIT License](https://img.shields.io/badge/Code_License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-Scientific_Computing-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![LaTeX](https://img.shields.io/badge/Manuscript-LaTeX-008080?logo=latex&logoColor=white)
![Astrophysics](https://img.shields.io/badge/Field-Computational_Astrophysics-663399)
![Research](https://img.shields.io/badge/Status-Research_Project-informational)

[![Last Commit](https://img.shields.io/github/last-commit/astrophygeek/nbody-chaos-reliability)](https://github.com/astrophygeek/nbody-chaos-reliability/commits/main)
[![GitHub Stars](https://img.shields.io/github/stars/astrophygeek/nbody-chaos-reliability)](https://github.com/astrophygeek/nbody-chaos-reliability/stargazers)

**Researcher:** Fatima Shahzad

**Field:** Computational Astrophysics | Celestial Mechanics | Nonlinear Dynamics

**Project:** Independent Computational Research

---

## Overview

Numerical simulations provide a powerful way to investigate gravitational systems whose dynamics cannot generally be described by simple analytical solutions. However, numerical approximations introduce errors that may become particularly significant during close encounters and in dynamically sensitive regions.

This research investigates how numerical integration methods, timestep selection, and solver tolerances influence orbital predictions and finite-time chaos diagnostics.

The central research question is:

**How can genuine dynamical instability be distinguished from numerical artifacts introduced by computational methods?**

The study examines numerical reliability through trajectory convergence, conservation diagnostics, finite-time Lyapunov exponents, and independent solver comparisons.

## Research Objectives

1. Establish numerical accuracy using gravitational benchmarks.
2. Compare integration methods and timestep-dependent errors.
3. Investigate close encounters and false numerical orbital escape.
4. Calculate finite-time Lyapunov exponents using variational equations.
5. Examine reliability across restricted three-body configurations.
6. Investigate energy, angular momentum, and Jacobi conservation.
7. Analyze trajectory and FTLE convergence.
8. Cross-check selected cases using independent adaptive solvers.

## Numerical Methods

| Method | Purpose |
|---|---|
| Forward Euler | Baseline integration and numerical error analysis |
| Leapfrog | Symplectic integration and orbital conservation |
| RK4 | Fixed-step fourth-order integration |
| DOP853 | High-order adaptive integration |
| Radau | Independent implicit adaptive solver comparison |

## Scientific Diagnostics

The project investigates:

- Trajectory agreement across numerical methods
- Timestep and convergence sensitivity
- Energy and angular-momentum conservation
- Jacobi-constant conservation
- Close gravitational encounters
- False numerical orbital escape
- Finite-time Lyapunov exponents (FTLEs)
- Independent solver verification
- Numerical reliability classification

A positive finite-time Lyapunov exponent can indicate sensitivity to initial conditions, but its numerical convergence must be assessed before interpreting it as evidence of physical chaos.

## Numerical Results

The organized repository includes:

- 34 scientific PNG plots
- 27 numerical CSV result files
- Available Objective 1 Python code and Jupyter notebook
- Objective 1 experiment outputs
- A LaTeX research manuscript

The numerical results cover analyses related to reliability screening, conservation diagnostics, convergence, and independent adaptive-solver comparisons.

The manuscript describes the experimental methodology, numerical findings, and interpretation.

## Repository Structure

```text
nbody-chaos-reliability/
|
|-- README.md
|-- LICENSE
|
|-- manuscript/
|   |-- main.tex
|   |-- main.pdf
|   `-- figures/
|
|-- figures/
|   `-- plots/
|
|-- results/
|   |-- numerical/
|   `-- objective_01/
|
|-- notebooks/
|   `-- objective_01_gravity.ipynb
|
|-- scripts/
|   `-- objective_01_gravity.py
|
`-- docs/
```

The tree lists the main research directories and files, rather than every generated artifact.

## Manuscript

**Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics**

- [Read the research paper (PDF)](manuscript/main.pdf)
- [View the LaTeX manuscript](manuscript/main.tex)
- [Browse scientific figures](figures/plots/)
- [Browse numerical datasets](results/numerical/)

### Compile the manuscript

Install a LaTeX distribution and `latexmk`, then run:

```bash
cd manuscript
latexmk -pdf main.tex
```

## Reproducibility and Limitations

This repository provides available numerical experiment results, scientific figures, and research documentation.

At present, the available notebook and Python script cover Objective 1. Complete executable workflows for all later experiments have not yet been consolidated into the repository.

Therefore, this repository should not currently be treated as a fully automated end-to-end reproduction package.

Future improvements may include additional experiment scripts, environment specifications, documented parameters, and automated numerical validation.

## Citation

Fatima Shahzad (2026). *Numerical Artifacts and the Reliability of Chaos Diagnostics in Gravitational N-Body Dynamics*. Independent computational astrophysics research project.

Repository: https://github.com/astrophygeek/nbody-chaos-reliability

This citation does not imply peer-reviewed publication or an assigned DOI.

## License

Original software code is distributed under the [MIT License](LICENSE), subject to authorization by its rights holder.

The manuscript, scientific figures, and numerical datasets are not covered by that software license unless their rights holders explicitly specify otherwise.

## Researcher

**Fatima Shahzad**

Independent Computational Astrophysics Research

Research interests include gravitational dynamics, celestial mechanics, numerical simulation, nonlinear dynamics, and orbital stability.
