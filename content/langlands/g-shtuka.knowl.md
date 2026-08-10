+++
id = "langlands/g-shtuka"
title = "G-shtuka"
kind = "knowl"
summary = "A principal G-bundle on a curve with a Frobenius identification away from bounded modification legs."
aliases = ["G-chtouca", "G-shtukas", "global G-shtuka", "multiple-leg G-shtuka"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
section_mode = "progressive"
+++

Let \(X/\mathbb F_q\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]], let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], and let \(I\) be a finite set. A **\(G\)-shtuka with legs
\((x_i)_{i\in I}\)** over \(S\) consists of a \(G\)-bundle \(\mathcal G\) on
\(X\times S\) and an isomorphism

\[
\varphi:
\mathcal G\big|_{(X\times S)\setminus\bigcup_{i\in I}\Gamma_{x_i}}
\xrightarrow{\ \sim\ }
{}^\tau\mathcal G
\big|_{(X\times S)\setminus\bigcup_{i\in I}\Gamma_{x_i}},
\qquad
{}^\tau\mathcal G=({\rm id}_X\times{\rm Frob}_S)^*\mathcal G,
\]

whose relative position at each leg is bounded by prescribed dominant
coweight data.

## Level and boundedness data

A level structure along a finite subscheme \(N\subset X\), disjoint from the
legs, trivializes the bundle compatibly with \(\varphi\). If a representation
\(W\) of \(\widehat G^I\) is used instead of a tuple of coweights, geometric
Satake supplies the corresponding bound and intersection complex.

Because the stack is generally not of finite type, one also uses
Harder–Narasimhan truncations and a quotient by a lattice in the adelic
center.

## Iterated modifications

For an ordered partition \(I=I_1\sqcup\cdots\sqcup I_k\), the Frobenius
isomorphism can be factored as a chain

\[
\mathcal G_0\dashrightarrow\mathcal G_1
\dashrightarrow\cdots\dashrightarrow
\mathcal G_k={}^\tau\mathcal G_0,
\]

where the \(j\)-th modification occurs at the legs in \(I_j\). This form
defines [[langlands/partial-frobenius-on-shtukas|partial Frobenius]]
operations.

## Cohomological structure

The intersection cohomology of stacks of bounded \(G\)-shtukas carries
commuting Hecke and partial-Frobenius actions. Fusion or
[[langlands/coalescence-of-shtuka-legs|coalescence]] identifies the
cohomology when legs merge. These operations provide the creation,
Galois-action, and annihilation maps used in [[langlands/excursion-operator|excursion operators]].

## References

1. Yakov Varshavsky, “Moduli spaces of principal \(F\)-bundles,” *Selecta
   Mathematica* 10 (2004), 131–166.
   [DOI](https://doi.org/10.1007/s00029-004-0383-0).
2. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” Definitions 0.2 and 0.6.
   [arXiv](https://arxiv.org/abs/1209.5352).
