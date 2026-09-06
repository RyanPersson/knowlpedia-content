+++
id = "differential-geometry/kahler-class"
title = "Kähler class"
kind = "definition"
summary = "The degree-two real de Rham cohomology class represented by a Kähler form."
aliases = ["cohomology class of a Kähler form"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/kahler-form", "fiber-bundles/de-rham-cohomology-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] and let \(\omega\) be a [[differential-geometry/kahler-form|Kähler form]] on \(X\). Since \(d\omega=0\), the form determines a class
\[
[\omega]\in H^2_{\mathrm{dR}}(X;\mathbb R)
\]
in [[fiber-bundles/de-rham-cohomology-group|real de Rham cohomology]]. This class is the **Kähler class** of \(\omega\). A class \(\kappa\in H^2_{\mathrm{dR}}(X;\mathbb R)\) is called a Kähler class if it has at least one representative that is a positive real \((1,1)\)-form. Thus being a Kähler class is stronger than merely having a closed \((1,1)\)-representative: positivity is indispensable.

## Structure and consequences

Kähler forms in the same class differ by an exact real \(2\)-form. On a compact [[differential-geometry/kahler-manifold|Kähler manifold]], the [[differential-geometry/ddbar-lemma|\(\partial\bar\partial\)-lemma]] refines this: two cohomologous Kähler forms differ by \(i\partial\bar\partial\varphi\) for a global real smooth function \(\varphi\), up to the chosen normalization. Positivity is then the open inequality that the modified form must continue to satisfy.

If \(X\) has complex dimension \(n\) and is compact, then
\[
\int_X\omega^n>0,
\]
so \([\omega]^n\neq0\).

## Examples and non-examples

On [[algebraic-geometry-foundations/projective-space|complex projective space]], the Fubini–Study form represents a Kähler class; with the standard integral normalization, it generates \(H^2(\mathbb{CP}^n;\mathbb Z)\). By contrast, the zero class on a positive-dimensional compact complex manifold is not Kähler: if \(\omega=d\eta\), then [[differential-geometry/stokes-theorem|Stokes' theorem]] would give \(\int_X\omega^n=0\), contradicting positivity.

## References

1. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §4, especially Consequence 4.3 and Example 4.4.
