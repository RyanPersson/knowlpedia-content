+++
id = "catalog/categories/abelian-groups"
title = "Category of abelian groups"
kind = "definition"
summary = "Abelian groups and additive homomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-groups/abelian-group"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of abelian groups** \(\mathbf{Ab}\) has [[algebra-groups/abelian-group|abelian groups]] as objects and additive maps \(f:A\to B\), satisfying \(f(x+y)=f(x)+f(y)\), as morphisms. Identities and composition are ordinary functions. Equivalently it is the [[algebra-category-theory/full-subcategory|full subcategory]] of [[catalog/categories/groups|groups]] on the abelian groups.

## Convention and comparison

A ring or [[linear-algebra/vector-space|vector space]] determines such an object only after its additive group has been specified. Its multiplicative [[algebra-rings/group-of-units|group of units]] is a different object and often has a different carrier.
