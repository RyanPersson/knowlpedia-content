+++
id = "complex-analysis/complex-derivative"
title = "Complex derivative"
kind = "definition"
summary = "The derivative defined by a complex difference quotient independent of direction."
aliases = ["complex differentiability", "complex-differentiable"]
domains = ["complex-analysis"]
prerequisites = ["shared-foundations/function", "shared-foundations/complex-numbers-c"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb C\) be open, \(f:U\to\mathbb C\), and \(z_0\in U\). The **complex derivative** of \(f\) at \(z_0\) is the limit
\[
f'(z_0)=\lim_{\substack{h\to0\\h\in\mathbb C}}\frac{f(z_0+h)-f(z_0)}{h},
\]
when it exists. The limit must have the same value as \(h\) approaches \(0\) through every complex direction.

## Real-linear interpretation

Viewing \(f\) as a map \(\mathbb R^2\to\mathbb R^2\), complex differentiability at \(z_0\) is equivalent to real differentiability there with derivative equal to multiplication by one complex number. Thus its real derivative must commute with multiplication by \(i\). The [[complex-analysis/cauchy-riemann-equations|Cauchy–Riemann equations]] express this constraint in coordinates.

## Holomorphicity

A function is [[differential-geometry/holomorphic-map|holomorphic]] on \(U\) when it is complex differentiable at every point of \(U\). Differentiability at one point is much weaker: it need not imply continuity of the derivative or complex differentiability nearby.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 2, §§1–2.
