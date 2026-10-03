+++
id = "catalog/arithmetic/associative-algebra-a-over-k"
title = "Specified associative K-algebra A"
kind = "definition"
summary = "Specified associative K-algebra A with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-modules/algebra-over-ring", "catalog/arithmetic/extension-field-k-over-f"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

A **specified associative \(K\)-algebra \(A\)** is an associative unital [[algebra-modules/algebra-over-ring|algebra]] with a fixed unital scalar map \(K\to Z(A)\), where \(Z(A)\) is its center. Given a specified [[catalog/arithmetic/extension-field-k-over-f|extension \(K/F\)]], composing scalar maps also makes \(A\) an \(F\)-algebra.

## Four types of maps

A \(K\)-module endomorphism is \(K\)-linear; an \(F\)-module endomorphism need only be \(F\)-linear. A corresponding algebra endomorphism also preserves multiplication, with preservation of \(1_A\) controlled separately by the category. The algebra need not be commutative.

## Dimensions and comparison

When \([K:F]=d\) and \(\dim_K A=m\) are finite, \(\dim_F A=dm\). Choosing bases identifies the two linear endomorphism rings with \(M_m(K)\) and \(M_{dm}(F)\). Algebra endomorphisms are constrained by the multiplication table; dimension alone does not determine them. In infinite dimension the displayed dimension product is interpreted as cardinal multiplication.
