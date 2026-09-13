+++
id = "linear-algebra/matrix-transpose"
title = "Transpose of a matrix"
kind = "definition"
summary = "The matrix obtained by interchanging row and column indices."
aliases = ["matrix transpose", "transposition of a matrix"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an \(m\times n\) [[linear-algebra/matrix|matrix]] \(A\), its **transpose** \(A^{\mathsf T}\) is the \(n\times m\) matrix defined by
\[
(A^{\mathsf T})_{ij}=A_{ji}.
\]
Transposition interchanges rows and columns and satisfies \((A^{\mathsf T})^{\mathsf T}=A\).

## Algebraic identities

Over a commutative field, \((AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}\), \((A+B)^{\mathsf T}=A^{\mathsf T}+B^{\mathsf T}\), and \((cA)^{\mathsf T}=cA^{\mathsf T}\), whenever the operations have compatible sizes.

For complex matrices, the transpose does not conjugate entries. The conjugate transpose is \(A^*=\overline A^{\mathsf T}\); these two operations agree for real matrices.
