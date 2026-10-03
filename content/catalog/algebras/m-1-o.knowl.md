+++
id = "catalog/algebras/m-1-o"
title = "M_1(O) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_1(O) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/octonion-algebra", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{1}(\mathbb O)\)** consists of \(1\)-by-\(1\) matrices with entries in [[nonassociative-algebra/octonion-algebra|O]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{1}X_{ir}Y_{rj}.
\]
Its unit is \(I_{1}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(8\), since there are \(1\) entries with \(8\) real coordinates each.

Two-factor matrix products are unambiguous, but multiplication is not associative: the coefficient algebra embeds in a diagonal corner, so its nonzero associators survive. No associative-algebra or ring view is assigned. Symmetrizing this product must not be assumed to give a [[nonassociative-algebra/jordan-algebra|Jordan algebra]].

## Size convention

For size one, \([a]\mapsto a\) identifies this named matrix construction with [[nonassociative-algebra/octonion-algebra|the coefficient algebra]], with the same product and scalar field.
