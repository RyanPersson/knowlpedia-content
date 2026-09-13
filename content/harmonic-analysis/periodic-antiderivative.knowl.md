+++
id = "harmonic-analysis/periodic-antiderivative"
title = "Periodic antiderivative"
kind = "theorem"
summary = "A periodic primitive, whose existence requires zero mean over a period."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/periodic-function", "measure-theory/zero-mean-function", "real-analysis/newton-leibniz-formula", "real-analysis/antiderivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a continuous \(L\)-periodic function \(f\), an \(L\)-periodic **antiderivative** exists exactly when \(\int_0^L f(s)\,ds=0\). Under this condition a primitive is
\[
F(x)=\int_0^x f(s)\,ds,
\]
and all primitives differ by a constant. There is exactly one with [[measure-theory/zero-mean-function|zero mean]] over a period.

## Proof and Fourier formula

Periodicity of a primitive forces \(0=F(L)-F(0)=\int_0^L f\). Conversely, periodicity of \(f\) gives \(F(x+L)-F(x)=\int_x^{x+L}f=0\). Subtract its average to normalize \(F\). If \(f\) is smooth with period one, the normalized primitive has coefficients \(\widehat F(m)=\widehat f(m)/(2\pi im)\) for \(m\ne0\), and \(\widehat F(0)=0\).
