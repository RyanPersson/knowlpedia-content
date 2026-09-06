+++
id = "analysis/line-porous-section-measure-decay"
title = "Line-section decay for line-porous sets"
kind = "theorem"
summary = "A line-porous set occupies only a power-decaying fraction of every line segment in the controlled scale range."
aliases = ["line porous intersection estimate", "line-section measure bound"]
domains = ["analysis", "geometric-measure-theory"]
section_mode = "progressive"
prerequisites = ["analysis/porosity-on-lines", "analysis/porous-set-measure-decay", "measure-theory/lebesgue-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(Y\subseteq\mathbb R^d\) be \(\nu\)-[[analysis/porosity-on-lines|porous on
lines]] from scales \(\alpha_0\) to \(\alpha_1\). There are
\(C,\gamma>0\), depending only on \(\nu\), such that every line segment
\(\tau\) of length \(R\), with \(\alpha_0<R<\alpha_1\), satisfies
\[
\mathcal L^1(\tau\cap Y)
\le C R\left(\frac{\alpha_0}{R}\right)^\gamma.
\]
Here \(\mathcal L^1\) is one-dimensional [[measure-theory/lebesgue-measure|Lebesgue measure]] on the supporting line.

## Proof idea

The intersection of \(Y\) with its supporting line is a one-dimensional
[[analysis/porosity-on-balls|porous set]]. Applying
[[analysis/porous-set-measure-decay|measure decay for porous sets]] in
dimension one yields the estimate.

## Role in fractal uncertainty

The estimate controls integrals of weights along all lines. That is precisely
the geometry measured by the
[[harmonic-analysis/radial-line-growth-functional|radial-line growth
functional]] in the
[[harmonic-analysis/higher-dimensional-beurling-malliavin-theorem|higher-dimensional Beurling–Malliavin theorem]].

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Corollary A.8.
