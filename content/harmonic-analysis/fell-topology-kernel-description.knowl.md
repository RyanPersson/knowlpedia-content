+++
id = "harmonic-analysis/fell-topology-kernel-description"
title = "Kernel description of Fell topology"
kind = "definition"
summary = "The kernel description of Fell topology expresses closure of irreducible representations through containment of intersections of their kernels."
aliases = ["primitive-ideal description of Fell topology", "hull-kernel convergence"]
domains = ["harmonic-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], let \(A=C^*(G)\) be its [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]], and identify its [[algebra-representation-theory/irreducible-representation|irreducible representations]] with the [[harmonic-analysis/unitary-dual|unitary dual]] \(\widehat G\). The [[harmonic-analysis/fell-topology|Fell topology]] has the following **kernel description**:
\[
[\pi]\in\overline S
\quad\Longleftrightarrow\quad
\bigcap_{[\rho]\in S}\ker\rho\subseteq\ker\pi
\]
for every \(S\subseteq\widehat G\). Equivalently, its closed sets are precisely the hulls of ideals, where the hull of an ideal \(I\triangleleft A\) is \(\{[\pi]:I\subseteq\ker\pi\}\). The criterion depends only on representation kernels, not on chosen representatives or realization spaces.

## Relation to the primitive ideal space

Each kernel \(\ker\pi\) is a [[operator-algebras/primitive-ideal|primitive ideal]], so the kernel map
\[
\kappa:\widehat G\longrightarrow\operatorname{Prim}(C^*(G)),
\qquad [\pi]\longmapsto\ker\pi,
\]
is a continuous surjection onto the [[operator-algebras/primitive-ideal-space|primitive ideal space]]. The displayed closure rule says precisely that the topology on \(\widehat G\) is read through the hull-kernel topology on primitive ideals. This description is equivalent to Fell's coefficient-function formulation [Fell, Theorem 2.2 and the group application](https://doi.org/10.1090/S0002-9947-1960-0146681-0).

## The type I distinction

When \(C^*(G)\) is a [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]], \(\kappa\) is bijective and identifies \(\widehat G\) with \(\operatorname{Prim}(C^*(G))\). In general, inequivalent irreducible representations can share a kernel. The kernel description then cannot distinguish them: they have exactly the same neighborhoods and violate the \(T_0\) separation axiom.

**Warning.** Even when the kernel map is bijective, the primitive ideal space and hence the Fell topology need not be Hausdorff. Type I gives a well-behaved parameterization by kernels, not Hausdorff separation.

## How to use the criterion

To prove \([\pi]\in\overline S\), it is enough to show that every element of \(C^*(G)\) annihilated by all representations in \(S\) is also annihilated by \(\pi\). To separate \([\pi]\) from \(\overline S\), one seeks \(a\in C^*(G)\) with \(\rho(a)=0\) for every \([\rho]\in S\) but \(\pi(a)\neq0\).

## References

1. J. M. G. Fell, “The Dual Spaces of \(C^*\)-Algebras,” *Transactions of the American Mathematical Society* 94 (1960), 365–403. [DOI record](https://doi.org/10.1090/S0002-9947-1960-0146681-0). Relevant: Theorem 2.2 and the application to group duals.
2. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: primitive ideals, spectra, and the hull-kernel topology.
