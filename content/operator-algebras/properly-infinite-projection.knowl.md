+++
id = "operator-algebras/properly-infinite-projection"
title = "Properly infinite projection"
kind = "definition"
summary = "A projection that contains two orthogonal subprojections, each equivalent to the original projection."
aliases = ["Murray–von Neumann properly infinite projection"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "linear-algebra/orthogonal-projection", "operator-algebras/murray-von-neumann-equivalence", "operator-algebras/infinite-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(p\) be a projection in a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\). The projection
\(p\) is
**properly infinite** if there are [[linear-algebra/orthogonal-projection|orthogonal projections]] \(p_1,p_2\leq p\)
such that
\[
p_1\sim p\sim p_2,
\]
where \(\sim\) is
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalence]]. Equivalently, two orthogonal copies of \(p\) can be embedded
under \(p\), often written \(p\oplus p\precsim p\) after passage to a matrix
algebra. Every properly infinite projection is
[[operator-algebras/infinite-projection|infinite]], since either \(p_i\) is a
proper subprojection equivalent to \(p\). The converse need not hold in a
general algebra.

## Examples

The identity of \(B(H)\) is properly infinite when \(H\) is
infinite-dimensional: split \(H\) into two orthogonal infinite-dimensional
subspaces, each unitarily isomorphic to \(H\). More generally, every
infinite-rank projection in \(B(H)\) is properly infinite. By contrast, no
nonzero projection in a [[operator-algebras/finite-von-neumann-algebra|finite von Neumann algebra]] is properly infinite.

## Relation to factors

In a [[operator-algebras/von-neumann-factor|von Neumann factor]], every infinite projection is properly infinite.
For [[operator-algebras/von-neumann-algebra|von Neumann algebras]] with nontrivial center, an infinite projection can
have finite behavior on some central summands, so infiniteness need not imply
proper infiniteness. Projection comparison and central support isolate the
summands on which the doubling condition holds.

## Permanence and type theory

Proper infiniteness is invariant under Murray–von Neumann equivalence and
unitary conjugacy, and orthogonal sums of properly infinite projections are
properly infinite. Merely dominating a properly infinite projection does not
force proper infiniteness when an additional finite central summand is
present. The identity is properly infinite in every type \(\mathrm
I_\infty\), type \(\mathrm{II}_\infty\), or type \(\mathrm{III}\) factor,
making the condition central to the infinite side of von Neumann algebra
classification.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [Publisher record](https://bookstore.ams.org/GSM/16/). Relevant: §6.3 on infinite and properly infinite projections.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on projection comparison and factor types.
