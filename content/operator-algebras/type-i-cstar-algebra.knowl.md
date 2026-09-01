+++
id = "operator-algebras/type-i-cstar-algebra"
title = "Type I C*-algebra"
kind = "definition"
summary = "A type I C*-algebra is one whose every irreducible represented image contains all compact operators on its representation space."
aliases = ["GCR C*-algebra", "GCR algebra", "postliminal C*-algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/irreducible-cstar-representation", "operator-algebras/compact-operator-cstar-algebra", "operator-algebras/von-neumann-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A \(C^*\)-algebra \(A\) is a **type I \(C^*\)-algebra**, also called **GCR** or **postliminal**, if for every [[operator-algebras/irreducible-cstar-representation|irreducible representation]] \(\pi\colon A\to B(H_\pi)\), the represented algebra contains the [[operator-algebras/compact-operator-cstar-algebra|compact operators]]:
\[
K(H_\pi)\subseteq\pi(A).
\]
This condition applies to nonunital as well as unital algebras and is independent of the chosen representative of the unitary-equivalence class. It is the \(C^*\)-algebraic type I condition, distinct from saying that a particular [[operator-algebras/von-neumann-algebra|von Neumann algebra]] is type I.

## Equivalent viewpoints

Equivalently, every [[operator-algebras/factorial-representation|factor representation]] \(\pi\) of \(A\) generates a [[operator-algebras/type-i-von-neumann-algebra|type I von Neumann algebra]] \(\pi(A)''\). Another characteristic consequence is that an [[algebra-representation-theory/irreducible-representation|irreducible representation]] is determined up to unitary equivalence by its kernel. Hence the spectrum of \(A\) maps bijectively to its [[operator-algebras/primitive-ideal-space|primitive ideal space]].

## Examples and contrasts

Every commutative \(C^*\)-algebra and every compact-operator algebra \(K(H)\) is type I. The stronger CCR, or liminal, condition requires \(\pi(A)=K(H_\pi)\) for every irreducible \(\pi\); type I only requires containment. Group \(C^*\)-algebras of type I groups supply important noncommutative examples, while many discrete groups have non-type-I full group algebras.

## References

1. G. K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 6 on type I and postliminal algebras.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on type I representations and von Neumann algebras.
