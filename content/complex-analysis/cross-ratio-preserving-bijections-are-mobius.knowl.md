+++
id = "complex-analysis/cross-ratio-preserving-bijections-are-mobius"
title = "Cross-ratio-preserving bijections are Möbius"
kind = "theorem"
summary = "A sphere bijection preserving every complex cross-ratio is a Möbius transformation."
aliases = ["cross-ratio characterization of Möbius transformations"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["complex-analysis/mobius-transformation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F:\widehat{\mathbb C}\to\widehat{\mathbb C}\) be a bijection such that
\[
[F(z_1),F(z_2);F(z_3),F(z_4)]
=[z_1,z_2;z_3,z_4]
\]
for every ordered quadruple of distinct points. Then \(F\) is a [[complex-analysis/mobius-transformation|Möbius transformation]].

## Proof

By the [[complex-analysis/sharp-three-transitivity-of-mobius-group|sharp three-transitivity of the Möbius group]], choose a Möbius transformation \(T\) agreeing with \(F\) on three distinct points. For every fourth point \(z\), preservation of its cross-ratio with the chosen triple forces \(F(z)=T(z)\). Hence \(F=T\) on the whole sphere.

## Scope

Preservation of [[complex-analysis/generalized-circle|generalized circles]] alone is weaker. Without an orientation or cross-ratio condition, it also permits [[complex-analysis/anti-mobius-transformation|anti-Möbius transformations]]. The theorem specifically assumes preservation of the complex-valued ordered [[complex-analysis/cross-ratio|cross-ratio]].

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapter 3, §§1–2.
