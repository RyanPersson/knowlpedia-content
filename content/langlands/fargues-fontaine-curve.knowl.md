+++
id = "langlands/fargues-fontaine-curve"
title = "Fargues-Fontaine curve"
kind = "knowl"
summary = "A one-dimensional curve built from a local field and a perfectoid characteristic-p space, translating isocrystals into vector bundles."
aliases = ["Fargues–Fontaine curve", "Fargues Fontaine curve", "adic Fargues-Fontaine curve"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
section_mode = "progressive"
+++

Let \(E\) be a nonarchimedean local field with [[algebra-commutative/residue-field|residue field]]
\(\mathbb F_q\), and let \(S\) be a perfectoid space over \(\mathbb F_q\).
The relative **Fargues–Fontaine curve** \(X_{S,E}\) is the quotient

\[
X_{S,E}=Y_{S,E}/\varphi^{\mathbb Z},
\]

where \(Y_{S,E}\) is a punctured adic space built from relative ramified
Witt vectors of \(S\), and \(\varphi\) is the Frobenius automorphism. The
Frobenius action on the relevant punctured locus is free and properly
discontinuous.

## Geometric case

For \(S=\operatorname{Spa}(C^\flat,C^{\flat+})\), where \(C\) is an
[[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]] perfectoid field containing \(E\), one obtains the
curve \(X_{C^\flat,E}\). Its algebraic avatar is a regular noetherian
one-dimensional scheme. Degree-one [[algebraic-geometry-foundations/closed-point|closed points]] encode untilts of
\(C^\flat\) to characteristic \(0\), together with an embedding of \(E\).

## Vector bundles and isocrystals

An isocrystal \((D,\varphi_D)\) over the completed maximal unramified
extension of \(E\) produces a [[fiber-bundles/vector-bundle|vector bundle]] \(\mathcal E(D,\varphi_D)\) on
the curve. Over an algebraically closed perfectoid base, every vector bundle
decomposes uniquely into slope bundles

\[
\bigoplus_{\lambda\in\mathbb Q}
\mathcal O(\lambda)^{\oplus m_\lambda}.
\]

This is the Fargues–Fontaine classification and is the curve-level analogue
of Dieudonné–Manin slope theory.

## Langlands role

The stack \(\operatorname{Bun}_G\) of \(G\)-bundles on relative
Fargues–Fontaine curves is the automorphic space in the geometrization of
local Langlands. Its geometric points are indexed by the
[[langlands/kottwitz-set-b-g|Kottwitz set \(B(G)\)]]. Modifications at
untilt divisors define local [[langlands/hecke-correspondence|Hecke correspondences]] and
[[langlands/local-shtuka|local shtuka spaces]].

## References

1. Laurent Fargues and Jean-Marc Fontaine, *Courbes et fibrés vectoriels en
   théorie de Hodge \(p\)-adique*, Astérisque 406, 2018.
   [Numdam](https://www.numdam.org/item/AST_2018__406__1_0/).
2. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Chapters II–III.
   [arXiv](https://arxiv.org/abs/2102.13459).
