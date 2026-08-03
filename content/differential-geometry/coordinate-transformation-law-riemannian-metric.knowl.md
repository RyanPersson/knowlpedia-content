+++
id = "differential-geometry/coordinate-transformation-law-riemannian-metric"
title = "Coordinate transformation law for a Riemannian metric"
kind = "theorem"
summary = "Metric coefficient matrices transform by inverse congruence under a change of coordinates."
aliases = ["Riemannian metric change of coordinates", "metric tensor coordinate transformation law"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian
manifold]], and let \(G_i\) and \(G_j\) be the matrices of \(g\) in overlapping
coordinate charts \(\varphi_i\) and \(\varphi_j\). Put

\[
J_{ij}(x)
=D(\varphi_j\circ\varphi_i^{-1})_{\varphi_i(x)},
\]

so that \(J_{ij}\) sends \(i\)-coordinate components of a tangent vector to
\(j\)-coordinate components. Then

\[
G_j=J_{ij}^{-T}G_iJ_{ij}^{-1},
\]

or equivalently \(G_i=J_{ij}^{T}G_jJ_{ij}\). This congruence law is exactly
the compatibility condition that makes the local matrices represent one
global symmetric covariant \(2\)-tensor.

## Derivation

If a tangent vector has coordinate columns \(v_i\) and
\(v_j=J_{ij}v_i\), invariance of its squared length gives

\[
v_i^TG_iv_i=v_j^TG_jv_j
=v_i^TJ_{ij}^TG_jJ_{ij}v_i.
\]

Since this holds for every \(v_i\), one obtains
\(G_i=J_{ij}^TG_jJ_{ij}\).

## Relation to the frame bundle

The smooth atlas supplies the
[[fiber-bundles/tangent-bundle-cocycle-from-coordinate-changes|
\(\operatorname{GL}(n,\mathbb R)\)-valued tangent cocycle]]. A Riemannian
metric selects the orthonormal frames, giving an
[[fiber-bundles/example-reduction-of-gl-structure-to-o-using-a-bundle-metric|
\(O(n)\)-reduction]] of the frame bundle. In orthonormal local frames the
metric matrix is \(I\), and transition matrices take values in \(O(n)\).

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Riemannian metrics in local coordinates and orthonormal frames.
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
