+++
id = "differential-geometry/ricci-curvature"
title = "Ricci curvature"
kind = "definition"
summary = "The symmetric covariant two-tensor obtained by tracing the Riemann curvature tensor."
aliases = ["Ricci tensor", "Ricci curvature tensor"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/riemann-curvature-tensor"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be an \(n\)-dimensional
[[differential-geometry/riemannian-manifold|Riemannian manifold]], and use the
curvature convention
\(R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z\) from the
[[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]].
The **Ricci curvature** is the covariant \(2\)-tensor
\[
\operatorname{Ric}(X,Y)
=\operatorname{tr}\bigl(Z\mapsto R(Z,X)Y\bigr).
\]
Equivalently, for any local orthonormal frame \(e_1,\ldots,e_n\),
\[
\operatorname{Ric}(X,Y)
=\sum_{i=1}^n g(R(e_i,X)Y,e_i).
\]
This contraction is independent of the chosen orthonormal frame and is
symmetric. It records the curvature averaged over directions orthogonal to a
given tangent direction.

## Geometric meaning

For a unit tangent vector \(X\), extend \(X\) to an [[linear-algebra/orthonormal-basis|orthonormal basis]]
\(X,e_2,\ldots,e_n\). Then
\[
\operatorname{Ric}(X,X)=\sum_{i=2}^n K(X,e_i),
\]
so Ricci curvature averages the sectional curvatures of planes containing
\(X\). It retains less directional information than the full Riemann tensor
but controls volume distortion, geodesic focusing, and the Bochner formula.

## Contractions and special metrics

Taking the metric trace of \(\operatorname{Ric}\) gives the scalar curvature
\(\operatorname{Scal}\). A metric is Einstein when
\(\operatorname{Ric}=\lambda g\) for a function \(\lambda\); in dimension at
least three, the contracted Bianchi identity forces \(\lambda\) to be constant
on each [[topology/connected-component|connected component]]. This is the contracted form of the
[[fiber-bundles/bianchi-identity|Bianchi identity]]. A metric is Ricci-flat when
\(\operatorname{Ric}=0\). Ricci-flatness does not imply that the full Riemann
tensor vanishes in dimensions four and higher.

## Examples and conventions

On an \(n\)-manifold of constant sectional curvature \(k\),
\[
\operatorname{Ric}=(n-1)k\,g.
\]
Thus the unit round sphere has positive Ricci curvature and [[linear-algebra/euclidean-space|Euclidean space]] has
zero Ricci curvature. In dimension two,
\(\operatorname{Ric}=K g\), so Ricci curvature and Gaussian curvature contain
the same information.

**Warning.** Reversing the sign convention for \(R\) reverses
\(\operatorname{Ric}\). Slot order also varies in the literature, so a Ricci
formula should be read together with its displayed curvature convention.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 1 on curvature conventions, contractions, and Einstein metrics.
2. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7, “Curvature,” on Ricci and scalar curvature.
