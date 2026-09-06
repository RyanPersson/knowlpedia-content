+++
id = "langlands/dominant-coweight"
title = "Dominant coweight"
kind = "definition"
summary = "A cocharacter pairing nonnegatively with every positive root determined by a Borel subgroup."
aliases = ["dominant cocharacter"]
domains = ["langlands", "representation-theory"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/borel-subgroup", "lie-groups/positive-root", "langlands/affine-grassmannian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], choose a maximal torus
\(T\subseteq B\) in a [[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]], and let \(\Phi^+\) be the resulting
[[lie-groups/positive-root|positive roots]]. A coweight \(\lambda\in X_*(T)\) is **dominant** if
\[
\langle\alpha,\lambda\rangle\geq 0
\qquad\text{for every }\alpha\in\Phi^+.
\]

Every Weyl-group orbit in \(X_*(T)\) contains a unique dominant coweight.
Dominant coweights index the positive-loop-group orbits on the
[[langlands/affine-grassmannian|affine Grassmannian]].

## References

1. T. A. Springer, *Linear Algebraic Groups*, 2nd ed., Birkhäuser, 1998,
   Chapters 7–8.
