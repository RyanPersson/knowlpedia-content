+++
id = "differential-geometry/sectional-curvature"
title = "Sectional curvature"
kind = "definition"
summary = "The curvature assigned by a Riemannian metric to each two-dimensional tangent plane."
aliases = ["section curvature"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/riemann-curvature-tensor"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 1
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]] and let \(P=\operatorname{span}(u,v)\subset T_pM\) be a two-dimensional plane in the [[differential-geometry/tangent-space|tangent space]] at \(p\). With the [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]] convention
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z,
\]
the **sectional curvature** of \(P\) is
\[
K_g(P)=\frac{g(R(u,v)v,u)}{g(u,u)g(v,v)-g(u,v)^2}.
\]
## Basis independence

The denominator is the squared area of the parallelogram spanned by \(u,v\), so the quotient is independent of the chosen basis of \(P\).

## Geometric meaning

Sectional curvature is the intrinsic curvature of the geodesic two-plane determined by \(P\), measured to second order by the metric. A metric has constant sectional curvature \(k\) when \(K_g(P)=k\) for every point and every tangent two-plane. In dimension two, sectional curvature is the Gaussian curvature.

## Relation to Ricci curvature

For a unit vector \(u\) and an orthonormal basis \(u,e_2,\ldots,e_n\) of \(T_pM\),
\[
\operatorname{Ric}(u,u)=\sum_{j=2}^n K_g(\operatorname{span}(u,e_j)).
\]
Thus Ricci curvature records the sum of sectional curvatures of planes containing a direction, while sectional curvature retains the individual two-plane information.

## Sign convention

Some authors define the Riemann tensor with the opposite overall sign, which reverses every sectional curvature. The displayed formula and the linked [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]] convention fix the sign used here.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7, sectional curvature.
2. Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992. [Publisher record](https://doi.org/10.1007/978-1-4757-2201-7). Relevant: Chapter 3, sectional curvature.
