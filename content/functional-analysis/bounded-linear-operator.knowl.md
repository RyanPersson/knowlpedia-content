+++
id = "functional-analysis/bounded-linear-operator"
title = "Bounded linear operator between normed spaces"
kind = "definition"
summary = "A linear map between normed spaces whose output norm is bounded by a fixed multiple of the input norm."
aliases = ["bounded operator between normed spaces"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/normed-vector-space", "linear-algebra/linear-map", "linear-algebra/operator-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) and \(Y\) be [[linear-algebra/normed-vector-space|normed vector
spaces]] over the same scalar field. A
[[linear-algebra/linear-map|linear map]] \(T:X\to Y\) is a
**bounded linear operator** if there is a constant \(C\geq0\) such that
\[
\lVert Tx\rVert_Y\leq C\lVert x\rVert_X
\qquad\text{for every }x\in X.
\]
The least such constant is the
[[linear-algebra/operator-norm|operator norm]]
\[
\lVert T\rVert=\sup_{\lVert x\rVert_X\leq1}\lVert Tx\rVert_Y.
\]
Boundedness here constrains the image of every vector uniformly; it does not
mean that the set \(T(X)\) is bounded.

## Equivalent continuity conditions

For a linear map between normed spaces, the following are equivalent:

- it is bounded;
- it is continuous at \(0\);
- it is continuous at every point; and
- it maps bounded subsets of \(X\) to bounded subsets of \(Y\).

Thus bounded linear operators are precisely the normed-space instances of
[[functional-analysis/continuous-linear-map|continuous linear maps]]. The
equivalence uses linearity; an arbitrary continuous nonlinear map need not
satisfy a global estimate by \(\lVert x\rVert\).

## Operator spaces

The bounded operators from \(X\) to \(Y\) form a [[linear-algebra/normed-vector-space|normed vector space]]
\(B(X,Y)\) under the operator norm. If \(Y\) is a
[[linear-algebra/banach-space|Banach space]], then \(B(X,Y)\) is Banach,
whether or not \(X\) is complete. When \(X=Y\), composition satisfies
\[
\lVert ST\rVert\leq\lVert S\rVert\lVert T\rVert,
\]
so \(B(X)=B(X,X)\) is a normed algebra and is a
[[functional-analysis/banach-algebra|Banach algebra]] when \(X\) is Banach.

## Examples and scope

Every linear map between finite-dimensional normed spaces is bounded. The
derivative \(D:C^1([0,1])\to C([0,1])\) is bounded when the source carries
the \(C^1\)-norm, but it is not bounded when both spaces are given the
[[real-analysis/supremum-norm|supremum norm]]. On an infinite-dimensional
normed space, discontinuous linear
maps can exist; they are everywhere-defined algebraic operators but are not
bounded linear operators.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter II on normed spaces and bounded operators.
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 4 on continuous linear mappings.
