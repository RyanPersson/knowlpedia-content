+++
id = "partial-differential-equations/linear-differential-operator"
title = "Linear partial differential operator"
kind = "definition"
summary = "A finite linear combination of partial derivatives with coefficient functions."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/multi-index-notation", "real-analysis/class-ck-map", "linear-algebra/linear-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **linear partial differential operator** of order at most \(m\) on an open set \(U\) has the form
\[
Lu(x)=\sum_{|\alpha|\le m}a_\alpha(x)\partial^\alpha u(x).
\]
The coefficients \(a_\alpha\) are prescribed functions. The map is [[linear-algebra/linear-map|linear]] in \(u\), although its coefficients may vary with \(x\). It has order exactly \(m\) if at least one coefficient of an order-\(m\) derivative is not identically zero.

## Systems and nonlinearity

For vector-valued \(u\), the coefficients may be matrices of compatible sizes. If the coefficients depend on the unknown itself, the resulting expression is generally nonlinear. For example, \(b(x)\partial_xu\) is linear in \(u\), whereas \(u\partial_xu\) is not.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
