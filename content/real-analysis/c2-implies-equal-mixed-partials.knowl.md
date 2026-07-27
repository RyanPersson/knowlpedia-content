+++
id = "real-analysis/c2-implies-equal-mixed-partials"
title = "C^2 implies equal mixed partials"
kind = "knowl"
summary = "A twice continuously differentiable real function has equal mixed second partial derivatives."
aliases = ["c2-implies-equal-mixed-partials", "C^2 implies equal mixed partials"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/c2-implies-equal-mixed-partials.md"
+++

Let $U\subseteq\mathbb R^n$ be [[topology/open-set|open]] and $f:U\to\mathbb R$ be of [[real-analysis/class-ck-map|class $C^2$]]. Then for every $a\in U$ and all indices $i,j$,
$$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$$

## Remarks

Apply [[real-analysis/mixed-partial-derivative|Schwarz's theorem]] at each $a\in U$. The $C^2$ hypothesis guarantees that the mixed [[real-analysis/partial-derivative|partial derivatives]] exist and are [[real-analysis/continuity-on-a-set|continuous]] near $a$.
