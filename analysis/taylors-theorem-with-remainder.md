---
title: "Taylor's Theorem with remainder"
description: "Approximates a smooth function by a polynomial with a controlled error term"
---

**Taylor's Theorem (Lagrange remainder)**: Let $f$ be $(n+1)$ times continuously differentiable on an {{< knowl id="interval" text="interval" >}} containing $a$ and $x$. Then there exists $\xi$ between $a$ and $x$ such that
$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
$

Taylor's theorem is the precise statement behind local polynomial approximation and error estimation. It is fundamental in asymptotics, numerical approximation, and in proving properties like analyticity of power series.
