+++
id = "complex-analysis/cross-ratio-invariance-under-mobius-transformations"
title = "Cross-ratio invariance under Möbius transformations"
kind = "theorem"
summary = "Every Möbius transformation preserves the cross-ratio of an ordered quadruple."
aliases = ["cross-ratio invariance"]
domains = ["complex-analysis", "projective-geometry"]
section_mode = "progressive"
+++

Let \(T\) be a [[complex-analysis/mobius-transformation|Möbius transformation]], and let \(z_1,z_2,z_3,z_4\) be four distinct points of the [[complex-analysis/riemann-sphere|Riemann sphere]]. Then
\[
[Tz_1,Tz_2;Tz_3,Tz_4]=[z_1,z_2;z_3,z_4].
\]

## Proof

Substitution proves the identity for
\[
T(z)=\frac{az+b}{cz+d};
\]
the factors of \(ad-bc\) and the denominators cancel. Equivalently, the [[complex-analysis/cross-ratio|cross-ratio]] is the projective coordinate that sends an ordered triple to \((1,0,\infty)\), so it is unchanged by changing homogeneous coordinates.

## Consequence

The cross-ratio is the basic invariant of ordered quadruples under the Möbius group. In fact, equality of cross-ratios is sufficient for two ordered quadruples of distinct points to lie in the same Möbius orbit, by the [[complex-analysis/sharp-three-transitivity-of-mobius-group|sharp three-transitivity of the Möbius group]].

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapter 3, §§1–2.
