+++
id = "complex-analysis/harmonic-maximum-principle"
title = "Maximum principle for harmonic functions"
kind = "theorem"
summary = "A nonconstant harmonic function cannot attain an interior maximum or minimum."
aliases = ["harmonic maximum principle", "strong maximum principle for harmonic functions"]
domains = ["complex-analysis", "potential-theory", "partial-differential-equations"]
prerequisites = ["complex-analysis/harmonic-function", "topology/simply-connected-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb R^n\) be connected and let
\(u:U\to\mathbb R\) be [[complex-analysis/harmonic-function|harmonic]]. If
\(u\) attains a maximum or a minimum at an interior point, then \(u\) is
constant on \(U\).

## Boundary form

If \(U\) is bounded, \(u\) is continuous on \(\overline U\), and harmonic on
\(U\), then
\[
\max_{\overline U}u=\max_{\partial U}u,\qquad
\min_{\overline U}u=\min_{\partial U}u.
\]

## Proof mechanism

The mean-value property says that an interior value is the average of nearby
values. If it is already maximal, every nearby value must be equal to it.
Connectedness propagates this local constancy throughout the domain.

## Use

Applying the boundary form to the difference of two solutions proves
uniqueness for the Dirichlet problem. It also bounds derivatives or auxiliary
harmonic functions by their boundary values.

## References

1. Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., AMS, 2010. [Publisher record](https://bookstore.ams.org/gsm-19-r/).
