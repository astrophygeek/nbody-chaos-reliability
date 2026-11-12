"""
OBJECTIVE 01 — REPRESENTING A GRAVITATIONAL SYSTEM
=================================================
Numerical Artifacts and Spurious Chaos in Gravitational N-Body Dynamics

A first computational physics implementation for Fatima.

WHAT THIS PROGRAM DOES
----------------------
1. Defines masses, positions, and velocities of a star and two planets.
2. Checks that arrays have consistent shapes and sensible values.
3. Calculates Newtonian gravitational acceleration for every object.
4. Calculates every pair's gravitational force, showing Newton's third law.
5. Calculates the system's center of mass and total momentum.
6. Makes a static diagram of the bodies and gravitational acceleration arrows.
7. Saves a readable text summary and an image.

WHAT IT DOES NOT DO YET
-----------------------
It does not move planets forward in time, compute orbital trajectories, or
measure chaos. Numerical integration starts in Objective 02. These are
snapshots at ONE instant, not a time-evolving solar system.

RUN
---
    python -m pip install numpy matplotlib
    python objective_01_gravity.py

OUTPUTS (written beside this program in the 'objective_01_output' folder)
-----------------------------------------------------------------------
    acceleration_vectors.png
    results.txt

UNITS
-----
We use deliberately simple, dimensionless units:
    G = 1
    mass unit = arbitrary reference mass
    length unit = arbitrary reference length
    time unit is implied by G = 1

This is normal in computational celestial mechanics. We choose normalized
units so that the physics is easy to inspect. Do not interpret the output
numbers as SI accelerations in m/s^2.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Save images without requiring a graphical desktop.
import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# SECTION 1: THE PHYSICAL SYSTEM
# ---------------------------------------------------------------------------
# Each row of positions and velocities represents one object.
# For example positions[1] = [1.0, 0.0] means planet 1 is at x=1, y=0.
# Velocity is included so we learn the full structure of a dynamical state.
# We will use it to MOVE the bodies in the next objective; it does not enter
# Newtonian gravitational acceleration at a given instant.

G = 1.0
NAMES = ("Star", "Planet A", "Planet B")
MASSES = np.array([1.0, 0.001, 0.002], dtype=float)
POSITIONS = np.array([
    [0.0, 0.0],     # Star
    [1.0, 0.0],     # Planet A
    [0.0, 1.6],     # Planet B
], dtype=float)
VELOCITIES = np.array([
    [0.0, 0.0],     # Star (illustrative snapshot, not a stable orbit)
    [0.0, 1.0],     # Planet A
    [-0.8, 0.0],    # Planet B
], dtype=float)


# ---------------------------------------------------------------------------
# SECTION 2: CHECK THE INPUTS BEFORE CALCULATING ANY PHYSICS
# ---------------------------------------------------------------------------

def validate_system(masses: np.ndarray,
                    positions: np.ndarray,
                    velocities: np.ndarray) -> None:
    """Reject malformed inputs rather than producing misleading answers."""
    if masses.ndim != 1:
        raise ValueError("masses must be a one-dimensional array")
    n = len(masses)
    if n < 2:
        raise ValueError("at least two bodies are needed for this example")
    if positions.shape != (n, 2) or velocities.shape != (n, 2):
        raise ValueError("positions and velocities must each have shape (N, 2)")
    if not (np.all(np.isfinite(masses))
            and np.all(np.isfinite(positions))
            and np.all(np.isfinite(velocities))):
        raise ValueError("all masses, positions, and velocities must be finite")
    if np.any(masses <= 0):
        raise ValueError("all masses must be strictly positive")
    for i in range(n):
        for j in range(i + 1, n):
            if np.array_equal(positions[i], positions[j]):
                raise ValueError(f"{i} and {j} occupy the same position")


# ---------------------------------------------------------------------------
# SECTION 3: UNDERSTAND ONE PAIR OF BODIES
# ---------------------------------------------------------------------------

def gravitational_force_on_i_from_j(
    r_i: np.ndarray, r_j: np.ndarray, m_i: float, m_j: float, G_value: float = G
) -> np.ndarray:
    """Vector force ON i DUE TO j: F_ij = G m_i m_j (r_j-r_i)/|r_j-r_i|^3."""
    displacement = r_j - r_i       # Direction: from object i toward object j.
    distance = np.linalg.norm(displacement)
    if distance == 0:
        raise ValueError("gravitational point masses cannot occupy the same point")
    return G_value * m_i * m_j * displacement / distance**3


# ---------------------------------------------------------------------------
# SECTION 4: GENERALIZE TO ALL N OBJECTS
# ---------------------------------------------------------------------------

def gravitational_accelerations(
    positions: np.ndarray, masses: np.ndarray, G_value: float = G
) -> np.ndarray:
    """Return a[i] = sum_j G*m[j]*(r[j]-r[i]) / |r[j]-r[i]|^3.

    Why does the body's own mass not appear in its acceleration?
    Because F = m_i*a_i, and Newtonian gravitational force contains m_i.
    Dividing the total force by m_i cancels that factor. A body's acceleration
    still depends on other bodies' masses and on their relative positions.
    """
    n = len(masses)
    a = np.zeros_like(positions, dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue  # An object does not exert gravitational force on itself.
            difference = positions[j] - positions[i]
            distance = np.linalg.norm(difference)
            if distance == 0:
                raise ValueError("overlapping point masses give undefined force")
            a[i] += G_value * masses[j] * difference / distance**3
    return a


# ---------------------------------------------------------------------------
# SECTION 5: CENTER OF MASS AND MOMENTUM
# ---------------------------------------------------------------------------

def center_of_mass(positions: np.ndarray, masses: np.ndarray) -> np.ndarray:
    """Weighted average location: sum_i(m_i*r_i)/sum_i(m_i)."""
    return np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)


def total_momentum(velocities: np.ndarray, masses: np.ndarray) -> np.ndarray:
    """Vector momentum: sum_i m_i*v_i. Useful in later orbit calculations."""
    return np.sum(masses[:, None] * velocities, axis=0)


# ---------------------------------------------------------------------------
# SECTION 6: CREATE A PHYSICAL EXPLANATION AND A STATIC VISUAL
# ---------------------------------------------------------------------------

def make_report(masses, positions, velocities, a) -> str:
    lines = [
        "OBJECTIVE 01 — NEWTONIAN GRAVITY AT A SINGLE INSTANT",
        "=" * 58,
        "Units are normalized: G = 1. This is NOT an orbital simulation yet.",
        "",
        "Each body has a mass m, position r=(x,y), velocity v=(vx,vy),",
        "and an acceleration a=(ax,ay) caused by other objects.",
        "",
    ]
    for i, name in enumerate(NAMES):
        lines += [
            f"{name}:",
            f"  mass             = {masses[i]:.6f}",
            f"  position         = {positions[i]}",
            f"  velocity         = {velocities[i]}",
            f"  acceleration     = {a[i]}",
            f"  |acceleration|   = {np.linalg.norm(a[i]):.9f}",
            "",
        ]

    lines += ["PAIRWISE FORCES (Newton's third law)"]
    for i in range(len(masses)):
        for j in range(i + 1, len(masses)):
            force_ij = gravitational_force_on_i_from_j(
                positions[i], positions[j], masses[i], masses[j]
            )
            force_ji = gravitational_force_on_i_from_j(
                positions[j], positions[i], masses[j], masses[i]
            )
            lines.append(f"  {NAMES[j]} on {NAMES[i]}: {force_ij}")
            lines.append(f"  {NAMES[i]} on {NAMES[j]}: {force_ji}")
            lines.append(f"  Sum (approximately zero): {force_ij + force_ji}")

    com = center_of_mass(positions, masses)
    p = total_momentum(velocities, masses)
    net_internal_force = np.sum(masses[:, None] * a, axis=0)
    lines += [
        "",
        f"Center of mass = {com}",
        f"Total momentum = {p}",
        f"Sum of all gravitational forces = {net_internal_force}",
        "(The last sum should be approximately zero: internal forces cancel.)",
        "",
        "WHAT TO NOTICE:",
        "* The arrow for acceleration points toward the combined pull of other bodies.",
        "* A large mass can have a small acceleration, even when its force is real.",
        "* Acceleration is not the same as velocity; a body can move in one",
        "  direction while gravity bends its motion toward another direction.",
        "* None of this yet proves whether an orbit is stable or chaotic.",
    ]
    return "\n".join(lines)


def make_figure(masses, positions, velocities, accelerations, output_path):
    """Draw current positions, blue velocity arrows, and red gravity arrows."""
    fig, ax = plt.subplots(figsize=(9.3, 7.0))
    fig.patch.set_facecolor("#08152b")
    ax.set_facecolor("#0e1f38")

    # Arrow scaling is VISUAL ONLY. Physical values appear in the report.
    velocity_scale = 0.43
    gravity_scale = 0.34 / max(np.linalg.norm(accelerations, axis=1).max(), 1e-12)
    colors = ("#f7c96d", "#8fd1ff", "#d7a5ff")

    for i, name in enumerate(NAMES):
        x, y = positions[i]
        marker_size = 340 if i == 0 else 115
        ax.scatter(x, y, s=marker_size, c=colors[i], edgecolor="white",
                   linewidth=0.8, zorder=5)
        ax.annotate(name, (x, y), xytext=(10, 13), textcoords="offset points",
                    color="white", fontsize=11, weight="bold")
        ax.arrow(x, y, velocities[i, 0] * velocity_scale,
                 velocities[i, 1] * velocity_scale,
                 color="#6bc4e9", width=0.008, head_width=0.045,
                 length_includes_head=True, zorder=4)
        ax.arrow(x, y, accelerations[i, 0] * gravity_scale,
                 accelerations[i, 1] * gravity_scale,
                 color="#ff806b", width=0.008, head_width=0.045,
                 length_includes_head=True, zorder=4)

    com = center_of_mass(positions, masses)
    ax.scatter(*com, s=100, marker="x", c="white", linewidths=2, zorder=6)
    ax.text(0.02, 0.03, "BLUE = velocity     CORAL = gravity acceleration     X = center of mass",
            transform=ax.transAxes, color="white", fontsize=10,
            bbox=dict(facecolor="#102b47", edgecolor="none", alpha=0.9, pad=8))
    ax.set_xlim(-0.5, 1.7)
    ax.set_ylim(-0.5, 2.15)
    ax.set_aspect("equal")
    ax.set_xlabel("x (normalized length)", color="white")
    ax.set_ylabel("y (normalized length)", color="white")
    ax.set_title("Objective 01 | A Snapshot of a Three-Body System",
                 color="white", fontsize=15, pad=18)
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#7c97b1")
    ax.grid(alpha=0.17, color="white", linestyle="--")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    validate_system(MASSES, POSITIONS, VELOCITIES)
    accelerations = gravitational_accelerations(POSITIONS, MASSES)

    # A physics sanity check, not a quiz: internal gravity must sum to zero.
    net_force = np.sum(MASSES[:, None] * accelerations, axis=0)
    if not np.allclose(net_force, [0.0, 0.0], atol=1e-12, rtol=0):
        raise AssertionError("The computed internal forces do not cancel")

    output_dir = Path(__file__).resolve().parent / "objective_01_output"
    output_dir.mkdir(exist_ok=True)
    report = make_report(MASSES, POSITIONS, VELOCITIES, accelerations)
    (output_dir / "results.txt").write_text(report + "\n", encoding="utf-8")
    make_figure(MASSES, POSITIONS, VELOCITIES, accelerations,
                output_dir / "acceleration_vectors.png")
    print(report)
    print(f"\nSaved diagram and text report to: {output_dir}")


if __name__ == "__main__":
    main()
