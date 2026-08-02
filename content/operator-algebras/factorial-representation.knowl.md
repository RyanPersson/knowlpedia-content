+++
id = "operator-algebras/factorial-representation"
title = "Factorial representation"
kind = "definition"
summary = "A representation whose generated von Neumann algebra is a factor."
aliases = ["factor representation", "primary representation"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(\pi:A\to\mathcal B(H)\) be a
[[operator-algebras/cstar-representation|representation of a
\(C^*\)-algebra]]. It is a **factorial representation**, or **factor
representation**, if its
[[operator-algebras/von-neumann-algebra-generated-by-representation|generated
von Neumann algebra]]
\[
\pi(A)''
\]
is a [[operator-algebras/von-neumann-factor|factor]]; equivalently,
\[
Z(\pi(A)'')=\mathbb C I_H.
\]
Thus factoriality excludes nontrivial central decompositions of the weak
closure of the represented algebra. It does not require
\(\pi(A)'=\mathbb C I_H\), which would be irreducibility, and it does not
require \(\pi\) to be faithful. Some authors use **primary representation**
for the same condition.

## Comparison with irreducibility

Every
[[operator-algebras/irreducible-cstar-representation|irreducible
representation]] is factorial because
\(\pi(A)'=\mathbb C I_H\) implies
\(\pi(A)''=\mathcal B(H)\). The converse fails: if a non-type-I factor \(M\)
acts by left multiplication on \(L^2(M)\), then the generated algebra is a
factor, but the commuting right action is nontrivial. Factoriality therefore
captures indecomposability at the level of central summands, not the absence
of all invariant subspaces.

## Central projections and decomposition

A central projection \(z\in Z(\pi(A)'')\) splits \(H\) into the reducing
subspaces \(zH\) and \((1-z)H\). Factoriality says that no such nontrivial
split is available inside the [[operator-algebras/von-neumann-algebra-generated-by-representation|generated von Neumann algebra]]. General
representations can often be decomposed, in a measure-theoretic sense, into
factorial representations; this is the factor analogue of decomposing a
finite-dimensional representation into primary pieces.

## Factorial states

A state on \(A\) is called factorial when its GNS representation is
factorial. Pure states yield irreducible, hence factorial, GNS
representations, but factorial states need not be pure. This distinction is
important for equilibrium states and for representations generating type II
or [[operator-algebras/type-iii-factor|type III factors]].

## References

1. Jacques Dixmier, *C*-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 5 on types of representations and primary representations.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on factors and factorial representations.
