+++
id = "catalog/categories/finite-simple-groups"
title = "Category of finite simple groups"
kind = "definition"
summary = "The full subcategory of finite groups on nontrivial simple objects."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/finite-groups", "algebra-groups/simple-group", "algebra-category-theory/full-subcategory", "algebra-groups/group-homomorphism"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

The catalogue's **category of finite simple groups** is the [[algebra-category-theory/full-subcategory|full subcategory]] of [[catalog/categories/finite-groups|finite groups]] whose objects are [[algebra-groups/simple-group|simple groups]]. It includes cyclic groups of prime order and nonabelian finite simple groups. Morphisms are all [[algebra-groups/group-homomorphism|group homomorphisms]] between these objects, including the constant map to the identity.

## This is not a category containing only isomorphisms

A homomorphism from a simple group has either trivial kernel or the whole group as kernel. Consequently, every nonconstant morphism here is injective, but it need not be surjective when the source and target differ.

For an [[catalog/finite-groups/relationships/endomorphisms-of-finite-simple-groups|endomorphism of one finite simple group]], injectivity does imply surjectivity.
