---
title: "Cauchy criterion for convergence in R^k"
description: "A sequence in Euclidean space converges iff it is Cauchy"
---

**Cauchy criterion for convergence in $\mathbb{R}^k$**: A sequence $(x_n)$ in $\mathbb{R}^k$ {{< knowl id="convergent-sequence" text="converges" >}} (with respect to the {{< knowl id="euclidean-norm" text="Euclidean norm" >}}) if and only if it is a {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}}; i.e.,
$x_n\to x \text{ for some } x\in\mathbb{R}^k
\quad\Longleftrightarrow\quad
\forall \varepsilon>0\;\exists N\;\forall m,n\ge N:\ \|x_n-x_m\|<\varepsilon.$

This is the {{< knowl id="complete-metric-space" text="completeness" >}} of Euclidean space and is central to analysis: it allows one to prove convergence by controlling pairwise distances rather than guessing the limit.
