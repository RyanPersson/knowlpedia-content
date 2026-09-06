+++
id = "harmonic-analysis/fell-topology"
title = "Fell topology on the unitary dual"
kind = "definition"
summary = "The Fell topology is the hull-kernel topology on equivalence classes of irreducible unitary representations."
aliases = ["Fell topology", "hull-kernel topology on the unitary dual", "Jacobson topology on irreducible representations"]
domains = ["harmonic-analysis", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/unitary-dual", "operator-algebras/full-group-cstar-algebra", "harmonic-analysis/weak-containment-unitary-representations"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. Via integrated forms, its [[harmonic-analysis/unitary-dual|unitary dual]] \(\widehat G\) is the spectrum of the [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]] \(C^*(G)\). The **Fell topology** is the hull-kernel topology: for \(S\subseteq\widehat G\), an irreducible class \([\pi]\) lies in \(\overline S\) exactly when
\[
\bigcap_{[\rho]\in S}\ker\rho\subseteq\ker\pi.
\]
Equivalently, \(\pi\) is [[harmonic-analysis/weak-containment-unitary-representations|weakly contained]] in the direct sum of the representations in \(S\). This definition is independent of representatives of the unitary-equivalence classes.

## Coefficients and convergence

Fell's coefficient-function description gives the same topology: neighborhoods control finite collections of [[harmonic-analysis/coefficient-function|coefficient functions]] on compact subsets of \(G\), allowing coefficients of a nearby representation to approximate those of the given one. This formulation is especially useful when representations are constructed concretely, whereas the kernel formulation exposes the topology's relation to ideals. Their equivalence is a theorem, not a separate topology.

## Separation and type I groups

The kernel map sends \(\widehat G\) onto the [[operator-algebras/primitive-ideal-space|primitive ideal space]] of \(C^*(G)\). For a [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]] it is a bijection, but outside the type I setting inequivalent [[algebra-representation-theory/irreducible-representation|irreducible representations]] can have the same kernel and hence cannot be separated by this topology. Even for type I groups, the Fell topology need not be Hausdorff.

## References

1. J. M. G. Fell, “The Dual Spaces of \(C^*\)-Algebras,” *Transactions of the American Mathematical Society* 94 (1960), 365–403. [DOI record](https://doi.org/10.1090/S0002-9947-1960-0146681-0). Relevant: hull-kernel topology, positive-type functions, and the group dual.
2. J. M. G. Fell and R. S. Doran, *Representations of \(*\)-Algebras, Locally Compact Groups, and Banach \(*\)-Algebraic Bundles*, vol. I, Academic Press, 1988. [Publisher record](https://www.sciencedirect.com/bookseries/pure-and-applied-mathematics/vol/125/suppl/C). Relevant: Chapter VII on weak containment and dual topologies.
