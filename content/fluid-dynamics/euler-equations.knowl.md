+++
id = "fluid-dynamics/euler-equations"
title = "Incompressible Euler equations"
kind = "definition"
summary = "The constant-density inviscid fluid equations, with pressure, advection, forcing, and zero divergence."
aliases = ["Euler equations", "inviscid incompressible flow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/material-derivative", "fluid-dynamics/incompressible-flow", "fluid-dynamics/pressure-field", "fluid-dynamics/external-force"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **incompressible Euler equations** are
\[
\partial_tu+(u\cdot\nabla)u+\nabla p=f,
\qquad\nabla\cdot u=0.
\]
They model constant-density inviscid motion: the momentum equation contains no viscous stress. Initial data, the spatial domain, boundary conditions, and the solution class are additional parts of an Euler problem.

## Relation to viscosity

Formally setting \(\nu=0\) in the [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equations]] gives this system. Justifying convergence of viscous solutions as \(\nu\downarrow0\) is a separate limiting problem, particularly near boundaries.

## Terminology

“Euler equations” can also refer to compressible fluid systems. The divergence-free, constant-density version is the one specified here.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
