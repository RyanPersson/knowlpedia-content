---
title: "L'Hôpital's Rule"
description: "Evaluates certain indeterminate limits using the limit of a quotient of derivatives"
---

**L'Hôpital's Rule (0/0 form, one-sided)**: Let $a<b$, and let $f,g:[a,b)\to\mathbb{R}$ be {{< knowl id="continuity-on-a-set" text="continuous" >}} on $[a,b)$ and {{< knowl id="differentiability-one-variable" text="differentiable" >}} on $(a,b)$. Assume:
- $f(a)=g(a)=0$,
- $g'(x)\neq 0$ for all $x\in(a,b)$,
- the limit $L=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}$ exists in $\mathbb{R}\cup\{\pm\infty\}$.

Then the limit $\lim_{x\to a^+}\frac{f(x)}{g(x)}$ exists and equals $L$:
$
\lim_{x\to a^+}\frac{f(x)}{g(x)}=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}=L.
$

This rule is a standard tool for evaluating difficult limits, but it must be used with all hypotheses in place (especially the differentiability and nonvanishing of $g'$ near the limit point).
