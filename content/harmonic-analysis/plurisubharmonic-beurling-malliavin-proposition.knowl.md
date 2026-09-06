+++
id = "harmonic-analysis/plurisubharmonic-beurling-malliavin-proposition"
title = "Plurisubharmonic Beurling–Malliavin proposition"
kind = "theorem"
summary = "A regular weight with controlled radial-line growth has a Lipschitz plurisubharmonic minorant with linear growth in imaginary directions."
aliases = ["PSH-BM", "PSH Beurling–Malliavin proposition"]
domains = ["harmonic-analysis", "several-complex-variables"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/radial-line-growth-functional", "harmonic-analysis/higher-dimensional-beurling-malliavin-theorem", "complex-analysis/plurisubharmonic-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Suppose \(\omega:\mathbb R^d\to\mathbb R_{\le0}\) satisfies the vanishing,
three-derivative, and
[[harmonic-analysis/radial-line-growth-functional|radial-line growth]]
hypotheses of the
[[harmonic-analysis/higher-dimensional-beurling-malliavin-theorem|higher-dimensional Beurling–Malliavin theorem]]. Then there is a continuous
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]]
\(u:\mathbb C^d\to\mathbb R\) such that
\[
u(x)\le\omega(x),\qquad u(x)=0\quad(|x|\le2),
\]
\[
|u(x_1)-u(x_2)|\le C_{\mathrm{Lip}}|x_1-x_2|,
\qquad
u(x)\le u(x+iy)\le u(x)+\rho|y|,
\]
where \(C_{\mathrm{Lip}},\rho\lesssim_d
\max(C_{\mathrm{reg}},C_{\mathrm{gr}})\).

## Why modification is needed

The original weight need not satisfy the transverse Hessian condition in the
[[harmonic-analysis/exact-plurisubharmonic-beurling-malliavin-proposition|exact
PSH-BM proposition]]. A dyadic modification produces a minorant with comparable
regularity and controlled line integrals, to which the exact extension applies.

## Role

This proposition solves the potential-theoretic half of the multiplier
problem. The
[[harmonic-analysis/analytic-beurling-malliavin-proposition|analytic BM
proposition]] then replaces \(u\) by the logarithmic size of an
[[complex-analysis/entire-function-several-variables|entire function]].

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Proposition 2.2 and §§3–4.
