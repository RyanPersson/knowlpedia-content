+++
id = "complex-analysis/mobius-characterization-by-schwarzian"
title = "Möbius characterization by the Schwarzian"
kind = "theorem"
summary = "A locally univalent holomorphic function has zero Schwarzian exactly when it is Möbius."
aliases = ["vanishing Schwarzian characterization", "zero Schwarzian theorem"]
domains = ["complex-analysis", "projective-geometry"]
prerequisites = ["complex-analysis/mobius-transformation", "complex-analysis/schwarzian-derivative", "complex-analysis/schwarzian-chain-rule"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be a connected domain, and let \(f:D\to\widehat{\mathbb C}\) be locally univalent and meromorphic. Then
\[
S(f)=0
\]
if and only if \(f\) is the restriction to \(D\) of a [[complex-analysis/mobius-transformation|Möbius transformation]].

## Proof idea

Every Möbius transformation has zero Schwarzian by direct substitution. Conversely, the differential equation \(S(f)=0\) has local solutions
\[
f(z)=\frac{az+b}{cz+d},
\qquad ad-bc\ne0.
\]
These local Möbius transformations agree on overlaps because they agree with \(f\). Connectedness and the [[complex-analysis/identity-theorem|identity theorem]] therefore produce one Möbius transformation on all of \(D\).

## Relation to equal Schwarzians

Applying this result after passing to a local inverse yields the theorem that [[complex-analysis/equal-schwarzians-differ-by-mobius|two locally univalent maps with equal Schwarzians differ by Möbius postcomposition]].

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
