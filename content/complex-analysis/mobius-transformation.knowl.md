+++
id = "complex-analysis/mobius-transformation"
title = "Möbius transformation"
kind = "definition"
summary = "A fractional linear automorphism of the Riemann sphere."
aliases = ["Mobius transformation", "fractional linear transformation", "linear fractional transformation"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["complex-analysis/riemann-sphere"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **Möbius transformation** is a map of the [[complex-analysis/riemann-sphere|Riemann sphere]]
\[
T(z)=\frac{az+b}{cz+d},
\qquad a,b,c,d\in\mathbb C,\qquad ad-bc\ne0,
\]
extended by \(T(-d/c)=\infty\) and \(T(\infty)=a/c\) when \(c\ne0\), with the evident affine conventions when \(c=0\).

## Matrix origin

The matrix
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]
acts linearly on \(\mathbb C^2\) and hence projectively on its lines. Multiplying \(A\) by a nonzero scalar does not change \(T\), so Möbius transformations are elements of \(PGL_2(\mathbb C)\). Composition corresponds to matrix multiplication.

## Geometry

Every Möbius transformation is a [[differential-geometry/biholomorphism|biholomorphism]] of the sphere and carries [[complex-analysis/generalized-circle|generalized circles]] to generalized circles. It is conformal and orientation preserving. Reflection or complex conjugation produces [[complex-analysis/anti-mobius-transformation|anti-Möbius transformations]], which are not holomorphic.

## Generators

Translations, nonzero complex dilations, and inversion \(z\mapsto1/z\) generate all Möbius transformations.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 3, §3.
