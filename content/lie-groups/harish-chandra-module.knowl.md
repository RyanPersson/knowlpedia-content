+++
id = "lie-groups/harish-chandra-module"
title = "Harish–Chandra module"
kind = "definition"
summary = "An admissible (g,K)-module that is finitely generated over the universal enveloping algebra."
aliases = ["admissible finitely generated (g,K)-module"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/g-k-module", "lie-groups/admissible-representation-real-reductive-group", "lie-groups/universal-enveloping-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]], \(K\) a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and \(\mathfrak g=\operatorname{Lie}(G)\otimes_{\mathbb R}\mathbb C\). A **Harish–Chandra module** is a [[lie-groups/g-k-module|\((\mathfrak g,K)\)-module]] \(V\) that is [[lie-groups/admissible-representation-real-reductive-group|admissible]] and finitely generated as a module over the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]] \(U(\mathfrak g)\). Explicitly, every irreducible \(K\)-representation occurs in \(V\) with finite multiplicity, and finitely many vectors generate \(V\) under \(U(\mathfrak g)\). These are independent finiteness requirements: neither is omitted from the standard definition used in real-reductive representation theory.

## From group representations

If \(\pi\) is an irreducible admissible representation of \(G\), its \(K\)-finite vectors carry the differentiated \(\mathfrak g\)-action and form a Harish–Chandra module. For an [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]], admissibility follows from Harish–Chandra’s finiteness theorem, and the resulting module is irreducible. This passage preserves the \(K\)-type multiplicities and infinitesimal action while forgetting the Hilbert topology.

## Structural consequences

Harish–Chandra modules have finite length. Their irreducible subquotients are again Harish–Chandra modules, and the center of \(U(\mathfrak g)\) acts locally finitely. These finiteness properties make algebraic tools—central characters, [[algebra-modules/composition-series-module|composition series]], homological functors, and induction—available for studying representations of noncompact groups.

## Conventions and scope

Some authors reserve “Harish–Chandra module” for a module obtained as the \(K\)-finite vectors of a particular globalization; others use the intrinsic two-condition definition above. A bare \((\mathfrak g,K)\)-module need not be Harish–Chandra. Likewise, an admissible module with no finite set of \(U(\mathfrak g)\)-generators is a decisive near-miss.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, §§3.3–3.5.
2. Anthony W. Knapp and David A. Vogan Jr., *Cohomological Induction and Unitary Representations*, Princeton University Press, 1995. [Publisher record](https://doi.org/10.1515/9781400883936). Relevant: Chapters I–II, especially the category \(C(\mathfrak g,K)\).
