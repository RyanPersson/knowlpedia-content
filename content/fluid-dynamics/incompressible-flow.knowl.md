+++
id = "fluid-dynamics/incompressible-flow"
title = "Incompressible velocity field"
kind = "definition"
summary = "A differentiable fluid velocity field with zero spatial divergence."
aliases = ["incompressible flow", "incompressibility"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/divergence-free-field"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A differentiable fluid velocity field is **incompressible** when
\[
\nabla_x\cdot u(t,x)=0
\]
throughout its domain. Thus each time slice is a [[real-analysis/divergence-free-field|divergence-free vector field]].

## Volume interpretation

For a smooth flow map, the Jacobian determinant satisfies
\[
\partial_t\det D_aX(t;s,a)
=(\nabla\cdot u)(t,X(t;s,a))\det D_aX(t;s,a).
\]
Since the determinant initially equals one, incompressibility preserves local volume while the flow map exists. The identity follows by differentiating the trajectory equation in \(a\) and using the determinant derivative formula.

## Density convention

The standard homogeneous incompressible model also assumes constant positive density. Divergence freedom is the kinematic constraint; constant density and the constitutive law are additional modeling assumptions.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
