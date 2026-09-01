+++
id = "nonassociative-algebra/octonionic-two-by-two-determinant"
title = "Determinant of a two-by-two octonionic Hermitian matrix"
kind = "definition"
summary = "The quadratic determinant on the octonionic spin factor."
aliases = ["octonionic two-by-two determinant", "determinant on H_2(O)", "determinant of a 2 by 2 octonionic Hermitian matrix"]
domains = ["nonassociative-algebra", "linear-algebra", "octonionic-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For an element
\[
A=\begin{pmatrix}a&q\\ \bar q&b\end{pmatrix}
\in [[nonassociative-algebra/octonionic-spin-factor|H_2(\mathbb O)]],
\qquad a,b\in\mathbb R,\quad q\in\mathbb O,
\]
its **determinant** is the real quadratic polynomial
\[
\det A=ab-|q|^2.
\]

## Positivity

The positive cone of \(H_2(\mathbb O)\) is the closure of the cone of matrices
with \(a>0\) and \(\det A>0\). Equivalently, \(A\) is positive semidefinite
when its associated real [[linear-algebra/quadratic-form|quadratic form]] on
\(\mathbb O^2\) is nonnegative.

## Polarization

Because the determinant is quadratic, it has a symmetric bilinear
polarization
\[
\det(A,B)=\frac12\bigl(\det(A+B)-\det A-\det B\bigr).
\]
This degree-two determinant and its polarization are the algebraic operations
used in the [[complex-analysis/octonionic-monge-ampere-measure|octonionic
Monge–Ampère measure]].

## Dimension warning

This determinant belongs to the rank-two spin factor. The
[[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]]
\(H_3(\mathbb O)\) has a cubic Jordan determinant, but there is no analogous
ordinary determinant on arbitrary-size octonionic Hermitian matrices.

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §1.2.
2. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. Relevant: Euclidean Jordan algebras and spin factors.
