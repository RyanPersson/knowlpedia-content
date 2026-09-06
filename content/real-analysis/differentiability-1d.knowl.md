+++
id = "real-analysis/differentiability-1d"
title = "Differentiability in one variable"
kind = "knowl"
summary = "The property of having a finite derivative at a point or on an interval."
aliases = ["differentiability-1d", "Differentiability in one variable"]
domains = ["real-analysis"]
prerequisites = ["shared-foundations/function"]
dependency_review_count = 1
legacy_source_path = "real-analysis/differentiability-1d.md"
+++

A [[shared-foundations/function|function]] \(f:I\to\mathbb R\) is **differentiable at** \(a\in I\) if the finite limit
\[
f'(a)=\lim_{\substack{x\to a\\x\in I,\ x\ne a}}\frac{f(x)-f(a)}{x-a}
\]
exists. It is **differentiable on \(I\)** if it is differentiable at every point of \(I\), with one-sided limits used at endpoints of an interval.

## Examples

- Every [[real-analysis/polynomial|polynomial]] is differentiable at every real number.
- The function \(f(x)=|x|\) is not differentiable at \(x=0\).

## Remarks

Differentiability is stronger than continuity, as recorded in [[real-analysis/differentiability-implies-continuity|differentiability implies continuity]]. It interacts with order and shape through results such as [[real-analysis/derivative-sign-implies-monotonicity|derivative sign implies monotonicity]].
