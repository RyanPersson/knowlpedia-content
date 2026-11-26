+++
id = "harmonic-analysis/poisson-summation-on-a-progression"
title = "Poisson summation on an arithmetic progression"
kind = "theorem"
summary = "Periodizing a Schwartz function on a real lattice evaluates its sum over a progression through Fourier samples."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/schwartz-space", "functional-analysis/fourier-transform-schwartz-space", "harmonic-analysis/fourier-coefficient", "harmonic-analysis/fourier-series", "harmonic-analysis/uniqueness-of-continuous-fourier-series"]
+++

If \(f:\mathbb R\to\mathbb C\) belongs to the [[functional-analysis/schwartz-space|Schwartz space]], \(q>0\) and \(b\in\mathbb R\), then
\[
\sum_{k\in\mathbb Z} f(b+kq)
=\frac1q\sum_{m\in\mathbb Z} e^{2\pi i mb/q}\widehat f(m/q),
\]
with the [[functional-analysis/fourier-transform-schwartz-space|Fourier transform]] \(\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-2\pi i u\xi}\,du\).

## Proof

Periodize \(f\) by \(P(x)=\sum_k f(x+kq)\). Rapid decay of \(f\) and each derivative gives uniform absolute convergence on \([0,q]\) after any number of differentiations. Its \(m\)-th [[harmonic-analysis/fourier-coefficient|Fourier coefficient]] is \(q^{-1}\int_0^q P(x)e^{-2\pi i mx/q}\,dx=q^{-1}\widehat f(m/q)\). Indeed translating each subinterval by \(kq\) leaves the exponential unchanged and the intervals tile the real line.

Twice integrating by parts bounds the nonconstant coefficients by a constant times \(m^{-2}\). Their [[harmonic-analysis/fourier-series|Fourier series]] converges absolutely and uniformly to a continuous function with those coefficients. It equals \(P\) by [[harmonic-analysis/uniqueness-of-continuous-fourier-series|uniqueness of Fourier coefficients for continuous periodic functions]]. Evaluating at \(b\) gives the assertion.

## References

- [Shifted Poisson summation for Gaussian weights](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L267)
