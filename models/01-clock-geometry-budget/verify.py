#!/usr/bin/env python3
"""Numerical sanity checks for DEM Toy Model 01 — Clock/Geometry Budget.

No third-party dependencies are required.

This script does not prove the model. It verifies that the documented formulas
reproduce the intended special-relativistic identities for representative and
randomized inputs.
"""

from __future__ import annotations

from math import isclose, sqrt
from random import Random


C_STAR = 299_792_458.0


def gamma(v: float, c_star: float = C_STAR) -> float:
    beta2 = (v / c_star) ** 2
    if beta2 >= 1.0:
        raise ValueError("gamma requires |v| < c_star")
    return 1.0 / sqrt(1.0 - beta2)


def proper_time(dt: float, v: float, c_star: float = C_STAR) -> float:
    return dt / gamma(v, c_star)


def lorentz_transform(
    t: float,
    x: float,
    u: float,
    c_star: float = C_STAR,
) -> tuple[float, float]:
    g = gamma(u, c_star)
    t_prime = g * (t - u * x / c_star**2)
    x_prime = g * (x - u * t)
    return t_prime, x_prime


def interval_sq(t: float, x: float, c_star: float = C_STAR) -> float:
    return c_star**2 * t**2 - x**2


def energy_momentum(
    mass: float,
    v: float,
    c_star: float = C_STAR,
) -> tuple[float, float]:
    g = gamma(v, c_star)
    momentum = g * mass * v
    energy = g * mass * c_star**2
    return energy, momentum


def assert_close(a: float, b: float, *, rel_tol: float = 1e-11) -> None:
    if not isclose(a, b, rel_tol=rel_tol, abs_tol=rel_tol):
        raise AssertionError(f"{a!r} != {b!r}")


def check_time_dilation() -> None:
    samples = [
        (0.0, 1.0),
        (0.6, 0.8),
        (0.8, 0.6),
        (0.99, sqrt(1.0 - 0.99**2)),
    ]

    for beta, expected_ratio in samples:
        ratio = proper_time(1.0, beta * C_STAR)
        assert_close(ratio, expected_ratio)


def check_interval_invariance() -> None:
    rng = Random(20260910)

    for _ in range(10_000):
        t = rng.uniform(-10.0, 10.0)
        x = rng.uniform(-2.0 * C_STAR, 2.0 * C_STAR)
        u = rng.uniform(-0.95, 0.95) * C_STAR

        t_prime, x_prime = lorentz_transform(t, x, u)

        before = interval_sq(t, x)
        after = interval_sq(t_prime, x_prime)

        assert_close(before, after, rel_tol=1e-9)


def check_dispersion_relation() -> None:
    rng = Random(20260911)

    for _ in range(10_000):
        mass = 10 ** rng.uniform(-3.0, 3.0)
        v = rng.uniform(-0.999, 0.999) * C_STAR
        energy, momentum = energy_momentum(mass, v)

        lhs = energy**2 - momentum**2 * C_STAR**2
        rhs = mass**2 * C_STAR**4

        assert_close(lhs, rhs, rel_tol=1e-9)


def check_metric_ratio() -> None:
    # If g_kappa / g_x = c_*^2, the documented mode-budget equation
    # reduces exactly to d_tau^2 = dt^2 - dx^2 / c_*^2.
    g_x = 7.0
    g_kappa = g_x * C_STAR**2

    dt = 3.0
    v = 0.73 * C_STAR
    dx = v * dt
    d_tau = proper_time(dt, v)

    lhs = g_kappa * d_tau**2 + g_x * dx**2
    rhs = g_kappa * dt**2

    assert_close(lhs, rhs, rel_tol=1e-11)


def main() -> None:
    check_time_dilation()
    check_interval_invariance()
    check_dispersion_relation()
    check_metric_ratio()

    print("DEM Toy Model 01 checks passed")
    print("  time dilation:          OK")
    print("  Lorentz interval:       OK (10,000 randomized checks)")
    print("  energy-momentum:        OK (10,000 randomized checks)")
    print("  metric-ratio budget:    OK")


if __name__ == "__main__":
    main()
