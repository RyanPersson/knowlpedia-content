+++
id = "catalog/algebras/m-n-split-c"
title = "M_n(C_s) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_n(C_s) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-complex-numbers", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For each integer \(n\geq1\), **\(M_{n}(\mathbb C_s)\)** consists of \(n\)-by-\(n\) matrices with entries in [[catalog/algebras/split-complex-numbers|C_s]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{n}X_{ir}Y_{rj}.
\]
Its unit is \(I_{n}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

Each of the \(n^2\) entries contributes \(2\) real coordinates, so the real dimension is \(2n^2\).

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\).

## Size convention

The entries for sizes one, two, and three are separate catalogue objects; this record is the parameterized family. Matrix size is not the dimension of the algebra.
