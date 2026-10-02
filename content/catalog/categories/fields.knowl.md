+++
id = "catalog/categories/fields"
title = "Category of fields"
kind = "definition"
summary = "Fields and unit-preserving field homomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-rings/field"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of fields** has [[algebra-rings/field|fields]] as objects and unit-preserving [[algebra-rings/ring-homomorphism|ring homomorphisms]] between them as morphisms. All fields satisfy \(0\ne1\). Every morphism is injective: its [[algebra-rings/kernel-is-ideal|kernel is an ideal]] in a field and cannot contain \(1\). Identities and composition are the usual functions.

## Convention and comparison

A [[algebra-fields-galois/field-extension|field extension]] supplies a morphism from its base field. An arbitrary [[linear-algebra/linear-map|linear map]] between the underlying [[linear-algebra/vector-space|vector spaces]] need not be a field morphism. In particular, there is no zero morphism between fields in this category.
