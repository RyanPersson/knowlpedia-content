---
title: "Uniform convergence and differentiation"
description: "Uniform convergence of derivatives plus convergence at one point implies uniform convergence of functions and term-by-term differentiation"
---

**Uniform convergence and differentiation**: Let $f_n:[a,b]\to\mathbb{R}$ be {{< knowl id="differentiability-one-variable" text="differentiable" >}} on $[a,b]$ (or on $(a,b)$ with suitable endpoint control). Assume:
- there exists $x_0\in[a,b]$ such that the sequence $(f_n(x_0))$ {{< knowl id="convergent-sequence" text="converges" >}} in $\mathbb{R}$, and
- the {{< knowl id="derivative" text="derivatives" >}} $f_n'$ converge {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="uniformly" >}} on $[a,b]$ to a function $g$.

Then $f_n$ converges uniformly on $[a,b]$ to a differentiable function $f$, and
$
f'(x)=g(x)\quad \text{for all } x\in[a,b].
$

This theorem provides the rigorous justification for differentiating a sequence (or series) term-by-term, under uniform convergence of derivatives.
