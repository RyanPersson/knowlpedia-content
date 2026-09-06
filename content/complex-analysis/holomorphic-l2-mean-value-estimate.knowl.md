+++
id = "complex-analysis/holomorphic-l2-mean-value-estimate"
title = "Holomorphic L2 mean-value estimate"
kind = "theorem"
summary = "The value of a holomorphic function is controlled by its L2 norm on any contained Euclidean ball."
aliases = ["L2-to-pointwise holomorphic estimate", "holomorphic mean-value bound"]
domains = ["complex-analysis", "several-complex-variables"]
section_mode = "progressive"
prerequisites = ["complex-analysis/plurisubharmonic-function", "complex-analysis/harmonic-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U\subseteq\mathbb C^d\) be open and \(f:U\to\mathbb C\) holomorphic. If
\(B_r(z)\subset U\), then
\[
|f(z)|\le C_d r^{-d}\|f\|_{L^2(B_r(z))}.
\]

## Proof

The function \(|f|^2\) is
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]], hence
subharmonic as a function on \(\mathbb R^{2d}\). Its ball mean-value inequality
gives
\[
|f(z)|^2\le |B_r|^{-1}\int_{B_r(z)}|f(w)|^2\,dw.
\]
Since \(|B_r|\asymp_d r^{2d}\), taking square roots proves the estimate.

## Use

The estimate converts the weighted \(L^2\) control supplied by the
[[complex-analysis/hormander-l2-dbar-theorem|Hörmander theorem]] into pointwise
upper bounds and local nonvanishing bounds.

## References

1. Lars Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990.
