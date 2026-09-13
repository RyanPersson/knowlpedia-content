+++
id = "fluid-dynamics/relative-kinetic-energy"
title = "Relative kinetic energy"
kind = "definition"
summary = "Half the squared L2 distance between two velocity fields."
aliases = ["difference energy"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/kinetic-energy", "measure-theory/lp-space", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For two velocities \(u,v\) with \(v-u\in L^2(\Omega)\), their **relative kinetic energy** at unit density is
\[
\mathcal E(v\mid u)=\frac12\int_\Omega|v-u|^2\,dx.
\]
It is the [[fluid-dynamics/kinetic-energy|kinetic energy]] of the difference field.

## Comparison interpretation

It is nonnegative and vanishes exactly when \(u=v\) almost everywhere. It is not the difference of their individual energies: \(\tfrac12\|v\|_2^2-\tfrac12\|u\|_2^2\) also includes a cross term. A relative-energy estimate can turn a bound on one reference flow into stability or uniqueness of a competitor.
