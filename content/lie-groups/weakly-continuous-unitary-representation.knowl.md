+++
id = "lie-groups/weakly-continuous-unitary-representation"
title = "Weakly continuous unitary representation"
kind = "definition"
summary = "A unitary representation whose matrix coefficients are continuous functions of the group element."
aliases = ["weakly continuous representation", "matrix-coefficient continuous unitary representation"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["topology/topological-group", "linear-algebra/hilbert-space", "algebra-groups/group-homomorphism", "harmonic-analysis/coefficient-function", "operator-algebras/weak-operator-topology", "lie-groups/weak-strong-continuity-equivalence-unitary-representations", "lie-groups/strongly-continuous-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/topological-group|topological group]] and \(H\) a complex [[linear-algebra/hilbert-space|Hilbert space]]. A [[algebra-groups/group-homomorphism|group homomorphism]]
\[
\pi:G\longrightarrow U(H)
\]
is a **weakly continuous unitary representation** if every [[harmonic-analysis/coefficient-function|matrix coefficient]]
\[
g\longmapsto\langle\pi(g)\xi,\eta\rangle
\]
is continuous for all \(\xi,\eta\in H\). Equivalently, \(\pi\) is continuous when \(U(H)\) carries the [[operator-algebras/weak-operator-topology|weak operator topology]]. By the [[lie-groups/weak-strong-continuity-equivalence-unitary-representations|weak–strong continuity equivalence]], this is equivalent to [[lie-groups/strongly-continuous-unitary-representation|strong continuity]]; no local compactness or separability assumption is needed. Its coefficient functions are therefore continuous complex-valued functions on \(G\).

## Why weak continuity implies strong continuity

Fix \(g_0\in G\) and \(\xi\in H\). Unitarity gives
\[
\|\pi(g)\xi-\pi(g_0)\xi\|^2
=2\|\xi\|^2-2\operatorname{Re}\langle\pi(g)\xi,\pi(g_0)\xi\rangle.
\]
Weak continuity makes the right-hand side tend to zero as \(g\to g_0\). Hence every [[fiber-bundles/orbit-map|orbit map]] \(g\mapsto\pi(g)\xi\) is norm-continuous. Strong continuity plainly implies weak continuity by continuity of the [[linear-algebra/inner-product|inner product]].

## Scope of the equivalence

The equivalence relies on the fixed norm of [[functional-analysis/unitary-operator|unitary operators]]. For general bounded-operator-valued representations, weak-operator continuity need not imply strong-operator continuity without additional assumptions. “Weakly continuous” here refers to weak operator topology, not to the Banach-space weak topology on \(B(H)\) or the ultraweak topology.

## Matrix coefficients

Weak continuity is often convenient because it can be checked through scalar-valued functions. Positive-definite functions arise as diagonal coefficients \(g\mapsto\langle\pi(g)\xi,\xi\rangle\), and polarization recovers all matrix coefficients from diagonal ones. Thus continuity of all diagonal coefficients is another equivalent test.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on unitary representations and continuity of matrix coefficients.
