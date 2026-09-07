+++
id = "differential-geometry/gaussian-curvature"
title = "Gaussian curvature"
kind = "definition"
summary = "The intrinsic sectional curvature of a Riemannian surface at each point."
aliases = ["curvature of a surface", "Gauss curvature"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/sectional-curvature"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 1
+++

Let \((S,g)\) be a two-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]]. Its **Gaussian curvature** is the function \(K:S\to\mathbb R\) whose value at \(p\) is the [[differential-geometry/sectional-curvature|sectional curvature]] of the unique two-plane \(T_pS\):
\[
K(p)=K_g(T_pS).
\]

## Curvature tensor formula

For an orthonormal basis \(e_1,e_2\) of \(T_pS\), using the stated [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]] convention,
\[
K(p)=g(R(e_1,e_2)e_2,e_1).
\]

## Intrinsic and extrinsic descriptions

The value \(K(p)\) depends only on the metric near \(p\), not on an embedding of \(S\) in Euclidean space. If \(S\) is embedded as a regular surface in \(\mathbb R^3\), then \(K\) is also the product of the two principal curvatures, with the usual induced metric.

## Examples and consequences

The Euclidean plane has \(K=0\), the unit round sphere has \(K=1\), and the hyperbolic plane of curvature \(-1\) has \(K=-1\). For a closed oriented Riemannian surface, the [[fiber-bundles/chern-gauss-bonnet-theorem|Chern–Gauss–Bonnet theorem]] gives
\[
\frac{1}{2\pi}\int_S K\,\operatorname{vol}_g=\chi(S).
\]

## Sign convention

Changing the overall sign convention for the Riemann curvature tensor changes the sign of \(K\). The convention here is the one displayed in the [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]] and [[differential-geometry/sectional-curvature|sectional curvature]] knowls.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7.
2. Manfredo P. do Carmo, *Differential Geometry of Curves and Surfaces*, Prentice Hall, 1976. Relevant: Chapters 4–5, Gaussian curvature and the Theorema Egregium.
