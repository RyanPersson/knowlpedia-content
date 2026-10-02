+++
id = "catalog/categories/complex-lie-groups"
title = "Category of complex Lie groups"
kind = "definition"
summary = "Complex Lie groups and holomorphic group homomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "lie-groups/complex-lie-group"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of complex Lie groups** has [[lie-groups/complex-lie-group|complex Lie groups]] as objects and holomorphic [[algebra-groups/group-homomorphism|group homomorphisms]] as morphisms. Its identity maps and composition are those of [[differential-geometry/holomorphic-map|holomorphic maps]]. Holomorphicity is a requirement on the manifold map, not a claim that the group's carrier is a complex [[linear-algebra/vector-space|vector space]].

## Forgetting complex structure

Forgetting complex structure gives a [[algebra-category-theory/faithful-functor|faithful functor]] to [[catalog/categories/real-lie-groups|real Lie groups]]. Entrywise conjugation on \(SL(2,\mathbb C)\) is a smooth real group automorphism but is antiholomorphic, so is not a morphism in this category. Its differential is real-linear and conjugate-linear on the complex [[lie-groups/lie-algebra|Lie algebra]].

## Lie algebra

Differentiating at the identity produces a complex-linear bracket-preserving map. This distinguishes the complex Lie-algebra view from the larger real-linear vector-space endomorphism space.
