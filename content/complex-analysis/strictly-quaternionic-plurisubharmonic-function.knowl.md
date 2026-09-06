+++
id = "complex-analysis/strictly-quaternionic-plurisubharmonic-function"
title = "Strictly quaternionic plurisubharmonic function"
kind = "definition"
summary = "A smooth quaternionic plurisubharmonic function with positive-definite quaternionic Hessian."
aliases = ["strictly quaternionic PSH function", "strict qPSH function"]
domains = ["complex-analysis", "quaternionic-analysis", "potential-theory"]
prerequisites = ["complex-analysis/quaternionic-hessian", "complex-analysis/quaternionic-plurisubharmonic-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A real-valued \(C^2\) function \(u\) on \(\Omega\subseteq\mathbb H^n\) is
**strictly quaternionic plurisubharmonic** if its
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]] is positive
definite at every point. Equivalently, the restriction of \(u\) to every
affine right quaternionic line is strictly subharmonic.

## Quantitative local form

On each relatively compact coordinate neighborhood, strictness is equivalent
to the existence of \(\varepsilon>0\) such that
\[
u(q)-\varepsilon|q|^2
\]
is [[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic]]. This formulation makes clear that strictness is an open
positivity condition.

## Geometric roles

Strictly quaternionic PSH defining functions characterize
[[complex-analysis/strictly-quaternionically-pseudoconvex-domain|strictly
quaternionically pseudoconvex domains]]. On a
[[differential-geometry/hypercomplex-manifold|hypercomplex manifold]], smooth
strictly quaternionic PSH functions are precisely the local potentials of
[[differential-geometry/hkt-metric|HKT metrics]].

## References

1. Semyon Alesker, “Quaternionic Monge–Ampère equations,” *Journal of Geometric Analysis* 13 (2003), 205–238. [arXiv record](https://arxiv.org/abs/math/0208005).
2. Semyon Alesker and Misha Verbitsky, “Plurisubharmonic functions on hypercomplex manifolds and HKT-geometry,” *Journal of Geometric Analysis* 16 (2006), 375–399. [arXiv record](https://arxiv.org/abs/math/0510140).
