+++
id = "catalog/categories/vector-spaces"
title = "Category of vector spaces over a field"
kind = "definition"
summary = "Vector spaces over one fixed field and linear maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "linear-algebra/linear-map"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix a field \(k\). The **category \(k\text{-}\mathbf{Vect}\)** has [[linear-algebra/vector-space|vector spaces]] over \(k\) as objects and [[linear-algebra/linear-map|\(k\)-linear maps]] as morphisms. Thus a morphism satisfies
\[
f(ax+by)=af(x)+bf(y)\qquad(a,b\in k).
\]
The identity map is linear, and a composite of linear maps is linear; these give the categorical identities and composition.

## Scalar field and dimension

The field is fixed throughout a Hom-set. A complex vector space can also be regarded as a real vector space by [[algebra-commutative/restriction-of-scalars|restriction of scalars]], but the allowed maps change. For finite-dimensional spaces of dimensions \(m\) and \(n\), bases identify the Hom-space with \(M_{n\times m}(k)\); the identification depends on the bases.

## Units and products

No algebra product or distinguished multiplicative unit is part of this category. Multiplication-preserving or bracket-preserving maps belong to more structured categories.
