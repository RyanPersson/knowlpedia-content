+++
id = "linear-algebra/hermitian-matrix"
title = "Hermitian matrix"
kind = "definition"
summary = "A complex square matrix equal to its conjugate transpose."
aliases = ["self-adjoint matrix"]
domains = ["linear-algebra"]
prerequisites = ["linear-algebra/orthonormal-basis"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A complex square matrix \(A=(a_{ij})\) is **Hermitian** if
\[
A^*=A,
\qquad\text{equivalently}\qquad
a_{ij}=\overline{a_{ji}},
\]
where \(A^*=\overline A^{\,T}\) is the conjugate transpose. Hermitian matrices are the matrices of self-adjoint linear operators on finite-dimensional complex inner-product spaces in [[linear-algebra/orthonormal-basis|orthonormal bases]].

## Spectral theorem

Every Hermitian matrix has real [[linear-algebra/eigenvalue|eigenvalues]] and is unitarily diagonalizable: there are a unitary matrix \(U\) and a real diagonal matrix \(D\) such that
\[
A=UDU^*.
\]
Conversely, every matrix of this form is Hermitian.

The special role of \(2\times2\) Hermitian matrices in Lorentz geometry is
treated by the [[lie-groups/hermitian-matrix-model-of-minkowski-space|Hermitian
matrix model of Minkowski space]].

## References

1. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013. [DOI record](https://doi.org/10.1017/CBO9781139020411). Relevant: Chapter 4.
