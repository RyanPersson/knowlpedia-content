+++
id = "catalog/categories/jordan-algebras"
title = "Category Jord of Jordan algebras"
kind = "definition"
summary = "Jordan algebras over one field and all product-preserving linear maps."
aliases = ["Jord category"]
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "nonassociative-algebra/jordan-algebra-homomorphism"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For a field \(k\) of characteristic different from \(2\), **\(\mathbf{Jord}_k\)** is the category of [[nonassociative-algebra/jordan-algebra|Jordan \(k\)-algebras]] and all [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphisms]]. Objects need not be unital. A morphism is a \(k\)-linear map satisfying
\[
f(x\circ y)=f(x)\circ f(y).
\]
Identities and composition are the corresponding linear functions.

## The catalogue convention

The real and complex categories are separate scalar choices. The [[catalog/categories/unital-jordan-algebras-arbitrary-maps|UJord category]] restricts the objects to unital algebras but keeps all these maps. The [[catalog/categories/unital-jordan-algebras-unital-maps|Jord1 category]] additionally requires maps to preserve units. These names are explicit conventions of this catalogue.

## Zero maps

The zero map always belongs to a Jord Hom-set, so such a Hom-set is never empty. A statement \(\operatorname{Hom}(J,K)=\{0\}\) means there is exactly one map, not no maps.
