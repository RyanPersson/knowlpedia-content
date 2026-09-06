+++
id = "langlands/local-global-compatibility"
title = "Local-global compatibility"
kind = "knowl"
summary = "Agreement between the localization of a global Galois representation and the local Langlands parameter of an automorphic component."
aliases = ["local-global compatibility for Galois representations", "local-global compatibility in the Langlands correspondence"]
domains = ["langlands", "number-theory", "representation-theory"]
prerequisites = ["algebra-fields-galois/number-field", "langlands/restricted-tensor-product-automorphic-representation", "langlands/algebraic-automorphic-representation", "algebra-fields-galois/decomposition-group", "langlands/local-l-parameter"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/number-field|number field]] and let

\[
\pi=\bigotimes_v'\pi_v
\]

be an [[langlands/restricted-tensor-product-automorphic-representation|restricted
tensor product]] defining an
[[langlands/algebraic-automorphic-representation|algebraic automorphic
representation]], and let
\(\rho_{\pi,\lambda}\) be an associated \(\ell\)-adic Galois
representation. **Local–global compatibility at \(v\)** asserts that the
restriction of \(\rho_{\pi,\lambda}\) to a
[[algebra-fields-galois/decomposition-group|decomposition group]] at \(v\)
matches the [[langlands/local-l-parameter|local Langlands parameter]] of
\(\pi_v\), after choosing an identification between complex and
\(\ell\)-adic coefficient fields and applying the stated normalization.

## Away from ell

For \(v\nmid\ell\), the comparison for
\(\operatorname{GL}_n\) is commonly written

\[
\operatorname{WD}\!\left(
\rho_{\pi,\lambda}|_{\Gamma_{F_v}}
\right)^{\mathrm{F\text{-}ss}}
\cong
\operatorname{rec}_{F_v}\!\left(
\pi_v\otimes |\det|^{(1-n)/2}
\right),
\]

with the twist altered if a different local Langlands normalization is used.
The superscript denotes Frobenius semisimplification: replace the Frobenius
action in the [[langlands/weil-deligne-representation|Weil–Deligne
representation]] by its semisimple part while retaining monodromy. Some
theorems prove
only ordinary semisimplification and therefore do not identify the
monodromy operator.

At an unramified place, the statement reduces to equality of the Frobenius
[[algebra-groups/conjugacy-class|conjugacy class]] with the [[langlands/satake-parameter|Satake parameter]].

## At places above ell

For \(v\mid\ell\), the comparison uses \(p\)-adic Hodge theory: the Galois
representation should be [[langlands/de-rham-galois-representation|de Rham]],
its [[langlands/hodge-tate-representation|Hodge–Tate cocharacters]] should match
the archimedean algebraic weights through the chosen embedding, and its
[[langlands/semistable-galois-representation|potentially semistable]]
Weil–Deligne parameter should match \(\pi_v\).
This is a different and generally harder assertion than compatibility away
from \(\ell\).

## Status must be qualified

There is no single theorem giving full local–global compatibility for every
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] and every algebraic automorphic representation. Strong
theorems exist for broad regular algebraic cuspidal families on
\(\operatorname{GL}_n\), with hypotheses depending on the number field,
polarization, and place. A statement must specify whether it preserves
monodromy and whether \(v\mid\ell\).

## References

1. Ila Varma, “Local-global compatibility for regular algebraic cuspidal
   automorphic representations when \(\ell\neq p\),” 2014.
   [arXiv](https://arxiv.org/abs/1411.2520).
2. Lambert A'Campo, Bence Hevesi, Jack A. Thorne, and Dmitri Whitmore,
   “Local-global compatibility of automorphic Galois representations over CM
   fields at \(p\),” 2026. [arXiv](https://arxiv.org/abs/2607.11763).
