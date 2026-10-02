+++
id = "catalog/algebras/m-2-h"
title = "M_2(H) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_2(H) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quaternion-division-algebra", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{2}(\mathbb H)\)** consists of \(2\)-by-\(2\) matrices with entries in [[linear-algebra/quaternion-division-algebra|H]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{2}X_{ir}Y_{rj}.
\]
Its unit is \(I_{2}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(16\), since there are \(4\) entries with \(4\) real coordinates each.

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\). The standard multiplication is real-bilinear. Choosing a copy of \(\mathbb C\subset\mathbb H\) does not make it a complex algebra: those scalars need not commute with matrix entries.

## Size convention

For every size at least two, \(E_{11}E_{22}=0\) exhibits nonzero [[algebra-rings/zero-divisor|zero divisors]]. Matrix size is not the dimension of the whole algebra.
