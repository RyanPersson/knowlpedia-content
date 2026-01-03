---
title: "Uniform convergence and integration"
description: "Uniform limits of integrable functions are integrable and integrals commute with uniform limits"
---

**Uniform convergence and integration (Riemann)**: Let $f_n:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} for each $n$, and suppose $f_n\to f$ {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="uniformly" >}} on $[a,b]$. Then:
- $f$ is Riemann integrable on $[a,b]$, and
- the integrals converge to the integral of the limit:
  $
  \lim_{n\to\infty}\int_a^b f_n(x)\,dx=\int_a^b f(x)\,dx.
  $

This theorem justifies passing limits through integrals when convergence is uniform, and it is a standard tool in approximation and {{< knowl id="series-of-functions" text="series-of-functions" >}} arguments.
