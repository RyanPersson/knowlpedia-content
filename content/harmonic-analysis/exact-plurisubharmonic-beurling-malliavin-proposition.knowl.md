+++
id = "harmonic-analysis/exact-plurisubharmonic-beurling-malliavin-proposition"
title = "Exact plurisubharmonic Beurling–Malliavin extension"
kind = "theorem"
summary = "Uniform Hilbert-transform and transverse Hessian bounds make a linewise Poisson extension plurisubharmonic after adding a multiple of the imaginary norm."
aliases = ["Exact PSH-BM", "exact PSH Beurling–Malliavin proposition"]
domains = ["harmonic-analysis", "several-complex-variables"]
prerequisites = ["complex-analysis/plurisubharmonic-function"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\omega:\mathbb R^d\to\mathbb R_{\le0}\) be \(C^2\) and compactly
supported. Assume every affine line \(\ell\) satisfies
\[
\|H[(\omega|_\ell)']\|_\infty\le C_1,
\]
and, for every line direction \(\widehat y\) and unit
\(\widehat v\perp\widehat y\),
\[
\frac1\pi\int_{\mathbb R}
\langle D^2\omega(x+t\widehat y)\widehat v,\widehat v\rangle\,dt
\ge-C_2.
\]
If \(C\ge\max(C_1,C_2)\), then
\[
u(x+iy)=E\omega(x+iy)+C|y|
\]
is continuous and [[complex-analysis/plurisubharmonic-function|plurisubharmonic]], and
\[
u(x)\le u(x+iy)\le u(x)+2C|y|.
\]

## Division of labor between the hypotheses

The [[harmonic-analysis/hilbert-transform|Hilbert-transform]] bound controls
complex disks centered on \(\mathbb R^d\). The transverse Hessian integral
controls the [[complex-analysis/levi-form|Levi form]] off the real locus via
the [[harmonic-analysis/beurling-malliavin-extension-operator|linewise Poisson
extension operator]].

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Proposition 3.1.
