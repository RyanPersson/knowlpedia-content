+++
id = "real-analysis/power-series"
title = "Power series"
kind = "knowl"
summary = "A series in powers of (x minus a center), defining a function on an interval of convergence."
aliases = ["power-series", "Power series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/power-series.md"
+++

A **power series** with real coefficients and center \(a\in\mathbb R\) is a series
\[
\sum_{n=0}^\infty c_n(x-a)^n.
\]

There is a radius \(R\in[0,\infty]\) such that the series converges absolutely for \(|x-a|<R\) and diverges for \(|x-a|>R\). When \(R<\infty\), convergence at the endpoints must be checked separately.

## Examples

- The geometric series \(\sum_{n=0}^\infty x^n\) has radius \(1\) and equals \(1/(1-x)\) for \(|x|<1\).
- The exponential series \(\sum_{n=0}^\infty x^n/n!\) has infinite radius of convergence.
