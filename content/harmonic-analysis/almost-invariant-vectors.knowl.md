+++
id = "harmonic-analysis/almost-invariant-vectors"
title = "Almost-invariant vectors"
kind = "definition"
summary = "Unit vectors moved arbitrarily little by each finite or compact set of group elements."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/invariant-vector", "lie-groups/strongly-continuous-unitary-representation"]
+++

A [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] \(\pi\) of a discrete group \(G\) **has almost-invariant vectors** if for every finite \(F\subseteq G\) and every \(\varepsilon>0\), there is a unit vector \(v\) satisfying
\[
\max_{g\in F}\|\pi(g)v-v\|<\varepsilon.
\]
For a strongly continuous representation of a locally compact group, replace finite \(F\) by compact \(Q\) and maximum by supremum.

## The quantifiers matter

The vector can depend on both \(F\) and \(\varepsilon\). An invariant vector supplies all these approximations, but approximating vectors need not converge to a nonzero invariant vector. A spectral gap rules out such approximations on the specified representation space.

## References

1. B. Bekka, P. de la Harpe, and A. Valette, [*Kazhdan’s Property (T)*](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), §1.1.
