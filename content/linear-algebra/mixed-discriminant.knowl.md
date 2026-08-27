+++
id = "linear-algebra/mixed-discriminant"
title = "Mixed discriminant"
kind = "definition"
summary = "The symmetric multilinear polarization of a determinant on self-adjoint matrices."
aliases = ["mixed determinant", "mixed Moore determinant"]
domains = ["linear-algebra", "convex-analysis", "quaternionic-analysis"]
section_mode = "progressive"
+++

Let \(A_1,\ldots,A_n\) be \(n\times n\) matrices in a class on which a
degree-\(n\) determinant is defined. Their **mixed discriminant** is
\[
D(A_1,\ldots,A_n)
=\frac1{n!}[t_1\cdots t_n]\,
\det(t_1A_1+\cdots+t_nA_n),
\]
where \([t_1\cdots t_n]\) denotes the coefficient of that monomial. This
normalization gives \(D(A,\ldots,A)=\det A\).

## Properties

The mixed discriminant is symmetric and multilinear. For real symmetric or
complex Hermitian matrices it polarizes the ordinary determinant; for
[[linear-algebra/hyperhermitian-form|hyperhermitian matrices]] it polarizes the
[[linear-algebra/moore-determinant|Moore determinant]]. It is nonnegative when
all its arguments are positive semidefinite.

## Role in Hessian measures

Applying \(D\) to Hessians of several functions produces mixed Monge–Ampère
expressions. In quaternionic pluripotential theory this leads to the
[[complex-analysis/mixed-quaternionic-monge-ampere-measure|mixed quaternionic
Monge–Ampère measure]]. This matrix construction is analogous to, but distinct
from, the [[convex-analysis/mixed-volume|mixed volume]] of
[[convex-analysis/convex-body|convex bodies]].

## References

1. A. D. Aleksandrov, “Mixed discriminants and mixed volumes,” *Matematicheskii Sbornik* 3 (1938), 227–251.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §1.
