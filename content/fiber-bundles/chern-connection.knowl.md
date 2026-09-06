+++
id = "fiber-bundles/chern-connection"
title = "Chern connection"
kind = "definition"
summary = "The unique connection on a Hermitian holomorphic vector bundle compatible with both structures."
aliases = ["canonical Hermitian connection", "Chern covariant derivative", "Chern connection of a Hermitian holomorphic bundle"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["differential-geometry/holomorphic-vector-bundle", "differential-geometry/complex-manifold", "differential-geometry/holomorphic-map", "fiber-bundles/hermitian-metric", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/hermitian-connection", "fiber-bundles/section-of-a-fiber-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to X\) be a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] over a [[differential-geometry/complex-manifold|complex manifold]], with [[differential-geometry/holomorphic-map|holomorphic transition maps]] and a [[fiber-bundles/hermitian-metric|Hermitian metric]] \(h\). The **Chern connection** is the unique [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\) that is a [[fiber-bundles/hermitian-connection|Hermitian connection]] and whose \((0,1)\)-part equals the bundle Dolbeault operator:
\[
\nabla^{0,1}=\bar\partial_E.
\]
Equivalently, a smooth [[fiber-bundles/section-of-a-fiber-bundle|section]] is holomorphic exactly when its \((0,1)\)-covariant derivative vanishes. Both the holomorphic structure and the metric are essential: neither one alone determines this connection.

## Local formula

In a local holomorphic frame, let \(H=(h(e_j,e_k))\) be the Hermitian metric matrix, using the convention that \(h\) is linear in its second argument. The connection matrix of the Chern connection is
\[
A=H^{-1}\partial H.
\]
Thus its \((0,1)\)-part vanishes in that frame, while metric compatibility determines its \((1,0)\)-part. This formula also proves uniqueness locally.

## Curvature

The [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature]] is
\[
F_\nabla=\bar\partial\!\left(H^{-1}\partial H\right),
\]
in the same convention, and has type \((1,1)\). For a [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]] with local holomorphic frame \(e\) and \(h(e,e)=H\), one has \(A=\partial\log H\) and \(F_\nabla=\bar\partial\partial\log H\). These formulas underlie the differential-geometric construction of Chern forms.

## Conventions and scope

Changing whether the Hermitian form is linear in its first or second argument, or changing the sign convention for curvature, alters the displayed local formulas but not the invariant characterization. The construction applies to every Hermitian holomorphic vector bundle; no [[differential-geometry/kahler-metric|Kähler metric]] on the base is required.

## References

1. S. Kobayashi, *Differential Geometry of Complex Vector Bundles*, Princeton University Press, 1987. [DOI record](https://doi.org/10.1515/9781400858682). Relevant: Chapter I, §4, existence, uniqueness, and curvature of the Chern connection.
2. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §4.2, Hermitian holomorphic bundles and their Chern connections.
