+++
id = "fiber-bundles/pullback-connection-on-a-vector-bundle"
title = "Pullback connection on a vector bundle"
kind = "definition"
summary = "The canonical connection on a pullback vector bundle induced by a connection on the original bundle."
aliases = ["pulled-back covariant derivative", "connection on f-star E"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/pullback-bundle", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/vector-bundle-valued-differential-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(f:N\to M\) be a [[fiber-bundles/smooth-map|smooth map]], let \(E\to M\) be a smooth real or complex [[fiber-bundles/vector-bundle|vector bundle]], and let \(\nabla\) be a [[fiber-bundles/connection-on-a-vector-bundle|connection]] on \(E\). The **pullback connection** \(f^*\nabla\) is the unique connection on the [[fiber-bundles/pullback-bundle|pullback bundle]] \(f^*E\to N\) such that
\[
(f^*\nabla)(f^*s)=f^*(\nabla s)
\]
for every local [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] \(s\) of \(E\). Here the right side is the pullback of the \(E\)-valued \(1\)-form \(\nabla s\), so it is a [[fiber-bundles/vector-bundle-valued-differential-form|\(f^*E\)-valued \(1\)-form]] on \(N\).

## Local construction

Every local section of \(f^*E\) can be written as a finite sum \(\sigma=\sum_i a_i f^*s_i\). The Leibniz rule forces
\[
(f^*\nabla)\sigma
=
\sum_i da_i\otimes f^*s_i
+\sum_i a_i f^*(\nabla s_i).
\]
This formula is independent of the chosen expression for \(\sigma\). In a local frame with \(\nabla=d+A\), the pullback connection is \(d+f^*A\).

## Curvature and functoriality

[[fiber-bundles/curvature-of-a-vector-bundle-connection|Curvature]] is natural under pullback:
\[
R^{f^*\nabla}=f^*R^\nabla.
\]
Thus a pullback of a flat connection is flat, although the converse need not hold because \(f\) may miss directions on which the original curvature is nonzero. Pullback is functorial: for \(g:L\to N\), the canonical identification \((f\circ g)^*E\cong g^*f^*E\) carries \((f\circ g)^*\nabla\) to \(g^*(f^*\nabla)\). These naturality statements follow from the local pullback formula.

If \(i:S\hookrightarrow M\) is an [[differential-geometry/embedded-submanifold|embedded submanifold]], \(i^*\nabla\) is the restriction of \(\nabla\) to directions tangent to \(S\).

## Examples and scope

For a constant map \(f:N\to\{x\}\subset M\), the pullback bundle is canonically \(N\times E_x\), and \(f^*\nabla\) is the trivial connection in this identification. Pulling back the Levi–Civita connection along a curve gives the covariant derivative used to define parallel [[fiber-bundles/vector-field|vector fields]] along that curve.

**Warning.** The pullback connection differentiates sections of \(f^*E\), not sections of \(E\) along arbitrary vector fields on \(M\). No immersion or submersion hypothesis on \(f\) is required.

## References

1. Loring W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55084-8). Relevant: §25, pullback connections and curvature.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter II, mappings and induced connections.
