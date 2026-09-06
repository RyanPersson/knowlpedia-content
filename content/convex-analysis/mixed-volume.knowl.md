+++
id = "convex-analysis/mixed-volume"
title = "Mixed volume"
kind = "definition"
summary = "The symmetric multilinear polarization of volume with respect to Minkowski addition."
aliases = ["mixed volume of convex bodies", "Minkowski mixed volume"]
domains = ["convex-analysis", "integral-geometry"]
prerequisites = ["convex-analysis/convex-body"]
dependency_review_count = 1
section_mode = "progressive"
+++

For [[convex-analysis/convex-body|convex bodies]]
\(K_1,\ldots,K_m\subseteq\mathbb R^m\), their **mixed volume** is
\[
V(K_1,\ldots,K_m)
=\frac1{m!}[t_1\cdots t_m]\,
\operatorname{vol}(t_1K_1+\cdots+t_mK_m).
\]
Here \([t_1\cdots t_m]\) extracts the indicated coefficient from the
homogeneous degree-\(m\) volume polynomial.

## Properties

Mixed volume is symmetric, translation-invariant, and multilinear with
respect to [[convex-analysis/minkowski-sum|Minkowski addition]] and
nonnegative scalar multiplication. It is monotone in each argument and
normalized by
\[
V(K,\ldots,K)=\operatorname{vol}(K).
\]

## Valuations

Fixing \(A_1,\ldots,A_{m-k}\) makes
\[
K\longmapsto V(K[k],A_1,\ldots,A_{m-k})
\]
a continuous translation-invariant
[[convex-analysis/valuation-on-convex-bodies|valuation]] homogeneous of degree
\(k\). Mixed volume is the convex-body counterpart of determinant
polarization, but it is not the same object as the
[[linear-algebra/mixed-discriminant|mixed discriminant]].

## References

1. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858). Relevant: Chapter 5.
