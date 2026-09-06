+++
id = "fiber-bundles/dual-connection"
title = "Dual connection"
kind = "definition"
summary = "The unique connection on a dual vector bundle for which differentiation obeys the natural evaluation pairing."
aliases = ["connection on the dual bundle", "contragredient connection"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/dual-vector-bundle", "fiber-bundles/vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\), and let \(E^*\to M\) be its [[fiber-bundles/dual-vector-bundle|dual vector bundle]]. The **dual connection** \(\nabla^*\) is the unique connection on \(E^*\) satisfying
\[
X\!\left(\lambda(s)\right)
=
\left(\nabla_X^*\lambda\right)(s)+\lambda\!\left(\nabla_Xs\right)
\]
for every [[fiber-bundles/vector-field|vector field]] \(X\), section \(s\) of \(E\), and section \(\lambda\) of \(E^*\). Equivalently,
\[
\left(\nabla_X^*\lambda\right)(s)
=X\!\left(\lambda(s)\right)-\lambda\!\left(\nabla_Xs\right).
\]
The defining identity says exactly that the natural evaluation pairing \(E^*\otimes E\to M\times\mathbb R\) is parallel.

## Local expression

If \(e_1,\ldots,e_r\) is a local frame, \(e^1,\ldots,e^r\) its dual frame, and
\[
\nabla e_j=\sum_i A^i{}_j\otimes e_i,
\]
then
\[
\nabla^*e^i=-\sum_j A^i{}_j\otimes e^j.
\]
Thus the connection matrix on the dual frame is \(-A^{\mathsf T}\). The minus sign is forced by differentiating \(e^i(e_j)=\delta^i_j\).

## Curvature

Using the convention \(R^\nabla(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}\), the dual curvature satisfies
\[
\left(R^{\nabla^*}(X,Y)\lambda\right)(s)
=-\lambda\!\left(R^\nabla(X,Y)s\right).
\]
Hence the curvature matrix of the dual connection is the negative transpose of the original curvature matrix.

## Conventions and scope

**Warning.** The superscript star denotes dualization here, not a Hermitian adjoint. For a [[fiber-bundles/complex-vector-bundle|complex vector bundle]], the complex-linear dual and the conjugate dual are different bundles; the displayed definition applies to the chosen dual pairing. Curvature signs must be adjusted if the opposite convention for \(R^\nabla\) is used.

## References

1. Loring W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55084-8). Relevant: induced connections on dual and tensor bundles.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter II, covariant differentiation on associated tensor bundles.
