+++
id = "partial-differential-equations/principal-part"
title = "Principal part of a differential operator"
kind = "definition"
summary = "The sum of the highest-order derivative terms in a linear differential operator."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/linear-differential-operator"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If a [[partial-differential-equations/linear-differential-operator|linear differential operator]] has order \(m\),
\[
L=\sum_{|\alpha|\le m}a_\alpha(x)\partial^\alpha,
\]
its **principal part** is
\[
L_m=\sum_{|\alpha|=m}a_\alpha(x)\partial^\alpha.
\]
The remaining terms have lower differential order.

## Example and conventions

For \(L=\partial_x^2+2\partial_x\partial_y+3\partial_y^2+b(x,y)\partial_x+c(x,y)\), the first three terms form the principal part. In an evolution equation, authors may use a parabolic order that counts one time derivative like two space derivatives; that convention must be declared.

An asymptotic argument may also call its leading approximation a “principal operator.” Leading size in a small parameter and highest differential order are different criteria and need not select the same terms.

## References

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
