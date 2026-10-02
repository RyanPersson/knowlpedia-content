+++
id = "catalog/categories/real-lie-groups"
title = "Category of real Lie groups"
kind = "definition"
summary = "Finite-dimensional real Lie groups and smooth group homomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "fiber-bundles/lie-group", "algebra-groups/group-homomorphism"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of real Lie groups** has finite-dimensional smooth [[fiber-bundles/lie-group|real Lie groups]] as objects and smooth [[algebra-groups/group-homomorphism|group homomorphisms]] as morphisms. Manifolds are Hausdorff and [[topology/second-countable-space|second countable]]. The identity maps and compositions are smooth group homomorphisms.

## Underlying real groups

A [[lie-groups/complex-lie-group|complex Lie group]] defines an object here by forgetting its complex structure. Smooth real Lie-group maps need not be holomorphic. Entrywise conjugation on \(SL(2,\mathbb C)\) illustrates the difference.

## Linear terminology

A matrix Lie group is generally not a vector subspace: it is not closed under addition or scalar multiplication. Thus “real-linear endomorphism of a Lie group” does not name the morphisms of this category. Use smooth group maps here, or specify an underlying [[lie-groups/lie-algebra|Lie algebra]], a representation space, or an ambient matrix-space extension when linearity is intended.
