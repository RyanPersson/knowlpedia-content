+++
id = "operator-algebras/disjoint-representations"
title = "Disjoint representations"
kind = "definition"
summary = "Representations of a C-star algebra having no nonzero unitarily equivalent subrepresentations."
aliases = ["disjoint C-star representations", "mutually disjoint representations"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/cstar-representation", "operator-algebras/unitary-equivalence-cstar-representations", "linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a complex [[operator-algebras/cstar-algebra|\(C^*\)-algebra]],
and let \(\pi_i:A\to B(H_i)\) be nondegenerate
[[operator-algebras/cstar-representation|representations]]. They are
**disjoint** if they have no nonzero subrepresentations that are
[[operator-algebras/unitary-equivalence-cstar-representations|unitarily equivalent]]. Equivalently, the only bounded operator \(T:H_1\to H_2\)
satisfying
\[
T\pi_1(a)=\pi_2(a)T\qquad(a\in A)
\]
is \(T=0\). Nondegeneracy removes irrelevant zero summands on which every
operator would intertwine. Disjointness is a relation between the represented
copies of \(A\), not merely a statement that the [[linear-algebra/hilbert-space|Hilbert spaces]] or the
norm-closed image algebras are nonisomorphic.

## Equivalent characterizations

If a nonzero intertwiner \(T\) exists, its polar decomposition supplies a
nonzero [[functional-analysis/partial-isometry|partial isometry]] intertwining
the two representations. Its initial and final spaces then carry unitarily
equivalent subrepresentations. This proves the equivalence between the two
formulations in the core.

After passing to the universal representation of \(A\), each \(\pi_i\) has a
normal extension to a central summand of \(A^{**}\). The representations are
disjoint exactly when the corresponding
[[operator-algebras/central-support|central support projections]] are
orthogonal. This is why disjointness is suited to central and direct-integral
decompositions.

## Relation to other equivalence notions

Unitary equivalence is the opposite extreme: it gives a unitary intertwiner,
so two nonzero unitarily equivalent representations are never disjoint.
[[operator-algebras/quasi-equivalent-representations|Quasi-equivalence]] also
precludes disjointness for nonzero representations, but it permits different
Hilbert-space multiplicities. [[operator-algebras/factorial-representation|Factor representations]] exhibit the basic
dichotomy: two factor representations are either quasi-equivalent or disjoint.

## Examples and scope

For a commutative algebra \(C_0(X)\), point-evaluation representations at
distinct points are disjoint: their one-dimensional subrepresentations are
inequivalent. Repeating one evaluation with any nonzero multiplicity does not
make it disjoint from the original evaluation, because a one-dimensional
common subrepresentation remains.

**Warning.** Inequivalent representations need not be disjoint. Two reducible
representations can fail to be unitarily equivalent while sharing a nonzero
summand.

## References

1. Jacques Dixmier, \(C^*\)-Algebras, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 5, §5.2 on disjointness and quasi-equivalence of representations.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on normal extensions, quasi-equivalence, and disjointness.
