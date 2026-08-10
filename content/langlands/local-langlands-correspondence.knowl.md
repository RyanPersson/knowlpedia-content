+++
id = "langlands/local-langlands-correspondence"
title = "Basic local Langlands correspondence"
kind = "knowl"
summary = "The finite-to-one parameterization of irreducible admissible representations by relevant local L-parameters."
aliases = ["local Langlands correspondence", "local Langlands conjecture", "basic LLC"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(F\) be a local field and \(G\) a connected reductive \(F\)-group. The
**basic local Langlands correspondence** predicts a surjective finite-to-one
map

\[
\operatorname{Irr}(G(F))
\longrightarrow
\Phi(G),
\qquad
\pi\longmapsto\varphi_\pi,
\]

from [[shared-foundations/equivalence-class|equivalence classes]] of irreducible admissible representations of \(G(F)\)
to \(\widehat G\)-conjugacy classes of relevant
[[langlands/local-l-parameter|local \(L\)-parameters]]. The finite fiber

\[
\Pi_\varphi(G)=
\{\pi\in\operatorname{Irr}(G(F)):\varphi_\pi=\varphi\}
\]

is the [[langlands/l-packet|\(L\)-packet]] of \(\varphi\).

## Status

This is a theorem for archimedean [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]], tori, and
\(\operatorname{GL}_n\), and it is established with refined structures for
many classical groups and numerous other families. For a general reductive
group over a nonarchimedean field, the full basic and refined statements remain
partly conjectural.

General constructions due to Genestier–Lafforgue and Fargues–Scholze attach
semisimplified parameters in broad settings. Questions such as surjectivity,
packet finiteness, recovery of monodromy, and all expected character identities
must still be distinguished from the existence of that semisimplified map.

## Structural requirements

A correspondence is not characterized by cardinality alone. It is expected to
respect unramified [[langlands/satake-parameter|Satake parameters]], central characters, twists,
contragredients, temperedness, parabolic induction, local \(L\)- and
\(\varepsilon\)-factors where defined, and endoscopic character identities.
The [[langlands/refined-local-langlands-correspondence|refined
correspondence]] supplies the internal structure of each packet.

## Basic examples

For a torus, packets are singletons and the correspondence is local class
field theory in dual-group form. For \(\operatorname{GL}_n\), packets are also
singletons, but the parameter is an \(n\)-dimensional Weil–Deligne
representation.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §§2.1–2.3, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. Michael Harris, “On the local Langlands correspondence,” 2003.
   [arXiv](https://arxiv.org/abs/math/0304324).
3. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” 2021. [arXiv](https://arxiv.org/abs/2102.13459).
