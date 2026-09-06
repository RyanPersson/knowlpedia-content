+++
id = "operator-algebras/comparison-theorem-for-projections"
title = "Comparison theorem for projections"
kind = "theorem"
summary = "Two projections in a von Neumann algebra become subequivalent in opposite directions after a central decomposition."
aliases = ["Murray–von Neumann comparison theorem"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/center-of-von-neumann-algebra", "operator-algebras/murray-von-neumann-subequivalence"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(p\) and \(q\) be projections in a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\). The
**comparison theorem for projections** states that there is a
[[operator-algebras/center-of-von-neumann-algebra|central projection]]
\(z\in Z(M)\) such that
\[
zp\precsim zq,\qquad (1-z)q\precsim(1-z)p,
\]
where \(\precsim\) denotes
[[operator-algebras/murray-von-neumann-subequivalence|Murray–von Neumann
subequivalence]]. Because \(z\) is central, \(zp,zq,(1-z)p\), and
\((1-z)q\) are projections in the corresponding central summands. Thus any
failure of global comparability is resolved by splitting the algebra along
its center.

## Factor case

If \(M\) is a factor, its only central projections are \(0\) and \(1\).
The theorem then says that any two projections are comparable:
\[
p\precsim q\quad\text{or}\quad q\precsim p.
\]
This total comparability of projection classes is one reason that numerical
or extended numerical dimension functions can classify projections in
factors.

## Interpretation of the central split

A general von Neumann algebra behaves like a family of factors over its
center. On some central components \(p\) is no larger than \(q\); on the
remaining components the reverse holds. The central projection \(z\) records
these first components. It need not be unique without an additional
maximality convention, but the theorem guarantees that at least one such
decomposition exists.

## Consequences

Projection comparison yields the Schröder–Bernstein property for
Murray–von Neumann equivalence and supports the decomposition of projections
into finite and properly infinite parts. Together with
[[operator-algebras/central-support|central support]], it is a principal tool
in the type classification and in the construction of center-valued
dimension functions.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [Publisher record](https://bookstore.ams.org/GSM/16/). Relevant: Theorem 6.2.7 and the surrounding comparison theory.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on comparison of projections.
