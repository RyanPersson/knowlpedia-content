+++
id = "differential-geometry/category-of-symplectic-manifolds"
title = "Category of symplectic manifolds and symplectic maps"
kind = "definition"
summary = "The category whose objects are symplectic manifolds and whose morphisms preserve the symplectic forms by pullback."
aliases = ["category of symplectic manifolds", "symplectic manifolds and symplectic maps"]
domains = ["differential-geometry", "category-theory"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/symplectic-map", "algebra-category-theory/category", "algebra-category-theory/core-of-a-category"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **category of symplectic manifolds** used here has finite-dimensional
Hausdorff second-countable
[[differential-geometry/symplectic-manifold|symplectic manifolds without
boundary]] \((M,\omega_M)\) as objects and
[[differential-geometry/symplectic-map|symplectic maps]] as morphisms.
Disconnected objects are allowed when their dimensions are globally bounded.
Thus a morphism
\[
f:(M,\omega_M)\longrightarrow(N,\omega_N)
\]
is a smooth map satisfying
\[
f^*\omega_N=\omega_M.
\]
Identity maps are symplectic, and pullback functoriality gives
\[
(g\circ f)^*\omega_P=f^*(g^*\omega_P)=\omega_M,
\]
so these data do form a category.

Nondegeneracy forces \(df\) to be injective at every point. Morphisms in this category are therefore [[fiber-bundles/smooth-immersion|smooth immersions]] and may increase dimension; they are not assumed to be diffeomorphisms. An isomorphism in the category is exactly a [[differential-geometry/symplectomorphism|symplectomorphism]].

## Maximal subgroupoid

Keeping every object but only the isomorphisms gives the [[algebra-category-theory/core-of-a-category|maximal subgroupoid]] of symplectic manifolds and symplectomorphisms. The automorphism group of \((M,\omega)\) in this subgroupoid is the [[differential-geometry/symplectomorphism-group|symplectomorphism group]]
\[
\operatorname{Symp}(M,\omega).
\]

This subgroupoid should **not** be called a “symplectic groupoid.” In standard symplectic geometry, a symplectic groupoid is a Lie groupoid whose arrow manifold carries a compatible multiplicative symplectic form, a substantially different structure.

## Terminology

Some sources reserve “symplectic map” for a symplectomorphism. Under that convention, their category is already a groupoid. The present corpus uses the broader pullback-preserving convention, under which a [[differential-geometry/symplectic-embedding|symplectic embedding]] of positive codimension is a morphism.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §§1.1–1.2, symplectic maps and submanifolds.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 1, symplectic manifolds and maps.
