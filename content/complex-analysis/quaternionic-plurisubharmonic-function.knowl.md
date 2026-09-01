+++
id = "complex-analysis/quaternionic-plurisubharmonic-function"
title = "Quaternionic plurisubharmonic function"
kind = "definition"
summary = "An upper-semicontinuous function on quaternionic space whose restriction to every right quaternionic line is subharmonic."
aliases = ["quaternionic PSH function", "quaternionic plurisubharmonicity", "qPSH function"]
domains = ["complex-analysis", "quaternionic-analysis", "potential-theory"]
prerequisites = ["complex-analysis/upper-semicontinuous-function", "complex-analysis/subharmonic-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb H^n\) be open. A function
\(u:\Omega\to[-\infty,\infty)\) is **quaternionic plurisubharmonic** if it is
[[complex-analysis/upper-semicontinuous-function|upper-semicontinuous]] and,
for every affine right quaternionic line
\(L=q_0+v\mathbb H\), the restriction \(u|_{\Omega\cap L}\) is
[[complex-analysis/subharmonic-function|subharmonic]] on the underlying real
four-dimensional line, or identically \(-\infty\) on a component.

## Smooth criterion

For \(u\in C^2(\Omega)\), this is equivalent to positive semidefiniteness of
the [[complex-analysis/quaternionic-hessian|quaternionic Hessian]]
\[
\left(\frac{\partial^2u}{\partial\bar q_i\,\partial q_j}\right).
\]
This is the quaternionic counterpart of positivity of the real Hessian for a
convex function and of the Levi form for a
[[complex-analysis/plurisubharmonic-function|complex PSH function]].

## Relation to convexity and subharmonicity

Every convex function on a convex open subset of \(\mathbb H^n\cong
\mathbb R^{4n}\) is quaternionic PSH, and every quaternionic PSH function is
ordinary subharmonic. The first inclusion is generally strict. These are
genuine quaternionic analogues, not an identification of convex, complex PSH,
and quaternionic PSH functions on a common domain.

## Basic closure properties

Finite maxima and nonnegative linear combinations of quaternionic PSH
functions remain quaternionic PSH. Locally uniform limits do as well, provided
the limit is not identically \(-\infty\) on a component. For continuous
quaternionic PSH functions, the
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère measure]] extends the smooth Hessian determinant.

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: §3.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §3.
