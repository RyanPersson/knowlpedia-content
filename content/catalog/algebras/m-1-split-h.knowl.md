+++
id = "catalog/algebras/m-1-split-h"
title = "M_1(H_s) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_1(H_s) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-quaternions", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{1}(\mathbb H_s)\)** consists of \(1\)-by-\(1\) matrices with entries in [[catalog/algebras/split-quaternions|H_s]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{1}X_{ir}Y_{rj}.
\]
Its unit is \(I_{1}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(4\), since there are \(1\) entries with \(4\) real coordinates each.

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\). Replacing each split quaternion by its two-by-two real matrix identifies this algebra with \(M_{2}(\mathbb R)\).

## Size convention

For size one, \([a]\mapsto a\) identifies this named matrix construction with [[catalog/algebras/split-quaternions|the coefficient algebra]], with the same product and scalar field.
