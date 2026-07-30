+++
id = "complex-analysis/cross-ratio-characterization-of-mobius-transformations"
title = "Cross-ratio characterization of Möbius transformations"
kind = "theorem"
summary = "Möbius transformations preserve cross-ratios and are uniquely determined by three point images."
aliases = ["cross-ratio invariance"]
domains = ["complex-analysis", "projective-geometry"]
section_mode = "progressive"
+++

Every [[complex-analysis/mobius-transformation|Möbius transformation]] \(T\) preserves the [[complex-analysis/cross-ratio|cross-ratio]]:
\[
[Tz_1,Tz_2;Tz_3,Tz_4]=[z_1,z_2;z_3,z_4].
\]
Moreover, for any two ordered triples of distinct points of \(\widehat{\mathbb C}\), there is a unique Möbius transformation sending the first triple to the second.

## Sharp three-transitivity

Send each ordered triple to \((1,0,\infty)\) using its cross-ratio coordinate and compose one normalization with the inverse of the other. Uniqueness follows because a Möbius transformation fixing three distinct points is the identity.

## Converse

A bijection of the Riemann sphere that preserves the complex cross-ratio of every ordered quadruple is Möbius. If one asks only that [[complex-analysis/generalized-circle|generalized circles]] be preserved, additional regularity or orientation hypotheses are needed to distinguish Möbius from [[complex-analysis/anti-mobius-transformation|anti-Möbius transformations]].

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapter 3, §§1–2.
