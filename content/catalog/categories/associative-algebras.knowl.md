+++
id = "catalog/categories/associative-algebras"
title = "Category of associative algebras with arbitrary homomorphisms"
kind = "definition"
summary = "Associative algebras over a fixed field and product-preserving linear maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "linear-algebra/vector-space", "algebra-modules/bilinear-map"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix a field \(k\). The **category of associative \(k\)-algebras with arbitrary homomorphisms** has \(k\)-vector spaces with a bilinear associative product as objects. A morphism \(f:A\to B\) is \(k\)-linear and satisfies
\[
f(xy)=f(x)f(y).
\]
Objects need not have units, and units are not required to be preserved when present. Identities and composition are the corresponding [[linear-algebra/linear-map|linear maps]].

## Unit-preserving variant

The [[catalog/categories/unital-associative-algebras|unital category]] requires units in the objects and their preservation by morphisms. In the arbitrary-map category, the zero map and a matrix-corner inclusion are allowed. Both categories have a forgetful functor to the [[catalog/categories/vector-spaces|category of vector spaces]], but most linear maps fail to preserve the product.
