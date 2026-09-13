+++
id = "partial-differential-equations/initial-datum"
title = "Initial datum for an evolution equation"
kind = "definition"
summary = "The prescribed state at the starting time, with a specified meaning of convergence to that state."
aliases = ["initial data", "initial velocity"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/limit-of-a-function-at-a-point", "linear-algebra/norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **initial datum** for an evolution equation is a prescribed state \(u_0\) at a starting time \(t_0\), expressed as \(u(t_0,\cdot)=u_0\). If the solution is initially defined only for \(t>t_0\), this condition is interpreted through a specified limit, for example
\[
\lim_{t\downarrow t_0}\|u(t,\cdot)-u_0\|_X=0
\]
in a chosen [[convex-analysis/norm-normed-vector-space|normed space]] \(X\). A pointwise initial condition is another possible convention.

## Constraints and sources

The datum must satisfy any required compatibility conditions, such as divergence freedom for an incompressible initial velocity. Initial data and forcing have different roles: data specify the starting state, whereas forcing is a prescribed source acting during the evolution. Zero initial data do not imply a zero solution when forcing is present.
