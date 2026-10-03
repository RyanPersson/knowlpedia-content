+++
id = "catalog/algebras/m-3-r"
title = "M_3(R) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_3(R) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{3}(\mathbb R)\)** consists of \(3\)-by-\(3\) matrices with entries in [[shared-foundations/real-numbers|R]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{3}X_{ir}Y_{rj}.
\]
Its unit is \(I_{3}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(9\), since there are \(9\) entries with \(1\) real coordinates each.

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\).

## Size convention

For every size at least two, \(E_{11}E_{22}=0\) exhibits nonzero [[algebra-rings/zero-divisor|zero divisors]]. Matrix size is not the dimension of the whole algebra.
