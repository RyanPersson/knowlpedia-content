+++
id = "differential-equations/linear-instability"
title = "Instability of a linear equilibrium"
kind = "definition"
summary = "Failure of uniform smallness of solutions from arbitrarily small initial data in a linear evolution."
aliases = []
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/linear-ode", "linear-algebra/euclidean-norm", "shared-foundations/first-order-logic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a constant-matrix [[differential-equations/linear-ode|linear system]] \(y'=Ay\), the zero equilibrium is **linearly unstable** in the dynamical sense if there is \(\eta>0\) such that, for every \(\delta>0\), some initial datum with \(\|y(0)\|<\delta\) has \(\|y(t)\|>\eta\) at a later time. This is failure of Lyapunov stability for this linear equation.

## A growing eigenmode

If \(Av=\lambda v\) with a real \(\lambda>0\) and \(v\ne0\), then \(y(t)=c e^{\lambda t}v\) proves instability. A complex eigenvalue with positive real part also gives exponentially growing modes. A nondiagonal Jordan block at an imaginary eigenvalue can cause polynomial growth, so positive exponential growth is a sufficient condition rather than the definition.

## Scope for nonlinear equations

Instability of a linearized equation does not by itself prove nonlinear blowup. One must show that a nonlinear solution follows the growing mode for the required interval and control the remainder. Large but bounded transient amplification alone is compatible with Lyapunov stability of a fixed finite-dimensional linear system.
