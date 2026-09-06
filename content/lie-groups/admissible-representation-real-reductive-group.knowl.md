+++
id = "lie-groups/admissible-representation-real-reductive-group"
title = "Admissible representation of a real reductive group"
kind = "definition"
summary = "A representation whose restriction to a maximal compact subgroup has finite multiplicity for every irreducible type."
aliases = ["admissible representation", "finite K-multiplicity representation"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/k-finite-vector", "lie-groups/k-type"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]]
and \(K\subseteq G\) a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]]. A representation \(V\) in the algebraic or continuous
real-reductive category is **admissible** when every irreducible
representation \(\tau\) of \(K\) occurs in its
[[lie-groups/k-finite-vector|\(K\)-finite part]] \(V_K\) with finite
multiplicity:
\[
\dim\operatorname{Hom}_K(E_\tau,V_K)<\infty.
\]
If \(V\) is already an algebraic \(K\)-module, take \(V_K=V\). For a
continuous unitary Hilbert representation, this says that every
[[lie-groups/k-type|\(K\)-type]] isotypic component is finite-dimensional.
The definition allows infinitely many distinct \(K\)-types and applies
equally to nonunitary globalizations and \((\mathfrak g,K)\)-modules.

## Algebraic formulation

For a \((\mathfrak g,K)\)-module the core condition is imposed directly on
its algebraic \(K\)-decomposition. This is the form used in Harish–Chandra
theory. If the module is also finitely generated over the
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]
\(U(\mathfrak g)\), it is a
[[lie-groups/harish-chandra-module|Harish–Chandra module]]. The distinction
matters: admissibility alone does not assert finite generation or finite
length.

## Harish–Chandra's finiteness theorem

For real reductive groups in the standard Harish–Chandra class,
[[lie-groups/irreducible-unitary-representation|irreducible unitary
representations]] are admissible. This deep theorem converts an
infinite-dimensional Hilbert representation into a discrete family of
finite-dimensional \(K\)-isotypic pieces. Admissibility of a reducible
representation is not automatic: an infinite Hilbert direct sum of the
trivial representation has infinite multiplicity for the trivial \(K\)-type.

## Conventions and scope

Some sources define admissibility for continuous representations on complete [[functional-analysis/locally-convex-space|locally convex spaces]] rather than only [[linear-algebra/hilbert-space|Hilbert spaces]]. The invariant content is finite \(K\)-multiplicity, together with enough regularity for the restriction to \(K\) to decompose. Since [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroups]] are conjugate, admissibility does not depend on the chosen \(K\), up to the corresponding transported types.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [DOI record](https://doi.org/10.1515/9781400883974). Relevant: Chapter VIII, “Admissible Representations.”
2. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, §§3.3–3.4.
