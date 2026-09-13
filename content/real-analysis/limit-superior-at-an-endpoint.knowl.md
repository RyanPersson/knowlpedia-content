+++
id = "real-analysis/limit-superior-at-an-endpoint"
title = "Limit superior of a function at an endpoint"
kind = "definition"
summary = "The infimum of the suprema over shrinking one-sided neighborhoods of the endpoint."
aliases = ["one-sided function limsup"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/supremum", "real-analysis/infimum", "convex-analysis/extended-real-number-system-and-conventions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(f:(a,T)\to[-\infty,\infty]\), with finite \(a<T\), the **limit superior at \(T\) from the left** is
\[
\limsup_{t\uparrow T}f(t)
=\inf_{0<\delta<T-a}\ \sup_{T-\delta<t<T} f(t).
\]
The suprema and infimum are interpreted in the [[convex-analysis/extended-real-number-system-and-conventions|extended real numbers]]. They may therefore equal either infinity.

## Unbounded endpoint behavior

The lim sup is \(+\infty\) exactly when \(f\) is unbounded above in every left neighborhood of \(T\). Equivalently, one can choose \(t_j\uparrow T\) with \(f(t_j)\to+\infty\). This does not require \(f(t)\to+\infty\) along every approach.

## Essential variant

For measurable functions, replacing each supremum by an [[measure-theory/essential-supremum|essential supremum]] gives the essential lim sup. The ordinary version can depend on values at isolated points; the essential version ignores changes on null sets.
