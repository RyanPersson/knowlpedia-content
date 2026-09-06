+++
id = "lie-groups/discrete-series-representation"
title = "Discrete series representation"
kind = "definition"
summary = "An irreducible unitary representation occurring as a closed subrepresentation of the left regular representation."
aliases = ["square-integrable representation"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "lie-groups/irreducible-unitary-representation", "shared-foundations/equivalence-class", "lie-groups/invariant-closed-subspace-unitary-representation", "harmonic-analysis/regular-representations-locally-compact-group", "algebra-representation-theory/regular-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a second-countable [[topology/locally-compact-group|locally compact group]] with left [[harmonic-analysis/haar-measure|Haar measure]]. A **discrete series representation** of \(G\) is an [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] whose [[shared-foundations/equivalence-class|equivalence class]] occurs as a [[lie-groups/invariant-closed-subspace-unitary-representation|closed \(G\)-invariant subspace]] of the [[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]] on \(L^2(G)\). Equivalently, it is an irreducible summand in the discrete part of that [[algebra-representation-theory/regular-representation|regular representation]]. The word “discrete” describes its occurrence as a Hilbert direct summand, not discreteness of the group, the representation space, or its parameter set.

## Coefficient criterion

When \(G\) is unimodular, \(\pi\) belongs to the discrete series exactly when it has a nonzero [[harmonic-analysis/coefficient-function|matrix coefficient]] in \(L^2(G)\). Irreducibility then yields square integrability and Schur orthogonality for all coefficients, with a positive formal degree depending on the normalization of Haar measure. This characterization explains the common alternative name “square-integrable representation.”

## Examples and existence

Every irreducible unitary representation of a compact group is discrete series after Haar measure is normalized. For connected semisimple real [[fiber-bundles/lie-group|Lie groups]] with finite center, Harish-Chandra's criterion says that discrete series exists exactly when the group has a compact Cartan subgroup, equivalently when its rank equals the rank of a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]].

## Relationship to relative discrete series

If the center is noncompact, central characters make a nonzero coefficient constant in modulus along central cosets, obstructing membership in \(L^2(G)\). The corresponding notion is then a [[lie-groups/square-integrable-modulo-center-representation|square-integrable representation modulo the center]]. Neither notion should be confused with the discrete spectrum of an automorphic quotient, where occurrence is measured in a different \(L^2\)-representation.

## References

1. Michel Duflo and Calvin C. Moore, *On the regular representation of a nonunimodular locally compact group*, Journal of Functional Analysis 21 (1976), 209–243. [DOI record](https://doi.org/10.1016/0022-1236%2876%2990079-3). Relevant: introduction and §§2–3 on the discrete part, square-integrable representations, and orthogonality operators.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained book record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XII on Harish-Chandra's discrete series.
