+++
id = "complex-analysis/holomorphic-parameter-integral"
title = "Holomorphic dependence of a parameter integral"
kind = "theorem"
summary = "Local integrable domination allows integration of a holomorphic family and passage of complex derivatives through the integral."
aliases = ["holomorphic parameter integral", "analytic parameter integration"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-map", "measure-theory/integrable-majorant", "measure-theory/fubinis-theorem", "complex-analysis/cauchy-integral-formula"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F(z,x)\) be measurable in \(x\), holomorphic in \(z\in\Omega\) outside a fixed null set, and suppose each compact \(K\subset\Omega\) has an [[measure-theory/integrable-majorant|integrable majorant]] \(g_K\) with \(|F(z,x)|\le g_K(x)\) for all \(z\in K\). Then
\[
H(z)=\int F(z,x)\,d\mu(x)
\]
is holomorphic and \(H^{(m)}(z)=\int\partial_z^mF(z,x)\,d\mu(x)\).

## Local justification

Use the Cauchy integral formula on a circle surrounding a smaller disc. Domination permits exchanging the contour and measure integrals. The Cauchy kernel then represents \(H\) as a holomorphic function and supplies integrable bounds for every fixed derivative on the smaller disc. The original majorant must hold throughout a complex compact neighborhood; a bound only at real parameters is insufficient for this argument.
