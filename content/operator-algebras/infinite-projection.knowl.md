+++
id = "operator-algebras/infinite-projection"
title = "Infinite projection"
kind = "definition"
summary = "A projection that is Murray–von Neumann equivalent to one of its proper subprojections."
aliases = ["Murray–von Neumann infinite projection"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/murray-von-neumann-equivalence", "functional-analysis/partial-isometry", "operator-algebras/finite-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] and
let \(p\in M\) be a projection. The projection \(p\) is **infinite** if there
exists a projection \(q\in M\) with \(q<p\) such that \(p\) and \(q\) are
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalent]]. Explicitly, some [[functional-analysis/partial-isometry|partial isometry]] \(v\in M\) satisfies
\(v^*v=p\) and \(vv^*=q\), while \(q\neq p\). Thus infiniteness is witnessed
inside the ambient algebra by moving all of \(p\) onto a proper part of itself.
A projection is [[operator-algebras/finite-projection|finite]] precisely when
no such proper equivalent subprojection exists.

## Examples and permanence

The identity of \(B(H)\) is infinite when \(H\) is infinite-dimensional: a
unitary from \(H\) onto a proper closed infinite-dimensional subspace gives the
required partial isometry. Every finite-rank projection in \(B(H)\) is finite.
If \(p\) is infinite and \(p\leq r\), then \(r\) is infinite as well. Unitary
conjugacy and Murray–von Neumann equivalence also preserve infiniteness.

## Proper infiniteness

An infinite projection need not be **properly infinite**. The latter means that
\(p\) contains two orthogonal subprojections \(p_1,p_2\leq p\), each
Murray–von Neumann equivalent to \(p\). Proper infiniteness is therefore a
stronger doubling condition. In a factor, every infinite projection is
properly infinite, but this implication can fail in a von Neumann algebra with
nontrivial center. The distinction matters in comparison theory and in the
classification of nonfactor algebras.

## Type-theoretic role

Finite and infinite are properties of projections relative to \(M\), not
statements about the cardinality of a set. A von Neumann algebra is type III
exactly when every nonzero projection is infinite, while semifinite algebras
have enough nonzero finite subprojections to meet every nonzero projection.
These projection comparisons underlie the Murray–von Neumann type
classification.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §6.3 on finite, infinite, and properly infinite projections.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on projection comparison and factor types.
