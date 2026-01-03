---
title: "Darboux's Theorem"
description: "Derivatives satisfy the intermediate value property even when they are not continuous"
---

**Darboux's Theorem**: Let $f:(a,b)\to\mathbb{R}$ be {{< knowl id="differentiability-one-variable" text="differentiable" >}}. If $x_1,x_2\in(a,b)$ with $x_1<x_2$ and $\alpha$ lies between $f'(x_1)$ and $f'(x_2)$, then there exists $c\in(x_1,x_2)$ such that
$
f'(c)=\alpha.
$

This theorem says {{< knowl id="derivative" text="derivatives" >}} cannot have jump discontinuities: they may be very irregular, but they still take all {{< knowl id="intermediate-value-theorem" text="intermediate values" >}}. It is a key qualitative property of differentiation that does not rely on {{< knowl id="continuity-on-a-set" text="continuity" >}} of $f'$.
