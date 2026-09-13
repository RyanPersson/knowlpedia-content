+++
id = "differential-equations/linear-ode"
title = "Linear ordinary differential system"
kind = "definition"
summary = "A system y prime equals A(t)y plus a prescribed forcing term."
aliases = ["homogeneous linear ODE", "inhomogeneous linear ODE", "linear differential system"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-equations/ordinary-differential-equation", "linear-algebra/matrix", "linear-algebra/linear-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **linear [[differential-equations/ordinary-differential-equation|ODE]] system** has the form \(y'=A(t)y+f(t)\), where \(A\) and \(f\) are prescribed. The system is homogeneous when \(f=0\) and inhomogeneous when a nonzero source is present. Homogeneous here refers to the absence of a source, not to a scaling law.

## Superposition

Linear combinations of solutions of the homogeneous system remain solutions. The difference of two solutions with the same source solves the homogeneous equation; consequently every inhomogeneous solution is a particular solution plus a homogeneous one. A [[differential-equations/fundamental-matrix|fundamental matrix]] organizes this solution space.
