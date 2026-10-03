+++
id = "catalog/categories/unital-jordan-algebras-unital-maps"
title = "Category Jord1 of unital Jordan algebras and unital maps"
kind = "definition"
summary = "Unital Jordan algebras with unit-preserving Jordan homomorphisms."
aliases = ["Jord1 category", "Jord₁ category"]
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "nonassociative-algebra/jordan-algebra-homomorphism"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For a field \(k\) of characteristic different from \(2\), **\(\mathbf{Jord}_{1,k}\)** has unital [[nonassociative-algebra/jordan-algebra|Jordan algebras]] as objects. Morphisms \(f:J\to K\) are \(k\)-linear, preserve the Jordan product, and satisfy
\[
f(1_J)=1_K.
\]
Identity maps and composites obey all three requirements.

## Relationship to UJord

This is a subcategory of [[catalog/categories/unital-jordan-algebras-arbitrary-maps|\(\mathbf{UJord}_k\)]] with the same objects and possibly fewer morphisms. The zero map to a nonzero algebra and a proper matrix-corner inclusion are excluded. The scalar map \(k\to J\), \(t\mapsto t1_J\), is the unique unit-preserving \(k\)-linear algebra map from the scalar Jordan algebra.

## Endomorphisms versus automorphisms

Restricting to unital maps can shrink the endomorphism monoid. It does not shrink the automorphism group of a unital object, because every bijective [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]] preserves the unit automatically.
