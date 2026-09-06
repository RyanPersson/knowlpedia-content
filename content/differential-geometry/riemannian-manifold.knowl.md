+++
id = "differential-geometry/riemannian-manifold"
title = "Riemannian manifold"
kind = "definition"
summary = "A smooth manifold equipped with a smoothly varying positive-definite inner product on its tangent spaces."
aliases = ["Riemannian metric on a manifold", "Riemannian structure", "Riemannian metric manifold"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "linear-algebra/inner-product", "fiber-bundles/bundle-metric", "fiber-bundles/tangent-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. A **Riemannian metric** on \(M\) is a smooth symmetric covariant \(2\)-tensor \(g\) such that \(g_p\) is a positive-definite [[linear-algebra/inner-product|inner product]] on \(T_pM\) for every \(p\in M\). Equivalently, \(g\) is a [[fiber-bundles/bundle-metric|bundle metric]] on the [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\). A **Riemannian manifold** is a pair \((M,g)\). In local coordinates, \(g=g_{ij}\,dx^i\otimes dx^j\), where the matrix \((g_{ij}(p))\) is symmetric positive definite at every point and each coefficient \(g_{ij}\) is smooth.

## Metric and volume constructions

The metric assigns each tangent vector a length \(\lVert v\rVert_g=\sqrt{g(v,v)}\) and each piecewise smooth curve \(\gamma\) a length
\[
L_g(\gamma)=\int \sqrt{g_{\gamma(t)}(\dot\gamma(t),\dot\gamma(t))}\,dt.
\]
Taking the infimum of curve lengths gives the Riemannian distance on each [[topology/connected-component|connected component]]. The metric also identifies \(TM\) with the [[fiber-bundles/cotangent-bundle|cotangent bundle]] and determines a canonical volume density; an orientation turns this density into a volume form.

## Canonical connection and curvature

Every Riemannian metric has a unique torsion-free, metric-compatible connection, the [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]]. It determines geodesics, parallel transport, and [[fiber-bundles/curvature|curvature]]. These structures depend on derivatives of \(g\), whereas lengths and angles are pointwise data.

## Examples and scope

The Euclidean metric \(\sum_i dx^i\otimes dx^i\) is the standard example on \(\mathbb R^n\). An immersion into [[linear-algebra/euclidean-space|Euclidean space]] pulls this metric back to a Riemannian metric when its differential is injective. Positive definiteness distinguishes Riemannian metrics from pseudo-Riemannian metrics, whose nondegenerate symmetric forms may have mixed signature. Smoothness is essential: an arbitrary choice of an inner product on each [[differential-geometry/tangent-space|tangent space]] does not necessarily define a Riemannian metric.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Graduate Texts in Mathematics 176, Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapters 2–5.
2. Manfredo P. do Carmo, *Riemannian Geometry*, Mathematics: Theory & Applications, Birkhäuser, 1992. [Publisher record](https://doi.org/10.1007/978-1-4757-2201-7). Relevant: Chapters 0–3.
