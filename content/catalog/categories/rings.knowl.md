+++
id = "catalog/categories/rings"
title = "Category of rings with arbitrary ring homomorphisms"
kind = "definition"
summary = "Associative rings, without requiring units, and additive multiplicative maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-rings/ring"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of rings with arbitrary ring homomorphisms** has [[algebra-rings/ring|associative rings]] as objects, without imposing a multiplicative identity. A morphism \(f:R\to S\) preserves addition and multiplication: \(f(x+y)=f(x)+f(y)\) and \(f(xy)=f(x)f(y)\). If units happen to exist, this category does not require \(f(1_R)=1_S\). Identities and composition are ordinary functions.

## Convention and comparison

The zero map is always allowed. For unital objects and maps preserving their units, use the [[catalog/categories/unital-rings|category of unital rings]]. The distinction is stored explicitly in the catalogue.
