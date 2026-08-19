+++
id = "harmonic-analysis/higher-dimensional-beurling-malliavin-theorem"
title = "Higher-dimensional Beurling–Malliavin multiplier theorem"
kind = "theorem"
summary = "Regular negative weights with summable radial-line growth admit nontrivial band-limited multipliers with controlled decay."
aliases = ["higher-dimensional BM theorem", "Cohen multiplier theorem"]
domains = ["harmonic-analysis", "several-complex-variables"]
section_mode = "progressive"
+++

Let \(\omega:\mathbb R^d\to\mathbb R_{\le0}\) vanish on \(B_2\), and suppose
that for \(0\le a\le3\)
\[
|D^a\omega(x)|\le C_{\mathrm{reg}}\langle x\rangle^{1-a},
\]
while its [[harmonic-analysis/radial-line-growth-functional|radial-line growth
functional]] satisfies
\[
\int_0^\infty\frac{G^*(r)}{1+r^2}\,dr\le C_{\mathrm{gr}}.
\]
For every \(\sigma>0\), there is \(f\in L^2(\mathbb R^d)\) with
\[
\operatorname{supp}\widehat f\subseteq B_\sigma,
\qquad |f(x)|\le C e^{c\sigma\omega(x)},
\qquad |f(x)|\ge\tfrac12\quad(x\in B_{r_{\min}}).
\]
One may take \(c\asymp_d\max(C_{\mathrm{reg}},C_{\mathrm{gr}})^{-1}\),
\(r_{\min}\asymp_d\min(\sigma,\sigma^{-1})\), and an explicit \(C\) depending
on \(d\) and \(\sigma\).

## Proof chain

The [[harmonic-analysis/plurisubharmonic-beurling-malliavin-proposition|PSH-BM
proposition]] constructs a plurisubharmonic minorant of the weight. The
[[harmonic-analysis/analytic-beurling-malliavin-proposition|analytic BM
proposition]] converts it to an entire \(L^2\) function. Finally the
[[harmonic-analysis/paley-wiener-bounded-fourier-support|Paley–Wiener theorem]]
gives the required Fourier support.

## Why this is weaker than the one-dimensional theorem

The classical theorem needs only Lipschitz regularity and a logarithmic
integral. The higher-dimensional result imposes symbol-type bounds through
third derivatives; these are nevertheless satisfied by the weights built from
line-porous sets.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Theorem 1.4.
