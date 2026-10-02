+++
id = "catalog/algebras/m-1-r"
title = "M_1(R) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_1(R) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{1}(\mathbb R)\)** consists of \(1\)-by-\(1\) matrices with entries in [[shared-foundations/real-numbers|R]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{1}X_{ir}Y_{rj}.
\]
Its unit is \(I_{1}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(1\), since there are \(1\) entries with \(1\) real coordinates each.

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\).

## Size convention

For size one, \([a]\mapsto a\) identifies this named matrix construction with [[shared-foundations/real-numbers|the coefficient algebra]], with the same product and scalar field.
