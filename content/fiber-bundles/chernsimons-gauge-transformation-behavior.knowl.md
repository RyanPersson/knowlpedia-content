+++
id = "fiber-bundles/chernsimons-gauge-transformation-behavior"
title = "Gauge transformation behavior of Chern–Simons forms"
kind = "knowl"
summary = "Under a gauge transformation, a Chern–Simons form changes by an exact term plus a group term, yielding a functional well-defined modulo integers in integral normalizations."
aliases = ["chernsimons-gauge-transformation-behavior", "Gauge transformation behavior of Chern–Simons forms"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/lie-group", "fiber-bundles/principal-connection", "fiber-bundles/curvature", "lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "fiber-bundles/chernsimons-gauge-transformation-behavior.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group a [[fiber-bundles/lie-group|Lie group]] \(G\), and let \(A\) be a [[fiber-bundles/principal-connection|principal connection]] on \(P\) with [[fiber-bundles/curvature|curvature]] \(F_A\). Fix an \(\mathrm{Ad}\)-invariant homogeneous polynomial \(P\) of degree \(k\) on the [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{g}\).

## Statement (name-level, with standard formula)

On a local trivialization (or globally after choosing a trivialization or reference datum), the Chern–Simons \((2k-1)\)-form \(\mathrm{CS}_P(A)\) satisfies
\[
d\,\mathrm{CS}_P(A)=P(F_A),
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]].

Under a gauge transformation \(g\) (locally, a smooth map \(g:U\to G\) in a trivialization), the transformed connection is
\[
A^g = g^{-1}Ag + g^{-1}dg,
\]
and the Chern–Simons form changes by a universal transgression formula of the form
\[
\mathrm{CS}_P(A^g)-\mathrm{CS}_P(A) \;=\; d\,\alpha_P(A,g)\;+\; g^*\eta_P,
\]
where:
- \(\alpha_P(A,g)\) is an explicit \((2k-2)\)-form built from \(A\) and \(g^{-1}dg\), and
- \(\eta_P\) is a closed \((2k-1)\)-form on \(G\) determined by \(P\) (the “group term”), expressed using the [[fiber-bundles/lie-bracket|Lie bracket]] and wedge products on \(\mathfrak{g}\)-valued forms.

Consequences on a closed manifold with the extra data needed to define the Chern–Simons functional (for example, a trivial bundle and a chosen global trivialization): if \(P\) corresponds (via Chern–Weil theory) to an integral characteristic class, then the number
\[
\int_M \mathrm{CS}_P(A)
\]
is invariant under gauge transformations modulo integers (with the conventional \(2\pi\)-normalization built into \(P\)). For a nontrivial bundle, the corresponding global object requires additional differential-cohomological or extension data; the local form alone need not glue to a form on \(M\).

## Examples

1. **Abelian case \(G=\mathrm{U}(1)\) (degree \(k=1\)).**
   Here \(A\) is an ordinary real \(1\)-form (in a trivialization) and gauge transformations act by \(A\mapsto A + d\phi\) for a circle-valued function. The Chern–Simons “form” is just \(A\), and its change is exact, so the integral over a closed loop depends only on the winding of the gauge function.

2. **Three-dimensional Chern–Simons for \(k=2\).**
   When \(k=2\) (so \(\mathrm{CS}_P\) is a \(3\)-form), the group term is the classical \(3\)-form on \(G\) built from \(g^{-1}dg\). In particular, on a trivial bundle with \(A=0\) one has
   \[
   \mathrm{CS}_P(A^g)=g^*\eta_P,
   \]
   and the integral over a closed \(3\)-manifold measures the homotopy class of \(g\) (an integer for integral normalizations).

3. **Gauge invariance modulo integers of the Chern–Simons functional.**
   For compact \(G\) and integral \(P\), the Chern–Simons functional on a closed \((2k-1)\)-manifold is a well-defined element of \(\mathbb{R}/\mathbb{Z}\); different representatives differ by an integer coming from the group term.
