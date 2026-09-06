+++
id = "complex-analysis/complex-projective-structure"
title = "Complex projective structure"
kind = "definition"
summary = "An atlas of local coordinates in the Riemann sphere whose transition maps are Möbius."
aliases = ["holomorphic projective structure", "CP1-structure"]
domains = ["complex-analysis", "differential-geometry", "projective-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemann-surface", "differential-geometry/complex-atlas", "complex-analysis/mobius-transformation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[differential-geometry/riemann-surface|Riemann surface]]. A **complex projective structure** on \(X\) is a maximal atlas of charts
\[
\varphi_\alpha:U_\alpha\longrightarrow
\varphi_\alpha(U_\alpha)\subseteq\mathbb P^1(\mathbb C)
\]
such that every transition map
\[
\varphi_\beta\circ\varphi_\alpha^{-1}
\]
is locally the restriction of a [[complex-analysis/mobius-transformation|Möbius transformation]] wherever it is defined.

## Underlying complex structure

Möbius transformations are biholomorphic, so a complex projective atlas is in particular a [[differential-geometry/complex-atlas|complex atlas]]. Thus a projective structure refines the complex structure of \(X\); it is extra data, not merely the assertion that \(X\) is a Riemann surface.

## Developing map and holonomy

Analytically continuing projective charts on the universal cover produces a locally biholomorphic developing map
\[
\operatorname{dev}:\widetilde X\to\mathbb P^1(\mathbb C)
\]
and a [[fiber-bundles/holonomy-representation|holonomy representation]]
\[
\rho:\pi_1(X)\to PGL_2(\mathbb C)
\]
for which \(\operatorname{dev}(\gamma x)=\rho(\gamma)\operatorname{dev}(x)\). The pair is defined only up to simultaneous postcomposition and conjugation by a Möbius transformation.

## Associated projective connection

Taking the [[complex-analysis/schwarzian-derivative|Schwarzian derivative]] of projective charts in an ordinary holomorphic coordinate produces a [[complex-analysis/projective-connection|holomorphic projective connection]].

## References

1. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective structures and projective connections.
2. William M. Goldman, “Projective structures with Fuchsian holonomy,” *Journal of Differential Geometry* 25 (1987), 297–326. [Project Euclid record](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-25/issue-3/Projective-structures-with-Fuchsian-holonomy/10.4310/jdg/1214440985.full). Relevant: developing maps and holonomy.
