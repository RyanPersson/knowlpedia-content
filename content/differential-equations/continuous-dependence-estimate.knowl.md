+++
id = "differential-equations/continuous-dependence-estimate"
title = "Continuous-dependence estimate for ODEs"
kind = "proposition"
summary = "A Lipschitz coefficient bounds the effect of initial-data and forcing errors by Gronwall amplification."
aliases = ["ODE stability estimate"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/gronwall-inequality", "differential-equations/initial-value-problem", "topology/locally-lipschitz-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(y'=F(t,y)\) and \(z'=F(t,z)+e(t)\) remain in a region where \(|F(t,y)-F(t,z)|\le L(t)|y-z|\), with \(L\ge0\) integrable. Then for \(t\ge s\),
\[
|y(t)-z(t)|\le e^{\int_s^tL}|y(s)-z(s)|
+\int_s^t e^{\int_\tau^tL}|e(\tau)|\,d\tau.
\]

## Derivation and scope

Subtract the integral equations and apply the [[differential-equations/gronwall-inequality|source form of Gronwall]]. For perturbed vector fields, put their difference along the comparison trajectory into \(e\). The estimate measures stability on the specified common region; it does not itself keep solutions inside that region.
