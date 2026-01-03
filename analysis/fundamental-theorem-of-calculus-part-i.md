---
title: "Fundamental Theorem of Calculus, Part I"
description: "Integrating a function produces an antiderivative at points of continuity"
---

**Fundamental Theorem of Calculus (Part I)**: Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} and define
$
F(x)=\int_a^x f(t)\,dt \qquad (x\in[a,b]).
$
Then $F$ is {{< knowl id="continuity-on-a-set" text="continuous" >}} on $[a,b]$. Moreover, if $f$ is continuous at a point $x_0\in(a,b)$, then $F$ is {{< knowl id="differentiability-one-variable" text="differentiable" >}} at $x_0$ and
$
F'(x_0)=f(x_0).
$

This theorem is the precise link "differentiation undoes integration" (at points where $f$ is continuous). It also provides a systematic way to construct antiderivatives.
