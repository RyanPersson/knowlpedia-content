+++
id = "complex-analysis/holomorphic-functions-are-analytic"
title = "Holomorphic functions are analytic"
kind = "theorem"
summary = "Complex differentiability on an open set forces a local convergent power-series expansion."
aliases = ["analyticity of holomorphic functions"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

If \(f\) is holomorphic on an open set \(U\subseteq\mathbb C\), then at every \(a\in U\) there is \(r>0\) such that
\[
f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(z-a)^n
\qquad (|z-a|<r).
\]
One may take any \(r\) for which the closed disc centered at \(a\) lies in \(U\). Thus one-variable complex differentiability implies complex analyticity.

## Proof mechanism

Apply the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]] on a circle around \(a\), expand
\[
\frac1{\zeta-z}
=\frac1{\zeta-a}\sum_{n\ge0}
\left(\frac{z-a}{\zeta-a}\right)^n,
\]
and integrate term by term. The coefficient formula is therefore forced by the boundary values of \(f\).

## Contrast with real analysis

A real \(C^\infty\) function need not equal its Taylor series. The equivalence of holomorphic and analytic behavior is a rigidity specific to complex analysis and explains why the analytic clause in [[differential-geometry/holomorphic-map|holomorphic map]] is a theorem, not an independent definition.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 4, §2.
