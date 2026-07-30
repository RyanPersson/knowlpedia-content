+++
id = "langlands/ramified-geometric-langlands"
title = "Ramified geometric Langlands"
kind = "definition"
summary = "Geometric Langlands for a pointed curve, with prescribed local singularities on the spectral side and level structure on the automorphic side."
aliases = ["geometric Langlands with ramification", "marked geometric Langlands"]
domains = ["langlands"]
section_mode = "progressive"
+++

Let \((X,D)\) be a
[[algebraic-geometry-foundations/pointed-algebraic-curve|pointed smooth
projective curve]] and set \(U=X\setminus D\). **Ramified geometric
Langlands** replaces unramified \(\widehat G\)-local systems on \(X\) by local
systems on \(U\) with specified
[[langlands/ramification-of-g-local-system|local behavior]] at \(D\). On the
automorphic side, it replaces bare \(G\)-bundles by bundles with compatible
[[langlands/level-structure-on-g-bundle|level structures]] and imposes
corresponding equivariance or character conditions on sheaves.

## Tame examples

For regular-singular local systems, one may prescribe monodromy conjugacy
classes at punctures. Borel or Iwahori level structures are common
automorphic counterparts. The precise correspondence depends on whether
monodromy is semisimple, unipotent, or carries additional residue data.

## Wild examples

Irregular connections require formal types and Stokes data. Their automorphic
counterparts use deeper level structures and character sheaves. “Ramified”
therefore does not specify one category until the local condition at every
marked point has been fixed.

## The projective line

Marked \(\mathbb P^1\) is a central source of examples because punctures
create nontrivial monodromy despite the unmarked sphere being simply
connected. The \(SL_2/PGL_2\) pair-of-pants theorem is one proved tamely
ramified case; it is not the same as unramified geometric Langlands on
\(\mathbb P^1\).

## References

1. David Nadler and Zhiwei Yun, “Geometric Langlands correspondence for
   \(SL(2)\), \(PGL(2)\) over the pair of pants,” *Compositio Mathematica*
   155 (2019), 1835–1942.
   [arXiv](https://arxiv.org/abs/1610.08398).
2. Edward Frenkel and Benedict Gross, “A rigid irregular connection on the
   projective line,” *Annals of Mathematics* 170 (2009), 1469–1512.
   [arXiv](https://arxiv.org/abs/0901.2163).
