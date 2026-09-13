+++
id = "topology/locally-lipschitz-map"
title = "Locally Lipschitz map"
kind = "definition"
summary = "A map satisfying a Lipschitz bound on some neighborhood of each point."
aliases = ["local Lipschitz continuity", "locally Lipschitz in the state"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/lipschitz-continuity", "topology/neighborhood"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A map between metric spaces is **locally Lipschitz** if each domain point has a neighborhood on which the map is [[topology/lipschitz-continuity|Lipschitz]]. The neighborhood and its constant may depend on the point.

## State variables and parameters

For \(F(t,y)\), local Lipschitz continuity **in \(y\), locally uniformly in \(t\)** means that near each \((t_0,y_0)\), a single finite \(L\) satisfies \(|F(t,y)-F(t,z)|\le L|y-z|\) for all allowed \(t,y,z\). This is the condition used in the local ODE theorem. A continuous state derivative \(D_yF\) supplies it by the mean value estimate on a small convex ball. Separate pointwise constants without local uniform control do not state the same hypothesis.
