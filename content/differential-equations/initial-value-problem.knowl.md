+++
id = "differential-equations/initial-value-problem"
title = "Initial-value problem for an ODE"
kind = "definition"
summary = "A differential equation together with the prescribed value of its state at one time."
aliases = ["ODE initial data", "Cauchy problem for an ODE"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/ordinary-differential-equation", "real-analysis/fundamental-theorem-of-calculus-i", "real-analysis/fundamental-theorem-of-calculus-ii"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

An **initial-value problem** prescribes
\[
y'=F(t,y),\qquad y(t_0)=y_0.
\]
For continuous \(F\), a classical solution is equivalently a continuous function satisfying the integral equation
\[
y(t)=y_0+\int_{t_0}^tF(s,y(s))\,ds.
\]
The equivalence follows from the [[real-analysis/fundamental-theorem-of-calculus-i|fundamental theorem of calculus]]. Existence and uniqueness require additional hypotheses on \(F\).

## Integration constants

For \(y'=g(t)\), antiderivatives differ by an integration constant; the initial value fixes it. In a parameterized problem, the initial value and hence this constant may depend on the parameter. Prescribing data at two endpoints is a boundary-value problem and has different solvability conditions.
