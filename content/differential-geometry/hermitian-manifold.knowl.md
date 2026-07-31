+++
id = "differential-geometry/hermitian-manifold"
title = "Hermitian manifold"
kind = "definition"
summary = "A complex manifold equipped with a Riemannian metric invariant under its complex structure."
aliases = ["Hermitian complex manifold", "Hermitian metric on a complex manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[differential-geometry/complex-manifold|complex manifold]] with its canonical complex structure \(J\) on the real [[fiber-bundles/tangent-bundle|tangent bundle]]. A **Hermitian manifold** is \(M\) together with a smooth Riemannian metric \(g\) satisfying
\[
g(JX,JY)=g(X,Y)
\]
for all real tangent vectors \(X,Y\) at the same point. Thus \((M,J,g)\) is an [[differential-geometry/almost-hermitian-manifold|almost-Hermitian manifold]] whose [[differential-geometry/almost-complex-structure|almost-complex structure]] is [[differential-geometry/integrable-almost-complex-structure|integrable]]. Equivalently, \(g\) determines a [[fiber-bundles/hermitian-metric|Hermitian metric]] on the [[differential-geometry/holomorphic-tangent-bundle|complex tangent bundle]]. Its fundamental form is the real \(2\)-form \(\omega(X,Y)=g(JX,Y)\).

## Associated form and local data

The [[differential-geometry/fundamental-form-almost-hermitian|fundamental \(2\)-form]] is nondegenerate and of complex type \((1,1)\). In holomorphic coordinates, the metric is represented by a smoothly varying positive-definite Hermitian matrix. These descriptions carry the same data as the \(J\)-invariant real Riemannian metric; they do not identify that real [[linear-algebra/bilinear-form|bilinear form]] with a sesquilinear form.

Every complex manifold under the usual second-countable convention admits a Hermitian metric: local standard metrics can be combined with a smooth partition of unity.

## Relationship to Kähler geometry

Hermitian compatibility does not require \(d\omega=0\). A Hermitian manifold is [[differential-geometry/kahler-manifold|Kähler]] precisely when its fundamental form is closed. This separates integrability of \(J\), already built into the complex-manifold hypothesis, from the additional differential condition on \(\omega\).

## Examples and non-examples

Complex [[linear-algebra/euclidean-space|Euclidean space]] with its standard Euclidean metric is Hermitian, as is [[algebraic-geometry-foundations/projective-space|complex projective space]] with the [[differential-geometry/fubini-study-metric|Fubini–Study metric]]. On \(\mathbb C^n\), a generic Riemannian metric is not Hermitian: if it assigns different lengths to \(X\) and \(JX\), it fails \(J\)-invariance.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §3.1, especially Definition 3.1.1 for the fundamental form of a Hermitian metric.
