+++
id = "differential-geometry/holomorphic-line-bundle"
title = "Holomorphic line bundle"
kind = "definition"
summary = "A holomorphic vector bundle whose fibers have complex dimension one."
aliases = ["analytic line bundle", "invertible holomorphic bundle"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/holomorphic-vector-bundle", "topology/open-cover", "fiber-bundles/transition-function", "differential-geometry/holomorphic-vector-bundle-morphism", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. A **holomorphic line bundle** on \(X\) is a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] \(L\to X\) of complex rank one. Equivalently, \(X\) has an [[topology/open-cover|open cover]] \(\{U_i\}\) and holomorphic trivializations \(L|_{U_i}\cong U_i\times\mathbb C\) whose [[fiber-bundles/transition-function|transition functions]] \(g_{ij}:U_i\cap U_j\to\mathbb C^\times\) are nowhere-vanishing holomorphic functions satisfying \(g_{ij}g_{jk}=g_{ik}\) on triple overlaps. Isomorphisms are invertible [[differential-geometry/holomorphic-vector-bundle-morphism|holomorphic vector-bundle morphisms]] over \(X\). Its fibers are one-dimensional complex [[linear-algebra/vector-space|vector spaces]] varying holomorphically over the base.

## Tensor operations

The tensor product \(L\otimes L'\), dual \(L^\vee\), and pullback \(f^*L\) along a [[differential-geometry/holomorphic-map|holomorphic map]] are holomorphic line bundles. Their transition functions are respectively \(g_{ij}g'_{ij}\), \(g_{ij}^{-1}\), and \(g_{ij}\circ f\). Isomorphism classes form an [[algebra-groups/abelian-group|abelian group]] under tensor product, with the trivial bundle as identity and the dual as inverse.

## Sections and local data

A [[differential-geometry/holomorphic-section|holomorphic section]] is represented in each trivialization by a holomorphic function \(s_i\) satisfying \(s_i=g_{ij}s_j\) under the stated transition convention. A nowhere-vanishing global holomorphic section gives a holomorphic trivialization. A smooth [[fiber-bundles/nowhere-vanishing-section|nowhere-vanishing section]] proves only smooth triviality and need not trivialize the holomorphic structure.

## Standard examples

The trivial bundle \(X\times\mathbb C\) is holomorphic. The top exterior power of the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]] is the canonical [[fiber-bundles/line-bundle|line bundle]]. Holomorphic line bundles also encode divisors and the Picard group.

## References

1. P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978. [DOI record](https://doi.org/10.1002/9781118032527). Relevant: Chapter 1, §1, holomorphic line bundles and divisors.
2. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, holomorphic vector bundles and line bundles.
