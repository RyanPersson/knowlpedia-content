+++
id = "catalog/categories/spin8-representations"
title = "Category of real Spin(8) representations"
kind = "definition"
summary = "Finite-dimensional real representations of the fixed compact Spin(8) group and intertwiners."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "linear-algebra/linear-map", "algebra-groups/group-homomorphism", "lie-groups/spin-group"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix the compact [[topology/simply-connected-space|simply connected]] group \(G=\operatorname{Spin}(8)\). The **category of finite-dimensional real \(G\)-representations** has pairs \((V,\rho)\), with \(V\) a finite-dimensional real [[linear-algebra/vector-space|vector space]] and \(\rho:G\to GL(V)\) a smooth [[algebra-groups/group-homomorphism|group homomorphism]], as objects. A morphism \((V,\rho)\to(W,\sigma)\) is a real-linear map \(T\) satisfying
\[
T\rho(g)=\sigma(g)T\qquad(g\in G).
\]
Identities and composition are ordinary linear identities and composition.

## Triality changes the action

The vector and two [[lie-groups/half-spin-representation|half-spin representations]] are three different objects of this category. Their eight-dimensional carriers are isomorphic as real vector spaces, but the actions are not pairwise intertwined by an invertible map. Triality permutes them by precomposing their actions with suitable automorphisms of the group; it does not identify them as representations of the fixed group with fixed action.
