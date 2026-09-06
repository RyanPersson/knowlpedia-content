+++
id = "lie-groups/psl2-complex"
title = "PSL(2,C)"
kind = "example"
summary = "The center quotient of SL(2,C), viewed either as a complex Lie group or as a six-dimensional real Lie group."
aliases = ["projective special linear group PSL(2,C)", "PSL2C"]
domains = ["lie-groups", "complex-analysis"]
section_mode = "progressive"
prerequisites = ["algebra-groups/projective-special-linear-group", "lie-groups/complex-lie-group", "lie-groups/underlying-real-lie-group", "lie-groups/lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The complex [[algebra-groups/projective-special-linear-group|projective special linear group]] is
\[
PSL(2,\mathbb C):=SL(2,\mathbb C)/\{\pm I\}.
\]
It is a connected [[lie-groups/complex-lie-group|complex Lie group]] of complex dimension \(3\). Its [[lie-groups/underlying-real-lie-group|underlying real Lie group]] has real dimension \(6\), and its [[lie-groups/lie-algebra|Lie algebra]] is \(\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\).

## Equivalent matrix description

Because every nonzero complex number has a square root, every class in \(PGL_2(\mathbb C)\) has a determinant-one representative, unique up to sign. Hence
\[
PSL(2,\mathbb C)\cong PGL_2(\mathbb C).
\]
This equality is special to fields for which the required determinant roots exist and must not be transferred to arbitrary fields.

Its principal geometric actions are recorded by focused theorem knowls: the
[[lie-groups/celestial-sphere-and-mobius-action|Möbius action on the celestial
sphere]], the [[lie-groups/psl2c-proper-lorentz-isomorphism|proper Lorentz
isomorphism]], and the [[lie-groups/psl2c-action-on-hyperbolic-three-space|
action on hyperbolic three-space]]. Its separate role as the complex points
of the adjoint [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of type \(A_1\) is treated in the
[[langlands-letter/knowls/langlands-dual-group|Langlands-dual-group]]
context.

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983, Chapters 3 and 7. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4).
2. John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 3rd ed., Springer, 2019, Chapters 3–4. [Publisher record](https://doi.org/10.1007/978-3-030-31597-9).
