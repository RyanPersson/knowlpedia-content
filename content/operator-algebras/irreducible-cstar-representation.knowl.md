+++
id = "operator-algebras/irreducible-cstar-representation"
title = "Irreducible representation of a C*-algebra"
kind = "definition"
summary = "A nonzero representation of a C*-algebra is irreducible when it has no nontrivial closed invariant Hilbert subspaces."
aliases = ["topologically irreducible *-representation", "irreducible C*-representation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-representation", "linear-algebra/orthogonal-complement"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi:A\to B(H)\) be a nonzero [[operator-algebras/cstar-representation|representation of a \(C^*\)-algebra]]. It is **irreducible** when the only closed subspaces \(K\subseteq H\) satisfying \(\pi(a)K\subseteq K\) for every \(a\in A\) are \(K=\{0\}\) and \(K=H\). Because \(A\) is closed under involution, every invariant closed subspace is automatically reducing: its [[linear-algebra/orthogonal-complement|orthogonal complement]] is invariant as well. The word “closed” is essential; irreducibility is a topological condition on the Hilbert-space representation, not algebraic simplicity of the underlying module.

## Equivalent characterizations

Irreducibility is equivalent to the [[operator-algebras/commutant|commutant]] condition
\[
\pi(A)'=\mathbb C I_H.
\]
It is also equivalent to every nonzero vector of \(H\) being cyclic, since the closure of \(\pi(A)\xi\) is an invariant subspace. These equivalences are standard forms of [[algebra-representation-theory/schurs-lemma|Schur's lemma]] for \(C^*\)-representations.

## Kernels and states

The [[operator-algebras/primitive-ideal|kernel of an irreducible representation]] is a primitive ideal. Through the [[operator-algebras/gns-construction|GNS construction]], [[operator-algebras/pure-state-cstar-algebra|pure states]] yield irreducible representations, and every irreducible representation is equivalent to one obtained from a pure state after choosing a unit vector. Thus irreducibles connect state-space geometry with ideal structure.

## Examples and non-examples

The defining representation of the [[operator-algebras/compact-operator-cstar-algebra|compact-operator \(C^*\)-algebra]] \(K(H)\) on a nonzero [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is irreducible. A direct sum \(\pi_1\oplus\pi_2\) with both summands nonzero is reducible because each summand is a proper closed invariant subspace. An irreducible representation may have a nonzero kernel, so it need not be faithful.

## References

1. Gerald J. Murphy, \(C^*\)-*Algebras and Operator Theory*, Academic Press, 1990. [Publisher record](https://shop.elsevier.com/books/c-algebras-and-operator-theory/murphy/978-0-08-092496-0). Relevant: section 3.3 on irreducible and cyclic representations.
2. Jacques Dixmier, \(C^*\)-*Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: section 2.5 on irreducible representations.
