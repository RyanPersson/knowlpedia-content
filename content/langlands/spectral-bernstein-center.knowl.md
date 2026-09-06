+++
id = "langlands/spectral-bernstein-center"
title = "Spectral Bernstein center"
kind = "knowl"
summary = "The ring of global functions on the stack of local Langlands parameters."
aliases = ["stable Bernstein center on the spectral side", "spectral center", "Z_spec"]
domains = ["langlands", "representation-theory", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/nonarchimedean-local-field", "langlands/stack-of-l-parameters"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\) over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] \(E\) and a
coefficient ring \(\Lambda\), the **spectral Bernstein center** is

\[
Z_{\mathrm{spec}}(G,\Lambda)
=
\Gamma\!\left(
[Z^1(W_E,\widehat G)_\Lambda/\widehat G],
\mathcal O
\right),
\]

the ring of global functions on the
[[langlands/stack-of-l-parameters|stack of local \(L\)-parameters]].

## Comparison with the ordinary center

The ordinary [[harmonic-analysis/bernstein-center|Bernstein center]]
\(Z(G(E),\Lambda)\) is the center of the category of
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth
\(G(E)\)-representations]], equivalently the
endomorphisms of its identity functor. Fargues–Scholze construct, under
their coefficient hypotheses, a canonical [[algebra-modules/algebra-homomorphism|algebra homomorphism]]

\[
\Psi_G:
Z_{\mathrm{spec}}(G,\Lambda)
\longrightarrow
Z(G(E),\Lambda).
\]

Evaluating the image on an [[algebra-representation-theory/irreducible-representation|irreducible representation]] recovers the
[[langlands/local-l-parameter|semisimple \(L\)-parameter]] attached by
[[langlands/excursion-operator|excursion operators]].

## Why global functions are coarser than the stack

An invariant regular function sees the semisimple closed orbit of a
parameter but not a representation of its
[[algebra-groups/centralizer|centralizer]]. Consequently the
center can decompose categories into parameter components without by itself
giving the internal parameterization of an \(L\)-packet.

## Status

The existence of the map is a theorem in the Fargues–Scholze framework,
with precise restrictions on coefficients, including inversion of relevant
[[langlands/component-group-of-l-parameter|component-group]] orders. For
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]]
\(G\), injectivity and a
characterization of its image as the stable part of the Bernstein center
belong to further conjectures in general.

It is therefore incorrect to call \(\Psi_G\) an unconditional isomorphism.

## Categorical refinement

The ring is the degree-zero shadow of the
[[langlands/spectral-action|spectral action]] of
[[algebraic-geometry-foundations/perfect-complex|perfect complexes]] on the
entire parameter stack. That action retains derived and stabilizer
information not visible to global functions alone.

## References

1. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Definition I.9.2 and Proposition I.9.3.
   [arXiv](https://arxiv.org/abs/2102.13459).
