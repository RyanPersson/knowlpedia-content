+++
id = "fluid-dynamics/navier-stokes-equations"
title = "Incompressible Navier–Stokes equations"
kind = "definition"
summary = "The constant-density momentum equation with quadratic advection, pressure, positive viscosity, forcing, and zero divergence."
aliases = ["Navier–Stokes equations", "forced Navier-Stokes equations", "incompressible NSE"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/partial-differential-equation", "fluid-dynamics/material-derivative", "fluid-dynamics/incompressible-flow", "fluid-dynamics/pressure-field", "fluid-dynamics/viscosity", "fluid-dynamics/external-force", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **incompressible Navier–Stokes equations** with constant kinematic viscosity \(\nu>0\) are
\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u+f,
\qquad \nabla\cdot u=0.
\]
Here \(u(t,x)\in\mathbb R^d\) is velocity, \(p(t,x)\) is [[fluid-dynamics/pressure-field|normalized pressure]], \(f\) is prescribed forcing, and the Laplacian acts on each Cartesian velocity component.

## Data and domain

An evolution problem also specifies an [[partial-differential-equations/initial-datum|initial velocity]] \(u_0\), normally divergence free, and a spatial domain. Common choices are \(\mathbb R^d\), a periodic box, or a bounded domain with boundary conditions. Setting \(f=0\) gives the unforced equation; it does not follow from \(u_0=0\).

## Meaning of solution

A [[partial-differential-equations/classical-solution|classical solution]] satisfies these relations pointwise with sufficient derivatives. Weaker formulations impose integral identities and additional function-space hypotheses. A regularity assertion must specify which formulation, data, forcing, and dimension it concerns.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
- [Charles L. Fefferman, Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
