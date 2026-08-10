+++
id = "langlands/local-shtuka"
title = "Local shtuka"
kind = "knowl"
summary = "A bounded Frobenius modification of G-bundles in local or Fargues-Fontaine geometry."
aliases = ["local G-shtuka", "moduli space of local shtukas", "p-adic shtuka"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
section_mode = "progressive"
+++

In the Fargues–Fontaine formulation, a **local \(G\)-shtuka** is a
[[algebra-fields-galois/frobenius-endomorphism|Frobenius-compatible]]
[[langlands/hecke-modification|modification]] of \(G\)-bundles at one or
more [[algebraic-geometry-foundations/tilt-and-untilt|untilt divisors]], with
relative positions bounded by specified
[[algebra-groups/conjugacy-class|conjugacy classes]] of
[[langlands-letter/knowls/maximal-torus-weight-lattice|cocharacters]].

A typical moduli space

\[
\operatorname{Sht}(G,b,\mu_\bullet)_K
\]

parametrizes a modification from the
[[langlands/g-bundle-on-fargues-fontaine-curve|bundle \(\mathcal E_b\)]]
to the trivial \(G\)-bundle, bounded at its legs by
\(\mu_\bullet=(\mu_i)\), together with a \(K\)-level trivialization, where
\(K\subset G(E)\) is
[[topology/locally-profinite-group|compact open]].

## Geometric data

Equivalently, on the Frobenius cover \(Y_{S,E}\), one describes a
[[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor]] with an
isomorphism to its Frobenius pullback away from the
leg divisors. Quotienting by Frobenius translates this into modifications
of bundles on the [[langlands/fargues-fontaine-curve|Fargues–Fontaine
curve]].

Multiple legs and ordered modifications give convolution versions. A
period map sends the moduli space to a twisted [[langlands/affine-grassmannian|affine Grassmannian]] bounded
by the cocharacters.

## Group actions

The tower over varying \(K\) carries commuting actions associated to
\(G(E)\), the self-quasi-isogeny group \(G_b(E)\), and [[langlands/weil-group|Weil groups]] of the
reflex fields of the legs. Its
[[algebraic-geometry-foundations/compactly-supported-etale-cohomology|compactly
supported cohomology]] therefore
produces representations on both the automorphic and Galois sides.

## Special cases

For one minuscule leg and suitable local Shimura data, these spaces recover
[[langlands/local-shimura-variety|local Shimura varieties]], including
[[langlands/rapoport-zink-space|Rapoport–Zink spaces]]. General local shtuka
spaces allow arbitrary
cocharacter bounds and several legs.

## Terminology boundary

Equal-characteristic local \(G\)-shtukas can also be defined using loop
groups over formal discs. The displayed Fargues–Fontaine definition is the
mixed/equal-characteristic geometric framework used by
Fargues–Scholze; it should not be confused with a global
[[langlands/g-shtuka|\(G\)-shtuka]] on a projective curve.

## References

1. Peter Scholze and Jared Weinstein, *Berkeley Lectures on \(p\)-adic
   Geometry*, Chapter 23, 2020.
   [AMS](https://bookstore.ams.org/ams-207).
2. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” §§I.7 and IX.3.
   [arXiv](https://arxiv.org/abs/2102.13459).
