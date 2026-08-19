+++
id = "harmonic-analysis/beurling-malliavin-multiplier-theorem"
title = "Beurling–Malliavin multiplier theorem"
kind = "theorem"
summary = "A Lipschitz negative weight with finite logarithmic integral majorizes the modulus of a nonzero band-limited L2 function."
aliases = ["BM multiplier theorem", "Beurling–Malliavin theorem"]
domains = ["harmonic-analysis", "complex-analysis"]
section_mode = "progressive"
+++

Let \(\omega:\mathbb R\to\mathbb R_{\le0}\) be Lipschitz and suppose
\[
\int_{\mathbb R}\frac{\omega(x)}{1+x^2}\,dx>-\infty.
\]
For every \(\sigma>0\), there is a nonzero \(f\in L^2(\mathbb R)\) such that
\[
\operatorname{supp}\widehat f\subseteq[-\sigma,\sigma],
\qquad |f(x)|\le e^{\omega(x)}\quad(x\in\mathbb R).
\]

## Meaning

The weight prescribes where and how rapidly the multiplier should decay.
[[topology/lipschitz-continuity|Lipschitz regularity]] rules out arbitrarily
sharp oscillation, while the logarithmic integral is the sharp global growth
condition. The conclusion balances this decay against
[[harmonic-analysis/bounded-fourier-support|bounded Fourier support]].

## Complex-analytic viewpoint

By the [[harmonic-analysis/paley-wiener-bounded-fourier-support|Paley–Wiener
theorem]], the problem is to construct an [[complex-analysis/entire-function|entire function]] of controlled
exponential type under the majorant \(e^\omega\) on the real axis. Classical
proofs use subharmonic majorants, outer functions, or carefully placed zeros.

## References

1. Arne Beurling and Paul Malliavin, “On Fourier transforms of measures with compact support,” *Acta Mathematica* 107 (1962), 291–309. [DOI record](https://doi.org/10.1007/BF02545787).
2. Javad Mashreghi, Fedor Nazarov, and Victor Havin, “The Beurling–Malliavin multiplier theorem: the seventh proof,” *St. Petersburg Mathematical Journal* 17 (2006), 699–744. [DOI record](https://doi.org/10.1090/S1061-0022-06-00922-5).
