+++
id = "langlands/transfer-factor"
title = "Endoscopic transfer factor"
kind = "knowl"
summary = "A normalized scalar comparing orbital integrals of matching elements on an endoscopic group and the original group."
aliases = ["transfer factor", "Langlands-Shelstad transfer factor", "endoscopic transfer factors"]
domains = ["langlands", "harmonic-analysis", "representation-theory"]
section_mode = "progressive"
prerequisites = ["langlands/endoscopic-datum", "langlands/strongly-regular-semisimple-element", "langlands/stable-orbital-integral", "langlands/orbital-integral", "harmonic-analysis/test-function-space-local-group", "algebra-groups/conjugacy-class", "langlands/kappa-orbital-integral"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be the endoscopic group in an
[[langlands/endoscopic-datum|endoscopic datum]] for \(G\). For related
[[langlands/strongly-regular-semisimple-element|strongly regular
semisimple]] elements \(\gamma_H\in H(F)\) and \(\delta\in G(F)\), an
**endoscopic transfer factor** is a nonzero complex scalar

\[
\Delta(\gamma_H,\delta)
\]

used to compare [[langlands/stable-orbital-integral|stable orbital integrals]] on \(H\) with weighted sums of
[[langlands/orbital-integral|orbital integrals]] on \(G\).

With one standard convention, matching
[[harmonic-analysis/test-function-space-local-group|test functions]] satisfy

\[
SO_{\gamma_H}(f^H)
=
\sum_{\delta}
\Delta(\gamma_H,\delta)\,O_\delta(f),
\]

where the sum runs over rational [[algebra-groups/conjugacy-class|conjugacy classes]] in the matching stable
class. Equivalently the right side is a normalized
[[langlands/kappa-orbital-integral|\(\kappa\)-orbital integral]].

## What the factor corrects

A \(\kappa\)-orbital integral depends on the chosen representative of a
stable class, whereas the left side is stable. The transfer factor changes
by the inverse scalar needed to cancel that dependence. It also records
root-theoretic discriminants and Galois-cohomological pairings.

## Construction data

The Langlands–Shelstad factor is assembled from terms customarily denoted

\[
\Delta_I\Delta_{II}\Delta_{III}\Delta_{IV}.
\]

Its construction uses choices such as splittings, \(a\)-data, \(\chi\)-data,
and compatible [[harmonic-analysis/haar-measure|Haar measures]]. Absolute normalizations can instead be fixed
by a [[langlands/whittaker-datum|Whittaker datum]] or by
[[langlands/rigid-inner-twist|rigid inner-twist data]]. The resulting
transfer identity is independent of auxiliary choices
when all terms are normalized coherently.

## Convention warning

Sources differ by inverses, complex conjugation, arithmetic versus geometric
normalization, and the use of \(\Delta'\) or \(\Delta_D\) in twisted
endoscopy. A formula containing a transfer factor is not meaningful until
the normalization of orbital integrals and [[langlands/local-langlands-correspondence|local Langlands correspondence]]
is also stated.

## References

1. Robert P. Langlands and Diana Shelstad, “On the definition of transfer
   factors,” *Mathematische Annalen* 278 (1987), 219–271.
   [DOI](https://doi.org/10.1007/BF01458070).
2. Robert E. Kottwitz and Diana Shelstad, “On splitting invariants and sign
   conventions in endoscopic transfer,” 2012.
   [arXiv](https://arxiv.org/abs/1201.5658).
