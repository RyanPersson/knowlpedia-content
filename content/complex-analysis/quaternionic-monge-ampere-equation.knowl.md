+++
id = "complex-analysis/quaternionic-monge-ampere-equation"
title = "Quaternionic Monge–Ampère equation"
kind = "definition"
summary = "A nonlinear elliptic equation prescribing the Moore determinant of a quaternionic Hessian."
aliases = ["quaternionic Monge-Ampere equation", "quaternionic determinant equation"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["complex-analysis/quaternionic-monge-ampere-measure", "complex-analysis/quaternionic-plurisubharmonic-function", "complex-analysis/quaternionic-hessian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

On a domain \(\Omega\subseteq\mathbb H^n\), a **quaternionic Monge–Ampère
equation** prescribes the
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic Hessian
measure]] of an unknown
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic function]] \(u\):
\[
\det_M\!\left(\frac{\partial^2u}
{\partial\bar q_i\,\partial q_j}\right)=f.
\]
For a nonsmooth \(u\), this equality is interpreted as equality of
[[complex-analysis/quaternionic-monge-ampere-measure|quaternionic
Monge–Ampère measures]].

## Elliptic branch

The equation is elliptic on the cone where the
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]] is positive
semidefinite. Requiring \(u\) to be
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic PSH]]
selects this branch, just as convexity does for the real equation and complex
plurisubharmonicity does for the complex equation.

## Dirichlet problem

Given boundary data \(\varphi\), the Dirichlet problem asks for
\[
\operatorname{MA}_{\mathbb H}(u)=f\,dV\quad\text{in }\Omega,
\qquad u|_{\partial\Omega}=\varphi.
\]
Existence and uniqueness hold in the continuous category on bounded strictly
quaternionically pseudoconvex domains under the standard nonnegativity
hypothesis on \(f\).

## References

1. Semyon Alesker, “Quaternionic Monge–Ampère equations,” *Journal of Geometric Analysis* 13 (2003), 205–238. [arXiv record](https://arxiv.org/abs/math/0208005).
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §5.
