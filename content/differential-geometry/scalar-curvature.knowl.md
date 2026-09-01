+++
id = "differential-geometry/scalar-curvature"
title = "Scalar curvature"
kind = "definition"
summary = "The metric trace of the Ricci curvature."
aliases = ["Ricci scalar", "scalar curvature function"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/pseudo-riemannian-manifold", "differential-geometry/ricci-curvature", "differential-geometry/riemann-curvature-tensor"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/pseudo-riemannian-manifold|pseudo-Riemannian manifold]]. Its **scalar curvature** is the smooth function
\[
\operatorname{Scal}_g=\operatorname{tr}_g(\operatorname{Ric})
=g^{ij}\operatorname{Ric}_{ij},
\]
obtained by contracting the [[differential-geometry/ricci-curvature|Ricci tensor]] with the inverse metric.

Scalar curvature is a single contraction of the curvature tensor and therefore does not determine the full curvature in dimensions greater than two. Its sign depends on the sign convention for the [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]]. The convention here agrees with the linked Ricci-curvature knowl.

## Applications

Scalar curvature appears as the curvature term in [[mathematical-physics/conformal-coupling-of-a-scalar-field|conformal scalar coupling]] and in geometric operators such as the conformal Laplacian.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7.
