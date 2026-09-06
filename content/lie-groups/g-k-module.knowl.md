+++
id = "lie-groups/g-k-module"
title = "(g,K)-module"
kind = "definition"
summary = "A compatible locally finite action of a complexified Lie algebra and a compact subgroup."
aliases = ["Harish-Chandra pair module", "compatible Lie algebra and compact-group module"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra", "linear-algebra/vector-space", "lie-groups/representation-of-a-lie-algebra", "lie-groups/k-finite-vector"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a real [[fiber-bundles/lie-group|Lie group]], \(K\subseteq G\) a compact subgroup with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak k_0\), and \(\mathfrak g=\operatorname{Lie}(G)\otimes_{\mathbb R}\mathbb C\). A **\((\mathfrak g,K)\)-module** is a complex [[linear-algebra/vector-space|vector space]] \(V\) with a [[lie-groups/representation-of-a-lie-algebra|\(\mathfrak g\)-module]] structure and a \(K\)-action such that every vector is [[lie-groups/k-finite-vector|\(K\)-finite]], the differential of the \(K\)-action equals the restricted \(\mathfrak k_0\)-action, and
\[
k\cdot(X\cdot v)=(\operatorname{Ad}(k)X)\cdot(k\cdot v)
\]
for \(k\in K\), \(X\in\mathfrak g\), and \(v\in V\). These conditions make the two actions infinitesimally and globally compatible.

## Equivalent algebraic viewpoint

The \(\mathfrak g\)-action extends uniquely to an action of the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]] \(U(\mathfrak g)\). The displayed compatibility then becomes
\[
k\cdot(u\cdot v)=(\operatorname{Ad}(k)u)\cdot(k\cdot v)
\qquad (u\in U(\mathfrak g)).
\]
Thus a \((\mathfrak g,K)\)-module retains both differential operators coming from \(G\) and the discrete decomposition into irreducible compact-group types.

## Relation to group representations

For a suitable smooth representation of \(G\), its \(K\)-finite smooth vectors inherit a \((\mathfrak g,K)\)-module structure by differentiation. Passing to this subspace discards the ambient topology but preserves much of the representation’s algebraic information. The reverse passage—from a \((\mathfrak g,K)\)-module to a topological representation of \(G\)—is a globalization problem and is not part of the definition.

## Conventions and scope

In the standard real-reductive setting, \(K\) is a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] and \(\mathfrak g\) is the complexified Lie algebra. Some sources formulate the \(K\)-action as an algebraic representation of a complex reductive group or impose connectedness assumptions. The local-finiteness and compatibility axioms above are the compact-group convention used in analytic representation theory.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, §3.3, “\((\mathfrak g,K)\)-modules.”
2. Anthony W. Knapp and David A. Vogan Jr., *Cohomological Induction and Unitary Representations*, Princeton University Press, 1995. [Publisher record](https://doi.org/10.1515/9781400883936). Relevant: Chapter II on the category \(C(\mathfrak g,K)\).
