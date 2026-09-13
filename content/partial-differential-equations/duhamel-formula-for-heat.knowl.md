+++
id = "partial-differential-equations/duhamel-formula-for-heat"
title = "Duhamel formula for the heat equation"
kind = "theorem"
summary = "The forced heat equation is represented by evolving the initial data and integrating evolved source increments."
aliases = ["forced heat representation"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/heat-semigroup", "partial-differential-equations/heat-kernel-solution", "measure-theory/lebesgue-integral", "real-analysis/fundamental-theorem-of-calculus-i"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For smooth rapidly decaying initial data \(u_0\) and a smooth source \(f(t,x)\) with a common compact spatial support on a finite time interval, a solution of
\[
\partial_tu-\nu\Delta u=f,\qquad u(0)=u_0,
\]
is given by the **heat Duhamel formula**
\[
u(t)=T_tu_0+\int_0^t T_{t-s}f(s)\,ds,
\]
where \(T_t\) is the [[partial-differential-equations/heat-semigroup|heat semigroup]].

## Verification and scope

Differentiating the integral gives the endpoint value \(f(t)\); its remaining terms give \(\nu\Delta\int_0^t T_{t-s}f(s)\,ds\). For these smooth data, spatial derivatives may instead fall on \(f\), justifying differentiation near \(s=t\). The integral vanishes at time zero. Rougher sources require the corresponding convergence and regularity estimates before the formula is interpreted as a classical solution.
