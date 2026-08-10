+++
id = "langlands/g-bundle-on-fargues-fontaine-curve"
title = "G-bundle on the Fargues-Fontaine curve"
kind = "knowl"
summary = "A principal G-bundle on a Fargues-Fontaine curve, classified on geometric points by a G-isocrystal."
aliases = ["G-bundle on the Fargues–Fontaine curve", "Fargues G-bundle", "Bun_G on the Fargues-Fontaine curve"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a nonarchimedean local field
\(E\). A **\(G\)-bundle on the Fargues–Fontaine curve** is a principal
\(G\)-bundle on \(X_{S,E}\); equivalently, in Tannakian form, it is an exact
tensor functor

\[
\operatorname{Rep}_E(G)
\longrightarrow
\operatorname{Bun}(X_{S,E}).
\]

As the perfectoid base \(S\) varies, these bundles form a \(v\)-stack
\(\operatorname{Bun}_G\).

## Bundle attached to an isocrystal

For \(b\in G(\breve E)\), every representation
\(\rho:G\to\operatorname{GL}(V)\) gives the isocrystal
\((V\otimes_E\breve E,\rho(b)\sigma)\), hence a [[fiber-bundles/vector-bundle|vector bundle]] on the curve.
The compatible family of these vector bundles defines a \(G\)-bundle
\(\mathcal E_b\). Its isomorphism class depends only on
\([b]\in B(G)\).

## Classification and strata

On geometric points, the assignment

\[
[b]\longmapsto\mathcal E_b
\]

is a bijection from the [[langlands/kottwitz-set-b-g|Kottwitz set \(B(G)\)]]
to \(|\operatorname{Bun}_G|\). The Newton and Kottwitz invariants give a
Harder–Narasimhan stratification

\[
\operatorname{Bun}_G
=
\bigsqcup_{b\in B(G)}\operatorname{Bun}_G^b.
\]

The stratum is a geometric stack, not merely a point; its automorphism
geometry contains the group \(G_b(E)\).

## Semistability

The bundle \(\mathcal E_b\) is semistable exactly when \(b\) is basic,
meaning that its Newton point is central. On the basic stratum, \(G_b\) is
an inner form of \(G\). The trivial class gives the open stratum

\[
\operatorname{Bun}_G^1\simeq [*/G(E)].
\]

This embeds the category of smooth \(G(E)\)-representations into sheaves on
\(\operatorname{Bun}_G\).

## Local Langlands role

[[langlands/hecke-modification|Hecke modifications]] of \(G\)-bundles at untilt divisors implement the
geometric Satake action. The Fargues conjecture and Fargues–Scholze theory
seek to organize sheaves on \(\operatorname{Bun}_G\) by
[[langlands/stack-of-l-parameters|local \(L\)-parameters]].

## References

1. Laurent Fargues, “\(G\)-torseurs en théorie de Hodge
   \(p\)-adique,” *Compositio Mathematica* 156 (2020), 2076–2110.
   [DOI](https://doi.org/10.1112/S0010437X20007317).
2. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Chapter III.
   [arXiv](https://arxiv.org/abs/2102.13459).
