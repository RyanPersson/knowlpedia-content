+++
id = "operator-algebras/bicommutant"
title = "Bicommutant"
kind = "definition"
summary = "The commutant of the commutant of a family of operators."
aliases = ["double commutant"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "operator-algebras/commutant"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and let \(S\subseteq B(H)\) be a family of bounded operators. If \(S'\) denotes the [[operator-algebras/commutant|commutant]] of \(S\), then the **bicommutant** or **double commutant** of \(S\) is
\[
S''=(S')'=\{T\in B(H):TR=RT\text{ for every }R\in S'\}.
\]
Thus \(S''\) consists of the operators that commute with every operator commuting with \(S\). The operation \(S\mapsto S''\) is extensive, monotone, and idempotent. A set satisfying \(S=S''\) is bicommutant-closed, but this condition alone does not make an arbitrary set a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].

## Closure properties

For subsets \(S,T\subseteq B(H)\), one has
\[
S\subseteq S'',\qquad
S\subseteq T\Longrightarrow S''\subseteq T'',\qquad
S''''=S''.
\]
The first inclusion follows because each element of \(S\) commutes with every element of \(S'\). The identity \(S'''=S'\) then gives idempotence. These are the axioms of a closure operation on subsets of \(B(H)\), although it is generally different from norm closure.

## The bicommutant theorem

If \(A\subseteq B(H)\) is a unital self-adjoint operator algebra, von Neumann's bicommutant theorem identifies three objects:
\[
A''=\overline{A}^{\,\mathrm{SOT}}
=\overline{A}^{\,\mathrm{WOT}}.
\]
Consequently, a unital *-subalgebra of \(B(H)\) is a von Neumann algebra exactly when it equals its bicommutant. The hypotheses matter: for a non-self-adjoint family, its bicommutant need not be self-adjoint.

## Ambient representation

The notation \(S''\) is relative to the inclusion \(S\subseteq B(H)\). An abstract algebra can have inequivalent concrete representations, and taking the bicommutant after representing it may produce different concrete von Neumann algebras. One must therefore specify the Hilbert space representation whenever the ambient \(B(H)\) is not already understood.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [AMS book record](https://doi.org/10.1090/gsm/015). Relevant: §5.1.
2. Jacques Dixmier, *Von Neumann Algebras*, North-Holland, 1981. [Elsevier book record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/27/suppl/C). Relevant: Chapter I, §§1–3.
