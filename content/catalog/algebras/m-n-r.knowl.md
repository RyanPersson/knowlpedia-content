+++
id = "catalog/algebras/m-n-r"
title = "M_n(R) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_n(R) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For each integer \(n\geq1\), **\(M_{n}(\mathbb R)\)** consists of \(n\)-by-\(n\) matrices with entries in [[shared-foundations/real-numbers|R]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{n}X_{ir}Y_{rj}.
\]
Its unit is \(I_{n}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

Each of the \(n^2\) entries contributes \(1\) real coordinates, so the real dimension is \(n^2\).

Matrix multiplication is associative because the coefficient algebra is associative; distributivity and rebracketing justify the equality of each entry of \((XY)Z\) and \(X(YZ)\).

## Size convention

The entries for sizes one, two, and three are separate catalogue objects; this record is the parameterized family. Matrix size is not the dimension of the algebra.
