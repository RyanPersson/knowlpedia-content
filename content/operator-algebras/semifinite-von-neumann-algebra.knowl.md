+++
id = "operator-algebras/semifinite-von-neumann-algebra"
title = "Semifinite von Neumann algebra"
kind = "definition"
summary = "A von Neumann algebra in which every nonzero projection dominates a nonzero finite projection."
aliases = ["semifinite W*-algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/finite-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is
**semifinite** if every nonzero projection \(p\in M\) dominates a nonzero
[[operator-algebras/finite-projection|finite projection]]: there is a projection
\(0\neq q\leq p\) that is finite relative to \(M\). Equivalently, the supremum
of the finite projections of \(M\) is \(1\), or every nonzero central summand
of \(M\) contains a nonzero finite projection. This is a property of the
algebra’s projection structure. It includes all type I and type II von Neumann
algebras and excludes every nonzero type III direct summand.

## Tracial characterization

Semifiniteness is equivalent to the existence of a faithful normal semifinite
trace on \(M\). Here “semifinite” for the trace means that every nonzero
positive element majorizes a nonzero positive element of finite trace; it does
not mean that the identity has finite trace. A semifinite von Neumann algebra
can also be equipped with a faithful normal semifinite center-valued trace.

## Examples and boundary cases

Every [[operator-algebras/finite-von-neumann-algebra|finite von Neumann algebra]] is semifinite. The algebra \(B(H)\) is
semifinite even when \(H\) is infinite-dimensional: finite-rank projections
provide finite subprojections, and the [[operator-algebras/operator-trace|canonical operator trace]] is faithful,
normal, and semifinite although it sends \(1\) to \(+\infty\). Type
\(\mathrm{II}_\infty\) factors are semifinite but not finite. A nonzero type
III algebra is not semifinite because it has no nonzero finite projection.

## Classification convention

**Warning.** “Semifinite von Neumann algebra” and “[[operator-algebras/semifinite-weight|semifinite weight]]” are
different predicates: the first classifies an algebra, while the second states
an approximation property of a particular
[[operator-algebras/weight-on-von-neumann-algebra|weight]]. Every von Neumann
algebra admits [[operator-algebras/normal-semifinite-faithful-weight|faithful normal semifinite weights]], including type III
algebras; requiring the weight to be tracial is what characterizes a
semifinite algebra.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §§6.3 and 6.5 on finite projections and semifinite type.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on semifinite von Neumann algebras and traces.
