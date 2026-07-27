+++
id = "measure-theory/set-of-measure-zero-in-rk"
title = "Set of measure zero in ℝ^k"
kind = "knowl"
summary = "A set that can be covered by countably many rectangles (or balls) with arbitrarily small total volume."
aliases = ["set-of-measure-zero-in-rk", "Set of measure zero in ℝ^k"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/set-of-measure-zero-in-rk.md"
+++

A set $N\subseteq\mathbb R^k$ has **Lebesgue measure zero**, or is a **null set**, if for every $\varepsilon>0$ there is a countable collection of $k$-dimensional boxes $\{R_n\}_{n=1}^\infty$ such that
$$
N \subseteq \bigcup_{n=1}^\infty R_n
\quad\text{and}\quad
\sum_{n=1}^\infty \operatorname{vol}(R_n) < \varepsilon.
$$

For $R=\prod_{j=1}^k[a_j,b_j]$, its volume is
$$
\operatorname{vol}(R)=\prod_{j=1}^k(b_j-a_j).
$$
(One may equivalently use open balls in place of rectangles; the definition is unchanged up to standard comparison arguments.)

Measure zero is a notion of smallness relevant to integration and differentiability. The Lebesgue criterion states that a bounded function on a compact rectangle is Riemann integrable if and only if its set of discontinuities has measure zero.

## Examples

- Any finite or countable subset of $\mathbb R^k$ has measure zero.
- Any $k$-dimensional affine hyperplane in $\mathbb R^{k+1}$ has measure zero in $\mathbb R^{k+1}$.
- The Cantor set has measure zero in $\mathbb R$.
