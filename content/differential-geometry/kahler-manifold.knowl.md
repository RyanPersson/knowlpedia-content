+++
id = "differential-geometry/kahler-manifold"
title = "Kähler manifold"
kind = "definition"
summary = "A Hermitian manifold whose fundamental two-form is closed."
aliases = ["Kählerian manifold", "Kahler manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,J,g)\) be a [[differential-geometry/hermitian-manifold|Hermitian manifold]], and let
\[
\omega(X,Y)=g(JX,Y)
\]
be its [[differential-geometry/fundamental-form-almost-hermitian|fundamental \(2\)-form]]. The manifold is **Kähler** if
\[
d\omega=0.
\]
Thus a Kähler manifold is a [[differential-geometry/complex-manifold|complex manifold]] with a \(J\)-invariant real Riemannian metric whose associated real \(2\)-form is closed. The metric \(g\) determines a sesquilinear Hermitian metric on the [[differential-geometry/holomorphic-tangent-bundle|complex tangent bundle]], but \(g\) itself remains a real bilinear form. The sign used for \(\omega\) does not affect the closedness condition.

## Equivalent characterizations

For a Hermitian manifold, the Kähler condition is equivalent to \(\nabla J=0\), where \(\nabla\) is the Levi–Civita connection of \(g\). Equivalently, parallel transport preserves both \(g\) and \(J\), so the holonomy acts through \(U(n)\). The connection and holonomy formulation is treated in [Huybrechts, Appendix 4.A](https://doi.org/10.1007/b137952).

## Structure and consequences

The closed, nondegenerate form \(\omega\) makes \(M\) a [[differential-geometry/symplectic-manifold|symplectic manifold]]. In complex dimension \(n\), the form \(\omega^n/n!\) is the Riemannian volume form for the compatible orientation. Kähler geometry therefore ties together complex, Riemannian, and symplectic structures without making those structures identical.

## Examples and non-examples

Complex Euclidean space, complex tori with flat Hermitian metrics, and [[algebraic-geometry-foundations/projective-space|complex projective space]] with the [[differential-geometry/fubini-study-metric|Fubini–Study metric]] are Kähler. In complex dimension greater than one, conformally replacing a [[differential-geometry/kahler-metric|Kähler metric]] by \(g'=e^f g\) for a nonconstant real function gives \(\omega'=e^f\omega\) and
\[
d\omega'=e^f\,df\wedge\omega,
\]
which is nonzero where \(df\neq0\); the new metric is Hermitian but not Kähler. In complex dimension one, every Hermitian metric is Kähler because every real \(3\)-form vanishes.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §3.1, Definition 3.1.6 for Kähler closedness, and Appendix 4.A for the Levi–Civita and holonomy characterization.
