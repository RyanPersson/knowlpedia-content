+++
id = "algebra-representation-theory/central-character"
title = "Central character of a representation"
kind = "definition"
summary = "The character by which the center of a group acts on a representation."
aliases = ["central character", "central quasicharacter", "character of the center of a representation"]
domains = ["algebra-representation-theory", "harmonic-analysis", "langlands"]
section_mode = "progressive"
+++

Let \(G\) be a group with [[algebra-groups/center-of-group|center]] \(Z(G)\),
and let \((\pi,V)\) be a representation. A **central character** of \(\pi\)
is a [[algebra-representation-theory/character|character]]
\(\omega_\pi:Z(G)\to k^\times\) such that

\[
\pi(z)=\omega_\pi(z)\operatorname{id}_V
\qquad(z\in Z(G)).
\]

For an
[[algebra-representation-theory/irreducible-representation|irreducible
representation]] over an
[[algebraic-geometry-foundations/algebraically-closed-field|algebraically
closed field]], the
existence and uniqueness of \(\omega_\pi\) follow from
[[algebra-representation-theory/schurs-lemma|Schur's lemma]] whenever
the endomorphism version of that lemma applies. For
[[topology/topological-group|topological groups]] and
continuous or smooth representations, the central character is required to
have the corresponding continuity or smoothness.

## Distinctions

This is different from the
[[lie-groups/infinitesimal-character|infinitesimal character]], which records
the action of the center of a
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]. It is also
different from a character of \(G\) itself: only the center must act by the
specified scalar.

## Langlands compatibility

For \(G=\operatorname{GL}_n(F)\), the determinant of a
[[langlands/local-l-parameter|local Langlands parameter]] corresponds under
[[langlands/local-class-field-theory|local class field theory]] to the central
character of the associated representation.  Analogous statements for a
general
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
use the map from its
[[langlands/l-group|\(L\)-group]] to the \(L\)-group of its
center.

## References

1. Jean-Pierre Serre, *Linear Representations of Finite Groups*, Graduate
   Texts in Mathematics 42, Springer, 1977, §2.2.
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   2022, §2.1. [arXiv](https://arxiv.org/abs/2201.07741).
