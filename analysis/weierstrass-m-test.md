---
title: "Weierstrass M-test"
description: "A comparison test guaranteeing uniform convergence of a series of functions"
---

**Weierstrass M-test**: Let $X$ be a set and let $f_n:X\to\mathbb{R}$ (or $\mathbb{C}$). Suppose there exist numbers $M_n\ge 0$ such that
$
|f_n(x)|\le M_n \quad \text{for all } x\in X \text{ and all } n,
$
and the numerical {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty M_n$ {{< knowl id="convergent-series" text="converges" >}}. Then the {{< knowl id="series-of-functions" text="function series" >}} $\sum_{n=1}^\infty f_n(x)$ {{< knowl id="uniform-convergence-of-a-series-of-functions" text="converges uniformly" >}} on $X$. In particular, it converges {{< knowl id="absolutely-convergent-series" text="absolutely" >}} and uniformly:
$
\sup_{x\in X}\sum_{n=1}^\infty |f_n(x)| < \infty.
$

The M-test is a primary mechanism for proving uniform convergence, especially for power series and Fourier-type expansions.
