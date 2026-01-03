---
title: "Term-by-term differentiation of power series"
description: "Inside the radius of convergence, a power series can be differentiated term-by-term"
---

**Term-by-term differentiation of power series**: Let
$
f(x)=\sum_{n=0}^\infty a_n (x-x_0)^n
$
have radius of convergence $R>0$. Define the derived {{< knowl id="series" text="series" >}}
$
\sum_{n=1}^\infty n a_n (x-x_0)^{n-1}.
$
Then:
- the derived series has the same radius of convergence $R$, and
- for every $|x-x_0|<R$, the function $f$ is {{< knowl id="differentiability-one-variable" text="differentiable" >}} and
  $
  f'(x)=\sum_{n=1}^\infty n a_n (x-x_0)^{n-1}.
  $

This theorem explains why power series define real-analytic (or complex-analytic) functions on their domain of convergence.
