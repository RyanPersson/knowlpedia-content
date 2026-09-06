+++
id = "differential-geometry/kahler-manifold"
title = "Kähler manifold"
kind = "definition"
summary = "A Hermitian manifold whose fundamental two-form is closed."
aliases = ["Kählerian manifold", "Kahler manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/hermitian-manifold", "differential-geometry/fundamental-form-almost-hermitian", "differential-geometry/complex-manifold", "fiber-bundles/hermitian-metric"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,J,g)\) be a [[differential-geometry/hermitian-manifold|Hermitian manifold]], and let
\[
\omega(X,Y)=g(JX,Y)
\]
be its [[differential-geometry/fundamental-form-almost-hermitian|fundamental \(2\)-form]]. The manifold is **Kähler** if
\[
d\omega=0.
\]
Thus a Kähler manifold is a [[differential-geometry/complex-manifold|complex manifold]] with a \(J\)-invariant real Riemannian metric whose associated real \(2\)-form is closed. The metric \(g\) determines a sesquilinear [[fiber-bundles/hermitian-metric|Hermitian metric]] on the [[differential-geometry/holomorphic-tangent-bundle|complex tangent bundle]], but \(g\) itself remains a real [[linear-algebra/bilinear-form|bilinear form]]. The sign used for \(\omega\) does not affect the closedness condition.

## Equivalent characterizations

For a Hermitian manifold, the Kähler condition is equivalent to \(\nabla J=0\), where \(\nabla\) is the Levi–Civita connection of \(g\). Equivalently, parallel transport preserves both \(g\) and \(J\), so the holonomy acts through \(U(n)\).

## Structure and consequences

The closed, nondegenerate form \(\omega\) makes \(M\) a [[differential-geometry/symplectic-manifold|symplectic manifold]]. In complex dimension \(n\), the form \(\omega^n/n!\) is the Riemannian volume form for the compatible orientation. Kähler geometry therefore ties together complex, Riemannian, and symplectic structures without making those structures identical.

## Morphisms

There is no single convention for a “Kähler morphism,” so the preserved data
must be named. A [[differential-geometry/holomorphic-map|holomorphic map]]
preserves the complex structures but need not preserve the metrics or Kähler
forms. A
[[differential-geometry/holomorphic-isometric-immersion|holomorphic
isometric immersion]], also called a Kähler immersion, additionally satisfies
\(f^*g_N=g_M\), equivalently \(f^*\omega_N=\omega_M\). If such a map is a
diffeomorphism, it is simultaneously a
[[differential-geometry/biholomorphism|biholomorphism]], Riemannian isometry,
and [[differential-geometry/symplectomorphism|symplectomorphism]].

## Examples and non-examples

Complex [[linear-algebra/euclidean-space|Euclidean space]], complex tori with flat Hermitian metrics, and [[algebraic-geometry-foundations/projective-space|complex projective space]] with the [[differential-geometry/fubini-study-metric|Fubini–Study metric]] are Kähler. In complex dimension greater than one, conformally replacing a [[differential-geometry/kahler-metric|Kähler metric]] by \(g'=e^f g\) for a nonconstant real function gives \(\omega'=e^f\omega\) and
\[
d\omega'=e^f\,df\wedge\omega,
\]
which is nonzero where \(df\neq0\); the new metric is Hermitian but not Kähler. In complex dimension one, every Hermitian metric is Kähler because every real \(3\)-form vanishes.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §3.1, Definition 3.1.6 for Kähler closedness, and Appendix 4.A for the Levi–Civita and holonomy characterization.
