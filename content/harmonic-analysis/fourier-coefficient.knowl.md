+++
id = "harmonic-analysis/fourier-coefficient"
title = "Periodic Fourier coefficient"
kind = "definition"
summary = "The normalized integral of a periodic function against a conjugate Fourier character."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-character", "measure-theory/lebesgue-integral", "measure-theory/l1-function", "shared-foundations/complex-conjugate"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a \(\mathbb Z^d\)-periodic function \(f\) integrable on \([0,1]^d\), its **Fourier coefficient** at \(m\in\mathbb Z^d\) is
\[
\widehat f(m)=\int_{[0,1]^d} f(x)\overline{e_m(x)}\,dx
=\int_{[0,1]^d}f(x)e^{-2\pi i m\cdot x}\,dx.
\]
The integral uses a unit-volume cell, and \(e_m\) is the [[harmonic-analysis/fourier-character|Fourier character]]. The coefficient satisfies \(|\widehat f(m)|\le\|f\|_{L^1([0,1]^d)}\).

## Other periods and real values

For a scalar \(2\pi\)-periodic function, \(\widehat f(m)=(2\pi)^{-1}\int_0^{2\pi}f(\theta)e^{-im\theta}\,d\theta\). If \(f\) is real-valued, conjugating the integral gives \(\widehat f(-m)=\overline{\widehat f(m)}\). Vector and matrix coefficients are defined componentwise.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
