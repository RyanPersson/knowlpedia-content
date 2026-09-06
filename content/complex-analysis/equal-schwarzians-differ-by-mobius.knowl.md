+++
id = "complex-analysis/equal-schwarzians-differ-by-mobius"
title = "Equal Schwarzians differ by Möbius postcomposition"
kind = "theorem"
summary = "Two locally univalent maps on a connected domain have the same Schwarzian exactly when one is a Möbius postcomposition of the other."
aliases = ["equal-Schwarzian theorem"]
domains = ["complex-analysis", "projective-geometry"]
section_mode = "progressive"
prerequisites = ["complex-analysis/mobius-transformation", "complex-analysis/mobius-characterization-by-schwarzian", "complex-analysis/schwarzian-chain-rule"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(D\subseteq\mathbb C\) be a connected domain, and let \(f,g:D\to\widehat{\mathbb C}\) be locally univalent meromorphic maps. Then
\[
S(f)=S(g)
\]
if and only if there is a [[complex-analysis/mobius-transformation|Möbius transformation]] \(T\) such that
\[
f=T\circ g
\]
on \(D\).

## Proof

The reverse implication follows from the [[complex-analysis/schwarzian-chain-rule|Schwarzian chain rule]] and \(S(T)=0\). For the forward implication, choose a local inverse of \(g\). The chain rule shows that \(f\circ g^{-1}\) has zero Schwarzian, so the [[complex-analysis/mobius-characterization-by-schwarzian|vanishing-Schwarzian characterization]] makes it locally Möbius. The local Möbius transformations agree on overlaps and therefore give one \(T\) on the connected domain.

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
