+++
id = "differential-equations/smooth-parameter-dependence"
title = "Smooth dependence of ODE solutions on parameters"
kind = "theorem"
summary = "Smooth coefficients and initial data yield solutions smooth in parameters on a common local domain."
aliases = ["ODE parameter derivatives", "smooth ODE dependence"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/picard-lindelof-theorem", "real-analysis/class-ck-map", "differential-equations/duhamel-formula"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(F(t,y,\lambda)\) is [[real-analysis/class-ck-map|\(C^k\)]], \(k\ge1\), near \((t_0,y_0,\lambda_0)\). The local solution of \(y'=F(t,y,\lambda)\) depends \(C^k\) on time, initial state, initial time and \(\lambda\), on a common sufficiently small neighborhood. Smooth parameterized initial data can be composed with this solution map.

## Variational equation

For one parameter and fixed initial time, \(z=\partial_\lambda y\) satisfies
\[
z'=D_yF(t,y,\lambda)z+\partial_\lambda F(t,y,\lambda),
\qquad z(t_0)=\partial_\lambda y_0.
\]
The [[differential-equations/duhamel-formula|Duhamel formula]] controls this derivative. Further differentiation gives linear equations in the highest parameter derivative, with sources involving lower derivatives. Uniform estimates over a longer interval require common bounds and a common domain; pointwise existence for each parameter does not supply them.

## References

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems, Theorem 2.11](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
