---
title: "Completeness of C(K) under the sup norm"
description: "On a compact metric space K, the space of continuous functions is complete in the sup metric"
---

Let $(K,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $C(K,\mathbb{R})$ denote the set of {{< knowl id="continuous-function" text="continuous functions" >}} $f:K\to\mathbb{R}$.

Define the **{{< knowl id="sup-norm" text="sup norm" >}}** by
$
\|f\|_\infty=\sup_{x\in K}|f(x)|,
$
and the induced metric
$
d_\infty(f,g)=\|f-g\|_\infty=\sup_{x\in K}|f(x)-g(x)|.
$

**Theorem**: The metric space $\bigl(C(K,\mathbb{R}),d_\infty\bigr)$ is {{< knowl id="complete-metric-space" text="complete" >}}.

This is the basic Banach-space fact behind many compactness and approximation arguments: {{< knowl id="uniform-convergence" text="uniform" >}} {{< knowl id="cauchy-sequence" text="Cauchy" >}} sequences of continuous functions converge uniformly to a continuous function.
