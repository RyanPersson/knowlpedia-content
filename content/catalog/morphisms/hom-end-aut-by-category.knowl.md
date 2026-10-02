+++
id = "catalog/morphisms/hom-end-aut-by-category"
title = "Hom, End, and Aut depend on the category"
kind = "page"
summary = "How the chosen scalar field, operations, units, and regularity determine the allowed maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/endomorphism-category", "algebra-category-theory/automorphism-category"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For objects \(A,B\) in a [[algebra-category-theory/category|category]] \(\mathcal C\), write
\[
\operatorname{Hom}_{\mathcal C}(A,B),\qquad
\operatorname{End}_{\mathcal C}(A)=\operatorname{Hom}_{\mathcal C}(A,A),\qquad
\operatorname{Aut}_{\mathcal C}(A)=\operatorname{End}_{\mathcal C}(A)^\times.
\]
Here the last expression means the invertible elements of the endomorphism monoid under composition. The category is part of the question: an object's carrier alone does not specify its allowed maps.

## What can change

For an algebra over a [[algebra-fields-galois/field-extension|field extension]] \(K/F\), there are four natural views: a \(K\)-vector space, an \(F\)-vector space, a \(K\)-algebra, and an \(F\)-algebra. Forgetting multiplication permits more maps; restricting scalars can also permit more maps. See [[catalog/morphisms/restriction-of-scalars-endomorphisms|the comparison of endomorphism spaces]].

For [[nonassociative-algebra/jordan-algebra|Jordan algebras]], the [[catalog/morphisms/jordan-unit-conventions|unit convention]] changes Hom and End, even though all three categories have the same automorphisms of a unital object.

For a [[fiber-bundles/lie-group|Lie group]] such as \(SL(2,\mathbb C)\), use [[catalog/categories/real-lie-groups|smooth real group maps]] or [[catalog/categories/complex-lie-groups|holomorphic group maps]]. Its [[lie-groups/example-sl2c|Lie algebra \(\mathfrak{sl}_2(\mathbb C)\)]] has distinct [[catalog/morphisms/linear-endomorphisms-of-sl2-complex|real-linear and complex-linear endomorphisms]]. A matrix group is not generally a [[linear-algebra/vector-space|vector space]].

## What the catalogue records

A record marked **complete** describes the whole requested Hom-set, endomorphism monoid, or automorphism group under its stated conditions. A **partial** record gives a verified family, constraint, or example, without claiming exhaustiveness. A missing record says **not catalogued**. It does not say that no maps exist.

This distinction is visible in the [[catalog/morphisms/finite-field-homomorphisms-by-category|finite-field examples]]: an empty field Hom-set can become a singleton containing the zero map after switching to arbitrary [[algebra-rings/ring-homomorphism|ring homomorphisms]].
