+++
id = "complex-analysis/strictly-quaternionically-pseudoconvex-domain"
title = "Strictly quaternionically pseudoconvex domain"
kind = "definition"
summary = "A smooth bounded quaternionic domain admitting local strictly quaternionic PSH defining functions."
aliases = ["quaternionic strictly pseudoconvex domain", "strict q-pseudoconvexity"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
prerequisites = ["complex-analysis/strictly-quaternionic-plurisubharmonic-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A bounded domain \(\Omega\subseteq\mathbb H^n\) with smooth boundary is
**strictly quaternionically pseudoconvex** if, near every
\(p\in\partial\Omega\), there is a smooth
[[complex-analysis/strictly-quaternionic-plurisubharmonic-function|strictly
quaternionic plurisubharmonic]] function \(\rho\) such that
\[
\Omega=\{\rho<0\},\qquad \rho(p)=0,
\qquad d\rho(p)\ne0
\]
within that neighborhood.

## Role of the defining function

The nonvanishing differential makes \(\rho=0\) a smooth local boundary, while
positive definiteness of its
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]] supplies the strict
pseudoconvexity. The condition is independent of the particular admissible
defining function.

## Examples and comparison

The Euclidean ball in \(\mathbb H^n\) is strictly quaternionically
pseudoconvex, with defining function \(\rho(q)=|q|^2-1\). The definition is
parallel to strict pseudoconvexity in several complex variables, but its
positivity is tested on quaternionic rather than complex lines.

## References

1. Semyon Alesker, “Quaternionic Monge–Ampère equations,” *Journal of Geometric Analysis* 13 (2003), 205–238. [arXiv record](https://arxiv.org/abs/math/0208005). Relevant: Definition 0.1.1.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §5.
