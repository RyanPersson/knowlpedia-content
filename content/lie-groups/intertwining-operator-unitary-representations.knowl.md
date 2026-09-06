+++
id = "lie-groups/intertwining-operator-unitary-representations"
title = "Intertwining operator between unitary representations"
kind = "definition"
summary = "A bounded linear operator commuting with the actions of a group on two Hilbert spaces."
aliases = ["intertwiner", "equivariant bounded operator"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "functional-analysis/bounded-linear-operator", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((\pi,\mathcal H_\pi)\) and \((\sigma,\mathcal H_\sigma)\) be [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representations]] of the same group \(G\). An **intertwining operator** from \(\pi\) to \(\sigma\) is a [[functional-analysis/bounded-linear-operator|bounded linear operator]] \(T:\mathcal H_\pi\to\mathcal H_\sigma\) satisfying
\[
T\pi(g)=\sigma(g)T\qquad\text{for every }g\in G.
\]
The [[linear-algebra/vector-space|vector space]] of all such operators is denoted \(\operatorname{Hom}_G(\pi,\sigma)\). Boundedness is part of the Hilbert-representation definition; an everywhere-defined algebraic operator satisfying the displayed identity need not be continuous.

## Basic properties

Intertwiners compose, identity operators intertwine a representation with itself, and the adjoint \(T^*\) intertwines \(\sigma\) with \(\pi\). The kernel of \(T\) and the closure of its range are invariant closed subspaces. Consequently, intertwiners are the morphisms in the category of unitary representations with bounded [[fiber-bundles/equivariant-map|equivariant maps]].

## Equivalence and irreducibility

A unitary intertwiner that is onto exhibits **unitary equivalence** of the two representations. For irreducible complex unitary representations, a nonzero intertwiner is a scalar multiple of a unitary equivalence; in particular, the commutant \(\operatorname{Hom}_G(\pi,\pi)\) consists of scalars. This is the Hilbert-space form of [[algebra-representation-theory/schurs-lemma|Schur's lemma]], using polar decomposition and closed invariant subspaces.

## Conventions and scope

In smooth or distribution representation theory, “intertwining operator” may mean a [[topology/continuous-map|continuous map]] for a locally convex topology, or a densely defined unbounded operator with an invariant domain. Those notions require the topology or domain to be stated and are not covered by this bounded Hilbert-space definition.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on intertwiners, equivalence, and irreducibility.
