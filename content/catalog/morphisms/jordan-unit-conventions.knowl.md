+++
id = "catalog/morphisms/jordan-unit-conventions"
title = "Jordan Hom-sets under the three unit conventions"
kind = "theorem"
summary = "UJord and Jord agree on maps between unital objects; Jord1 restricts maps, but all three have the same automorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/jordan-algebras", "catalog/categories/unital-jordan-algebras-arbitrary-maps", "catalog/categories/unital-jordan-algebras-unital-maps"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Let \(J,K\) be unital [[nonassociative-algebra/jordan-algebra|Jordan algebras]] over a fixed field \(k\) of characteristic different from \(2\). Under the catalogue conventions for [[catalog/categories/jordan-algebras|Jord]], [[catalog/categories/unital-jordan-algebras-arbitrary-maps|UJord]], and [[catalog/categories/unital-jordan-algebras-unital-maps|Jord1]],
\[
\operatorname{Hom}_{\mathbf{Jord}_{1,k}}(J,K)
\subseteq\operatorname{Hom}_{\mathbf{UJord}_k}(J,K)
=\operatorname{Hom}_{\mathbf{Jord}_k}(J,K).
\]
The inclusion can be strict. However,
\[
\operatorname{Aut}_{\mathbf{Jord}_{1,k}}(J)
=\operatorname{Aut}_{\mathbf{UJord}_k}(J)
=\operatorname{Aut}_{\mathbf{Jord}_k}(J).
\]

## Proof and strictness

The Hom equality follows because UJord is a [[algebra-category-theory/full-subcategory|full subcategory]] on unital objects. Jord1 imposes the additional equation \(f(1_J)=1_K\). If \(K\ne0\), the zero homomorphism belongs to the two larger Hom-sets and fails that equation.

If \(f:J\to K\) is surjective and preserves the Jordan product, then for every \(b=f(a)\),
\[
f(1_J)\circ b=f(1_J\circ a)=b.
\]
Thus \(f(1_J)\) is the target's unique unit. In particular every invertible [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]] is unit-preserving.

## A concrete endomorphism comparison

For the real scalar Jordan algebra \(\mathbb R\), every real-linear map is \(t\mapsto ct\). Product preservation says \(c^2=c\), so
\[
\operatorname{End}_{\mathbf{Jord}_{\mathbb R}}(\mathbb R)
=\operatorname{End}_{\mathbf{UJord}_{\mathbb R}}(\mathbb R)=\{0,\operatorname{id}\},
\qquad
\operatorname{End}_{\mathbf{Jord}_{1,\mathbb R}}(\mathbb R)=\{\operatorname{id}\}.
\]
All three automorphism groups are trivial.
