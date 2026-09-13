+++
id = "partial-differential-equations/cauchy-problem"
title = "Cauchy problem for an evolution PDE"
kind = "definition"
summary = "An evolution equation together with prescribed initial data."
aliases = ["initial-value problem for a PDE"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/partial-differential-equation", "partial-differential-equations/initial-datum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **Cauchy problem** specifies an evolution [[partial-differential-equations/partial-differential-equation|PDE]] and the required [[partial-differential-equations/initial-datum|initial data]]. For a first-order time equation it has the schematic form
\[
\partial_tu=\mathcal F(t,x,u,\nabla u,\ldots),
\qquad u(t_0,x)=u_0(x).
\]
The spatial domain, coefficient functions, forcing, and class in which the solution is sought are part of the problem.

## Higher time order and boundaries

A second-order time equation usually requires both \(u(t_0,x)\) and \(\partial_tu(t_0,x)\). On a bounded spatial domain one generally also imposes boundary conditions, giving an initial-boundary-value problem. On the whole space, decay or integrability assumptions often replace boundary conditions.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
