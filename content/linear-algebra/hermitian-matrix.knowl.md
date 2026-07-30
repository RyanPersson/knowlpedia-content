+++
id = "linear-algebra/hermitian-matrix"
title = "Hermitian matrix"
kind = "definition"
summary = "A complex square matrix equal to its conjugate transpose."
aliases = ["self-adjoint matrix"]
domains = ["linear-algebra"]
section_mode = "progressive"
+++

A complex square matrix \(A=(a_{ij})\) is **Hermitian** if
\[
A^*=A,
\qquad\text{equivalently}\qquad
a_{ij}=\overline{a_{ji}},
\]
where \(A^*=\overline A^{\,T}\) is the conjugate transpose. Hermitian matrices are the matrices of self-adjoint linear operators on finite-dimensional complex inner-product spaces in orthonormal bases.

## Spectral theorem

Every Hermitian matrix has real [[linear-algebra/eigenvalue|eigenvalues]] and is unitarily diagonalizable: there are a unitary matrix \(U\) and a real diagonal matrix \(D\) such that
\[
A=UDU^*.
\]
Conversely, every matrix of this form is Hermitian.

## The two-by-two space

The Hermitian \(2\times2\) matrices form a four-dimensional real vector space:
\[
\begin{pmatrix}
t+z & x-iy\\
x+iy & t-z
\end{pmatrix},
\qquad t,x,y,z\in\mathbb R.
\]
Its determinant is \(t^2-x^2-y^2-z^2\), which realizes the Minkowski quadratic form in a matrix model.

## References

1. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013. [DOI record](https://doi.org/10.1017/CBO9781139020411). Relevant: Chapter 4.
