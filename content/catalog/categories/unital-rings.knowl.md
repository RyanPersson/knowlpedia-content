+++
id = "catalog/categories/unital-rings"
title = "Category of unital rings"
kind = "definition"
summary = "Unital associative rings and unit-preserving ring homomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-rings/unital-ring"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of unital rings** has [[algebra-rings/unital-ring|unital associative rings]] as objects. Morphisms \(f:R\to S\) preserve addition, multiplication, and the unit: \(f(1_R)=1_S\). Identities and composition are the corresponding functions. The zero ring is allowed as an object.

## Convention and comparison

The zero function into a nonzero unital ring is not a morphism. An inclusion of a matrix corner generally belongs to the [[catalog/categories/rings|category with arbitrary ring homomorphisms]] but not to this category, because it sends the smaller unit to a proper idempotent.
