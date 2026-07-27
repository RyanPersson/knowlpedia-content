+++
id = "operator-algebras/dixmier-trace"
title = "Dixmier trace"
kind = "definition"
summary = "A singular trace on the Marcinkiewicz–Macaev ideal obtained by applying an invariant generalized limit to logarithmic singular-value means."
aliases = ["non-normal singular trace", "Tr-omega"]
domains = ["operator-algebras", "noncommutative-geometry"]
section_mode = "progressive"
+++

Let \(H\) be a separable [[linear-algebra/hilbert-space|Hilbert space]] and let
\(\omega\) be a dilation-invariant generalized limit on [[real-analysis/bounded-sequence|bounded sequences]]. For
a positive operator \(T\) in the
[[operator-algebras/marcinkiewicz-macaev-ideal|Marcinkiewicz–Macaev ideal]]
\(\mathcal M_{1,\infty}(H)\), its **Dixmier trace** is
\[
\operatorname{Tr}_{\omega}(T)=
\omega\left(\left\{
\frac{1}{\log(1+N)}\sum_{n=1}^{N}\mu_n(T)
\right\}_{N\geq1}\right),
\]
where \(\mu_n(T)\) are the singular values in decreasing order. The functional
extends linearly from positive operators to \(\mathcal M_{1,\infty}(H)\). It is
positive, unitarily invariant, tracial, and vanishes on trace-class operators,
but its value can depend on \(\omega\).

## Why the logarithmic mean appears

For \(T\in\mathcal M_{1,\infty}\), the [[real-analysis/partial-sums|partial sums]] of singular values grow at
most logarithmically, so the sequence supplied to \(\omega\) is bounded. The
generalized limit extracts an asymptotic coefficient even when the ordinary
limit does not exist. Dilation invariance is the ingredient that makes the
result a trace rather than merely a unitarily invariant functional. The
construction and the precise admissible generalized limits are developed in
[Lord–Sukochev–Zanin, Chapters 5–6](https://doi.org/10.1515/9783110262551).

## Measurable operators

A positive \(T\) is Dixmier measurable when
\(\operatorname{Tr}_{\omega}(T)\) has the same value for every admissible
\(\omega\). A sufficient and standard criterion is convergence of the
logarithmic means in the displayed formula; then the Dixmier trace equals that
ordinary limit. For a diagonal operator with eigenvalues \(1/n\), the
logarithmic means converge to \(1\), so every Dixmier trace gives value \(1\).

## Relation to ordinary integration

The [[operator-algebras/operator-trace|canonical operator trace]] sums
singular values and is finite on the trace-class ideal. The Dixmier trace
instead detects the critical \(1/n\) decay scale and vanishes on that smaller
ideal. This singular behavior permits the noncommutative integral of a
critical-order infinitesimal in a
[[noncommutative-geometry/spectral-triple|spectral triple]]; Connes develops
this role in [Noncommutative Geometry, Chapter IV](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

## Conventions and scope

**Warning.** The notation \(\mathcal L^{1,\infty}\) is not uniform across the
literature: it may denote the [[operator-algebras/weak-schatten-ideal|weak Schatten ideal]] or the logarithmic
Marcinkiewicz ideal. The former is strictly contained in the latter under the
conventions used here. Also, not every singular trace is a Dixmier trace, and
a Dixmier trace is not normal on \(B(H)\).

## References

1. S. Lord, F. Sukochev, and D. Zanin, *Singular Traces: Theory and Applications*, De Gruyter, 2013. [DOI record](https://doi.org/10.1515/9783110262551). Relevant: Chapters 5–6 on Dixmier traces and measurable operators.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted record](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §2 on the Dixmier trace and the noncommutative integral.
