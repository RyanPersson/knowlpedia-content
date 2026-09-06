+++
id = "langlands-letter/knowls/nonabelian-h1-galois-cohomology"
title = "Nonabelian H1 and Galois 1-cocycles"
kind = "definition"
summary = "The pointed set of continuous Galois 1-cocycles modulo twisted conjugacy."
aliases = ["nonabelian-h1-galois-cohomology", "Nonabelian \\(H^1(\\Gamma,G)\\) and 1-Cocycles"]
domains = ["langlands-letter"]
prerequisites = ["langlands/twisted-conjugacy", "shared-foundations/pointed-set"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/nonabelian-h1-galois-cohomology.md"
section_mode = "progressive"
+++

Let a group \(\Gamma\) act on a group \(A\). A **nonabelian
\(1\)-cocycle** is a map \(z:\Gamma\to A\) satisfying

\[
z_{\sigma\tau}
=
z_\sigma\,{}^\sigma z_\tau.
\]

Two cocycles are cohomologous when they differ by
[[langlands/twisted-conjugacy|twisted conjugacy]]:

\[
z'_\sigma
=
a^{-1}z_\sigma\,{}^\sigma a
\]

for some \(a\in A\). Their classes form the [[shared-foundations/pointed-set|pointed set]]

\[
H^1(\Gamma,A),
\]

whose basepoint is the trivial cocycle. Unless \(A\) is abelian, this is not
naturally a group.

## Galois form

For an algebraic \(k\)-group \(G\), one writes

\[
H^1(k,G)
=
H^1(\Gamma_k,G(k_s)),
\]

using continuous cocycles for the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]].
It classifies
[[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsors]] over
\(k\) up to
isomorphism. If \(K/k\) is finite Galois, then
\(H^1(\operatorname{Gal}(K/k),G(K))\) records torsors split by \(K\).

## Forms require a different coefficient group

[[langlands-letter/knowls/galois-descent-forms|Forms of \(G\)]] are
classified by \(H^1(k,\operatorname{Aut}(G_{k_s}))\).
Inner forms come from \(H^1(k,G_{\mathrm{ad}})\), while a pure inner twist
uses a lift in \(Z^1(k,G)\). Suppressing the coefficient group loses the
mathematical content.

## Stable conjugacy

For a [[langlands/strongly-regular-semisimple-element|strongly regular semisimple]] \(\gamma\) with torus centralizer
[[algebra-groups/centralizer|\(G_\gamma\)]], rational
[[algebra-groups/conjugacy-class|conjugacy classes]] inside its
[[langlands/stable-conjugacy|stable class]] are
parametrized by

\[
\ker\!\left[
H^1(k,G_\gamma)\to H^1(k,G)
\right].
\]

This is the cohomological obstruction whose Fourier analysis leads to
[[langlands/endoscopic-datum|endoscopy]] and
[[langlands/kappa-orbital-integral|\(\kappa\)-orbital integrals]].

## Relation to the letter

The letter's inner twisting is a class in the appropriate inner
[[algebra-groups/automorphism-group|automorphism group]]. “Locally trivial at almost all places” means that its
restriction to the corresponding local cohomology sets is the basepoint.

## References

1. Jean-Pierre Serre, *Galois Cohomology*, Springer, 1997.
2. Robert E. Kottwitz, “Stable trace formula: cuspidal tempered terms,”
   *Duke Mathematical Journal* 51 (1984), 611–650.
