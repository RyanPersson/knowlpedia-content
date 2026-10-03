+++
id = "catalog/categories/unital-associative-algebras"
title = "Category of unital associative algebras"
kind = "definition"
summary = "Unital associative algebras over a field and unit-preserving linear algebra maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "catalog/categories/associative-algebras"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix a field \(k\). The **category \(k\text{-}\mathbf{Alg}_1\)** has unital associative \(k\)-algebras as objects. A morphism \(f:A\to B\) is \(k\)-linear, multiplicative, and unit-preserving:
\[
f(xy)=f(x)f(y),\qquad f(1_A)=1_B.
\]
Identities and composition are ordinary map identities and composition. Equivalently the maps preserve the ring operations and commute with the specified central scalar maps from \(k\).

## Comparison with arbitrary maps

For a nonzero target, the zero [[linear-algebra/linear-map|linear map]] is not a morphism here. A bijective multiplicative linear map between unital algebras is automatically unital, since its value on the source unit acts as a unit on the entire target. Hence adding the unit condition changes general Hom-sets and endomorphism monoids, but not automorphism groups of unital objects.

The catalogue's \(K\)-algebra versus \(F\)-algebra comparisons use this unit-preserving convention unless the arbitrary-map category is named explicitly.
