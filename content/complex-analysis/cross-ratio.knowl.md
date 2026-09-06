+++
id = "complex-analysis/cross-ratio"
title = "Cross-ratio"
kind = "definition"
summary = "A Möbius-invariant coordinate of an ordered quadruple on the projective line."
aliases = ["anharmonic ratio", "double ratio"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["complex-analysis/riemann-sphere", "shared-foundations/ordered-pair", "shared-foundations/function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For an ordered quadruple of distinct points \(z_1,z_2,z_3,z_4\in\widehat{\mathbb C}\), this knowl uses the **cross-ratio**
\[
[z_1,z_2;z_3,z_4]
=\frac{(z_1-z_3)(z_2-z_4)}
{(z_1-z_4)(z_2-z_3)}.
\]
Cases involving \(\infty\) are defined by taking limits.

## Examples

For instance, taking the fourth point to infinity gives
\[
[z_1,z_2;z_3,\infty]=\frac{z_1-z_3}{z_2-z_3}.
\]

## Projective meaning

There is a unique [[complex-analysis/mobius-transformation|Möbius transformation]] sending \(z_2,z_3,z_4\) to \(1,0,\infty\). Its value at \(z_1\) is the displayed cross-ratio. This makes projective invariance immediate.

The precise invariance statement is the [[complex-analysis/cross-ratio-invariance-under-mobius-transformations|cross-ratio invariance theorem]]. Conversely, a bijection of the sphere preserving all complex cross-ratios is [[complex-analysis/cross-ratio-preserving-bijections-are-mobius|necessarily Möbius]].

## Ordering convention

The order matters. Permuting four distinct points changes a value \(\lambda\) among
\[
\lambda,\quad \frac1\lambda,\quad 1-\lambda,\quad
\frac1{1-\lambda},\quad\frac{\lambda}{\lambda-1},\quad
\frac{\lambda-1}{\lambda}.
\]
Other books choose a permutation of the four arguments as their defining convention, so formulas should always be checked against the stated ordering.

## Real and circular criterion

Four distinct points lie on one [[complex-analysis/generalized-circle|generalized circle]] exactly when their cross-ratio is real. This connects the invariant to the circle-preserving geometry of Möbius transformations.

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapter 3.
