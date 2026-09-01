+++
id = "topology/convergence-in-product-metric-spaces"
title = "Convergence in product metric spaces"
kind = "knowl"
summary = "A sequence in X×Y converges iff each coordinate sequence converges"
aliases = ["convergence-in-product-metric-spaces", "Convergence in product metric spaces"]
domains = ["topology"]
prerequisites = ["topology/metric-space", "shared-foundations/cartesian-product", "topology/cauchy-sequence"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/convergence-in-product-metric-spaces.md"
+++

Let \((X,d_X)\) and \((Y,d_Y)\) be [[topology/metric-space|metric spaces]]. On the [[shared-foundations/cartesian-product|product]] \(X\times Y\), define the metric
\[
d_\infty\bigl((x,y),(x',y')\bigr)=\max\{d_X(x,x'),\,d_Y(y,y')\}.
\]
**Proposition (coordinatewise convergence)**: A sequence \(((x_n,y_n))\) in \(X\times Y\) converges to \((x,y)\) (with respect to \(d_\infty\)) if and only if
\[
x_n\to x \text{ in } X \quad\text{and}\quad y_n\to y \text{ in } Y.
\]
Likewise, \(((x_n,y_n))\) is [[topology/cauchy-sequence|Cauchy]] in \(X\times Y\) iff \((x_n)\) is Cauchy in \(X\) and \((y_n)\) is Cauchy in \(Y\).

## Remarks

Any equivalent product metric yields the same notion of [[topology/convergent-sequence|convergence]]; one example is \(d_1=d_X+d_Y\).
This proposition justifies treating product convergence as "simultaneous convergence of components."
