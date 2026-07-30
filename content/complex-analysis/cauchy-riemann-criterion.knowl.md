+++
id = "complex-analysis/cauchy-riemann-criterion"
title = "Cauchy–Riemann criterion"
kind = "theorem"
summary = "A regularity-sensitive criterion for a function to be holomorphic."
aliases = ["Cauchy-Riemann criterion"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb C\) be open and write \(f=u+iv:U\to\mathbb C\). If \(u\) and \(v\) are \(C^1\) and satisfy the [[complex-analysis/cauchy-riemann-equations|Cauchy–Riemann equations]] throughout \(U\), then \(f\) is [[differential-geometry/holomorphic-map|holomorphic]]. Conversely, a holomorphic function satisfies those equations; indeed, holomorphic functions are smooth.

## Pointwise form

At a single point, real differentiability of \(f\) together with the Cauchy–Riemann equations is equivalent to existence of the [[complex-analysis/complex-derivative|complex derivative]] at that point. Continuity of the partial derivatives near the point is a convenient sufficient condition for real differentiability.

## Regularity warning

Merely having partial derivatives that satisfy the equations pointwise is not, by itself, a safe holomorphicity criterion: existence of partial derivatives need not imply real differentiability. Weaker hypotheses are available in distributional and Sobolev formulations, but they are separate regularity theorems rather than the elementary \(C^1\) criterion.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 2, §2.
