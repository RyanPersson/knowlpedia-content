+++
id = "algebraic-geometry-foundations/smooth-projective-curve"
title = "Smooth projective curve"
kind = "definition"
summary = "A smooth one-dimensional projective scheme over a field, the standard global base for geometric Langlands."
aliases = ["smooth projective algebraic curve"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraic-curve", "algebraic-geometry-foundations/smooth-morphism", "algebraic-geometry-foundations/projective-morphism", "algebraic-geometry-foundations/projective-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **smooth projective curve** over a field \(k\) is an
[[algebraic-geometry-foundations/algebraic-curve|algebraic curve]] \(X\) whose
structure morphism \(X\to\operatorname{Spec}k\) is smooth and which admits a
closed immersion into some [[algebraic-geometry-foundations/projective-space|projective space]] over \(k\). Equivalently, its
structure morphism is both
[[algebraic-geometry-foundations/smooth-morphism|smooth]] of relative
dimension \(1\) and
[[algebraic-geometry-foundations/projective-morphism|projective]].

In the geometric Langlands setting one commonly assumes that \(k\) is
[[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]] of characteristic \(0\) and that \(X\) is connected. The
automorphic stack [[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|\(\operatorname{Bun}_G(X)\)]]
and the spectral stack of
[[langlands/g-local-system|\(\widehat G\)-local systems]] both depend on this
curve.

## Complex-analytic picture

For \(k=\mathbb C\), every connected component of \(X(\mathbb C)\) is a
compact [[differential-geometry/riemann-surface|Riemann surface]]. If \(X\) is connected, then \(X(\mathbb C)\) is a
compact connected Riemann surface. The algebraic, analytic, Betti, and de
Rham formulations are related but are not literally the same categories
without comparison theorems.

## References

1. Jean-Pierre Serre, “Géométrie algébrique et géométrie analytique,”
   *Annales de l’Institut Fourier* 6 (1956), 1–42.
   [DOI](https://doi.org/10.5802/aif.59).
