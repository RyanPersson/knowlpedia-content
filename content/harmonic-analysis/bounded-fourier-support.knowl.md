+++
id = "harmonic-analysis/bounded-fourier-support"
title = "Bounded Fourier support"
kind = "definition"
summary = "The spectral localization condition that a Fourier transform vanish outside a bounded frequency set."
aliases = ["compact Fourier support", "band-limited function", "frequency localization"]
domains = ["harmonic-analysis", "functional-analysis"]
prerequisites = ["measure-theory/almost-everywhere", "topology/bounded-set"]
dependency_review_count = 1
section_mode = "progressive"
+++

A function \(f\in L^2(\mathbb R^d)\) has **bounded Fourier support** if its
\(L^2\) Fourier transform vanishes [[measure-theory/almost-everywhere|almost everywhere]] outside some [[topology/bounded-set|bounded set]]
\(K\subset\mathbb R^d\):
\[
\operatorname{supp}\widehat f\subseteq K.
\]
When \(K=B_\sigma\), the number \(\sigma\) is a frequency or spectral radius.

## Meaning for an \(L^2\) function

The Fourier transform is defined through the
[[harmonic-analysis/plancherel-theorem-lca|Plancherel theorem]], so its support
is the essential support of an \(L^2\)-equivalence class. Altering
\(\widehat f\) on a [[measure-theory/null-set|null set]] does not change the condition.

## Analytic characterization

The [[harmonic-analysis/paley-wiener-bounded-fourier-support|Paley–Wiener
theorem]] identifies ball-supported Fourier transforms with restrictions of
[[complex-analysis/entire-function-several-variables|entire functions of
several variables]] of controlled exponential type. Bounded Fourier support is
therefore a strong analyticity constraint, not merely a decay condition.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §7.3.
