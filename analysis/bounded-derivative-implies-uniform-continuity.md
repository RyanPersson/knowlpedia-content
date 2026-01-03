---
title: "Bounded derivative implies uniform continuity"
description: "A bounded derivative gives a Lipschitz bound, hence uniform continuity"
---

Let $I\subseteq\mathbb{R}$ be an {{< knowl id="interval" text="interval" >}} and let $f:I\to\mathbb{R}$ be {{< knowl id="differentiability-one-variable" text="differentiable" >}} on $I^\circ$.

**Proposition**: Suppose there exists $M\ge 0$ such that $|f'(x)|\le M$ for all $x\in I^\circ$. Then for all $x,y\in I$,
$
|f(x)-f(y)|\le M|x-y|.
$
In particular, $f$ is {{< knowl id="lipschitz-continuity" text="Lipschitz" >}} on $I$ and hence {{< knowl id="uniform-continuity" text="uniformly continuous" >}} on $I$.

This proposition is one of the most common applications of the {{< knowl id="mean-value-theorem" text="mean value theorem" >}}: {{< knowl id="derivative" text="derivatives" >}} control global oscillation.
