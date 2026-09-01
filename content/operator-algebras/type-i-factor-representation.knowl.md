+++
id = "operator-algebras/type-i-factor-representation"
title = "Type I factor representation"
kind = "definition"
summary = "A factor representation whose generated von Neumann algebra is a type I factor."
aliases = ["type I representation", "factor representation of type I"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/cstar-representation", "operator-algebras/von-neumann-algebra", "operator-algebras/type-i-factor", "operator-algebras/bicommutant"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A **type I factor representation** of \(A\) is a nondegenerate [[operator-algebras/cstar-representation|\(*\)-representation]] \(\pi\colon A\to B(H)\) such that the generated [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
\[
\pi(A)''
\]
is a [[operator-algebras/type-i-factor|type I factor]]. Here the double prime denotes the [[operator-algebras/bicommutant|bicommutant]] in \(B(H)\). Factoriality means that the center of \(\pi(A)''\) consists only of scalar multiples of the identity.
Both requirements matter: a type I generated algebra can have nontrivial center, while a factor can have type II or type III.

## Spatial form

A type I factor acting on \(H\) has a tensor-product decomposition
\[
H\cong K\otimes L,\qquad
\pi(A)''\cong B(K)\otimes 1_L.
\]
The auxiliary [[linear-algebra/hilbert-space|Hilbert space]] \(L\) records multiplicity. Thus the generated algebra is abstractly isomorphic to \(B(K)\), but need not equal all of \(B(H)\). When \(L\) is one-dimensional, \(\pi\) is irreducible.

## Role in type I C*-algebras

A \(C^*\)-algebra is type I exactly when every factor representation is of type I. This factor-representation criterion is equivalent to the compact-operator criterion in the definition of a [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]]. It is especially useful for representations that are not irreducible but still generate a factor.

## Terminology

Some authors call any representation \(\pi\) with \(\pi(A)''\) a [[operator-algebras/type-i-von-neumann-algebra|type I von Neumann algebra]] a **type I representation**, without requiring the generated algebra to be a factor. Such a representation may decompose over a nontrivial center. “Type I factor representation” includes the factoriality hypothesis and avoids this ambiguity.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on type I von Neumann algebras and representations.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 6 on factor representations and type I \(C^*\)-algebras.
