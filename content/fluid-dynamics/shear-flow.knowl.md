+++
id = "fluid-dynamics/shear-flow"
title = "Parallel shear flow"
kind = "definition"
summary = "A velocity in one fixed direction whose magnitude varies in a transverse coordinate."
aliases = ["shear flow", "parallel flow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/partial-derivative", "fluid-dynamics/vorticity"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A planar [[fluid-dynamics/velocity-field|velocity field]] called a **parallel shear flow** has the form
\[
u(x_1,x_2,x_3)=(U(x_2),0,0),
\]
where the velocity is parallel to a fixed direction and its speed varies transversely. It is incompressible, and \(U'(x_2)\) measures its shear. Its vorticity is \((0,0,-U'(x_2))\).

## Advection and evolution

For this profile, \((u\cdot\nabla)u=0\), since the field is independent of \(x_1\). Allowing \(U=U(t,x_2)\), the unforced Navier–Stokes equation with constant pressure reduces to \(\partial_tU=\nu\partial_{x_2}^2U\).

## Terminology

Shear can also describe differential motion in more general geometries. In a rotating flow, variation of angular velocity with radius is differential rotation, and its shear expressions include the cylindrical geometry.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
