+++
id = "analysis/porous-set-measure-decay"
title = "Measure decay for porous sets"
kind = "theorem"
summary = "Truncated ball porosity forces a quantitative power saving in local Lebesgue measure."
aliases = ["porosity volume bound", "porous-set volume decay"]
domains = ["analysis", "geometric-measure-theory", "measure-theory"]
prerequisites = ["analysis/porosity-on-balls", "analysis/box-porosity"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\subseteq\mathbb R^d\) be \(\nu\)-[[analysis/porosity-on-balls|porous on
balls]] from scales \(\alpha_0\) to \(\alpha_1\). There are constants
\(C,\gamma>0\), depending only on \(\nu\) and \(d\), such that every ball \(B\)
of radius \(R\) with \(\alpha_0<R<\alpha_1\) satisfies
\[
|X\cap B|\le C R^d\left(\frac{\alpha_0}{R}\right)^\gamma.
\]

## Mechanism

Choose an \(L\)-adic grid with \(L\asymp_d\nu^{-1}\). [[analysis/porosity-on-balls|Ball porosity]] gives
[[analysis/box-porosity|box porosity]], so at every admissible depth at least
one child of each occupied cube is empty. Iterating the factor
\(1-L^{-d}\) through \(N\asymp\log(R/\alpha_0)\) levels gives the power
saving.

## Quantitative exponent

One may choose \(\gamma\) comparable from below to
\(\nu^d/|\log\nu|\), with a dimension-dependent constant. Sharpness of this
particular expression is not asserted.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Lemmas A.6–A.7.
