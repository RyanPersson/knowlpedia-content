+++
id = "langlands-letter/knowls/embeddings-qbar-to-q_p"
title = "Choosing an embedding \\(\\overline{\\mathbb Q}\\hookrightarrow\\overline{\\mathbb Q}_p\\)"
kind = "knowl"
summary = "How a p-adic embedding selects a place and a decomposition subgroup, with changes acting by conjugacy."
aliases = ["embeddings-qbar-to-q_p", "p-adic embedding of the algebraic closure"]
domains = ["langlands-letter"]
prerequisites = ["algebra-fields-galois/decomposition-group", "langlands-letter/knowls/galois-extension-and-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/embeddings-qbar-to-q_p.md"
section_mode = "progressive"
+++

Choosing an embedding

\[
\iota_p:\overline{\mathbb Q}
\hookrightarrow
\overline{\mathbb Q}_p
\]

extending \(\mathbb Q\hookrightarrow\mathbb Q_p\) is equivalent to choosing
a place of \(\overline{\mathbb Q}\) above \(p\). It identifies the
[[algebra-fields-galois/decomposition-group|decomposition subgroup]] at that
place with

\[
\operatorname{Gal}(\overline{\mathbb Q}_p/\mathbb Q_p),
\]

up to the usual conjugacy in the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\).

## Effect of changing the embedding

A different choice gives a conjugate decomposition subgroup. At an
unramified prime, the corresponding
[[algebra-fields-galois/inertia-subgroup|inertia subgroup]] acts trivially,
and the
[[langlands-letter/knowls/frobenius-unramified|Frobenius elements]] are
conjugate.
Therefore conjugacy-invariant data such as [[linear-algebra/characteristic-polynomial|characteristic polynomials]],
[[langlands/satake-parameter|Satake conjugacy classes]], and
[[langlands-letter/knowls/euler-product-and-local-factor|local
\(L\)-factors]] do **not** change.

This choice should not be confused with omitting finitely many ramified or
bad places from an Euler product; that finite set is determined by the
global arithmetic data, not by changing \(\iota_p\).

## General number-field form

For a [[algebra-fields-galois/number-field|number field]] \(F\) and a finite place \(v\), an embedding
\(\overline F\hookrightarrow\overline{F_v}\) extending \(F\hookrightarrow
F_v\) selects a [[algebra-fields-galois/decomposition-group|decomposition
subgroup]] \(\Gamma_{F_v}\subset\Gamma_F\).
It is needed to formulate the localization of a global Galois
representation and hence [[langlands/local-global-compatibility|local–global
compatibility]], while the final local
[[algebra-groups/conjugacy-class|conjugacy class]] is independent of the
choice.

## Coefficient embeddings are separate

Comparing a complex automorphic parameter with an
[[langlands/compatible-system-of-galois-representations|\(\ell\)-adic
Galois representation]] also requires an isomorphism
\(\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C\). That coefficient-field
choice is logically distinct from selecting a place above \(p\).

## References

1. Jean-Pierre Serre, *Local Fields*, Springer, 1979, Chapters I and IV.
