+++
id = "catalog/categories/unital-jordan-algebras-arbitrary-maps"
title = "Category UJord of unital Jordan algebras with arbitrary maps"
kind = "definition"
summary = "Unital Jordan objects with maps that may fail to preserve the unit."
aliases = ["UJord category"]
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "catalog/categories/jordan-algebras"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For a field \(k\) of characteristic different from \(2\), **\(\mathbf{UJord}_k\)** is the [[algebra-category-theory/full-subcategory|full subcategory]] of [[catalog/categories/jordan-algebras|\(\mathbf{Jord}_k\)]] whose objects possess a multiplicative unit. Morphisms remain all \(k\)-linear Jordan-product-preserving maps; they are not required to preserve units. The identity and composite maps are those of Jord.

## Full subcategory means the same Hom-sets

For unital \(J,K\),
\[
\operatorname{Hom}_{\mathbf{UJord}_k}(J,K)
=\operatorname{Hom}_{\mathbf{Jord}_k}(J,K).
\]
The unit of each object is unique, but its image under a homomorphism may be a proper idempotent or zero. An inclusion of a matrix corner is a basic example. This use of UJord is an explicit catalogue convention rather than a universal notation.

## Automorphisms

A surjective homomorphism between unital [[nonassociative-algebra/jordan-algebra|Jordan algebras]] preserves the unit: if \(b=f(a)\), then \(f(1)\circ b=f(1\circ a)=b\). Thus bijective homomorphisms agree with the automorphisms in the unit-preserving category.
