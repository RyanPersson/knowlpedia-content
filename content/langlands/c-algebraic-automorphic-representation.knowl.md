+++
id = "langlands/c-algebraic-automorphic-representation"
title = "C-algebraic automorphic representation"
kind = "knowl"
summary = "An automorphic representation whose archimedean parameter is integral after the half-sum-of-positive-roots shift."
aliases = ["C-algebraic representation", "C-algebraic automorphic representations"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[langlands-letter/knowls/global-local-fields-completions|number field]]
\(F\), and let
\(\pi\) be an [[langlands/automorphic-representation|automorphic
representation]] of \(G(\mathbb A_F)\). It is **\(C\)-algebraic** if every
archimedean component \(\pi_v\) is \(C\)-algebraic.

Concretely, after choosing a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]] and
[[lie-groups/positive-root|positive roots]], write the
restriction of the archimedean [[langlands/local-l-parameter|Langlands parameter]] to
\(\mathbb C^\times\) using a cocharacter exponent
\(\lambda_\sigma\in X_*(\widehat T)\otimes_\mathbb Z\mathbb C\). If
\(\delta\) is the half-sum of the positive roots, then the condition is

\[
\lambda_\sigma-\delta\in X_*(\widehat T).
\]

Although the formula uses choices, the integrality condition does not.

## Meaning of the letter C

[[langlands/cohomological-automorphic-representation|Cohomological automorphic representations]] are \(C\)-algebraic. Equivalently,
the [[lie-groups/infinitesimal-character|infinitesimal character]] is integral in the Harish-Chandra normalization
appropriate to the infinitesimal character of a finite-dimensional
algebraic representation.

For [[langlands/isobaric-automorphic-representation|isobaric
representations]] of \(\operatorname{GL}_n\), this agrees with
Clozel's convention for an
[[langlands/algebraic-automorphic-representation|algebraic automorphic
representation]].

## Difference from L-algebraicity

The [[langlands/l-algebraic-automorphic-representation|\(L\)-algebraic]]
condition is \(\lambda_\sigma\in X_*(\widehat T)\), without the
\(\delta\)-shift. Thus the two conditions differ by half the sum of the
positive roots. They coincide when \(\delta\) lies in the relevant integral
lattice, but can be disjoint for some groups.

## Expected arithmetic object

The most direct Galois-valued conjecture for \(C\)-algebraic
representations uses the \(C\)-group, the \(L\)-group of a canonical central
extension of \(G\). It is generally incorrect to assert without further
qualification that a \(C\)-algebraic representation gives a Galois
representation into the ordinary \(L\)-group of \(G\).

## References

1. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” Definitions
   2.3.3 and 3.1.2. [arXiv](https://arxiv.org/abs/1009.0785).
2. Laurent Clozel, “Motifs et formes automorphes: applications du principe
   de fonctorialité,” 1990.
