+++
id = "differential-geometry/almost-quaternionic-manifold"
title = "Almost-quaternionic manifold"
kind = "definition"
summary = "A real manifold whose tangent bundle carries a rank-three family of endomorphisms locally satisfying the quaternion relations."
aliases = ["almost quaternionic structure"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
+++

An **almost-quaternionic manifold** is a [[fiber-bundles/smooth-manifold|smooth real manifold]] \(M\) of dimension \(4n\), \(n\geq1\), together with a rank-three smooth subbundle
\[
Q\subseteq\operatorname{End}_{\mathbb R}(TM)
\]
such that near every point \(Q\) has a frame \(I,J,K\) satisfying
\[
I^2=J^2=K^2=-\operatorname{id}_{TM},
\qquad IJ=K=-JI.
\]
Equivalently, the frame bundle of \(M\) reduces to \(\operatorname{GL}(n,\mathbb H)\operatorname{Sp}(1)\). The datum is the subbundle \(Q\), not a globally selected triple: on overlaps, admissible triples may rotate by an \(\operatorname{SO}(3)\)-valued change of frame.

## Equivalent structure-group description

At each point, \(Q_x\) is the copy of the imaginary quaternions acting on \(T_xM\). The group \(\operatorname{GL}(n,\mathbb H)\) commutes with this action, while \(\operatorname{Sp}(1)\) conjugates and rotates the imaginary units. Their common central element acts trivially, so the effective structure group is the product modulo its diagonal center. This gives the equivalence between the endomorphism-subbundle and \(G\)-structure descriptions [Salamon, pp. 143–145](https://doi.org/10.1007/BF01393378).

## Nearby stronger structures

A global frame \(I,J,K\) of \(Q\) satisfying the quaternion relations is an almost hypercomplex structure, which is strictly stronger. Adding a Riemannian metric for which every local \(I,J,K\) is orthogonal reduces the structure group further to [[lie-groups/compact-symplectic-product-group|\(\operatorname{Sp}(n)\operatorname{Sp}(1)\)]] and gives an almost quaternionic Hermitian manifold. A torsion-free connection preserving \(Q\) makes the structure quaternionic for \(n>1\); this is an integrability condition, not part of “almost quaternionic.”

## Examples and near-misses

Quaternionic Euclidean space \(\mathbb H^n\) has the trivial bundle \(Q\) spanned globally by right multiplication by \(i,j,k\). Quaternionic projective space \(\mathbb H P^n\) carries a canonical \(Q\) but, in general, no preferred global triple. An [[differential-geometry/almost-complex-structure|almost-complex structure]] \(I\) alone is a near-miss: it supplies one complex direction but not a rank-three bundle containing local \(J,K\) with \(IJ=K=-JI\).

## Dimension four and terminology

**Warning.** In real dimension four, almost-quaternionic structures are closely tied to oriented conformal structures, and definitions of “quaternionic” or “quaternionic Kähler” often adopt special curvature conventions. In dimensions \(4n\geq8\), the structure-group and torsion-free-connection formulation is the standard one. An almost-quaternionic manifold is also not a [[fiber-bundles/quaternionic-vector-bundle|quaternionic vector bundle]] in the stronger sense of choosing a global right \(\mathbb H\)-module structure on \(TM\).

## References

1. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [DOI record](https://doi.org/10.1007/BF01393378). Relevant: pp. 143–145 on almost quaternionic structures and the structure group \(\operatorname{GL}(n,\mathbb H)\operatorname{Sp}(1)\).
2. Simon Salamon, “Differential Geometry of Quaternionic Manifolds,” *Annales Scientifiques de l’École Normale Supérieure* 19 (1986), 31–55. [Stable journal record](https://www.numdam.org/item/ASENS_1986_4_19_1_31_0/). Relevant: §1 on quaternionic structures and their associated bundles.
