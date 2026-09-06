+++
id = "lie-groups/k-type"
title = "K-type"
kind = "definition"
summary = "An irreducible compact-group representation occurring in the restriction of a representation to K."
aliases = ["isotypic K-type", "compact-subgroup type"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["lie-groups/k-finite-vector", "lie-groups/strongly-continuous-unitary-representation", "shared-foundations/equivalence-class", "lie-groups/irreducible-representation-lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(K\) be a compact group and \(V\) a complex \(K\)-representation that is a direct sum of finite-dimensional irreducibles, as happens for the [[lie-groups/k-finite-vector|\(K\)-finite part]] of a [[lie-groups/strongly-continuous-unitary-representation|continuous unitary representation]]. A **\(K\)-type** of \(V\) is an [[shared-foundations/equivalence-class|equivalence class]] \(\tau\) of [[lie-groups/irreducible-representation-lie-group|irreducible finite-dimensional \(K\)-representations]] for which
\[
\operatorname{Hom}_K(E_\tau,V)\neq 0,
\]
where \(E_\tau\) is a representative. Its multiplicity is \(\dim\operatorname{Hom}_K(E_\tau,V)\). The **\(\tau\)-isotypic component** \(V(\tau)\) is the sum of all \(K\)-submodules isomorphic to \(E_\tau\); it is naturally isomorphic to \(E_\tau\otimes\operatorname{Hom}_K(E_\tau,V)\).

## Decomposition

For a unitary representation of \(K\), the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]] gives an orthogonal Hilbert direct sum of isotypic components. Its \(K\)-finite part is the algebraic direct sum
\[
V_K=\bigoplus_{\tau\in\widehat K}V(\tau).
\]
Thus each \(K\)-finite vector involves only finitely many \(K\)-types, although the representation may contain infinitely many types overall.

## Example

For \(K=S^1\), every [[algebra-representation-theory/irreducible-representation|irreducible representation]] is a character \(z\mapsto z^m\), \(m\in\mathbb Z\). Under rotations on \(L^2(S^1)\), the \(m\)-th \(K\)-type is the one-dimensional span of the Fourier mode \(z^m\), and its multiplicity is one. A general compact group can have higher-dimensional irreducible \(K\)-types and multiplicities larger than one.

## Conventions and scope

The phrase “a \(K\)-type” may mean either the equivalence class \(\tau\), a chosen model \(E_\tau\), or the associated isotypic component; context should distinguish them. A \(K\)-type is not an individual vector. In real-reductive theory, \(K\) is normally a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]].

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [DOI record](https://doi.org/10.1515/9781400883974). Relevant: Chapter VIII on \(K\)-types and admissible representations.
2. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 3, especially §3.3.
