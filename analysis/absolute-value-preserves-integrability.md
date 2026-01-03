---
title: "Absolute value preserves Riemann integrability"
description: "If f is Riemann integrable then |f| is Riemann integrable, and |∫f| ≤ ∫|f|"
---

Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}}.

**Proposition**: The function $|f|$ is Riemann integrable on $[a,b]$. Moreover,
$
\left|\int_a^b f(x)\,dx\right|\le \int_a^b |f(x)|\,dx.
$

This is a basic stability property: composing with the {{< knowl id="continuity-on-a-set" text="continuous" >}} map $x\mapsto |x|$ preserves Riemann integrability.
