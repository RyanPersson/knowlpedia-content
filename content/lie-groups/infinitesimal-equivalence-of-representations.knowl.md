+++
id = "lie-groups/infinitesimal-equivalence-of-representations"
title = "Infinitesimal equivalence of admissible representations"
kind = "definition"
summary = "The relation in which two admissible representations have isomorphic maximal-compact-subgroup-finite modules."
aliases = ["infinitesimally equivalent representations"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]], \(K\) a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and \((\pi,E)\), \((\sigma,F)\) two admissible continuous representations whose [[lie-groups/k-finite-vector|\(K\)-finite parts]] are [[lie-groups/harish-chandra-module|Harish–Chandra modules]]. They are **infinitesimally equivalent** if there is a linear isomorphism
\[
T:E_K\longrightarrow F_K
\]
that intertwines both the action of \(K\) and the differentiated action of the complexified [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\). Equivalently, \(E_K\) and \(F_K\) are isomorphic as \((\mathfrak g,K)\)-modules. No continuity of \(T\) on the ambient completed spaces is part of this definition.

## Data retained and forgotten

Infinitesimal equivalence retains every \(K\)-type and its multiplicity, the action of the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]], [[lie-groups/infinitesimal-character|infinitesimal characters]], and the submodule structure of the Harish–Chandra module. It forgets the topology and norm of the global representation. Consequently, topological equivalence implies infinitesimal equivalence, but the converse requires a globalization theorem or additional hypotheses. This distinction is part of the standard passage between admissible group representations and \((\mathfrak g,K)\)-modules [Wallach, Chapter 4, §4.5](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4).

## Relation to globalization

Different Banach or distribution globalizations of one Harish–Chandra module are infinitesimally equivalent even when their ambient topologies are unlike. Inside the Casselman–Wallach category, however, the [[lie-groups/casselman-wallach-globalization-theorem|globalization theorem]] upgrades infinitesimal equivalence uniquely to a continuous \(G\)-isomorphism. Thus the relation is strictly weaker in a broad topological category but coincides with isomorphism in the smooth admissible moderate-growth Fréchet category.

## Example and near-miss

The smooth and distribution globalizations attached to the same irreducible Harish–Chandra module have the same \(K\)-finite vectors and are therefore infinitesimally equivalent. By contrast, two representations with the same infinitesimal character need not be infinitesimally equivalent: equality of the central character records only the action of \(Z(U(\mathfrak g))\), not the entire \((\mathfrak g,K)\)-module.

## Conventions and scope

Some authors define infinitesimal equivalence first for admissible Hilbert representations and then extend it to other globalizations. The invariant criterion is the \((\mathfrak g,K)\)-module isomorphism in the core. Merely intertwining the \(\mathfrak g\)-actions is insufficient because it can lose the action of the possibly disconnected compact group \(K\).

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 4, §4.5 on infinitesimal equivalence.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VIII on admissible representations and their underlying \((\mathfrak g,K)\)-modules.
