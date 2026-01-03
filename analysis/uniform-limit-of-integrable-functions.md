---
title: "Uniform limit of integrable functions is integrable"
description: "Uniform convergence preserves Riemann integrability and allows exchanging limit and integral"
---

Let $f_n:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} for each $n$ and suppose $f_n\to f$ {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="uniformly" >}} on $[a,b]$.

**Proposition**:
- The limit function $f$ is Riemann integrable on $[a,b]$.
- The integrals converge to the integral of the limit:
  $
  \lim_{n\to\infty}\int_a^b f_n(x)\,dx=\int_a^b f(x)\,dx.
  $

This is the standard mechanism for proving integrability of limits and justifies passing limits through integrals under uniform convergence.
