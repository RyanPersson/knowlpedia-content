+++
id = "linear-algebra/moore-determinant"
title = "Moore determinant"
kind = "definition"
summary = "The real polynomial determinant of a hyperhermitian quaternionic matrix."
aliases = ["Moore determinant of a quaternionic Hermitian matrix", "quaternionic Moore determinant"]
domains = ["linear-algebra", "quaternionic-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hyperhermitian-form", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For an \(n\times n\) [[linear-algebra/hyperhermitian-form|hyperhermitian
matrix]] \(A\), let \(R_A\) be the real \(4n\times4n\) matrix of the
associated real-linear operator. The **Moore determinant** is the unique real
homogeneous polynomial \(\det_M A\), normalized by \(\det_M I=1\), such that
\[
\det_{\mathbb R}(R_A)=(\det_M A)^4.
\]
It has degree \(n\) and agrees with the ordinary determinant when \(A\) has
complex Hermitian entries.

## Basic formulas

If \(A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\) with
\(\lambda_i\in\mathbb R\), then
\(\det_M A=\prod_i\lambda_i\). For
\[
A=\begin{pmatrix}a&q\\ \bar q&b\end{pmatrix},
\qquad a,b\in\mathbb R,
\]
one has \(\det_M A=ab-|q|^2\). In particular, the Moore determinant is
nonnegative on positive-semidefinite hyperhermitian matrices.

## Congruence law

For a quaternionic matrix \(C\),
\[
\det_M(C^*AC)=\det_M(A)\det_M(C^*C).
\]
This is the replacement for multiplicativity needed in
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]]
geometry. The Moore determinant is not a determinant on all quaternionic
matrices; it is defined on the hyperhermitian subspace. The Dieudonné
determinant is a different construction with a different domain and codomain.

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: §§1.1–1.2.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §1.
