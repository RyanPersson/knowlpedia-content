+++
id = "fluid-dynamics/rate-of-strain"
title = "Rate-of-strain tensor"
kind = "definition"
summary = "The symmetric part of the spatial velocity gradient."
aliases = ["strain-rate tensor", "symmetric velocity gradient"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/jacobian-matrix", "linear-algebra/matrix-transpose", "linear-algebra/symmetric-matrix"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a differentiable velocity field, the **rate-of-strain tensor** is the symmetric matrix
\[
D(u)=\frac12\bigl(\nabla u+(\nabla u)^{\mathsf T}\bigr),
\qquad
D(u)_{ij}=\frac12(\partial_j u_i+\partial_i u_j).
\]
Here \(\nabla u\) denotes the [[real-analysis/jacobian-matrix|velocity Jacobian]], with \((\nabla u)_{ij}=\partial_j u_i\).

## Infinitesimal deformation

If two nearby particles have infinitesimal separation \(\xi\), then \(\dot\xi=(\nabla u)\xi\) and
\[
\frac{d}{dt}|\xi|^2=2\xi^{\mathsf T}D(u)\xi.
\]
The skew-symmetric part of the gradient contributes local rotation but not this change in squared length. Incompressibility implies \(\operatorname{tr}D(u)=0\).

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
