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
projective curve]] over \(k\), and let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
algebraic group]]. The **moduli stack of \(G\)-bundles**,
\(\operatorname{Bun}_G(X)\), assigns to each \(k\)-scheme \(S\) the groupoid
of [[algebraic-geometry-foundations/principal-g-bundle-on-scheme|principal
\(G_S\)-bundles]] on \(X\times_k S\).

Morphisms are bundle isomorphisms, so this construction retains automorphism
groups rather than merely recording isomorphism classes. Under the stated
hypotheses, \(\operatorname{Bun}_G(X)\) is an
[[algebraic-geometry-foundations/algebraic-stack|algebraic stack]] locally of
finite type over \(k\).

## Automorphic role

The automorphic side of de Rham geometric Langlands is built from
[[algebraic-geometry-foundations/d-module|\(D\)-modules]] on
\(\operatorname{Bun}_G(X)\).
[[langlands/hecke-correspondence|Hecke correspondences]] modify a bundle at a
point of \(X\) and define functors on this category.

## Examples and cautions

For \(G=GL_n\), principal \(G\)-bundles are equivalent to rank-\(n\) vector
bundles. For \(G=\mathbb G_m\), \(\operatorname{Bun}_G\) is the Picard stack.
When \(X\) is geometrically connected, its connected components are indexed
by degree.

The notation suppresses the fixed curve. It also suppresses derived
enhancements used in the modern correspondence.

## References

1. Vladimir Drinfeld and Carlos Simpson, “B-structures on G-bundles and
   local triviality,” *Mathematical Research Letters* 2 (1995), 823–829.
   [DOI](https://doi.org/10.4310/MRL.1995.v2.n6.a14).
2. Jochen Heinloth, “Uniformization of \(G\)-bundles,” *Mathematische
   Annalen* 347 (2010), 499–528.
   [DOI](https://doi.org/10.1007/s00208-009-0443-4).
