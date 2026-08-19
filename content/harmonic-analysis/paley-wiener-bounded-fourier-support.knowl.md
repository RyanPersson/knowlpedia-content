+++
id = "harmonic-analysis/paley-wiener-bounded-fourier-support"
title = "Paley–Wiener theorem for bounded Fourier support"
kind = "theorem"
summary = "An L2 function is band limited exactly when it extends to an entire function of the corresponding exponential type."
aliases = ["L2 Paley–Wiener theorem", "Paley–Wiener criterion"]
domains = ["harmonic-analysis", "complex-analysis"]
section_mode = "progressive"
+++

Let \(f\in L^2(\mathbb R^d)\) and \(\sigma>0\). With the Fourier convention
\(\widehat f(\xi)=\int f(x)e^{-2\pi i x\cdot\xi}\,dx\), the condition
\[
\operatorname{supp}\widehat f\subseteq B_{\sigma/(2\pi)}
\]
holds if and only if \(f\) is the restriction to \(\mathbb R^d\) of an
[[complex-analysis/entire-function-several-variables|entire function]]
\(F:\mathbb C^d\to\mathbb C\) for which
\[
|F(x+iy)|\le A e^{\sigma|y|}
\]
for some \(A>0\) and all \(x,y\in\mathbb R^d\).

## Forward direction

Fourier inversion over the bounded support defines
\(F(z)=\int\widehat f(\xi)e^{2\pi i z\cdot\xi}\,d\xi\). The bounded frequency
region makes the integral entire and gives the exponential bound by
[[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz]].

## Reverse direction

Shift the contour in a complex line parallel to a fixed frequency \(\xi\).
When \(2\pi|\xi|>\sigma\), exponential decay in the shifted half-plane forces
\(\widehat f(\xi)=0\). A standard approximation removes auxiliary Schwartz
regularity used in the contour argument.

## Normalization warning

If the Fourier exponential is \(e^{-ix\cdot\xi}\), the ball radius is
\(\sigma\) rather than \(\sigma/(2\pi)\).

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: Theorem 7.3.1.
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Theorem 2.1 and Appendix A.3.
