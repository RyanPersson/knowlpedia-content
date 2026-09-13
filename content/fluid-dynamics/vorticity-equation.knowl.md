+++
id = "fluid-dynamics/vorticity-equation"
title = "Vorticity equation for incompressible flow"
kind = "identity"
summary = "The curl of the momentum equation, with transport, vortex stretching, diffusion, and curl of forcing."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/vorticity", "fluid-dynamics/navier-stokes-equations", "fluid-dynamics/material-derivative", "real-analysis/schwarz-clairaut-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a smooth three-dimensional solution of the [[fluid-dynamics/navier-stokes-equations|incompressible Navier–Stokes equations]] with constant \(\nu\), the [[fluid-dynamics/vorticity|vorticity]] satisfies
\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega+\nabla\times f.
\]
The term \((\omega\cdot\nabla)u\) is vortex stretching and tilting. For the Euler equations, take \(\nu=0\).

## Derivation

Take curl of the momentum equation. The pressure gradient has zero curl, curl commutes with time derivatives and the Laplacian, and
\[
\nabla\times((u\cdot\nabla)u)
=(u\cdot\nabla)\omega-(\omega\cdot\nabla)u
\]
when \(\nabla\cdot u=0\). The identity follows by expanding components, or by writing \((u\cdot\nabla)u=\nabla(|u|^2/2)-u\times\omega\).

## Planar flows

For a two-dimensional velocity independent of the third coordinate, the stretching term vanishes. The scalar vorticity then obeys a transport-diffusion equation with the corresponding scalar curl of the force.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
