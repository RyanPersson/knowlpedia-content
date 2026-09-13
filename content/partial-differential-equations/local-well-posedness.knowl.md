+++
id = "partial-differential-equations/local-well-posedness"
title = "Local well-posedness of an evolution problem"
kind = "definition"
summary = "Local existence, uniqueness in a specified class, and continuous dependence on the data."
aliases = ["local well posedness"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/cauchy-problem", "topology/continuous-map", "topology/neighborhood"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An evolution problem is **locally well posed** near a datum \(u_0\) in a data space \(X\) if there are a time \(T>t_0\), a neighborhood \(V\subseteq X\) of \(u_0\), and a specified solution space \(Y_T\) such that:

1. Every datum in \(V\) has a solution on \([t_0,T]\).
2. The solution is unique in the asserted class.
3. The map from the datum to its solution in \(Y_T\) is [[topology/continuous-map|continuous]].

The equation, coefficients, and forcing are held fixed unless the data space explicitly includes them.

## Dependence on the chosen spaces

Well-posedness is a statement about both an equation and its data and solution topologies. Existence alone is insufficient. Uniqueness in a smooth class also does not automatically imply uniqueness in every larger weak-solution class.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
