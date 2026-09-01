+++
id = "differential-geometry/boundary-defining-function"
title = "Boundary defining function"
kind = "definition"
summary = "A smooth nonnegative function that vanishes simply and exactly on the boundary of a manifold."
aliases = ["defining function for a boundary", "local boundary defining function"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/manifold-with-boundary", "fiber-bundles/regular-value"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]]. A **boundary defining function** is a smooth function \(\rho:M\to[0,\infty)\) such that
\[
\rho^{-1}(0)=\partial M
\qquad\text{and}\qquad
d\rho_p\neq0\quad\text{for every }p\in\partial M.
\]
Equivalently, \(0\) is a [[fiber-bundles/regular-value|regular value]] of \(\rho\) and its zero set is exactly the boundary. A local boundary defining function on an open set \(U\subseteq M\) satisfies the same conditions with \(\partial M\cap U\) in place of \(\partial M\). Nonnegativity fixes which side of the regular hypersurface belongs to \(M\).

## Local normal form

The regular-value condition implies that near every [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]] there are boundary coordinates
\[
(x^1,\ldots,x^{n-1},r),\qquad r\geq0,
\]
in which \(\rho=r\). Consequently \(d\rho\) spans the conormal line of the boundary. Conversely, the final coordinate in any [[differential-geometry/boundary-chart|boundary chart]] is a local defining function. This local normal form is the reason the nonvanishing differential, rather than mere set-theoretic vanishing, belongs in the definition.

## Existence and comparison

Every smooth manifold with boundary admits a global boundary defining function. One construction starts from a [[differential-geometry/collar-neighborhood-theorem|collar]], uses its inward coordinate near the boundary, and extends it to a positive function on the remaining interior. If \(\rho\) and \(\rho'\) are two defining functions, then near the boundary
\[
\rho'=a\rho
\]
for a smooth positive function \(a\). Thus their first-order vanishing agrees up to a positive scale, while their extensions deep in the interior may be unrelated.

## Examples and non-examples

On the half-space \(\mathbb H^n\), the last coordinate \(x^n\) is a boundary defining function. On the closed unit ball, \(\rho(x)=1-\lVert x\rVert^2\) is one because its differential is nonzero on the sphere.

The function \((x^n)^2\) has the correct zero set on \(\mathbb H^n\) but is not a defining function: its differential vanishes along the boundary. A signed defining function on a larger manifold containing the boundary hypersurface is also not nonnegative on both sides; restricting it to the chosen side recovers the convention used here.

## References

1. Richard B. Melrose, *The Atiyah–Patodi–Singer Index Theorem*, A K Peters/CRC Press, 1993. [Publisher DOI record](https://doi.org/10.1201/9781439864609). Relevant: Chapter 1, boundary defining functions and product structures.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: manifolds with boundary, regular level sets, and collar neighborhoods.
