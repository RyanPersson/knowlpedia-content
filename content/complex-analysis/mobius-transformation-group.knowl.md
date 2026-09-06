+++
id = "complex-analysis/mobius-transformation-group"
title = "Möbius transformation group"
kind = "definition"
summary = "The group of fractional linear automorphisms of the Riemann sphere."
aliases = ["Möbius group", "Mobius group", "fractional linear group"]
domains = ["complex-analysis", "lie-groups", "projective-geometry"]
section_mode = "progressive"
prerequisites = ["complex-analysis/mobius-transformation", "algebra-groups/group", "complex-analysis/cross-ratio"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **Möbius transformation group** is the group of all [[complex-analysis/mobius-transformation|Möbius transformations]] under composition. The projective action gives canonical isomorphisms
\[
\operatorname{Möb}(\widehat{\mathbb C})
\cong PGL_2(\mathbb C)
\cong PSL_2(\mathbb C),
\]
where the second isomorphism uses the existence of square roots in \(\mathbb C\).

## Action on triples

The action on the [[complex-analysis/riemann-sphere|Riemann sphere]] is [[complex-analysis/sharp-three-transitivity-of-mobius-group|sharply three-transitive]]: for any two ordered triples of distinct points, there is exactly one Möbius transformation carrying the first triple to the second. The [[complex-analysis/cross-ratio|cross-ratio]] is the corresponding invariant of ordered quadruples.

For finite triples, first send the three points to \(0,1,\infty\) by the cross-ratio formula; composing the map for the target triple gives existence. A nonidentity fractional-linear map has at most two fixed points, so a map fixing \(0,1,\infty\) is the identity. This proves uniqueness, and the matrix formula shows composition and inversion remain in \(PGL_2(\mathbb C)\).

## Complex Lie group

The group has complex dimension \(3\) and underlying real dimension \(6\). In the \(PSL_2(\mathbb C)\) presentation it is \(SL_2(\mathbb C)/\{\pm I\}\), connecting Möbius geometry to the Lorentz and hyperbolic actions of [[lie-groups/psl2-complex|the projective special linear group]].

## Conformal group of the round sphere

Under stereographic projection, the Möbius group is exactly the group of orientation-preserving conformal diffeomorphisms of the round \(2\)-sphere. The full conformal [[differential-geometry/diffeomorphism-group|diffeomorphism group]] also contains orientation-reversing [[complex-analysis/anti-mobius-transformation|anti-Möbius transformations]], such as complex conjugation composed with a Möbius transformation.

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4). Relevant: Chapters 3–4.
