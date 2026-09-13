+++
id = "real-analysis/one-sided-jet-limits-from-derivative-bounds"
title = "One-sided jet limits from uniform derivative bounds"
kind = "theorem"
summary = "Bounds on one more time derivative give compatible endpoint limits for every spatial and temporal derivative."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cartesian-jet", "real-analysis/fundamental-theorem-of-calculus-i", "real-analysis/uniform-convergence-differentiation", "real-analysis/class-ck-function", "topology/compact-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(f\in C^\infty(U\times(0,T))\), \(T<\infty\). Suppose every mixed derivative is uniformly bounded on \(K\times(T-\delta_K,T)\) for each compact \(K\subset U\), with some \(\delta_K>0\). Then each \(\partial_x^\alpha\partial_t^j f\) has a locally uniform limit as \(t\uparrow T\). These limits form a compatible smooth [[real-analysis/cartesian-jet|endpoint jet]]: if \(F_j(x)=\lim_{t\uparrow T}\partial_t^jf(x,t)\), then
\[
F_j\in C^\infty(U),\qquad
\partial_x^\alpha F_j=\lim_{t\uparrow T}\partial_x^\alpha\partial_t^jf.
\]

## Time Cauchy estimate and compatibility

A bound for \(\partial_t(\partial_x^\alpha\partial_t^jf)\) gives a uniform Lipschitz estimate in time, hence the endpoint limit. On small rectangular boxes inside \(U\), the fundamental theorem of calculus along spatial coordinate segments identifies the spatial derivatives of each limit. Passing to the endpoint in the time identity gives
\[
\partial_x^\alpha\partial_t^jf(x,t)
=\partial_x^\alpha F_j(x)-\int_t^T\partial_x^\alpha\partial_t^{j+1}f(x,s)\,ds.
\]
This records compatibility of consecutive normal derivatives. A bound for \(f\) alone is insufficient, as a bounded oscillatory function near \(T\) need not have a limit.
