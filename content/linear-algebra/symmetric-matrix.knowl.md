+++
id = "linear-algebra/symmetric-matrix"
title = "Symmetric matrix"
kind = "definition"
summary = "A square matrix equal to its transpose."
aliases = []
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix-transpose"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A square matrix \(A\) is **symmetric** when \(A=A^{\mathsf T}\), equivalently \(A_{ij}=A_{ji}\) for all indices. Here \(A^{\mathsf T}\) is the [[linear-algebra/matrix-transpose|transpose]].

## Symmetric part

Over a field of characteristic different from two, every square matrix has the decomposition
\[
A=\frac{A+A^{\mathsf T}}2+\frac{A-A^{\mathsf T}}2.
\]
The first term is symmetric and the second is skew-symmetric. For real vectors, the skew-symmetric part contributes zero to \(x^{\mathsf T}Ax\).

## Real and complex conventions

A real symmetric matrix is self-adjoint for the Euclidean inner product. For a complex matrix, symmetry \(A=A^{\mathsf T}\) differs from the Hermitian condition \(A=A^*\).
