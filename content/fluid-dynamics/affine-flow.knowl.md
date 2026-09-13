+++
id = "fluid-dynamics/affine-flow"
title = "Affine velocity field"
kind = "definition"
summary = "A velocity field affine in position, with a time-dependent matrix and translation vector."
aliases = ["affine background flow"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "linear-algebra/matrix", "linear-algebra/trace", "linear-algebra/symmetric-matrix", "linear-algebra/quadratic-form"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **affine velocity field** on \(\mathbb R^d\) has the form
\[
u(t,x)=A(t)x+b(t),
\]
with a [[linear-algebra/matrix|matrix]] \(A(t)\) and vector \(b(t)\). It is incompressible exactly when \(\operatorname{tr}A(t)=0\).

## Exact momentum calculation

For differentiable \(A,b\),
\[
\partial_tu+(u\cdot\nabla)u
=(A'+A^2)x+b'+Ab,
\qquad \Delta u=0.
\]
If \(\operatorname{tr}A=0\) and \(S=A'+A^2\) is symmetric, the unforced Euler and Navier–Stokes momentum equations are solved by
\[
p(t,x)=-\tfrac12 x^{\mathsf T}S(t)x-(b'(t)+A(t)b(t))\cdot x,
\]
up to an additive function of time. Conversely, on the whole space a pressure gradient cancelling this affine acceleration requires \(A'+A^2\) to be symmetric.

## Integrability

A nonzero affine velocity on \(\mathbb R^d\) has infinite total kinetic energy. Such fields are still useful as local models or backgrounds; satisfying the local equations does not supply the decay required by a finite-energy whole-space problem.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
