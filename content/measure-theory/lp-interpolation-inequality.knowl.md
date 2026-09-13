+++
id = "measure-theory/lp-interpolation-inequality"
title = "Interpolation between two Lebesgue norms"
kind = "theorem"
summary = "The Lp norm at an intermediate reciprocal exponent is bounded by a geometric mean of endpoint norms."
aliases = ["Lp interpolation inequality", "log-convexity of Lp norms"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "convex-analysis/holder-inequality-integrals", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(1\le p_0,p_1\le\infty\), \(0\le\theta\le1\), and
\[
\frac1p=\frac{1-\theta}{p_0}+\frac{\theta}{p_1}.
\]
For \(f\in L^{p_0}\cap L^{p_1}\), the **Lebesgue interpolation inequality** is
\[
\|f\|_p\le\|f\|_{p_0}^{1-\theta}\|f\|_{p_1}^{\theta}.
\]

## Direct proof

For finite distinct endpoints and \(0<\theta<1\), apply [[convex-analysis/holder-inequality-integrals|Hölder's inequality]] to \(|f|^{p(1-\theta)}|f|^{p\theta}\), with conjugate exponents \(p_0/[p(1-\theta)]\) and \(p_1/(p\theta)\). If an endpoint is infinity, bound its factor by the essential supremum. Coincident endpoints and \(\theta=0,1\) give equality. This is an estimate for one function, distinct from an operator interpolation theorem.
