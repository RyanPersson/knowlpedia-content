+++
id = "catalog/categories/nonassociative-algebras"
title = "Category of nonassociative algebras"
kind = "definition"
summary = "Vector spaces with a bilinear multiplication and product-preserving linear maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "nonassociative-algebra/nonassociative-algebra"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix a field \(k\). The **category of nonassociative \(k\)-algebras** has [[nonassociative-algebra/nonassociative-algebra|\(k\)-algebras]] with a bilinear multiplication as objects, without requiring associativity, commutativity, a unit, or the Jordan identity. Morphisms are \(k\)-linear maps preserving that multiplication. Identities and composition are ordinary map composition.

## Which product is being forgotten

An associative, alternative, Lie, or [[nonassociative-algebra/jordan-algebra|Jordan algebra]] can be considered here with its own specified bilinear product. Changing from an associative product \(xy\) to a commutator \([x,y]\) or to \((xy+yx)/2\) changes the algebra structure; it is not merely forgetting an axiom. The catalogue must record that construction explicitly.

## Sedenions

The sedenions fit this broad category despite failing the composition-algebra and alternative-algebra identities. No division or Jordan property follows from membership here.
