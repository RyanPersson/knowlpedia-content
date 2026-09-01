+++
id = "operator-algebras/faithful-cstar-representation"
title = "Faithful representation of a C*-algebra"
kind = "definition"
summary = "An injective representation of a C*-algebra by bounded operators on a Hilbert space."
aliases = ["faithful *-representation", "injective C*-representation"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/cstar-representation", "linear-algebra/hilbert-space", "operator-algebras/faithful-star-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(\pi:A\to\mathcal B(H)\) be a
[[operator-algebras/cstar-representation|representation]] on a complex
[[linear-algebra/hilbert-space|Hilbert space]]. The representation is
**faithful** when \(\pi\) is injective, equivalently
\[
\ker\pi=\{0\}.
\]
Faithfulness means that the operator realization loses no algebra elements or
relations. It does not require \(\pi\) to be irreducible, surjective onto
\(\mathcal B(H)\), unital, or nondegenerate. Thus faithfulness is the
specialization to representations of the general notion of a
[[operator-algebras/faithful-star-homomorphism|faithful \(*\)-homomorphism]].

## Equivalent characterizations

Every \(*\)-homomorphism between \(C^*\)-algebras is contractive, and such a
map is injective exactly when it is isometric. Consequently,
\[
\pi\text{ is faithful}
\quad\Longleftrightarrow\quad
\lVert\pi(a)\rVert=\lVert a\rVert\text{ for every }a\in A.
\]
Its image is then norm closed, and \(\pi\) is a \(*\)-isomorphism from \(A\)
onto the concrete \(C^*\)-algebra \(\pi(A)\).

## Existence and use

The [[operator-algebras/gelfand-naimark-theorem|Gelfand–Naimark theorem]]
states that every \(C^*\)-algebra has a faithful representation on some
Hilbert space. This permits
abstract \(C^*\)-algebras to be studied as norm-closed self-adjoint operator
algebras without changing their norms.

## Examples and distinctions

The defining action of \(K(H)\) on \(H\) is faithful. If
\(\pi:A\to\mathcal B(H)\) is faithful, then
\(a\mapsto\pi(a)\oplus0\) on \(H\oplus K\) remains faithful but is degenerate
when \(K\neq0\). By contrast, a quotient representation \(A\to A/I\) with
\(I\neq0\) is not faithful because its kernel is \(I\).

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on injective \(*\)-homomorphisms and Theorem 3.4.1 on faithful representations.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on represented \(C^*\)-algebras.
