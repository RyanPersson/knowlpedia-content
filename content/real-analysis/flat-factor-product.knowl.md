+++
id = "real-analysis/flat-factor-product"
title = "Flat factors absorb polynomial derivative growth"
kind = "theorem"
summary = "A flat factor makes a product smoothly zero-extendible when every derivative of the other factor grows at most polynomially."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/flat-function", "real-analysis/multi-index-leibniz-rule", "real-analysis/taylors-theorem-with-remainder", "real-analysis/smooth-zero-extension"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(h\in C^\infty((-\varepsilon,\varepsilon))\) is [[real-analysis/flat-function|flat at zero]] and \(F\in C^\infty(U\times(0,\varepsilon))\). Assume that, for each compact \(K\subset U\) and each mixed derivative, some constants \(C,N\ge0\) satisfy
\[
\sup_{x\in K}|\partial_x^\alpha\partial_t^kF(x,t)|\le C t^{-N}
\]
for sufficiently small positive \(t\). Then \(h(t)F(x,t)\), extended by zero for \(t\le0\), is smooth and flat on \(t=0\).

## Proof

Taylor's theorem and flatness give \(|h^{(j)}(t)|\le C_{j,M}t^M\) for every fixed \(j,M\). In the [[real-analysis/multi-index-leibniz-rule|Leibniz formula]] for any derivative of \(hF\), choose \(M\) larger than the finitely many growth exponents that occur. Each term then tends to zero locally uniformly in \(x\). Apply the [[real-analysis/smooth-zero-extension|zero-extension criterion]].

## Scope of the hypothesis

The exponent may depend on the derivative order and on \(K\). No conclusion holds for unrestricted growth: a factor \(e^{1/t^2}\) cancels \(e^{-1/t^2}\) exactly and leaves a nonvanishing product.
