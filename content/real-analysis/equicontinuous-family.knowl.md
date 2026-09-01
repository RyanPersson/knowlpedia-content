+++
id = "real-analysis/equicontinuous-family"
title = "Equicontinuous family"
kind = "knowl"
summary = "A family of functions that satisfies the equicontinuity condition at every point."
aliases = ["equicontinuous-family", "Equicontinuous family"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/pointwise-bounded-family", "real-analysis/arzela-ascoli-theorem", "real-analysis/space-of-continuous-functions", "real-analysis/uniform-metric"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/equicontinuous-family.md"
+++

A family \(\mathcal F\) of functions from a metric space \((X,d_X)\) to a metric space \((Y,d_Y)\) is **equicontinuous on \(X\)** if, for every \(x_0\in X\) and \(\varepsilon>0\), there exists \(\delta>0\) such that, for every \(f\in\mathcal F\) and \(x\in X\),
\[
d_X(x,x_0)<\delta \implies d_Y\bigl(f(x),f(x_0)\bigr)<\varepsilon.
\]

Equicontinuity provides uniform control of continuity across the family and is a key hypothesis (together with [[real-analysis/pointwise-bounded-family|pointwise boundedness]]) in the [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli theorem]] for subsets of [[real-analysis/space-of-continuous-functions|spaces of continuous functions]] equipped with the [[real-analysis/uniform-metric|uniform metric]].

## Examples

- Any family of Lipschitz functions with a common Lipschitz constant is equicontinuous. For example, \(f_a(x)=\sin(x+a)\), \(a\in\mathbb R\), is equicontinuous on \(\mathbb R\).
- The family \(f_n(x)=x^n\) is not equicontinuous on \([0,1]\).
