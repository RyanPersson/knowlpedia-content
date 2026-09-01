+++
id = "complex-analysis/sharp-three-transitivity-of-mobius-group"
title = "Sharp three-transitivity of the Möbius group"
kind = "theorem"
summary = "A unique Möbius transformation carries any ordered triple of distinct sphere points to any other."
aliases = ["Möbius transformations are sharply three-transitive"]
domains = ["complex-analysis", "algebra-groups", "projective-geometry"]
prerequisites = ["complex-analysis/riemann-sphere", "complex-analysis/mobius-transformation", "complex-analysis/mobius-transformation-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For any two ordered triples
\[
(z_1,z_2,z_3),\qquad (w_1,w_2,w_3)
\]
of distinct points of the [[complex-analysis/riemann-sphere|Riemann sphere]], there is a unique [[complex-analysis/mobius-transformation|Möbius transformation]] \(T\) satisfying
\[
T(z_i)=w_i\qquad(i=1,2,3).
\]
Thus the action of the [[complex-analysis/mobius-transformation-group|Möbius group]] on the sphere is sharply three-transitive.

## Proof

There is a Möbius transformation carrying each ordered triple to \((1,0,\infty)\), given by its [[complex-analysis/cross-ratio|cross-ratio coordinate]]. Composing one normalization with the inverse of the other gives existence. A Möbius transformation fixing three distinct points is the identity, which gives uniqueness.

## Quadruple invariant

Once the images of three points are fixed, the image of a fourth is determined by [[complex-analysis/cross-ratio-invariance-under-mobius-transformations|cross-ratio invariance]]. Consequently, two ordered quadruples of distinct points are in the same Möbius orbit exactly when their cross-ratios agree.

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapter 3, §§1–2.
