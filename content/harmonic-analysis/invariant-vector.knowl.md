+++
id = "harmonic-analysis/invariant-vector"
title = "Invariant vector of a unitary representation"
kind = "definition"
summary = "A vector fixed by every represented group element."
aliases = ["fixed vector of a representation"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["algebra-representation-theory/group-representation", "functional-analysis/unitary-operator"]
+++

For a [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] \(\pi:G\to\mathcal U(H)\), an **invariant vector** is \(v\in H\) with \(\pi(g)v=v\) for every \(g\in G\). The invariant subspace is
\[
H^G=\bigcap_{g\in G}\ker(\pi(g)-I).
\]
It is closed, and its orthogonal complement is invariant.

## Fixed vector versus invariant subspace

An invariant line may transform by a nontrivial character and contain no nonzero invariant vector. For Koopman representations, constants always form a trivial subrepresentation; ergodicity says the orthogonal complement of constants contains no invariant vector.
