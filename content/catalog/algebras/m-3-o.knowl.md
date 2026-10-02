+++
id = "catalog/algebras/m-3-o"
title = "M_3(O) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_3(O) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/octonion-algebra", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{3}(\mathbb O)\)** consists of \(3\)-by-\(3\) matrices with entries in [[nonassociative-algebra/octonion-algebra|O]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{3}X_{ir}Y_{rj}.
\]
Its unit is \(I_{3}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(72\), since there are \(9\) entries with \(8\) real coordinates each.

Two-factor matrix products are unambiguous, but multiplication is not associative: the coefficient algebra embeds in a diagonal corner, so its nonzero associators survive. No associative-algebra or ring view is assigned. Symmetrizing this product must not be assumed to give a [[nonassociative-algebra/jordan-algebra|Jordan algebra]].

## Size convention

For every size at least two, \(E_{11}E_{22}=0\) exhibits nonzero zero divisors. Matrix size is not the dimension of the whole algebra.
