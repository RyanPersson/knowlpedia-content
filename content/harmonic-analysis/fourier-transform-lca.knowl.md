+++
id = "harmonic-analysis/fourier-transform-lca"
title = "Fourier transform on a locally compact abelian group"
kind = "definition"
summary = "The transform integrating an integrable function against the characters of a locally compact abelian group."
aliases = ["group Fourier transform", "LCA Fourier transform"]
domains = ["harmonic-analysis", "functional-analysis", "algebra-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] that is [[algebra-groups/abelian-group|abelian]], let \(\widehat G\) be its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]], and fix a [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\) on \(G\). For an [[measure-theory/l1-function|\(L^1\) function]] \(f\) on \(G\), its **Fourier transform** is the function on \(\widehat G\) defined by
\[
\widehat f(\gamma)
=
\int_G f(x)\overline{\gamma(x)}\,d\mu(x),
\qquad \gamma\in\widehat G.
\]
The conjugate specifies the sign convention; using \(\gamma(x)\) gives the inverse convention. The transform is bounded and continuous and vanishes at infinity.

## Convolution and translation

For \(f,g\in L^1(G)\), the [[harmonic-analysis/convolution-on-locally-compact-group|convolution]] theorem states
\[
\widehat{f*g}(\gamma)=\widehat f(\gamma)\widehat g(\gamma).
\]
Thus the Fourier transform converts the group-defined convolution product into pointwise multiplication on the dual group. Translation by \(y\in G\) becomes multiplication by the character value \(\overline{\gamma(y)}\).

## Inversion and Plancherel normalization

There is a unique normalization of Haar measure \(\widehat\mu\) on \(\widehat G\) with the following property: if \(f\in L^1(G)\) and \(\widehat f\in L^1(\widehat G)\), then \(f\) agrees [[measure-theory/almost-everywhere|almost everywhere]] with the continuous function
\[
f(x)
=
\int_{\widehat G}\widehat f(\gamma)\gamma(x)\,d\widehat\mu(\gamma)
\]
With the same normalization, the transform extends uniquely from \(L^1(G)\cap L^2(G)\) to a unitary map
\[
L^2(G,\mu)\longrightarrow L^2(\widehat G,\widehat\mu),
\]
which is the [[harmonic-analysis/plancherel-theorem-lca|Plancherel theorem for locally compact abelian groups]].

Rescaling \(\mu\) rescales \(\widehat f\), so the [[harmonic-analysis/dual-haar-measure|dual Haar measure]] must be normalized correspondingly.

## Standard models

For \(G=\mathbb R^n\) and characters \(\gamma_\xi(x)=e^{2\pi i x\cdot\xi}\), the definition is the classical Euclidean Fourier transform with exponent \(-2\pi i x\cdot\xi\). For \(G=\mathbb Z\), the dual is the circle and the transform produces a Fourier series. If \(G\) is compact, \(\widehat G\) is discrete; if \(G\) is discrete, \(\widehat G\) is compact.

The general LCA construction, inversion, and duality are treated in [Rudin, the opening chapters].

## References

1. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: the opening chapters on LCA groups, Fourier transforms, inversion, and duality.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Routledge publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781032922218). Relevant: Chapter 4, “Analysis on Locally Compact Abelian Groups.”
