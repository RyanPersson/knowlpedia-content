+++
id = "linear-algebra/hyperhermitian-form"
title = "Hyperhermitian form"
kind = "definition"
summary = "A quaternionic Hermitian form, represented in a basis by a self-adjoint quaternionic matrix."
aliases = ["quaternionic Hermitian form", "hyperhermitian matrix", "quaternionic Hermitian matrix"]
domains = ["linear-algebra", "quaternionic-analysis"]
prerequisites = ["linear-algebra/quaternionic-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional right
[[linear-algebra/quaternionic-vector-space|quaternionic vector space]]. A
**hyperhermitian form** is a map \(a:V\times V\to\mathbb H\) that is additive
in each variable and satisfies
\[
a(x,yq)=a(x,y)q,
\qquad
a(x,y)=\overline{a(y,x)}.
\]
Thus it is right-linear in the second variable and conjugate-linear in the
first. It is positive definite if \(a(x,x)>0\) for every \(x\ne0\).

## Matrix presentation

After choosing a basis, \(a\) is represented by a matrix \(A=(a_{ij})\) with
\(A^*=A\), equivalently \(a_{ij}=\overline{a_{ji}}\), through
\[
a(x,y)=\sum_{i,j}\overline{x_i}a_{ij}y_j.
\]
The representing matrix is therefore self-adjoint over \(\mathbb H\). Under a
change of basis by \(C\), it transforms by congruence as \(A\mapsto C^*AC\).

## Spectral theorem and positivity

Every hyperhermitian matrix is unitarily diagonalizable with real diagonal
entries. It is positive semidefinite exactly when those entries are
nonnegative. The [[linear-algebra/moore-determinant|Moore determinant]] is the
determinant adapted to this self-adjoint class.

## Terminology

“Hyperhermitian” here describes linear algebra over \(\mathbb H\). A
[[differential-geometry/hyperhermitian-manifold|hyper-Hermitian manifold]] is a
geometric structure whose tangent-space metrics give such forms, but it also
includes a smoothly varying hypercomplex triple.

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: §1.
2. Fuzhen Zhang, “Quaternions and matrices of quaternions,” *Linear Algebra and its Applications* 251 (1997), 21–57. [DOI record](https://doi.org/10.1016/0024-3795(95)00543-9).
