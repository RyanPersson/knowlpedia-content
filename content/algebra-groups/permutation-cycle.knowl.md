+++
id = "algebra-groups/permutation-cycle"
title = "Cycle of a permutation"
kind = "definition"
summary = "A cyclic orbit in the disjoint-cycle decomposition of a finite permutation."
aliases = ["disjoint cycle decomposition", "n-cycle"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["shared-foundations/finite-permutation", "algebra-groups/orbit"]
+++

A **cycle** \((a_1\ a_2\ \cdots\ a_r)\) is the [[shared-foundations/finite-permutation|permutation]] sending \(a_j\) to \(a_{j+1}\), \(a_r\) to \(a_1\), and fixing all other elements. Its support is one orbit of length \(r\). Every finite permutation is a product of cycles with disjoint supports, uniquely up to the order of the cycles and cyclic rotation of each notation.

## Single-cycle permutations

An \(n\)-cycle on an \(n\)-point set is transitive: every point lies in the same orbit. There are \((n-1)!\) such permutations, obtained by fixing one starting element and ordering the remaining elements around the cycle.

These are precisely the [[ergodic-theory/finite-uniform-system|ergodic permutations for uniform probability]]. For \(n=1\), the identity is the one-cycle and the system is ergodic.
