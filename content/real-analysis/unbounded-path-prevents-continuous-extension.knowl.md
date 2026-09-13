+++
id = "real-analysis/unbounded-path-prevents-continuous-extension"
title = "Unbounded values approaching a point prevent continuous extension"
kind = "theorem"
summary = "Growth along a converging space-time sequence contradicts continuity at its limit point."
aliases = ["local blowup obstruction to smooth continuation"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["topology/continuous-map", "topology/convergent-sequence", "linear-algebra/norm", "topology/compact-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(u\) be a function with values in a finite-dimensional normed space. If points \((x_j,t_j)\) in its domain satisfy
\[
(x_j,t_j)\to(x_*,T),\qquad |u(x_j,t_j)|\to\infty,
\]
then \(u\) has no [[topology/continuous-map|continuous]] extension to a neighborhood of \((x_*,T)\) agreeing with its original values.

## Proof and comparison use

Continuity of an extension would give \(u(x_j,t_j)\to u(x_*,T)\), a finite value. Equivalently, a continuous extension is bounded on a sufficiently small compact neighborhood. Thus a divergent sequence inside that neighborhood is impossible.

If a uniqueness theorem forces a proposed extension or competing solution to agree with \(u\) before \(T\), the same sequence rules out that competitor. The uniqueness statement and its hypotheses must be supplied separately. The spatial points must remain near a finite point; growth only along points escaping to infinity gives no such local contradiction.
