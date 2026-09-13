+++
id = "fluid-dynamics/kinetic-energy-identity"
title = "Global kinetic-energy identity"
kind = "theorem"
summary = "Smooth incompressible flow balances energy change and viscous dissipation against work by the force."
aliases = ["energy equality", "global energy balance"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/local-kinetic-energy-balance", "fluid-dynamics/solenoidal-integration-cancellation", "fluid-dynamics/viscous-dissipation", "real-analysis/fundamental-theorem-of-calculus-i", "topology/flat-torus", "real-analysis/compactly-supported-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a smooth incompressible Navier–Stokes solution on a flat torus, with periodic pressure and force, or on \(\mathbb R^n\) with a fixed compact spatial support for the velocity on each compact time interval, the **kinetic-energy identity** is
\[
\frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(r)\|_2^2\,dr
=\frac12\|u(s)\|_2^2+\int_s^t\int f(r,x)\cdot u(r,x)\,dx\,dr.
\]
It follows by integrating the [[fluid-dynamics/local-kinetic-energy-balance|local balance]]. All fields are smooth where the compact-support integrals are taken.

## Cancellation and scope

Divergence terms have zero integral by the stated support or periodicity conditions. Differentiating the identity gives \(\tfrac12\frac d{dt}\|u\|_2^2+\nu\|\nabla u\|_2^2=\langle f,u\rangle\). Whole-space smoothness and an \(L^2\) bound alone do not justify discarding flux at infinity; decay, approximation, or a separate cutoff argument is needed in that setting.

## References

- [Ryzhik, Lecture notes for Math 256B (2024), §§5–6](https://math.stanford.edu/~ryzhik/notes-256B-24.pdf).
