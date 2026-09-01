+++
id = "complex-analysis/quaternionic-monge-ampere-dirichlet-theorem"
title = "Dirichlet theorem for the quaternionic Monge–Ampère equation"
kind = "theorem"
summary = "Existence and uniqueness of a continuous quaternionic PSH solution on a bounded strictly pseudoconvex domain."
aliases = ["quaternionic Monge-Ampere Dirichlet theorem", "Dirichlet problem for quaternionic Monge–Ampère"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
prerequisites = ["complex-analysis/strictly-quaternionically-pseudoconvex-domain"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb H^n\) be a bounded
[[complex-analysis/strictly-quaternionically-pseudoconvex-domain|strictly
quaternionically pseudoconvex domain]]. If \(f\in C(\overline\Omega)\) is
nonnegative and \(\varphi\in C(\partial\Omega)\), then there is a unique
\(u\in C(\overline\Omega)\), quaternionic plurisubharmonic on \(\Omega\), such
that
\[
\operatorname{MA}_{\mathbb H}(u)=f\,dV,
\qquad u|_{\partial\Omega}=\varphi.
\]

## Interpretation

The interior equation is an equality of
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère measures]]. Thus the theorem includes degenerate right-hand sides
that may vanish, and the solution need not be \(C^2\).

## Smooth ball case

When \(\Omega\) is the unit ball, \(f>0\) and both \(f\) and \(\varphi\) are
smooth, the solution is smooth up to the boundary. This stronger regularity
statement should not be silently extended to arbitrary continuous data.

## References

1. Semyon Alesker, “Quaternionic Monge–Ampère equations,” *Journal of Geometric Analysis* 13 (2003), 205–238. [arXiv record](https://arxiv.org/abs/math/0208005). Relevant: Theorems 0.1.2–0.1.3.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: Theorems 5.2 and 5.4.
