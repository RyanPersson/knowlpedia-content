+++
id = "complex-analysis/residue"
title = "Residue"
kind = "definition"
summary = "The coefficient of the inverse-linear term in a Laurent expansion."
aliases = ["complex residue"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(f\) be holomorphic on a punctured neighborhood of \(a\), with [[complex-analysis/laurent-series|Laurent expansion]]
\[
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-a)^n.
\]
The **residue** of \(f\) at \(a\) is
\[
\operatorname{Res}(f,a)=c_{-1}
=\frac{1}{2\pi i}\int_{|z-a|=\rho}f(z)\,dz
\]
for any sufficiently small positively oriented circle.

## Computation at poles

At a simple pole,
\[
\operatorname{Res}(f,a)=\lim_{z\to a}(z-a)f(z).
\]
At a pole of order \(m\),
\[
\operatorname{Res}(f,a)
=\frac{1}{(m-1)!}
\left.\frac{d^{m-1}}{dz^{m-1}}\bigl((z-a)^m f(z)\bigr)\right|_{z=a}.
\]

## Role

Only the coefficient of \((z-a)^{-1}\) contributes to a contour integral around \(a\). The [[complex-analysis/residue-theorem|residue theorem]] turns this local coefficient into a global integration tool.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 5, §§1–2.
