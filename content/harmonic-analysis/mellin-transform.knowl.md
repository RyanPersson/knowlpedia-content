+++
id = "harmonic-analysis/mellin-transform"
title = "Mellin transform"
kind = "definition"
summary = "The multiplicative integral transform with kernel x to a complex power."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/laplace-transform"]
+++

For a measurable \(f:(0,\infty)\to\mathbb C\), its **Mellin transform** is
\[
 \mathcal M f(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x}
\]
at those \(s\in\mathbb C\) where the integral converges absolutely.

## Logarithmic coordinates

Setting \(x=e^t\) gives \(\int_{\mathbb R}f(e^t)e^{st}\,dt\), a bilateral [[harmonic-analysis/laplace-transform|Laplace transform]] in the additive coordinate \(t\).

## References

- [Lib/Analytic/DirichletTheta.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean)
