+++
id = "harmonic-analysis/unitary-dual"
title = "Unitary dual of a locally compact group"
kind = "definition"
summary = "The space of unitary-equivalence classes of irreducible continuous unitary representations of a locally compact group."
aliases = ["unitary dual", "dual object of a group", "G-hat", "irreducible dual"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. Its
**unitary dual**, denoted \(\widehat G\), is the set of
[[lie-groups/unitary-equivalence-of-representations|unitary-equivalence
classes]] \([\pi]\) of strongly continuous
[[lie-groups/irreducible-unitary-representation|irreducible unitary
representations]] of \(G\) on nonzero complex [[linear-algebra/hilbert-space|Hilbert spaces]]. The set is
equipped with the [[harmonic-analysis/fell-topology|Fell topology]], defined by approximation of coefficient
functions uniformly on compact subsets. This topology, not a generally
available group operation, is part of the standard meaning of \(\widehat G\).
For abelian \(G\), every [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] is one-dimensional,
and \(\widehat G\) recovers the [[harmonic-analysis/pontryagin-dual|Pontryagin dual group]].

## The Fell topology

Informally, \([\pi]\) is near a class \([\rho]\) when selected diagonal
coefficients of \(\rho\) can be approximated on a chosen compact subset of
\(G\) by finite sums of diagonal coefficients of \(\pi\). This description is
independent of representatives. The resulting space need not be Hausdorff;
its separation properties encode substantial representation-theoretic
information.

## Operator-algebraic interpretation

[[lie-groups/strongly-continuous-unitary-representation|Strongly continuous unitary representations]] of \(G\) correspond to
nondegenerate representations of the full group \(C^*\)-algebra \(C^*(G)\).
Consequently, \(\widehat G\) is naturally the spectrum of irreducible
representations of \(C^*(G)\). Passing from a representation to its kernel
maps this spectrum onto the [[operator-algebras/primitive-ideal-space|primitive ideal space]], but distinct irreducible
representations can have the same kernel unless additional hypotheses, such
as type I regularity, are imposed.

## Scope and nearby duals

The unitary dual includes all irreducible unitary representations. The
tempered dual is generally a proper subspace defined by
[[harmonic-analysis/weak-containment-unitary-representations|weak
containment]] in the [[algebra-representation-theory/regular-representation|regular representation]]. Nor should \(\widehat G\) be
confused with the algebraic dual of a [[lie-groups/lie-algebra|Lie algebra]] or with the set of all
continuous characters; these coincide with the relevant unitary dual only in
special abelian settings.

## References

1. J. M. G. Fell and R. S. Doran, *Representations of \(*\)-Algebras, Locally Compact Groups, and Banach \(*\)-Algebraic Bundles*, vol. 1, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/representations-of-algebras-locally-compact-groups-and-banach-algebraic-bundles/fell/978-0-12-252721-0). Relevant: Chapter VII on representation spaces and their topology.
2. Jacques Dixmier, \(C^*\)-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: chapters on spectra and the dual of a locally compact group.
