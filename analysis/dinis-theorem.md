---
title: "Dini's Theorem"
description: "On a compact space, monotone pointwise convergence of continuous functions to a continuous limit is uniform"
---

**Dini's Theorem**: Let $K$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $f_n:K\to\mathbb{R}$ be {{< knowl id="continuity-on-a-set" text="continuous" >}} for all $n$. Suppose:
- for each $x\in K$, the sequence $f_n(x)$ is {{< knowl id="monotone-sequence" text="monotone" >}} in $n$ (either nondecreasing for all $x$, or nonincreasing for all $x$), and
- $f_n(x)\to f(x)$ {{< knowl id="pointwise-convergence" text="pointwise" >}} on $K$ for some continuous function $f:K\to\mathbb{R}$.

Then $f_n\to f$ {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="uniformly" >}} on $K$.

Dini's theorem is a compactness-based upgrade from pointwise to uniform convergence when monotonicity is present. It is especially useful when uniform estimates are hard but monotone structure is available.
