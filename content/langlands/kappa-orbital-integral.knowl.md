+++
id = "langlands/kappa-orbital-integral"
title = "Kappa-orbital integral"
kind = "knowl"
summary = "A character-weighted sum of orbital integrals inside one stable conjugacy class."
aliases = ["κ-orbital integral", "kappa orbital integral", "endoscopic orbital integral"]
domains = ["langlands", "harmonic-analysis", "representation-theory"]
prerequisites = ["langlands/strongly-regular-semisimple-element", "algebra-fields-galois/local-field", "langlands-letter/knowls/nonabelian-h1-galois-cohomology", "algebra-groups/conjugacy-class", "langlands/stable-conjugacy"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\gamma\in G(F)\) be [[langlands/strongly-regular-semisimple-element|strongly regular semisimple]] over a
[[algebra-fields-galois/local-field|local field]].
Write

\[
A_\gamma=
\ker\!\left[H^1(F,G_\gamma)\to H^1(F,G)\right],
\]

which is a kernel in
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|nonabelian Galois
cohomology]] and parametrizes the rational
[[algebra-groups/conjugacy-class|conjugacy classes]] in the
[[langlands/stable-conjugacy|stable class]] of \(\gamma\). Given a character
\(\kappa:A_\gamma\to\mathbb C^\times\), the **\(\kappa\)-orbital integral**
is

\[
O_\gamma^\kappa(f)
=
\sum_{\gamma'}
\kappa(\operatorname{inv}(\gamma,\gamma'))\,
O_{\gamma'}(f),
\]

with compatible centralizer measures.

## Dependence on a basepoint

The invariant \(\operatorname{inv}(\gamma,\gamma')\) uses \(\gamma\) as a
basepoint. Replacing that basepoint multiplies the distribution by a scalar.
The [[langlands/transfer-factor|transfer factor]] compensates for this
dependence in [[langlands/endoscopic-transfer|endoscopic transfer]].

For the trivial character \(\kappa=1\), the expression is the
[[langlands/stable-orbital-integral|stable orbital integral]].

## Dual interpretation

[[langlands/tate-nakayama-duality|Tate–Nakayama duality]] relates characters
of the cohomological group \(A_\gamma\) to
[[langlands/component-group-of-l-parameter|component-group]] data in the dual
centralizer. The corresponding
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
[[langlands-letter/knowls/langlands-dual-group|dual-group]] element determines
an [[langlands/endoscopic-datum|endoscopic group]].
Thus the Fourier decomposition of ordinary orbital terms across a stable
class produces the endoscopic pieces of the trace formula.

## Convention warning

Some sources sum over a larger \(H^1(F,G_\gamma)\), insert Kottwitz signs, or
write the character inversely. The choice of
\(\operatorname{inv}(\gamma,\gamma')\), transfer-factor normalization, and
[[harmonic-analysis/haar-measure|Haar measures]] must be read as one package.

## References

1. Robert E. Kottwitz, “Stable trace formula: cuspidal tempered terms,”
   *Duke Mathematical Journal* 51 (1984), 611–650.
   [DOI](https://doi.org/10.1215/S0012-7094-84-05129-9).
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §2.2.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
