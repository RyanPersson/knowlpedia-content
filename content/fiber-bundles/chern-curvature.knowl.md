+++
id = "fiber-bundles/chern-curvature"
title = "Curvature of the Chern connection"
kind = "definition"
summary = "The End(E)-valued curvature two-form of a Hermitian holomorphic vector bundle's Chern connection."
aliases = ["Chern curvature", "Hermitian curvature"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["differential-geometry/holomorphic-vector-bundle", "differential-geometry/complex-manifold", "fiber-bundles/hermitian-metric", "fiber-bundles/chern-connection", "fiber-bundles/curvature-of-a-vector-bundle-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(E\to X\) be a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] over a [[differential-geometry/complex-manifold|complex manifold]], equipped with a [[fiber-bundles/hermitian-metric|Hermitian metric]] \(h\). If \(\nabla\) is its [[fiber-bundles/chern-connection|Chern connection]], the **Chern curvature** is the [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature]]
\[
F_\nabla=\nabla^2\in\Omega^2(X;\operatorname{End}E).
\]
It has pure type \((1,1)\): \(F_\nabla^{2,0}=F_\nabla^{0,2}=0\). In a holomorphic frame with metric matrix \(H\), using the convention \(\nabla=d+H^{-1}\partial H\), one has
\[
F_\nabla=\bar\partial\!\left(H^{-1}\partial H\right).
\]
Thus it is determined jointly by the holomorphic structure and the Hermitian metric.

## Type and local formula

The vanishing of the \((0,2)\)-part expresses the integrability of the holomorphic structure, while metric compatibility eliminates the conjugate \((2,0)\)-part. Thus the Chern connection packages the holomorphic and Hermitian data into an \(\operatorname{End}E\)-valued [[differential-geometry/differential-form-of-type-pq|\((1,1)\)-form]].

For a [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]] with a local holomorphic frame \(e\) and \(H=h(e,e)\), the formula reduces to
\[
F_\nabla=\bar\partial\partial\log H.
\]
Changing the curvature or Hermitian-linearity convention may insert a minus sign.

## Geometric consequences

Invariant polynomials applied to \(F_\nabla\) produce [[fiber-bundles/closed-differential-form|closed differential forms]] representing the Chern classes of \(E\). In particular, under the displayed convention,
\[
\frac{\sqrt{-1}}{2\pi}\operatorname{tr}(F_\nabla)
\]
represents the first Chern class in de Rham cohomology. Contraction of \(F_\nabla\) with a Hermitian form on the base gives the mean-curvature endomorphism used in the Hermitian [[fiber-bundles/yangmills-equation|Yang–Mills equation]].

## Examples and non-examples

The trivial holomorphic bundle with its constant standard metric has \(H=I\), hence \(F_\nabla=0\). A nonconstant Hermitian metric on the same holomorphic line bundle can have nonzero Chern curvature. The curvature of an arbitrary connection on a [[fiber-bundles/complex-vector-bundle|complex vector bundle]] is not Chern curvature unless that connection is the Chern connection for specified holomorphic and Hermitian structures; in particular, it need not have type \((1,1)\).

## References

1. Shoshichi Kobayashi, *Differential Geometry of Complex Vector Bundles*, Princeton University Press, 1987. [Publisher record](https://doi.org/10.1515/9781400858682). Relevant: Chapter I, §5, curvature of Hermitian holomorphic vector bundles.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: §4.2, Chern connections and curvature.
