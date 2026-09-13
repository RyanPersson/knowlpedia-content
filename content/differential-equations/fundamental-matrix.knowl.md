+++
id = "differential-equations/fundamental-matrix"
title = "Fundamental matrix and principal propagator"
kind = "definition"
summary = "An invertible matrix of homogeneous solutions that transports data between two times."
aliases = ["ODE propagator", "principal fundamental matrix", "evolution matrix"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/linear-ode", "differential-equations/picard-lindelof-theorem", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For continuous \(A(t)\), a **fundamental matrix** \(X(t)\) is an invertible matrix whose columns solve the [[differential-equations/linear-ode|linear system]] \(y'=A(t)y\). Its associated principal propagator is
\[
\Phi(t,s)=X(t)X(s)^{-1},\qquad
\partial_t\Phi(t,s)=A(t)\Phi(t,s),\quad\Phi(s,s)=I.
\]
It maps the state at time \(s\) to the state at time \(t\), independently of the chosen fundamental matrix.

## Composition and inverse

Uniqueness of the initial-value problem gives
\[
\Phi(t,s)\Phi(s,r)=\Phi(t,r),\qquad
\Phi(t,s)^{-1}=\Phi(s,t).
\]
Differentiating the inverse yields \(\partial_s\Phi(t,s)=-\Phi(t,s)A(s)\). On a compact time interval, the [[differential-equations/gronwall-inequality|Gronwall bound]] is \(\|\Phi(t,s)\|\le\exp(\int_{\min(s,t)}^{\max(s,t)}\|A(\tau)\|\,d\tau)\).
