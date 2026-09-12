+++
id = "lie-groups/lattice-in-lie-group"
title = "Lattice in a Lie group"
kind = "definition"
summary = "A discrete subgroup whose homogeneous quotient has finite invariant measure."
aliases = ["Lie-group lattice", "finite-covolume discrete subgroup"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/discrete-subgroup", "harmonic-analysis/haar-measure"]
+++

A **lattice** in a Lie group \(G\) is a [[lie-groups/discrete-subgroup|discrete subgroup]] \(\Gamma\) such that \(\Gamma\backslash G\) admits a nonzero finite \(G\)-invariant Radon measure for the right action. This is the finite-covolume condition; the invariant measure is locally finite and compatible with [[harmonic-analysis/haar-measure|Haar measure]].

## Geometry

For \(G=\operatorname{PSL}_2(\mathbb C)\), finite covolume is equivalent to finite hyperbolic volume of \(\Gamma\backslash\mathbb H^3\). The stabilizer of an interior point is compact, so passing from \(G\) to hyperbolic space preserves finiteness of quotient volume.

## Distinguish the meanings of lattice

The subgroup \(\mathbb Z^n\subseteq\mathbb R^n\) is a familiar example. This definition also covers nonabelian groups; it has no connection with the meet-and-join axioms of an order-theoretic lattice.

## References

1. T. Church, B. Farb, and A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of SL_n O_K*, Example 5.6, p. 31 of the linked version. [Author-hosted paper](https://math.uchicago.edu/~farb/papers/Steinberg2.pdf) Example 5.6 for the Bianchi application.
