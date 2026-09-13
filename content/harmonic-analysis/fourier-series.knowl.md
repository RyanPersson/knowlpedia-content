+++
id = "harmonic-analysis/fourier-series"
title = "Periodic Fourier series"
kind = "definition"
summary = "The series of characters weighted by the Fourier coefficients of a periodic function."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-coefficient", "real-analysis/series", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **Fourier series** associated with an integrable \(\mathbb Z^d\)-periodic function \(f\) is
\[
\sum_{m\in\mathbb Z^d}\widehat f(m)e^{2\pi i m\cdot x}.
\]
For example, rectangular partial sums retain the [[harmonic-analysis/fourier-coefficient|coefficients]] with \(|m_i|\le N\) for every \(i\). Other summation methods must be specified.

## Convergence is an additional assertion

The definition supplies coefficients and a series, but not pointwise equality with \(f\). Smooth periodic functions have [[harmonic-analysis/smooth-fourier-reconstruction|convergence with every derivative]]. An \(L^2\) function has convergence in \(L^2\) for rectangular partial sums. Merely continuous functions can have divergent pointwise Fourier partial sums.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
