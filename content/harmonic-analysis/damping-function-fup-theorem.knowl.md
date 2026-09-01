+++
id = "harmonic-analysis/damping-function-fup-theorem"
title = "Damping-function fractal uncertainty theorem"
kind = "theorem"
summary = "Uniform damping functions for affine rescalings of a frequency set imply a fractal uncertainty principle against porous physical sets."
aliases = ["Han–Schlag FUP theorem", "damping functions imply FUP"]
domains = ["harmonic-analysis"]
prerequisites = ["analysis/porosity-on-balls", "harmonic-analysis/damping-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\subseteq[-1,1]^d\) be \(\nu\)-[[analysis/porosity-on-balls|porous on
balls]] from scales \(h\) to \(1\), and let
\(Y\subseteq[-h^{-1},h^{-1}]^d\). Assume there are fixed
\(c_2,c_3,\alpha\in(0,1)\) such that, for every \(h<s<1\) and every allowed
translation \(\eta\),
\[
sY+[-4,4]^d+\eta
\]
admits a [[harmonic-analysis/damping-function|damping function]] with spectral
radius \(c_1=20\nu\sqrt d\) and parameters \(c_2,c_3,\alpha\). Then constants
\(C,\beta>0\), depending only on these parameters and \(d\), satisfy
\[
\operatorname{supp}\widehat f\subseteq Y
\quad\Longrightarrow\quad
\|f\mathbf1_X\|_2\le Ch^\beta\|f\|_2.
\]

## Iteration mechanism

Damping functions yield a uniform
[[analysis/quantitative-unique-continuation|quantitative unique-continuation]]
estimate. It shows that at each scale a fixed portion of \(f\)'s mass lies in
the holes of \(X\). Iterating over order \(\log(h^{-1})\) scales turns the fixed
loss into the power \(h^\beta\).

## Convention

Equivalent versions use \(\ell^1\) cubes and \(\ell^1\)-decay. Norm
equivalence in finite-dimensional [[linear-algebra/euclidean-space|Euclidean space]] changes the constants but
not the theorem.

## References

1. Rui Han and Wilhelm Schlag, “A higher-dimensional Bourgain–Dyatlov fractal uncertainty principle,” *Analysis & PDE* 13 (2020), Theorem 5.1. [DOI record](https://doi.org/10.2140/apde.2020.13.813).
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Theorem 1.6 and Appendix A.1.
