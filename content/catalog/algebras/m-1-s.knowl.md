+++
id = "catalog/algebras/m-1-s"
title = "M_1(S) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_1(S) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/sedenions", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{1}(\mathbb S)\)** consists of \(1\)-by-\(1\) matrices with entries in [[catalog/algebras/sedenions|S]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{1}X_{ir}Y_{rj}.
\]
Its unit is \(I_{1}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(16\), since there are \(1\) entries with \(16\) real coordinates each.

Two-factor matrix products are unambiguous, but multiplication is not associative: the coefficient algebra embeds in a diagonal corner, so its nonzero associators survive. No associative-algebra or ring view is assigned. Symmetrizing this product must not be assumed to give a [[nonassociative-algebra/jordan-algebra|Jordan algebra]].

## Size convention

For size one, \([a]\mapsto a\) identifies this named matrix construction with [[catalog/algebras/sedenions|the coefficient algebra]], with the same product and scalar field.
