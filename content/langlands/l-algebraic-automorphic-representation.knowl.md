+++
id = "langlands/l-algebraic-automorphic-representation"
title = "L-algebraic automorphic representation"
kind = "knowl"
summary = "An automorphic representation whose archimedean Langlands-parameter exponents are integral cocharacters."
aliases = ["L-algebraic representation", "L-algebraic automorphic representations"]
domains = ["langlands", "number-theory", "representation-theory"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/number-field", "langlands/automorphic-representation", "langlands-letter/knowls/maximal-torus-weight-lattice", "langlands/local-l-parameter"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/number-field|number field]]
\(F\), and let
\(\pi\) be an [[langlands/automorphic-representation|automorphic
representation]] of \(G(\mathbb A_F)\). It is **\(L\)-algebraic** if every
archimedean component \(\pi_v\) is \(L\)-algebraic.

After choosing a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]], write
the restriction of the archimedean
[[langlands/local-l-parameter|Langlands parameter]] to \(\mathbb C^\times\) with exponent

\[
\lambda_\sigma\in
X_*(\widehat T)\otimes_\mathbb Z\mathbb C.
\]

The condition is

\[
\lambda_\sigma\in X_*(\widehat T).
\]

The corresponding condition for the conjugate exponent follows from
admissibility, and the property is independent of the auxiliary choices.

## Meaning of the letter L

This is the normalization in which an associated \(\ell\)-adic Galois
representation is expected to take values directly in the
[[langlands/l-group|\(L\)-group]]:

\[
\rho_{\pi,\iota}:
\operatorname{Gal}(\overline F/F)
\longrightarrow {}^L G(\overline{\mathbb Q}_\ell).
\]

This assertion is a general conjecture. It includes compatibility with
unramified [[langlands/satake-parameter|Satake parameters]] and predicted
[[langlands/hodge-tate-representation|Hodge–Tate cocharacters]].

## Difference from C-algebraicity

The [[langlands/c-algebraic-automorphic-representation|\(C\)-algebraic]]
condition requires \(\lambda_\sigma-\delta\) to be integral, where
\(\delta\) is half the sum of the [[lie-groups/positive-root|positive roots]]. The two conditions
therefore differ by the \(\delta\)-shift. For
\(\operatorname{GL}_n\), an appropriate norm twist relates them, but the
twist need not descend to every reductive group.

## Scope warning

\(L\)-algebraic does not mean that the automorphic \(L\)-function is
algebraic, nor does it by itself imply cuspidality, regularity, or the
existence of a known Galois representation. Those are separate conditions
or theorems.

## References

1. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” Definitions
   2.3.1 and 3.1.1 and Conjecture 3.2.1.
   [arXiv](https://arxiv.org/abs/1009.0785).
