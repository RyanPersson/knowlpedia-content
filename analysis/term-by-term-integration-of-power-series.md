---
title: "Term-by-term integration of power series"
description: "Inside the radius of convergence, a power series can be integrated term-by-term"
---

**Term-by-term integration of power series**: Let
$
f(x)=\sum_{n=0}^\infty a_n (x-x_0)^n
$
have radius of convergence $R>0$. Define
$
F(x)=\sum_{n=0}^\infty \frac{a_n}{n+1}(x-x_0)^{n+1}.
$
Then $F$ has the same radius of convergence $R$, and for all $|x-x_0|<R$,
$
F'(x)=f(x).
$
Equivalently, for $x$ with $|x-x_0|<R$,
$
\int_{x_0}^{x} f(t)\,dt = \sum_{n=0}^\infty \frac{a_n}{n+1}(x-x_0)^{n+1}.
$

This result provides an explicit antiderivative of a power {{< knowl id="series" text="series" >}} inside its disk/interval of convergence and is used to compute integrals and derive expansions.
