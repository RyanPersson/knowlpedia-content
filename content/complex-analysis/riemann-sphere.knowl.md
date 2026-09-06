+++
id = "complex-analysis/riemann-sphere"
title = "Riemann sphere"
kind = "definition"
summary = "The extended complex plane as a compact Riemann surface, analytically equal to the complex projective line."
aliases = ["extended complex plane", "complex projective line as a Riemann surface", "CP1"]
domains = ["complex-analysis", "differential-geometry", "projective-geometry"]
prerequisites = ["differential-geometry/complex-atlas", "differential-geometry/riemann-surface"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **Riemann sphere** is the one-point compactification
\[
\widehat{\mathbb C}=\mathbb C\cup\{\infty\}
\]
equipped with the [[differential-geometry/complex-atlas|complex atlas]] whose coordinate near finite points is \(z\) and whose coordinate near \(\infty\) is \(w=1/z\). It is a compact [[differential-geometry/riemann-surface|Riemann surface]] analytically isomorphic to the complex projective line \(\mathbb P^1(\mathbb C)\).

## Projective description

The point \([z_0:z_1]\in\mathbb P^1(\mathbb C)\) corresponds to \(z=z_0/z_1\) when \(z_1\ne0\), while \([1:0]\) corresponds to \(\infty\). The two affine charts are related by \(w=1/z\). This is the analytic form of the [[algebraic-geometry-foundations/projective-line|projective line]], not a replacement for its scheme-theoretic structure.

## Topological sphere

Stereographic projection identifies \(\widehat{\mathbb C}\) homeomorphically, indeed conformally, with the round sphere \(S^2\). Neighborhoods of \(\infty\) correspond to complements of compact subsets of \(\mathbb C\), realizing the [[topology/one-point-compactification|one-point compactification]] topology.

## Functions and symmetry

Holomorphic automorphisms of the sphere are exactly [[complex-analysis/mobius-transformation|Möbius transformations]]. A [[complex-analysis/meromorphic-function|meromorphic function]] on a plane domain is equivalently a holomorphic map into \(\widehat{\mathbb C}\), with poles sent to \(\infty\).

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§2 and 8.
