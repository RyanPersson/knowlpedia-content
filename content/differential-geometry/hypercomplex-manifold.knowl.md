+++
id = "differential-geometry/hypercomplex-manifold"
title = "Hypercomplex manifold"
kind = "definition"
summary = "A smooth manifold carrying three integrable complex structures that satisfy the quaternion relations."
aliases = ["hypercomplex structure"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/integrable-almost-complex-structure", "differential-geometry/complex-manifold", "differential-geometry/tangent-space", "linear-algebra/quaternionic-vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **hypercomplex manifold** is a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) equipped with three smooth bundle endomorphisms \(I,J,K:TM\to TM\) such that
\[
I^2=J^2=K^2=-\operatorname{id}_{TM},\qquad IJ=K=-JI,
\]
and each of \(I,J,K\) is an [[differential-geometry/integrable-almost-complex-structure|integrable almost-complex structure]]. Thus each member of the triple defines a [[differential-geometry/complex-manifold|complex-manifold structure]], while the relations make every [[differential-geometry/tangent-space|tangent space]] a left [[linear-algebra/quaternionic-vector-space|quaternionic vector space]]. In particular, the real dimension of \(M\) is divisible by four. The ordered triple is part of the structure; merely specifying its rank-three span gives the weaker notion of an almost-quaternionic structure.

## Canonical connection

Every hypercomplex manifold has a unique torsion-free [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla^{\mathrm{Ob}}\) on \(TM\) satisfying
\[
\nabla^{\mathrm{Ob}}I=\nabla^{\mathrm{Ob}}J=\nabla^{\mathrm{Ob}}K=0.
\]
This is the **[[differential-geometry/obata-connection|Obata connection]]**. Its existence and uniqueness convert the three integrability conditions into a useful differential-geometric structure: parallel transport is quaternionic-linear, and the holonomy lies in \(GL(n,\mathbb H)\).

## Relationship to quaternionic geometry

The span
\[
Q=\operatorname{span}_{\mathbb R}\{I,J,K\}\subseteq\operatorname{End}(TM)
\]
is an [[differential-geometry/almost-quaternionic-manifold|almost-quaternionic structure]]. Because the Obata connection is torsion-free and preserves \(Q\), it makes \(M\) a [[differential-geometry/quaternionic-manifold|quaternionic manifold]]. The converse need not hold: a quaternionic manifold generally has only local admissible triples, related on overlaps by rotations, and need not admit any globally distinguished \(I,J,K\).

If \(M\) also has a Riemannian metric that is Hermitian for \(I,J,K\) and whose Levi-Civita connection preserves the triple, then \(M\) is hyperkähler. Metric compatibility alone gives a [[differential-geometry/hyperhermitian-manifold|hyper-Hermitian manifold]] and does not force the associated two-forms to be closed.

## Quaternionic potential theory

After choosing \(I\), the [[differential-geometry/del-j-operator|
\(\partial_J\) operator]] combines with the Dolbeault operator to form
\(\partial\partial_Ju\). Positivity of this form defines a
[[differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex|
quaternionic plurisubharmonic function on a hypercomplex manifold]]. Its
strictly positive smooth local potentials produce
[[differential-geometry/hkt-metric|HKT metrics]].

## Examples and non-examples

The quaternionic vector space \(\mathbb H^n\), and every quotient of it by a lattice acting by translations, has the constant hypercomplex triple given by left multiplication by \(i,j,k\). More generally, a [[differential-geometry/hyperkahler-manifold|hyperkähler manifold]] is hypercomplex after forgetting its metric.

Three smooth endomorphisms satisfying the quaternion relations define only an almost-hypercomplex structure. If one of their Nijenhuis tensors is nonzero, the resulting structure is not hypercomplex because the required complex structure is not integrable.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [Oxford DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: §6.2, hypercomplex structures and the Obata connection.
2. Simon Salamon, “Quaternionic Manifolds,” *Symposia Mathematica* 26, 1982, 139–151. [Stable repository record](https://hdl.handle.net/11583/1405679). Relevant: quaternionic and hypercomplex structures.
