+++
id = "harmonic-analysis/dual-haar-measure"
title = "Dual Haar measure"
kind = "definition"
summary = "The dual Haar measure is the uniquely normalized Haar measure on the Pontryagin dual that makes Fourier transformation unitary on L2."
aliases = ["Plancherel-normalized Haar measure", "dual measure on the Pontryagin dual"]
domains = ["harmonic-analysis", "measure-theory", "functional-analysis"]
prerequisites = ["topology/locally-compact-group", "algebra-groups/abelian-group", "harmonic-analysis/haar-measure", "harmonic-analysis/pontryagin-dual", "harmonic-analysis/fourier-transform-lca", "functional-analysis/unitary-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] that is [[algebra-groups/abelian-group|abelian]], with [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\), and let \(\widehat G\) be its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]]. The **dual Haar measure** \(\widehat\mu\) is the unique Haar measure on \(\widehat G\) for which the [[harmonic-analysis/fourier-transform-lca|Fourier transform]]
\[
\widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,d\mu(x)
\]
extends from \(L^1(G,\mu)\cap L^2(G,\mu)\) to a [[functional-analysis/unitary-operator|unitary operator]]
\[
L^2(G,\mu)\longrightarrow L^2(\widehat G,\widehat\mu).
\]
Thus \(\widehat\mu\) is not an independent normalization: it is determined by \(\mu\) and the chosen Fourier-transform convention.

## Fourier inversion

The [[harmonic-analysis/fourier-inversion-lca|Fourier inversion theorem]] says that, with the dual normalization, sufficiently integrable functions satisfy
\[
f(x)=\int_{\widehat G}\widehat f(\gamma)\gamma(x)\,d\widehat\mu(\gamma).
\]
More precisely, if \(f\in L^1(G)\) and \(\widehat f\in L^1(\widehat G)\), the right side gives a continuous representative equal to \(f\) [[measure-theory/almost-everywhere|almost everywhere]]. This inversion criterion and the unitary \(L^2\) extension in the [[harmonic-analysis/plancherel-theorem-lca|Plancherel theorem]] determine the same normalization.

## Scaling and bidual normalization

If \(\mu\) is replaced by \(c\mu\) for \(c>0\), then \(\widehat\mu\) must be replaced by \(c^{-1}\widehat\mu\). Applying the construction again on \(\widehat G\), and identifying \(G\) with its bidual through [[harmonic-analysis/pontryagin-duality-theorem|Pontryagin duality]], recovers the original measure \(\mu\).

## Standard normalizations

For \(G=\mathbb R^n\) with [[measure-theory/lebesgue-measure|Lebesgue measure]] and characters \(x\mapsto e^{2\pi i x\cdot\xi}\), the dual measure is Lebesgue measure. For \(G=\mathbb Z\) with counting measure, the dual circle has normalized Haar [[probability/probability-measure|probability measure]]. Conversely, normalized Haar measure on the circle is dual to counting measure on \(\mathbb Z\).

**Warning.** Changing the exponential from \(e^{2\pi i x\cdot\xi}\) to \(e^{i x\cdot\xi}\) changes the Euclidean dual measure by a power of \(2\pi\).

## References

1. W. Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [DOI record](https://doi.org/10.1002/9781118165621). Relevant: Haar measure on the dual group, inversion, and Plancherel theory.
2. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, dual measures and Fourier analysis on locally compact abelian groups.
