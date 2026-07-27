+++
id = "lie-groups/maximal-compact-subgroup-real-reductive-group"
title = "Maximal compact subgroup of a real reductive group"
kind = "definition"
summary = "A compact subgroup maximal by inclusion, canonically associated up to conjugacy with a Cartan involution."
aliases = ["maximal compact K", "maximal compact subgroup"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

A **maximal compact subgroup** of a
[[lie-groups/real-reductive-lie-group|real reductive Lie group]] \(G\) is a
compact subgroup \(K\subseteq G\) not properly contained in any other compact
subgroup. For a Cartan involution of \(G\), its fixed-point subgroup
\[
K=G^\theta=\{g\in G:\theta(g)=g\}
\]
is maximal compact, and its [[lie-groups/lie-algebra|Lie algebra]] is the \(+1\)-eigenspace
\(\mathfrak k\) in the
[[lie-groups/cartan-decomposition-real-reductive-lie-algebra|Cartan
decomposition]] \(\mathfrak g=\mathfrak k\oplus\mathfrak p\). Conversely,
after conjugacy, maximal compact subgroups arise this way. Hence \(K\) is not
canonical as a subgroup, but its conjugacy class is canonical.

## Conjugacy and topology

Every compact subgroup of \(G\) is contained in a maximal compact subgroup,
and any two maximal compact subgroups are conjugate in \(G\). Moreover, the
inclusion \(K\hookrightarrow G\) is a homotopy equivalence in the standard
Cartan setting because \(G\) is diffeomorphic to \(K\times\mathfrak p\).
Thus many topological invariants of \(G\) can be computed from \(K\)
[Knapp, Chapter VI, §4](https://link.springer.com/book/9780817642594).

## Role in representation theory

Restricting a representation of \(G\) to the compact group \(K\) decomposes
it into finite-dimensional \(K\)-types. Their multiplicities formulate
admissibility and provide the algebraic skeleton of [[lie-groups/harish-chandra-module|Harish–Chandra modules]].
The subgroup also enters the decompositions \(G=K\exp(\mathfrak p)\) and
\(G=KAN\), so it connects representation theory to harmonic analysis and
geometry.

## Example and warning

For \(G=\mathrm{GL}_n(\mathbb R)\), one may take
\(K=\mathrm O(n)\); for \(G=\mathrm{SL}_n(\mathbb R)\), one takes
\(\mathrm{SO}(n)\). A maximal compact subgroup is generally not a Cartan
subgroup: these are different notions, despite the common use of the letter
\(K\) in Cartan theory.

## References

1. A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [Publisher record](https://link.springer.com/book/9780817642594). Relevant: Chapter VI, §4 on maximal compact subgroups.
2. S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapter VI on the global structure associated with \(K\).
