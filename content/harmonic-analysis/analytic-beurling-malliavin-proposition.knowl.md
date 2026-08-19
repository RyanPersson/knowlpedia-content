+++
id = "harmonic-analysis/analytic-beurling-malliavin-proposition"
title = "Analytic Beurling–Malliavin proposition"
kind = "theorem"
summary = "A controlled plurisubharmonic function is majorized by the logarithmic modulus of a nonvanishing entire L2 function with matching growth."
aliases = ["A-BM", "analytic BM proposition"]
domains = ["harmonic-analysis", "several-complex-variables"]
section_mode = "progressive"
+++

Let \(u:\mathbb C^d\to\mathbb R\) be plurisubharmonic, with \(u|_{\mathbb R^d}
\le0\), \(u=0\) on the real ball \(B_2\), Lipschitz constant
\(C_{\mathrm{Lip}}\) on \(\mathbb R^d\), and
\[
u(x)\le u(x+iy)\le u(x)+\rho|y|.
\]
Then there is an [[complex-analysis/entire-function-several-variables|entire
function]] \(f:\mathbb C^d\to\mathbb C\) such that
\[
|f(x+iy)|\le A e^{2\rho|y|},\qquad
|f(x)|\le C e^{u(x)},\qquad f|_{\mathbb R^d}\in L^2,
\]
and \(|f(x)|\ge1/2\) on a ball of radius comparable to
\(\min(\rho,\rho^{-1})\). The constant \(C\) is explicit in
\(d,C_{\mathrm{Lip}},\rho\).

## Construction

Choose a cutoff \(h\) equal to one near the origin. The
[[complex-analysis/hormander-l2-dbar-theorem|Hörmander theorem]] solves
\(\bar\partial g=\bar\partial h\) with a carefully augmented
plurisubharmonic weight. Then \(f=h-g\) is entire. The added logarithmic term
forces \(g\) to be small near the origin, while an auxiliary decaying weight
makes \(f|_{\mathbb R^d}\) square-integrable.

## From L2 to pointwise bounds

The [[complex-analysis/holomorphic-l2-mean-value-estimate|holomorphic
\(L^2\) mean-value estimate]] converts the weighted integral estimate for \(g\)
and \(f\) into the displayed pointwise bounds.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Proposition 2.3 and §5.
