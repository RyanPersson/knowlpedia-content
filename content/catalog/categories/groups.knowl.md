+++
id = "catalog/categories/groups"
title = "Category of groups"
kind = "definition"
summary = "Groups and identity-preserving multiplicative maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-groups/group-homomorphism"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of groups** \(\mathbf{Grp}\) has [[algebra-groups/group|groups]] as objects and [[algebra-groups/group-homomorphism|group homomorphisms]] as morphisms. Thus a map \(f:G\to H\) obeys \(f(xy)=f(x)f(y)\). It automatically sends identity to identity and inverses to inverses. Identities and composition are the corresponding functions.

## Convention and comparison

This category imposes no topology or differentiability. The constant map with value the target identity is always a morphism; a constant map with any other value is not.
