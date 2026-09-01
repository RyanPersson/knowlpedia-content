+++
id = "operator-algebras/liminal-cstar-algebra"
title = "Liminal C*-algebra"
kind = "definition"
summary = "A C*-algebra whose every irreducible represented image is the algebra of compact operators."
aliases = ["CCR C*-algebra", "completely continuous C*-algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/irreducible-cstar-representation", "operator-algebras/compact-operator-cstar-algebra", "algebra-representation-theory/irreducible-representation", "operator-algebras/elementary-cstar-algebra", "linear-algebra/compact-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) is **liminal**, or **CCR**, if every [[operator-algebras/irreducible-cstar-representation|irreducible representation]] \(\pi\colon A\to B(H_\pi)\) has image
\[
\pi(A)=K(H_\pi),
\]
the [[operator-algebras/compact-operator-cstar-algebra|compact operators]] on its representation space. [[algebra-representation-theory/irreducible-representation|Irreducible representations]] are understood to be nonzero and nondegenerate. Thus every irreducible quotient of \(A\), viewed through its faithful irreducible representation, is an [[operator-algebras/elementary-cstar-algebra|elementary \(C^*\)-algebra]].
The defining equality is stronger than requiring the irreducible image merely to contain the [[linear-algebra/compact-operator|compact operators]].

## Relation to type I

Every liminal algebra is a [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]], since equality with \(K(H_\pi)\) implies the containment required in the type I definition. The converse fails: a type I algebra may have an irreducible image properly containing the compact operators.

For example, \(K(H)+\mathbb C1\) on an infinite-dimensional \(H\) is type I but not liminal. Its identity representation has image strictly larger than \(K(H)\).

## Examples and permanence

Every commutative \(C^*\)-algebra is liminal: its irreducible representations are one-dimensional, and \(K(\mathbb C)=\mathbb C\). Every elementary algebra is liminal as well.

Closed [[algebra-rings/two-sided-ideal|two-sided ideals]] and quotients of a liminal algebra are liminal. Extensions of liminal algebras, however, require care; the class is not characterized merely by having liminal ideal and quotient without additional hypotheses.

## Representation-theoretic meaning

The abbreviation CCR comes from “completely continuous representations,” an older name reflecting that every operator in every irreducible image is compact. The condition makes the irreducible representation theory particularly rigid: an irreducible representation is determined up to unitary equivalence by its kernel. This permits the spectrum of \(A\) to be identified set-theoretically with its [[operator-algebras/primitive-ideal-space|primitive ideal space]], although the associated topology can still be non-Hausdorff.

## References

1. Jacques Dixmier, *C*-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Google Books record](https://books.google.com/books?id=gQFq0AEACAAJ). Relevant: §4.2 on liminal algebras.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 6 on liminal and type I algebras.
