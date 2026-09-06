+++
id = "langlands/kottwitz-set-b-g"
title = "Kottwitz set B(G)"
kind = "knowl"
summary = "The set of Frobenius-conjugacy classes in a reductive group over the completed maximal unramified extension."
aliases = ["Kottwitz set", "sigma-conjugacy classes in G", "G-isocrystals"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "langlands-letter/knowls/unramified-extension-local", "langlands-letter/knowls/frobenius-unramified", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/twisted-conjugacy", "shared-foundations/pointed-set"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(\breve E\) be the completion of its maximal
[[langlands-letter/knowls/unramified-extension-local|unramified extension]],
and let \(\sigma\) be
[[langlands-letter/knowls/frobenius-unramified|Frobenius]]. For a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(E\)-group]] \(G\), the **Kottwitz set**

\[
B(G)=G(\breve E)/{\sim_\sigma}
\]

is the set of
[[langlands/twisted-conjugacy|\(\sigma\)-conjugacy classes]], where

\[
b'\sim_\sigma b
\quad\Longleftrightarrow\quad
b'=g\,b\,\sigma(g)^{-1}
\]

for some \(g\in G(\breve E)\).

It is a [[shared-foundations/pointed-set|pointed set]], not generally a group.

## Newton and Kottwitz invariants

A class \([b]\) has two principal invariants:

\[
\nu_b\in
\left(X_*(T)_\mathbb Q^+\right)^\Gamma,
\qquad
\kappa_G(b)\in\pi_1(G)_\Gamma.
\]

Here \(X_*(T)\) is the
[[langlands-letter/knowls/maximal-torus-weight-lattice|cocharacter lattice]]
of a maximal torus and \(\Gamma\) is the relevant
[[langlands-letter/knowls/galois-extension-and-group|Galois group]]. The
Newton point records slopes, while the Kottwitz invariant is the
generalized degree. Their compatible pair determines \([b]\); more
precisely, the map \((\nu,\kappa)\) is injective with a characterized image.

For \(G=\operatorname{GL}_n\), \(B(G)\) is the set of isomorphism classes of
rank-\(n\) [[algebraic-geometry-foundations/isocrystal|isocrystals]],
\(\nu_b\) is the Newton-slope polygon, and
\(\kappa_G(b)\) is its endpoint.

## Basic classes

A class is **basic** when \(\nu_b\) is central. The associated group

\[
G_b(R)=
\{g\in G(R\otimes_E\breve E):
g\,b=b\,\sigma(g)\}
\]

is then an
[[langlands-letter/knowls/galois-descent-forms|inner form]] of \(G\). Basic
classes correspond to
[[algebraic-geometry-foundations/harder-narasimhan-filtration|semistable]]
\(G\)-bundles on the
[[langlands/fargues-fontaine-curve|Fargues–Fontaine curve]].

## Bundle classification

The Fargues construction assigns to \(b\) a
[[langlands/g-bundle-on-fargues-fontaine-curve|\(G\)-bundle
\(\mathcal E_b\)]]. On geometric points this gives a bijection

\[
B(G)\xrightarrow{\sim}|\operatorname{Bun}_G|.
\]

The Newton [[shared-foundations/partial-order|partial order]] becomes the specialization order among bundle
strata.

## References

1. Robert E. Kottwitz, “Isocrystals with additional structure II,”
   *Compositio Mathematica* 109 (1997), 255–339.
   [Numdam](https://www.numdam.org/item/CM_1997__109_3_255_0/).
2. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” §§I.4 and III.2.
   [arXiv](https://arxiv.org/abs/2102.13459).
