+++
id = "asymptotics/asymptotic-scale"
title = "Asymptotic scale"
kind = "definition"
summary = "An ordered sequence whose successive functions are negligible relative to their predecessors."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/little-o", "shared-foundations/sequence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **asymptotic scale** at \(\varepsilon=0^+\) is a sequence of eventually nonzero scalar functions \((\phi_j)_{j\ge0}\) such that
\[
\phi_{j+1}=o(|\phi_j|)\qquad(\varepsilon\downarrow0)
\]
for every fixed \(j\). Thus the order of the sequence records successively smaller contributions in the sense of [[asymptotics/little-o|little-o]].

## Examples

The powers \(1,\varepsilon,\varepsilon^2,\ldots\) form a scale. So do \(\varepsilon^{a_j}\) for any strictly increasing sequence of real exponents. Scales may also contain logarithms and need not consist of integral powers.

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
