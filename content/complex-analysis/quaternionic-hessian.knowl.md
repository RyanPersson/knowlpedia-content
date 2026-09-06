+++
id = "complex-analysis/quaternionic-hessian"
title = "Quaternionic Hessian"
kind = "definition"
summary = "The hyperhermitian matrix of mixed Cauchy–Fueter derivatives of a real-valued function."
aliases = ["quaternionic Hessian matrix", "Hessian over the quaternions"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["complex-analysis/cauchy-fueter-operators", "linear-algebra/hyperhermitian-form", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a real-valued \(C^2\) function \(u\) on an open subset of
\(\mathbb H^n\), its **quaternionic Hessian** is
\[
\operatorname{Hess}_{\mathbb H}u
=\left(\frac{\partial^2u}
{\partial\bar q_i\,\partial q_j}\right)_{i,j=1}^n,
\]
using the [[complex-analysis/cauchy-fueter-operators|Cauchy–Fueter operator]]
convention fixed there. This matrix is
[[linear-algebra/hyperhermitian-form|hyperhermitian]].

## Positivity criterion

A \(C^2\) function is
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic]] exactly when its quaternionic Hessian is positive
semidefinite at every point. Strict plurisubharmonicity corresponds to positive
definiteness.

## Transformation law

Under a right quaternionic-linear change of variables \(q\mapsto Aq\), the
Hessian transforms by hyperhermitian congruence. Consequently its
[[linear-algebra/moore-determinant|Moore determinant]] has the covariance
needed to define the
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère operator]].

## Order convention

The transpose/order in the displayed matrix is essential. Early versions of
several foundational papers used the transposed convention and were later
corrected. In this knowl, rows are indexed by \(\partial_{\bar q_i}\) and
columns by \(\partial_{q_j}\).

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” revised 2024. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: §§2–3.
2. Semyon Alesker, “Quaternionic Monge–Ampère equations,” *Journal of Geometric Analysis* 13 (2003), 205–238. [arXiv record](https://arxiv.org/abs/math/0208005).
