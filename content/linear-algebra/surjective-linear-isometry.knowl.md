+++
id = "linear-algebra/surjective-linear-isometry"
title = "Surjective linear isometry"
kind = "knowl"
summary = "A bijective linear map that preserves the norm exactly."
aliases = ["surjective linear isometry", "linear isometric equivalence", "linear isometry group"]
domains = ["linear-algebra", "topology"]
prerequisites = ["linear-algebra/normed-vector-space", "linear-algebra/linear-map"]
dependency_review_count = 1
+++

Let \(E\) and \(F\) be [[linear-algebra/normed-vector-space|normed vector spaces]]. A **surjective linear isometry** is a surjective [[linear-algebra/linear-map|linear map]] \(T:E\to F\) satisfying
\[
\lVert Tx\rVert=\lVert x\rVert
\]
for every \(x\in E\). Norm preservation makes \(T\) injective, so it is a bijection and its inverse is also a linear isometry.

When \(E=F\), these maps form a group under composition and act on the [[linear-algebra/unit-sphere|unit sphere]]. Two normed spaces are linearly isometric when such a map exists between them.
