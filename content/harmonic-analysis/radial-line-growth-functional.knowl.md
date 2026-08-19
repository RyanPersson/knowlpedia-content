+++
id = "harmonic-analysis/radial-line-growth-functional"
title = "Radial-line growth functional of a weight"
kind = "definition"
summary = "A maximal averaged magnitude along radial lines used as the growth condition in a higher-dimensional multiplier theorem."
aliases = ["Cohen growth functional", "radial growth function G-star"]
domains = ["harmonic-analysis", "analysis"]
section_mode = "progressive"
+++

For a measurable weight \(\omega:\mathbb R^d\to\mathbb R\), define
\[
G(x)=\int_{1/2}^{2}|\omega(sx)|\,ds,
\qquad
G^*(r)=\sup_{|x|=r}G(x).
\]
The **radial-line growth condition** is
\[
\int_0^\infty\frac{G^*(r)}{1+r^2}\,dr<\infty.
\]

## Geometric meaning

The first average smooths the weight along a short radial segment; the
spherical supremum then records the worst direction at radius \(r\). The final
integral measures whether these worst directional masses can be summed over
scales.

## One-dimensional comparison

For \(d=1\), the growth integral is comparable, up to absolute constants, to
\(\int_{\mathbb R}|\omega(t)|/(1+t^2)\,dt\), the condition in the classical
[[harmonic-analysis/beurling-malliavin-multiplier-theorem|Beurling–Malliavin
multiplier theorem]].

## Role of line porosity

When \(\omega\) is assembled from cubes meeting a
[[analysis/porosity-on-lines|line-porous set]], the
[[analysis/line-porous-section-measure-decay|line-section measure estimate]]
controls \(G^*\) on every [[analysis/dyadic-annulus|dyadic annulus]].

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: equations (1.9)–(1.13).
