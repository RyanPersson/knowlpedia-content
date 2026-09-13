+++
id = "partial-differential-equations/convex-integration"
title = "Convex integration"
kind = "definition"
summary = "A method using increasingly fine oscillations to realize a nonlinear differential constraint from relaxed data."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/differential-inclusion", "convex-analysis/convex-hull", "partial-differential-equations/weak-formulation", "harmonic-analysis/oscillatory-modulation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

**Convex integration** is a family of construction methods for [[partial-differential-equations/differential-inclusion|differential inclusions]] and related equations. One starts with a relaxed constraint, often involving a suitable [[convex-analysis/convex-hull|convex hull]], and introduces finer [[harmonic-analysis/oscillatory-modulation|oscillations]] to approach the original nonlinear constraint. The proof must control errors, convergence, and passage to the limit in the chosen solution class; a formal oscillatory ansatz alone is not a solution.

For a [[partial-differential-equations/weak-formulation|weak formulation]], the limit must satisfy every required test identity.

## Fluid equations

Fluid constructions often reduce a stress defect through an iteration. The convergence topology must justify the quadratic momentum term as well as any claimed energy property. Convex integration can yield [[partial-differential-equations/nonuniqueness|nonuniqueness]], but the conclusion depends on the precise equation and class. Buckmaster and Vicol constructed nonunique finite energy weak solutions of three-dimensional periodic Navier–Stokes. Finite energy weak solutions in that result should not be identified with Leray–Hopf solutions satisfying the energy inequality.

## References

- [Buckmaster and Vicol, Nonuniqueness of weak solutions to the Navier–Stokes equation (2019)](https://annals.math.princeton.edu/wp-content/uploads/annals-v189-n1-p03-s.pdf).
