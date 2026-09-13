+++
id = "fluid-dynamics/momentum-flux"
title = "Momentum flux tensor in an incompressible fluid"
kind = "definition"
summary = "The tensor whose i,j entry is the flux of the ith momentum component in the jth spatial direction."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "linear-algebra/outer-product", "fluid-dynamics/pressure-field", "fluid-dynamics/rate-of-strain", "fluid-dynamics/viscosity"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

With density normalized to one, the advective **momentum flux tensor** is \(u\otimes u\), whose entry \(u_i u_j\) transports momentum component \(i\) in direction \(j\). Including pressure and constant Newtonian viscosity gives the total flux
\[
J=u\otimes u+pI-2\nu D(u).
\]
The sign of the viscous term corresponds to writing the balance law as \(\partial_tu+\nabla\cdot J=f\).

## Flux across a surface

For a unit normal \(n\), the vector \(Jn\) gives the total momentum flux across the oriented surface. In components it is \((Jn)_i=\sum_jJ_{ij}n_j\), so the tensor convention agrees with [[real-analysis/divergence-of-tensor|row divergence]].

## Advective versus total flux

“Momentum flux” sometimes denotes just \(u\otimes u\). Pressure and viscous contributions must be included when converting the full momentum equation into conservative form.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
