+++
id = "algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve"
title = "Moduli stack of G-bundles on a curve"
kind = "definition"
summary = "The algebraic stack Bun_G whose families are principal G-bundles on a fixed curve."
aliases = ["Bun_G", "stack of G-bundles"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth
projective curve]] over \(k\), and let \(G\) be a connected reductive
algebraic group. The **moduli stack of \(G\)-bundles**,
\(\operatorname{Bun}_G(X)\), assigns to each \(k\)-scheme \(S\) the groupoid
of [[algebraic-geometry-foundations/principal-g-bundle-on-scheme|principal
\(G\)-bundles]] on \(X\times S\).

Morphisms are bundle isomorphisms. Consequently
\(\operatorname{Bun}_G(X)\) is an
[[algebraic-geometry-foundations/algebraic-stack|algebraic stack]], rather
than merely the set of isomorphism classes of bundles.

## Automorphic role

The automorphic side of de Rham geometric Langlands is built from
[[algebraic-geometry-foundations/d-module|\(D\)-modules]] on
\(\operatorname{Bun}_G(X)\). Hecke correspondences modify a bundle at a point
of \(X\) and define operators on this sheaf category.

## Examples and cautions

For \(G=GL_n\), objects are rank-\(n\) vector bundles. For \(G=\mathbb G_m\),
\(\operatorname{Bun}_G\) is the Picard stack, whose connected components are
indexed by degree.

The notation suppresses the fixed curve. It also suppresses derived
enhancements used in the modern correspondence.

## References

1. Vladimir Drinfeld and Carlos Simpson, “B-structures on G-bundles and
   local triviality,” *Mathematical Research Letters* 2 (1995), 823–829.
   [DOI](https://doi.org/10.4310/MRL.1995.v2.n6.a14).
