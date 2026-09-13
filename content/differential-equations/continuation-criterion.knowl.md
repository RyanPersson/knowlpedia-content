+++
id = "differential-equations/continuation-criterion"
title = "Continuation criterion for a finite-dimensional ODE"
kind = "theorem"
summary = "A solution can be extended past a finite endpoint if its time-state graph stays in a compact subset of the equation domain."
aliases = ["ODE extension criterion", "maximal ODE interval"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/picard-lindelof-theorem", "topology/compact-set", "real-analysis/fundamental-theorem-of-calculus-i"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F\) satisfy the [[differential-equations/picard-lindelof-theorem|local existence and uniqueness hypotheses]] on an open set \(U\subset\mathbb R\times\mathbb R^m\). Suppose a solution on \([t_0,T)\), with \(T<\infty\), has its graph in a compact subset \(K\subset U\). Then it extends beyond \(T\).

## Reason

Continuity bounds \(F\) on \(K\), so the solution is Lipschitz in time and has a limit \(y_T\) at \(T\). Compactness puts \((T,y_T)\) inside \(K\subset U\). Apply local existence there and join by uniqueness. Thus failure of continuation at a finite maximal time forces escape from every such compact subset. A bounded state does not suffice if the equation domain has a finite boundary that the trajectory approaches.

## Maximal interval

The maximal existence interval through fixed initial data is the union of the intervals on which its solution can be continued. Uniqueness makes the continuations agree on overlaps. The criterion above describes an obstruction at a finite endpoint of that interval.
