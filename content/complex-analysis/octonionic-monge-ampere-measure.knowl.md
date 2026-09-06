+++
id = "complex-analysis/octonionic-monge-ampere-measure"
title = "Octonionic Monge–Ampère measure"
kind = "definition"
summary = "The determinant-Hessian measure of a continuous octonionic plurisubharmonic function on the octonionic plane."
aliases = ["octonionic Monge-Ampere operator", "octonionic Hessian measure"]
domains = ["complex-analysis", "octonionic-analysis", "potential-theory"]
prerequisites = ["complex-analysis/octonionic-plurisubharmonic-function", "complex-analysis/octonionic-hessian", "nonassociative-algebra/octonionic-two-by-two-determinant"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a \(C^2\) [[complex-analysis/octonionic-plurisubharmonic-function|
octonionic plurisubharmonic function]] \(u\) on
\(\Omega\subseteq\mathbb O^2\), its **octonionic Monge–Ampère measure** is
\[
\operatorname{MA}_{\mathbb O}(u)
=\det\!\left(\operatorname{Hess}_{\mathbb O}u\right)dV,
\]
using the
[[nonassociative-algebra/octonionic-two-by-two-determinant|quadratic
determinant]] on [[nonassociative-algebra/octonionic-spin-factor|
\(H_2(\mathbb O)\)]].

## Continuous potentials

For continuous octonionic PSH functions, the smooth expression extends
uniquely to a nonnegative Borel measure such that locally
[[real-analysis/uniform-convergence|uniform convergence]]
of potentials implies weak convergence of measures. This is the octonionic
analogue of the Aleksandrov and Chern–Levine–Nirenberg continuity theorems.

## Max-min identity

If \(u,v\) and \(\min(u,v)\) are continuous octonionic PSH functions, then
the corresponding determinant measures satisfy the same inclusion–exclusion
identity under \(\max\) and \(\min\) as in the
[[complex-analysis/quaternionic-blocki-formula|quaternionic Błocki formula]].
This identity is what turns support-function Hessian measures into valuations.

## Scope

The measure is defined here on \(\mathbb O^2\). It should not be presented as
an octonionic Monge–Ampère operator in arbitrary dimension.

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §§3.2–3.3.
