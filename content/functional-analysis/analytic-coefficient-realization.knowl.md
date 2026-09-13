+++
id = "functional-analysis/analytic-coefficient-realization"
title = "Holomorphic realization of weighted analytic coefficients"
kind = "proposition"
summary = "The factorial-binomial coefficient bound gives a convergent radial series and a common complex parameter radius."
aliases = ["realization of analytic coefficient series"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/two-index-analytic-coefficient-space", "real-analysis/taylors-theorem-with-remainder", "real-analysis/power-series", "complex-analysis/locally-uniform-limit-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F\) have finite [[functional-analysis/two-index-analytic-coefficient-space|two-index norm]]. For each \(0<r<R\), its radial series and parameter Taylor series give a jointly holomorphic extension near \(|Y|\le r\) and \(\eta\in I\), with any sufficiently small parameter radius strictly below
\[
\rho(1-r/R).
\]
At interval endpoints use the same Taylor series to extend from the one-sided data.

## Estimate

Dropping the polynomial denominators from the weights and writing \(q=r/R<1\) gives
\[
\sum_{\alpha\ge0}\sup_I|\partial_\eta^\beta F_\alpha|r^\alpha
\le\|F\|_{R,\rho}\rho^{-\beta}\beta!
\sum_{\alpha\ge0}\binom{\alpha+\beta}{\beta}q^\alpha
=\frac{\|F\|_{R,\rho}\rho^{-\beta}\beta!}{(1-q)^{\beta+1}}.
\]
The generating identity follows by differentiating the geometric series \(\beta\) times. Taylor's remainder tends to zero at smaller parameter distances. Absolute convergence gives a holomorphic power series, and overlapping local extensions agree by analytic uniqueness. A strict loss of radius leaves room for derivative estimates of every fixed order.
