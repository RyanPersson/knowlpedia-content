+++
id = "partial-differential-equations/partial-differential-equation"
title = "Partial differential equation"
kind = "definition"
summary = "An equation relating an unknown function of several variables to its partial derivatives."
aliases = ["PDE", "PDE system"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/partial-derivative", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **partial differential equation** (PDE) is an equation for an unknown function \(u\) of several independent variables involving its [[real-analysis/partial-derivative|partial derivatives]]. A finite-order equation can be written schematically as
\[
F\bigl(x,(\partial^\alpha u(x))_{|\alpha|\le m}\bigr)=0.
\]
Its order is the highest derivative order on which the relation actually depends. A system consists of several such relations, often for a vector-valued unknown.

## Time and space

For an evolution equation, one variable is distinguished as time \(t\), with the remaining variables denoted \(x\). The heat equation \(\partial_tu=\nu\Delta u\) is first order in time and second order in space. The way a solution satisfies the equation must be specified; [[partial-differential-equations/classical-solution|classical solutions]] satisfy it pointwise.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
