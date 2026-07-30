+++
id = "lie-groups/hermitian-matrix-model-of-minkowski-space"
title = "Hermitian matrix model of Minkowski space"
kind = "construction"
summary = "Hermitian 2×2 matrices model Minkowski space, with determinant equal to the negative of the collection's quadratic form."
aliases = ["Pauli matrix model of Minkowski space", "Hermitian 2 by 2 model of spacetime"]
domains = ["lie-groups", "linear-algebra", "mathematical-physics"]
section_mode = "progressive"
+++

Identify \(v=(t,x,y,z)\in\mathbb R^{1,3}\) with the [[linear-algebra/hermitian-matrix|Hermitian matrix]]
\[
X(v)=
\begin{pmatrix}
t+z&x-iy\\
x+iy&t-z
\end{pmatrix}.
\]
Then
\[
\det X(v)=t^2-x^2-y^2-z^2.
\]
For the \((-+++)\) Minkowski quadratic form fixed at [[linear-algebra/minkowski-vector-space|Minkowski vector space]], this says
\[
\det X(v)=-q(v).
\]
Thus the determinant is the opposite of the quadratic form used in this collection; it is not being identified with \(q\) itself.

## The SL(2,C) action

For \(A\in SL(2,\mathbb C)\), define
\[
X\longmapsto AXA^\dagger,
\]
where \(A^\dagger=\overline A^{\mathsf T}\). This map preserves Hermitian matrices and
\[
\det(AXA^\dagger)=\det A\,\det X\,\overline{\det A}=\det X.
\]
It therefore preserves \(q\) and determines a real-linear Lorentz transformation. Composition of matrices makes this a homomorphism from \(SL(2,\mathbb C)_{\mathbb R}\) into \(SO^+(1,3)\).

## Null vectors and rank one

A nonzero future null vector corresponds to a nonzero positive-semidefinite rank-one Hermitian matrix. Such a matrix has the form \(zz^\dagger\) for \(z\in\mathbb C^2\setminus\{0\}\), and rescaling \(z\) by a nonzero complex scalar preserves its null ray. This gives the [[differential-geometry/celestial-sphere|celestial sphere]] its \(\mathbb{CP}^1\) description.

## References

1. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §§1.2–1.3. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
2. Rolf Berndt, *An Introduction to Symplectic Geometry*, AMS, 2001, Appendix A. [Publisher record](https://doi.org/10.1090/gsm/026).
