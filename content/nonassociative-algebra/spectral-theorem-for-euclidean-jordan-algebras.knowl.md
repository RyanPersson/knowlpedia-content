+++
id = "nonassociative-algebra/spectral-theorem-for-euclidean-jordan-algebras"
title = "Spectral theorem for Euclidean Jordan algebras"
kind = "theorem"
summary = "Every element of a Euclidean Jordan algebra is a real linear combination of a Jordan frame, with uniquely determined eigenvalues."
aliases = ["Jordan spectral theorem", "spectral decomposition in a Euclidean Jordan algebra", "EJA spectral theorem"]
domains = ["nonassociative-algebra", "linear-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/euclidean-jordan-algebra", "nonassociative-algebra/jordan-frame"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(J\) be a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean
Jordan algebra]] of rank \(r\). For every \(x\in J\), there is a
[[nonassociative-algebra/jordan-frame|Jordan frame]]
\((c_1,\ldots,c_r)\) and real numbers \(\lambda_1,\ldots,\lambda_r\) such that

\[
x=\lambda_1c_1+\cdots+\lambda_rc_r.
\]

The multiset of eigenvalues
\(\{\lambda_1,\ldots,\lambda_r\}\), including multiplicities, is uniquely
determined by \(x\). The diagonalizing frame need not be unique when an
eigenvalue is repeated.

## Spectral idempotents

If \(\mu_1,\ldots,\mu_s\) are the distinct eigenvalues, collecting equal
terms gives

\[
x=\mu_1e_1+\cdots+\mu_se_s,
\]

where the \(e_j\) are nonzero pairwise
[[nonassociative-algebra/orthogonal-jordan-idempotents|orthogonal
idempotents]] summing to the unit. These coarser spectral idempotents are
uniquely determined by \(x\); each is the sum of the primitive frame
idempotents carrying the same eigenvalue.

## Functional calculus

For a real function \(f\) defined on the spectrum of \(x\), set

\[
f(x)=\sum_{i=1}^r f(\lambda_i)c_i.
\]

This is independent of the choice of diagonalizing frame. In particular, one
defines

\[
\operatorname{tr}_J(x)=\sum_i\lambda_i,
\qquad
\det_J(x)=\prod_i\lambda_i.
\]

The element \(x\) is invertible exactly when no \(\lambda_i\) vanishes, and
then \(x^{-1}=\sum_i\lambda_i^{-1}c_i\). It lies in the cone of squares
exactly when every eigenvalue is nonnegative.

## Matrix model

For \(J=H_n(\mathbb R)\) with product
\(a\circ b=(ab+ba)/2\), this is the ordinary spectral theorem for real
symmetric matrices. The \(c_i\) are rank-one [[linear-algebra/orthogonal-projection|orthogonal projections]], and the
Jordan trace and determinant agree with the usual matrix invariants. The
Jordan theorem extends the same mechanism to [[nonassociative-algebra/spin-factor-jordan-algebra|spin factors]], quaternionic
Hermitian matrices, and the exceptional [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]].

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford
   University Press, 1994, Chapter III, Theorem 1.2. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, Chapter 13.
   [Publisher record](https://doi.org/10.1007/b97489).
