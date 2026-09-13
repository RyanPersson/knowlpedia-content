+++
id = "partial-differential-equations/classical-solution"
title = "Classical solution of a PDE"
kind = "definition"
summary = "A function with the required classical derivatives that satisfies a PDE pointwise."
aliases = ["classical PDE solution", "smooth solution"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/partial-differential-equation", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **classical solution** of a [[partial-differential-equations/partial-differential-equation|PDE]] is a function whose derivatives appearing in the equation exist with the stipulated classical regularity and satisfy the equation pointwise. A **smooth solution** has continuous derivatives of every order in its open space-time domain.

## Example of the required regularity

For a second-order parabolic equation, one common classical class has continuous first time derivatives and continuous spatial derivatives through order two. Such a solution need not be smooth merely by definition; further regularity may follow from the equation and its coefficients.

## Initial and boundary values

Regularity on an open time interval does not by itself specify behavior at its endpoints. An initial condition may require continuity to \(t=0\) pointwise or in a chosen function-space norm. Boundary conditions and the regularity used to interpret them are additional parts of the problem.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
