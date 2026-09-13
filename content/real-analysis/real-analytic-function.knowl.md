+++
id = "real-analysis/real-analytic-function"
title = "Real-analytic function"
kind = "definition"
summary = "A function locally represented by a convergent real power series."
aliases = ["real analytic map", "real analyticity"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/power-series", "real-analysis/multi-index-notation", "topology/open-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A function on an open subset of \(\mathbb R^n\) is **real analytic** if near every point \(a\) it is represented by a convergent [[real-analysis/power-series|power series]]
\[
f(x)=\sum_{\alpha\in\mathbb N^n}c_\alpha(x-a)^\alpha.
\]
The series converges absolutely in a neighborhood of \(a\); its coefficients are \(c_\alpha=\partial^\alpha f(a)/\alpha!\). For a vector-valued map the definition applies to each component.

## Smoothness and complex extension

Real analyticity implies smoothness. Locally the same convergent series gives a holomorphic function of complex variables. A smooth function need not be analytic: the function \(e^{-1/x^2}\) for \(x\ne0\), extended by zero at zero, has every derivative zero there but is positive nearby. Therefore specifying all Taylor coefficients need not determine a smooth function.
