+++
id = "functional-analysis/continuous-linear-map"
title = "Continuous linear map between topological vector spaces"
kind = "definition"
summary = "A linear map that is continuous for the given vector-space topologies."
aliases = ["continuous linear operator", "continuous linear transformation"]
domains = ["functional-analysis", "topology", "linear-algebra"]
section_mode = "progressive"
prerequisites = ["functional-analysis/topological-vector-space", "linear-algebra/linear-map", "topology/neighborhood"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) and \(F\) be [[functional-analysis/topological-vector-space|topological vector spaces]] over the same field. A **continuous linear map** \(T:E\to F\) is a [[linear-algebra/linear-map|linear map]] that is continuous for the given topologies. Linearity makes continuity at one point equivalent to continuity everywhere. In particular, \(T\) is continuous exactly when, for every [[topology/neighborhood|neighborhood]] \(V\) of \(0\) in \(F\), there is a neighborhood \(U\) of \(0\) in \(E\) such that
\[
T(U)\subseteq V.
\]
Thus continuity compares the chosen topologies on the source and target; it is not an algebraic property of the underlying linear map.

## Normed-space specialization

If \(E\) and \(F\) are [[linear-algebra/normed-vector-space|normed vector spaces]], continuity is equivalent to the existence of \(C\geq 0\) such that
\[
\lVert Tx\rVert_F\leq C\lVert x\rVert_E
\qquad (x\in E).
\]
This familiar bounded-operator criterion is a special feature of norm topologies. For general topological vector spaces, continuity is expressed with zero-neighborhoods or families of seminorms rather than one [[linear-algebra/operator-norm|operator norm]].

## Locally convex criterion

Suppose \(E\) and \(F\) are [[functional-analysis/locally-convex-space|locally convex]]. For every continuous [[convex-analysis/seminorm|seminorm]] \(q\) on \(F\), continuity of \(T\) implies that there are continuous seminorms \(p_1,\ldots,p_n\) on \(E\) and \(C>0\) with
\[
q(Tx)\leq C\max_{1\leq j\leq n}p_j(x).
\]
Conversely, such estimates for a defining family of seminorms on \(F\) imply continuity. This is the standard form used for spaces of smooth functions and distributions.

## Categorical role

Identity maps and composites of continuous linear maps are continuous and linear. Topological vector spaces with these maps therefore form a category. A linear bijection need not be an isomorphism in this category: its inverse must also be continuous.

## References

1. Nicolas Bourbaki, *Topological Vector Spaces: Chapters 1–5*, Springer, 2003. [Springer DOI record](https://doi.org/10.1007/978-3-642-61715-7). Relevant: Chapters I and III.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter III, “Linear Mappings.”
