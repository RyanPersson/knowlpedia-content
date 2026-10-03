+++
id = "catalog/categories/finite-groups"
title = "Category of finite groups"
kind = "definition"
summary = "Finite groups with all group homomorphisms between them."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-groups/finite-group", "catalog/categories/groups", "algebra-category-theory/full-subcategory", "algebra-groups/group-homomorphism"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

The **category of finite groups** \(\mathbf{FinGrp}\) is the [[algebra-category-theory/full-subcategory|full subcategory]] of the [[catalog/categories/groups|category of groups]] whose objects are [[algebra-groups/finite-group|finite groups]]. Its morphisms are all [[algebra-groups/group-homomorphism|group homomorphisms]] between these objects; identities and composition are the corresponding functions.

## Maps do not change when finiteness is recorded

For finite groups \(G,H\),
\[
\operatorname{Hom}_{\mathbf{FinGrp}}(G,H)=\operatorname{Hom}_{\mathbf{Grp}}(G,H).
\]
Finiteness restricts the objects, rather than adding a condition to their group homomorphisms. The constant map to the target identity is included.
