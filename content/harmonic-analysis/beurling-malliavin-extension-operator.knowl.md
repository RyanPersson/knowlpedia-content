+++
id = "harmonic-analysis/beurling-malliavin-extension-operator"
title = "Linewise Poisson extension operator"
kind = "construction"
summary = "An operator extending a function on real Euclidean space by taking a Poisson average along the real line determined by the imaginary direction."
aliases = ["Cohen extension operator", "linewise harmonic extension"]
domains = ["harmonic-analysis", "several-complex-variables"]
section_mode = "progressive"
+++

For suitable \(\omega:\mathbb R^d\to\mathbb R\), define its **linewise Poisson
extension** \(E\omega:\mathbb C^d\to\mathbb R\) by
\[
E\omega(x+iy)=\frac1\pi\int_{\mathbb R}
\frac{\omega(x+ty)}{1+t^2}\,dt.
\]
When \(y=0\), the formula gives \(E\omega(x)=\omega(x)\).

## Linewise harmonicity

For fixed \(x\\) and nonzero \(y\), restriction to the complex line
\(z\mapsto x+zy\) is the
[[harmonic-analysis/poisson-extension-upper-half-plane|Poisson extension]] of
the restriction of \(\omega\) to the real line \(x+\mathbb R y\). Thus it is
harmonic separately along every such complex line away from the real locus.

## Convergence

If \(\omega\) is Lipschitz and satisfies the
[[harmonic-analysis/radial-line-growth-functional|radial-line growth
condition]], the defining integral is absolutely convergent and its symmetric
truncations converge uniformly on compact subsets.

## Levi-form structure

Transverse components of the [[complex-analysis/levi-form|Levi form]] of
\(E\omega\) are line integrals of the real Hessian of \(\omega\), that is,
[[harmonic-analysis/x-ray-transform|X-ray transforms]]. Adding \(C|y|\) can
therefore make the extension plurisubharmonic under explicit linewise bounds.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: §3.
