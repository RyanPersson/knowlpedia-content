+++
id = "complex-analysis/quaternionic-monge-ampere-continuity-theorem"
title = "Continuity of quaternionic Monge–Ampère measures"
kind = "theorem"
summary = "Locally uniform convergence of continuous quaternionic PSH functions implies weak convergence of their Hessian measures."
aliases = ["quaternionic Aleksandrov theorem", "quaternionic Chern–Levine–Nirenberg theorem"]
domains = ["complex-analysis", "quaternionic-analysis", "potential-theory"]
section_mode = "progressive"
+++

Let \(u_m,u\) be continuous
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic functions]] on \(\Omega\subseteq\mathbb H^n\). If
\(u_m\to u\) uniformly on compact subsets, then
\[
\operatorname{MA}_{\mathbb H}(u_m)
\rightharpoonup \operatorname{MA}_{\mathbb H}(u)
\]
weakly as Borel measures. The same statement holds for
[[complex-analysis/mixed-quaternionic-monge-ampere-measure|mixed measures]]
when each potential converges locally uniformly.

## Significance

This theorem both characterizes the nonsmooth quaternionic Monge–Ampère
measure and makes it stable under approximation. It is the quaternionic
counterpart of Aleksandrov's continuity theorem for convex Hessian measures
and of the Chern–Levine–Nirenberg continuity theory in complex analysis.

## Application to convex bodies

Convergence of [[convex-analysis/convex-body|convex bodies]] in the
[[topology/hausdorff-distance|Hausdorff metric]] is equivalent to locally
[[real-analysis/uniform-convergence|uniform convergence]] of their
[[convex-analysis/support-function|support
functions]]. The theorem therefore supplies the continuity part of the
[[convex-analysis/pluripotential-valuation-construction|pluripotential
construction of valuations]].

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: Theorem 3.4.
2. Semyon Alesker, “Valuations on convex sets, non-commutative determinants, and pluripotential theory,” *Advances in Mathematics* 195 (2005), 561–595. [arXiv record](https://arxiv.org/abs/math/0401219).
