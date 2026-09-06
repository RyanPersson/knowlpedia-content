+++
id = "harmonic-analysis/line-porosity-damping-function-theorem"
title = "Damping functions from line porosity"
kind = "theorem"
summary = "A bounded set porous on every line admits band-limited damping functions with enhanced decay on that set."
aliases = ["line porous sets admit damping functions"]
domains = ["harmonic-analysis", "analysis"]
prerequisites = ["analysis/porosity-on-lines", "harmonic-analysis/damping-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(Y\subseteq[-3h^{-1},3h^{-1}]^d\) be
\(\nu\)-[[analysis/porosity-on-lines|porous on lines]] from scales \(\mu>1\) to
\(h^{-1}\). There is \(\alpha=\alpha(\nu)<1\) such that, for every
\(0<\sigma<1\), \(Y\) admits a
[[harmonic-analysis/damping-function|damping function]] with spectral radius
\(c_1=\sigma\). The remaining parameters have the form
\[
c_2=c(d,\mu)\sigma^{C_d},\qquad
c_3=c(\nu,d)\sigma,
\]
and one may choose \(\alpha\le1-c\nu/|\log\nu|\).

## Construction

Cover each [[analysis/dyadic-annulus|dyadic annulus]] by a
[[analysis/finitely-overlapping-family|finitely overlapping family]] of cubes.
Place scaled [[differential-geometry/bump-function|bump functions]] on cubes
meeting \(Y\) and sum them to form a negative weight. The
[[analysis/line-porous-section-measure-decay|line-section measure bound]] gives
the growth hypothesis for the
[[harmonic-analysis/higher-dimensional-beurling-malliavin-theorem|higher-dimensional Beurling–Malliavin theorem]].

## Final polynomial decay

The multiplier obtained from Beurling–Malliavin has rapid decay on \(Y\) but
only a global bound. Multiplication by a fixed Schwartz function preserves
controlled Fourier support up to convolution and supplies the required
\(\langle x\rangle^{-d}\) decay.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Proposition 1.7 and §6.1.
