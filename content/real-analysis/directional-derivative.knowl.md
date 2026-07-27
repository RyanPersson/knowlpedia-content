+++
id = "real-analysis/directional-derivative"
title = "Directional derivative"
kind = "knowl"
summary = "The derivative of a function along a line through a point in a specified direction."
aliases = ["directional-derivative", "Directional derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/directional-derivative.md"
+++

A **directional derivative** of a function $f:U\to\mathbb R$, where $U\subseteq\mathbb R^n$ is open, at $a\in U$ in the direction $v\in\mathbb R^n$ is the limit
$$
D_vf(a)=\lim_{t\to 0}\frac{f(a+tv)-f(a)}{t},
$$
when it exists.

If $f$ is [[real-analysis/differentiable-map|differentiable]] at $a$, then $D_vf(a)$ exists for every $v$ and equals $Df(a)v$, where $Df(a)$ is the [[real-analysis/frechet-derivative|Fréchet derivative]].

## Examples

- If $f(x,y)=x^2+y^2$, then at $a=(1,0)$ in the direction $v=(1,1)$,
  $$
  D_v f(a)=\lim_{t\to 0}\frac{(1+t)^2+t^2-1}{t}=2.
  $$
- For $f(x,y)=|x|$, one has $D_{(0,1)}f(0,0)=0$, but $D_{(1,0)}f(0,0)$ does not exist. Its one-sided directional derivative with $t\to0^+$ equals $1$.
