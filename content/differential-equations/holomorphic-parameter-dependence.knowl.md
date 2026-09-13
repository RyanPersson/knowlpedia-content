+++
id = "differential-equations/holomorphic-parameter-dependence"
title = "Holomorphic dependence of local ODE solutions"
kind = "theorem"
summary = "A holomorphic vector field gives a local solution holomorphic in time, initial data and parameters."
aliases = ["analytic dependence for ODEs", "analytic ODE solution"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/picard-iteration", "complex-analysis/locally-uniform-limit-theorem", "differential-geometry/holomorphic-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(F(z,y,\lambda)\) is jointly [[differential-geometry/holomorphic-map|holomorphic]] near \((z_0,y_0,\lambda_0)\), the equation
\[
\partial_z y=F(z,y,\lambda),\qquad y(z_0)=y_0
\]
has a unique local solution jointly holomorphic in \(z\), initial state and \(\lambda\), on sufficiently small common neighborhoods.

## Picard argument

Choose a complex product neighborhood with uniform bounds on \(F\) and its state derivative. On a small time disc the Picard map preserves a ball and contracts it uniformly for all parameters in the chosen neighborhood. Its iterates are holomorphic and converge uniformly on smaller compact sets, so their limit is holomorphic. A version with real time, continuous time dependence and holomorphic state/parameter dependence follows by the same integral iteration. Extending a common parameter neighborhood along a longer trajectory requires uniform domain and coefficient control.

## References

- [Gerald Teschl, Ordinary Differential Equations and Dynamical Systems, Theorem 4.2](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
