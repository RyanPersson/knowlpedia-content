+++
id = "fluid-dynamics/angular-average"
title = "Angular average in cylindrical components"
kind = "definition"
summary = "The normalized average in the angular variable, with a stated convention for vector components."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/cylindrical-coordinates", "measure-theory/lebesgue-integral", "real-analysis/periodic-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an integrable \(2\pi\)-periodic scalar function \(F(r,\theta,z)\), its **angular average** is
\[
\langle F\rangle_\theta(r,z)=\frac1{2\pi}\int_0^{2\pi}F(r,\theta,z)\,d\theta.
\]
For vector or tensor fields expressed in the moving [[real-analysis/cylindrical-coordinates|cylindrical frame]], a componentwise angular average integrates the cylindrical coefficients separately. This convention must be named because the basis vectors depend on \(\theta\).

## Why the frame matters

The vector field \(e_r(\theta)\) has cylindrical coefficients \((1,0,0)\). Their componentwise average is \((1,0,0)\), while its average as a Cartesian vector is zero. Similarly, taking an auxiliary mean before evaluating auxiliary variables as functions of \((r,\theta,z,t)\) need not equal the angular average of the evaluated field.
