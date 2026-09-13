+++
id = "linear-algebra/moving-frame"
title = "Moving frame for a family of subspaces"
kind = "definition"
summary = "A smoothly varying full-column-rank matrix whose columns span the subspace at each parameter."
aliases = ["frame matrix", "moving basis"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "linear-algebra/left-inverse", "convex-analysis/linearly-independent-and-linearly-dependent-sets", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **moving frame** for a smooth family of \(k\)-dimensional subspaces of \(\mathbb R^n\) is a smooth matrix \(B(q)\in\mathbb R^{n\times k}\) of full column rank whose columns span the subspace at parameter \(q\). A vector in that subspace is uniquely written \(v=B(q)c\); a [[linear-algebra/left-inverse|left inverse]] recovers \(c=L(q)v\).

## Differentiating a frame representation

Along a differentiable parameter curve,
\[
v'=B c'+B'c,
\qquad c'=L(v'-B'c).
\]
The term \(B'c\) records the moving basis. If \(v'=Kv\) and the evolution is compatible with the moving subspaces, then
\[
c'=L(KB-B')c.
\]
Choosing an orthonormal frame gives \(L=B^T\). A nonorthonormal frame instead needs its actual left inverse; the derivative terms persist in either choice.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
