+++
id = "differential-geometry/cotangent-lift"
title = "Cotangent lift"
kind = "construction"
summary = "The contragredient diffeomorphism of cotangent bundles induced by a diffeomorphism of base manifolds."
aliases = ["cotangent functor on diffeomorphisms", "lifted diffeomorphism of cotangent bundles", "cotangent-lifted diffeomorphism", "canonical lift"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/diffeomorphism|diffeomorphism]]. Its **cotangent lift** is the map
\[
T^*f:T^*M\longrightarrow T^*N,\qquad
T^*f(\alpha_x)=(f^{-1})^*\alpha_x
=\alpha_x\circ d(f^{-1})_{f(x)}.
\]
Thus \(T^*f(\alpha_x)\) lies over \(f(x)\). Although [[fiber-bundles/pullback-of-covectors|pullback of covectors]] is contravariant, inserting \(f^{-1}\) makes the lift travel in the same direction as \(f\). The lift is a diffeomorphism with inverse \(T^*(f^{-1})\), and it requires no metric, connection, or other auxiliary choice.

## Functoriality

For composable diffeomorphisms \(f\) and \(g\),
\[
T^*(g\circ f)=T^*g\circ T^*f,
\qquad
T^*(\operatorname{id}_M)=\operatorname{id}_{T^*M}.
\]
These identities follow from the chain rule and the reversal built into covector pullback. They make the cotangent construction covariant on the groupoid whose morphisms are diffeomorphisms.

## Preservation of canonical forms

The lift preserves the tautological one-form:
\[
(T^*f)^*\theta_N=\theta_M.
\]
Consequently it preserves the [[differential-geometry/canonical-symplectic-form-cotangent|canonical symplectic forms]], so every cotangent lift is a [[differential-geometry/symplectomorphism|symplectomorphism]]. This intrinsic preservation property is a central reason cotangent lifts occur in mechanics; see [Abraham and Marsden, Chapter 3](https://authors.library.caltech.edu/records/3n0y2-7wa09).

## Scope

**Warning.** A general smooth map \(f:M\to N\) gives a pullback bundle map \(f^*T^*N\to T^*M\), not a canonical map \(T^*M\to T^*N\). The cotangent lift in the displayed direction therefore uses invertibility essentially.

## References

1. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., Benjamin/Cummings, 1978. [CaltechAUTHORS record](https://authors.library.caltech.edu/records/3n0y2-7wa09). Relevant: Chapter 3, cotangent lifts and canonical forms.
2. Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer, 1999. [DOI record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: §6.3, cotangent lifts.
