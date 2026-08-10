+++
id = "langlands/endoscopic-transfer"
title = "Endoscopic transfer"
kind = "knowl"
summary = "The matching of test functions and stable distributions between a group and an endoscopic group."
aliases = ["transfer of orbital integrals", "endoscopic matching", "endoscopic character transfer"]
domains = ["langlands", "harmonic-analysis", "representation-theory"]
section_mode = "progressive"
+++

Let \(\mathfrak e\) be an [[langlands/endoscopic-datum|endoscopic datum]]
for a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive
group]] \(G\), with endoscopic group \(H\). A
[[harmonic-analysis/test-function-space-local-group|test function]]
\(f^H\in C_c^\infty(H(F))\) is an **endoscopic transfer** of
\(f\in C_c^\infty(G(F))\) if, for every
[[langlands/strongly-regular-semisimple-element|strongly
\(G\)-regular]] element
\(\gamma_H\in H(F)\),

\[
SO_{\gamma_H}(f^H)
=
\sum_{\delta\leftrightarrow\gamma_H}
\Delta(\gamma_H,\delta)\,O_\delta(f).
\]

The right side uses the [[langlands/transfer-factor|transfer factor]] and
runs over rational [[algebra-groups/conjugacy-class|conjugacy classes]] in \(G(F)\) matching
\(\gamma_H\).

## Matching functions

The local transfer theorem asserts, in the established endoscopic settings,
that every test function on \(G(F)\) has a transfer on \(H(F)\). The transfer
is not unique as a function; its [[langlands/stable-orbital-integral|stable orbital integrals]] are the prescribed
data. Variants cover archimedean fields, nonarchimedean fields, [[lie-groups/lie-algebra|Lie algebras]],
and twisted endoscopy.

The [[langlands/fundamental-lemma|fundamental lemma]] is the especially
important unramified assertion that the unit of the [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke algebra]]
transfers to the corresponding unit, with normalized measures.

## Spectral transfer

Duality of
[[harmonic-analysis/distribution-local-group|invariant distributions]]
converts geometric transfer into
character identities.
[[langlands/stable-distribution|Stable distributions]] built from characters
on \(H(F)\) transfer to linear combinations of characters in
[[langlands/l-packet|\(L\)-packets]] or
[[langlands/a-packet|\(A\)-packets]] on \(G(F)\).
This is the mechanism by which endoscopy describes packet structure.

## Global use

For factorizable functions, compatible local transfers define an adelic
transfer. Comparing the trace formula for \(G\) with [[langlands/stable-trace-formula|stable trace formulas]]
for its endoscopic groups yields endoscopic classification and instances of
[[langlands-letter/knowls/langlands-functoriality-l-homomorphism|Langlands
functoriality]].

## Scope

Endoscopic transfer realizes a structured class of \(L\)-homomorphisms. It
does not encompass every case of functoriality. Ordinary, twisted, and
weighted transfer are distinct assertions.

## References

1. Jean-Loup Waldspurger, “Endoscopie et changement de caractéristique,”
   *Journal of the Institute of Mathematics of Jussieu* 5 (2006), 423–525.
   [DOI](https://doi.org/10.1017/S1474748006000028).
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §§2–3.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
