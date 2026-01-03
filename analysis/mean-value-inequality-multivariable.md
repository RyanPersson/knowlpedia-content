---
title: "Mean value inequality (multivariable)"
description: "Bounds the change of a differentiable map by the supremum of its derivative norm"
---

**Mean value inequality (multivariable)**: Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}^m$ be {{< knowl id="differentiable-map" text="differentiable" >}}. Suppose $x,y\in U$ and the line segment
$
[x,y]=\{x+t(y-x):0\le t\le 1\}
$
is contained in $U$. If there is a constant $M$ such that
$
\|Df(z)\| \le M \quad \text{for all } z\in[x,y]
$
(where $\|Df(z)\|$ is the {{< knowl id="operator-norm" text="operator norm" >}}), then
$
\|f(y)-f(x)\|\le M\|y-x\|.
$

This inequality is the multivariable analogue of the one-dimensional {{< knowl id="mean-value-theorem" text="mean value estimate" >}} and is used to prove {{< knowl id="lipschitz-continuity" text="Lipschitz bounds" >}}, uniqueness results, and the {{< knowl id="inverse-function-theorem-rk" text="inverse" >}}/{{< knowl id="implicit-function-theorem" text="implicit function theorems" >}}.
