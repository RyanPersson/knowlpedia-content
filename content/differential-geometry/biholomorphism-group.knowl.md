+++
id = "differential-geometry/biholomorphism-group"
title = "Biholomorphism group"
kind = "definition"
summary = "The automorphism group of a complex manifold in the category of complex manifolds and holomorphic maps."
aliases = ["holomorphic automorphism group", "Aut_hol(X)", "group of biholomorphisms"]
domains = ["differential-geometry", "complex-analysis", "algebra-groups"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/category-of-complex-manifolds"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[differential-geometry/complex-manifold|complex manifold]] \(X\), its **biholomorphism group** or **holomorphic automorphism group** is
\[
\operatorname{Aut}_{\mathrm{hol}}(X)
=\{f:X\to X:f\text{ is a biholomorphism}\}.
\]
Composition is the group operation. This is precisely the automorphism group of \(X\) in the [[differential-geometry/category-of-complex-manifolds|category of complex manifolds]], whose morphisms are holomorphic maps.

Every biholomorphism is a diffeomorphism of the underlying smooth manifold, giving an injective homomorphism
\[
\operatorname{Aut}_{\mathrm{hol}}(X)\hookrightarrow\operatorname{Diff}(X).
\]
It is generally a proper subgroup because a smooth diffeomorphism need not have complex-linear differential.

## Examples

The holomorphic automorphism group of \(\mathbb C\) consists of affine maps \(z\mapsto az+b\) with \(a\neq0\). The automorphism group of the [[complex-analysis/riemann-sphere|Riemann sphere]] is the [[complex-analysis/mobius-transformation-group|Möbius group]]
\[
\operatorname{Aut}_{\mathrm{hol}}(\mathbb P^1(\mathbb C))
\cong PGL_2(\mathbb C).
\]
For \(\mathbb C^n\) with \(n>1\), the group includes many nonlinear automorphisms and is much larger than the complex-affine group.

## Topological and Lie-group structure

The notation above first denotes an abstract group. One may equip it with a compact-open or finer topology, and under hypotheses such as compactness of \(X\), automorphism theorems give it a finite-dimensional complex Lie-group structure. Such additional structure is not automatic for an arbitrary noncompact complex manifold and is not built into the definition.

If \(X\) carries a Hermitian or Kähler metric, the subgroup of holomorphic
automorphisms that also preserve the metric is smaller. Its elements are the
diffeomorphic instances of
[[differential-geometry/holomorphic-isometric-immersion|holomorphic
isometric immersions]].

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapters 1–2, holomorphic maps and automorphisms.
2. Shoshichi Kobayashi, *Transformation Groups in Differential Geometry*, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-61981-6). Relevant: automorphism groups of geometric structures.
