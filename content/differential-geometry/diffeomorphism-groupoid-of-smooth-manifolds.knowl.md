+++
id = "differential-geometry/diffeomorphism-groupoid-of-smooth-manifolds"
title = "Diffeomorphism groupoid of smooth manifolds"
kind = "definition"
summary = "The maximal subgroupoid of the smooth-manifold category, retaining every manifold but only diffeomorphisms."
aliases = ["core of the category of smooth manifolds", "Man core", "Man superscript simeq"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

The **diffeomorphism groupoid of smooth manifolds** is the category
\[
\mathbf{Man}^{\simeq}
\]
whose objects are finite-dimensional [[fiber-bundles/smooth-manifold|smooth
manifolds]] and whose morphisms are
[[fiber-bundles/diffeomorphism|diffeomorphisms]]. Every morphism is invertible,
so this category is a [[algebra-category-theory/groupoid|groupoid]].

It is the [[algebra-category-theory/core-of-a-category|core]], or maximal
subgroupoid, of
[[differential-geometry/category-of-smooth-manifolds|\(\mathbf{Man}\)]].
Thus it contains every object of \(\mathbf{Man}\), but only the isomorphisms
among its smooth maps.

## What the core forgets

Passing from \(\mathbf{Man}\) to \(\mathbf{Man}^{\simeq}\) preserves the
question “are these manifolds diffeomorphic?” and all diffeomorphism groups.
It discards noninvertible geometry: inclusions, submersions, constant maps,
covering projections that are not one-sheeted, and smooth functions
\(M\to\mathbb R\).

In particular, “the category whose morphisms are diffeomorphisms” is a
reasonable classification groupoid, but it is not the usual category of
smooth manifolds. Constructions such as pullback of smooth functions and the
[[differential-geometry/tangent-functor|tangent functor]] are defined on the larger category.

## Automorphisms

The automorphism group of \(M\) in \(\mathbf{Man}^{\simeq}\) is its
[[differential-geometry/diffeomorphism-group|diffeomorphism group]]
\(\operatorname{Diff}(M)\). Distinct objects in the same connected component
of this groupoid are diffeomorphic, while automorphisms record the symmetries
of an individual representative.

## References

1. Emily Riehl, *Category Theory in Context*, Dover, 2016. [Author's edition](https://emilyriehl.github.io/files/context.pdf). Relevant: categories, isomorphisms, subcategories, and groupoids.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth maps and diffeomorphisms.
