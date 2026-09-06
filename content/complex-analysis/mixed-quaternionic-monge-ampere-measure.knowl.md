+++
id = "complex-analysis/mixed-quaternionic-monge-ampere-measure"
title = "Mixed quaternionic Monge–Ampère measure"
kind = "definition"
summary = "The polarized measure obtained from quaternionic Hessians of several plurisubharmonic functions."
aliases = ["mixed quaternionic Hessian measure", "mixed quaternionic Monge-Ampere measure"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["complex-analysis/quaternionic-plurisubharmonic-function", "complex-analysis/quaternionic-hessian", "linear-algebra/mixed-discriminant", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For \(C^2\)
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic functions]]
\(u_1,\ldots,u_n\) on \(\Omega\subseteq\mathbb H^n\), their **mixed
quaternionic Monge–Ampère measure** is
\[
D\bigl(\operatorname{Hess}_{\mathbb H}u_1,\ldots,
\operatorname{Hess}_{\mathbb H}u_n\bigr)dV,
\]
where \(D\) is the [[linear-algebra/mixed-discriminant|mixed discriminant]] of
hyperhermitian matrices.

## Extension and diagonal case

For continuous [[complex-analysis/quaternionic-plurisubharmonic-function|
quaternionic PSH functions]], the mixed expression extends uniquely as a
nonnegative measure continuous under locally
[[real-analysis/uniform-convergence|uniform convergence]] in each
argument. On the diagonal it recovers the
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère measure]]:
\[
\operatorname{MA}_{\mathbb H}(u)
=D(\operatorname{Hess}_{\mathbb H}u,\ldots,
\operatorname{Hess}_{\mathbb H}u)dV.
\]

## References

1. Semyon Alesker, “Valuations on convex sets, non-commutative determinants, and pluripotential theory,” *Advances in Mathematics* 195 (2005), 561–595. [arXiv record](https://arxiv.org/abs/math/0401219).
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: Theorem 3.6.
