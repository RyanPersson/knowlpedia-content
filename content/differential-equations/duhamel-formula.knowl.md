+++
id = "differential-equations/duhamel-formula"
title = "Duhamel formula for a linear ODE"
kind = "definition"
summary = "The initial state is propagated and every source contribution is propagated from its insertion time."
aliases = ["variation of constants", "variation of parameters"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/fundamental-matrix", "differential-equations/linear-ode", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For continuous \(A,f\), the solution of \(y'=A(t)y+f(t)\), \(y(s)=y_s\), is
\[
y(t)=\Phi(t,s)y_s+\int_s^t\Phi(t,\tau)f(\tau)\,d\tau,
\]
where \(\Phi\) is the [[differential-equations/fundamental-matrix|principal propagator]] of the homogeneous system. This is **Duhamel's formula**, also called variation of constants.

## Verification

Differentiate the integral: its moving endpoint contributes \(f(t)\), and differentiating the propagator contributes \(A(t)\) times the integral. The initial condition follows at \(t=s\). Equivalently, differentiating \(X(t)^{-1}y(t)\) gives \(X(t)^{-1}f(t)\). Bounds on \(\Phi\) therefore turn source bounds into solution bounds.
