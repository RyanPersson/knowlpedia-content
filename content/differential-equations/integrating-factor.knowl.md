+++
id = "differential-equations/integrating-factor"
title = "Integrating factor for a scalar linear ODE"
kind = "definition"
summary = "Multiplication by exp of an integral turns y prime plus a(t)y into one derivative."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/linear-ode", "real-analysis/exponential-function", "real-analysis/product-rule", "real-analysis/fundamental-theorem-of-calculus-i", "real-analysis/fundamental-theorem-of-calculus-ii"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For continuous \(a,f\), the [[differential-equations/linear-ode|equation]] \(y'+a(t)y=f(t)\) has **integrating factor**
\[
\mu(t)=\exp\left(\int_{t_0}^ta(s)\,ds\right).
\]
The product rule gives \((\mu y)'=\mu f\), so
\[
y(t)=\mu(t)^{-1}\left(y(t_0)+\int_{t_0}^t\mu(s)f(s)\,ds\right).
\]

## Regularity and matrices

For integrable \(a,f\), the same formula gives an absolutely continuous solution and the equation holds almost everywhere. For matrix coefficients at different times, multiplication need not commute; replacing a scalar integral exponential by a matrix exponential requires a commutation condition. The general matrix construction uses a [[differential-equations/fundamental-matrix|propagator]].
