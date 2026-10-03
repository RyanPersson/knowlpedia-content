+++
id = "catalog/algebras/m-2-c"
title = "M_2(C) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_2(C) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{2}(\mathbb C)\)** consists of \(2\)-by-\(2\) matrices with entries in [[shared-foundations/complex-numbers-c|C]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{2}X_{ir}Y_{rj}.
\]
Its unit is \(I_{2}\). The scalar field for this catalogue object is \(\mathbb C\).

## Dimension and multiplication

The real dimension is \(8\), since there are \(4\) entries with \(2\) real coordinates each. Its complex dimension is \(4\).

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\).

## Size convention

For every size at least two, \(E_{11}E_{22}=0\) exhibits nonzero [[algebra-rings/zero-divisor|zero divisors]]. Matrix size is not the dimension of the whole algebra.
