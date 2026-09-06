+++
id = "operator-algebras/type-i-ideal-quotient-stability"
title = "Type I stability under ideals and quotients"
kind = "theorem"
summary = "Closed ideals and quotient algebras of a type I C*-algebra are again type I."
aliases = ["type I ideal theorem", "GCR ideals and quotients"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/closed-two-sided-ideal", "operator-algebras/type-i-cstar-algebra", "operator-algebras/cstar-exact-sequence"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a type I \(C^*\)-algebra and let \(I\) be a
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]. Then both
\(I\) and \(A/I\) are
[[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebras]]. Thus in
every [[operator-algebras/cstar-exact-sequence|short exact sequence]]
\[
0\longrightarrow I\longrightarrow A\longrightarrow A/I\longrightarrow0
\]
with type I middle algebra, the ideal and quotient inherit the type I
property. Equivalently, the class of GCR algebras is closed under passing to
closed ideals and quotients. The result applies without separability or
unitality assumptions.

## Representation-theoretic mechanism

An
[[operator-algebras/irreducible-cstar-representation|irreducible representation]]
of \(A/I\) lifts along the quotient map to an [[algebra-representation-theory/irreducible-representation|irreducible representation]] of
\(A\), so its image contains the
[[operator-algebras/compact-operator-cstar-algebra|compact operators]]. For an
irreducible representation of \(I\), the standard extension to \(A\)
transfers the same compact-operator containment. These two correspondences
explain why both halves of the theorem are representation-theoretically
natural.

## Three-space form

Type I is also an extension-stable property: if \(I\) and \(A/I\) are type I,
then \(A\) is type I. Consequently, in a [[algebra-modules/short-exact-sequence|short exact sequence]], knowing any
appropriate ideal–quotient decomposition permits induction through a
[[operator-algebras/type-i-composition-series|composition series]].
This converse is not automatic for an arbitrary class of \(C^*\)-algebras.

## Example

The [[linear-algebra/compact-operator|compact operators]] \(K(H)\) form an ideal in
\(K(H)+\mathbb C I_H\), and the quotient is \(\mathbb C\). Both are type I, so
extension stability recovers that the unitized algebra is type I. The example
also shows that the theorem does not preserve the stronger liminal property
through arbitrary extensions.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, Academic Press, 1979. [DOI record for the revised edition](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Proposition 6.2.6 on ideals, quotients, and extensions of type I algebras.
2. Jacques Dixmier, *C*-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 4 on postliminal ideals and quotients.
