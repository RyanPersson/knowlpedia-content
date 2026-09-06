+++
id = "complex-analysis/anti-mobius-transformation"
title = "Anti-Möbius transformation"
kind = "definition"
summary = "An orientation-reversing conformal automorphism of the Riemann sphere."
aliases = ["anti-Mobius transformation", "antiholomorphic Möbius transformation"]
domains = ["complex-analysis", "differential-geometry"]
prerequisites = ["complex-analysis/riemann-sphere", "complex-analysis/mobius-transformation"]
dependency_review_count = 1
section_mode = "progressive"
+++

An **anti-Möbius transformation** is a map of the [[complex-analysis/riemann-sphere|Riemann sphere]] of the form
\[
T(z)=\frac{a\overline z+b}{c\overline z+d},
\qquad ad-bc\ne0,
\]
with the usual extensions at a zero of the denominator and at \(\infty\). Equivalently, it is a [[complex-analysis/mobius-transformation|Möbius transformation]] composed with complex conjugation.

## Conformal orientation

Anti-Möbius transformations are antiholomorphic, conformal, and orientation reversing. They are not [[differential-geometry/holomorphic-map|holomorphic maps]] of Riemann surfaces. Every orientation-reversing conformal automorphism of the round \(2\)-sphere is anti-Möbius.

## Composition

The composite of two anti-Möbius transformations is Möbius, while composing a Möbius and an anti-Möbius transformation in either order is anti-Möbius. Together the two types form the full conformal automorphism group of the round sphere; the [[complex-analysis/mobius-transformation-group|Möbius group]] is its orientation-preserving subgroup of index \(2\).

## Circle geometry

Like Möbius transformations, anti-Möbius transformations preserve [[complex-analysis/generalized-circle|generalized circles]]. A circle-preserving bijection therefore need not be holomorphic; orientation or cross-ratio conjugation distinguishes the two cases.

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapters 3–4.
