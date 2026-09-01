+++
id = "real-analysis/uniform-cauchy"
title = "Uniform Cauchy sequence"
kind = "knowl"
summary = "A Cauchy condition for function sequences with a uniform bound over the domain."
aliases = ["uniform-cauchy", "Uniform Cauchy sequence"]
domains = ["real-analysis"]
prerequisites = ["topology/metric-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/uniform-cauchy.md"
+++

A sequence of functions \(f_n:X\to Y\) into a [[topology/metric-space|metric space]] \((Y,d)\) is **uniform Cauchy** on \(X\) if, for every \(\varepsilon>0\), there exists \(N\) such that for all \(m,n\ge N\) and \(x\in X\),
\[
d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon.
\]
Equivalently,
\[
\sup_{x\in X} d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon \quad \text{for all } m,n\ge N.
\]

## Remarks

If \(Y\) is complete, a sequence is uniform Cauchy if and only if it [[real-analysis/uniform-convergence|converges uniformly]] to a function \(X\to Y\). Without completeness, a uniform Cauchy sequence need not have a \(Y\)-valued limit.

## Examples

- On \([0,1]\), \(f_n(x)=x/n\) is uniform Cauchy because
  \[
  \sup_{x\in[0,1]}|f_m(x)-f_n(x)|\le|1/m-1/n|.
  \]
- On \([0,1]\), the sequence \(f_n(x)=x^n\) is not uniform Cauchy.
