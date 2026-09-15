+++
id = "harmonic-analysis/kazhdan-property-t"
title = "Kazhdan property (T)"
kind = "definition"
summary = "The property that almost-invariant vectors force a nonzero invariant vector in every unitary representation."
aliases = ["property T", "Kazhdan group"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/almost-invariant-vectors", "harmonic-analysis/invariant-vector", "topology/locally-compact-group"]
+++

A locally compact group \(G\) has **Kazhdan's property \((T)\)** if every strongly continuous unitary representation with [[harmonic-analysis/almost-invariant-vectors|almost-invariant vectors]] has a nonzero invariant vector. Equivalently, there is a compact set \(Q\subseteq G\) and \(\varepsilon>0\) such that any representation having a unit vector \(v\) with \(\sup_{g\in Q}\|\pi(g)v-v\|<\varepsilon\) contains a nonzero invariant vector.

Such \((Q,\varepsilon)\) is a **Kazhdan pair**. For a discrete group, \(Q\) is finite.

## Consequence for Koopman theory

Every ergodic probability-preserving action of a discrete property-\((T)\) group has a [[ergodic-theory/spectral-gap|spectral gap]]. Otherwise its reduced Koopman representation would have almost-invariant vectors, so property \((T)\) would give a nonzero invariant vector, contradicting ergodicity.

The property concerns all unitary representations of the group. A particular action can have a spectral gap even when its group does not have property \((T)\).

## References

1. B. Bekka, P. de la Harpe, and A. Valette, [*Kazhdan’s Property (T)*](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), Definition 1.1.3, Theorem 1.2.1, and §6.3.
