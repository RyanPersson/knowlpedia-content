+++
id = "harmonic-analysis/fourier-orthogonality"
title = "Orthogonality of periodic Fourier characters"
kind = "lemma"
summary = "Distinct integer-frequency characters have zero averaged Hermitian product."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-character", "shared-foundations/complex-conjugate", "measure-theory/fubinis-theorem", "real-analysis/newton-leibniz-formula", "linear-algebra/inner-product", "measure-theory/lp-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For [[harmonic-analysis/fourier-character|Fourier characters]] on a unit cell,
\[
\int_{[0,1]^d}e_m(x)\overline{e_n(x)}\,dx
=\begin{cases}1,&m=n,\\0,&m\ne n.\end{cases}
\]
Thus they are orthonormal for the normalized \(L^2\) inner product.

## Proof

The integrand is \(e_{m-n}\). Fubini factors the integral into one-dimensional integrals. For an integer \(k\ne0\), \(\int_0^1e^{2\pi iks}\,ds=(e^{2\pi ik}-1)/(2\pi ik)=0\); for \(k=0\) it equals one.

## Products without conjugation

Likewise \(\int e_me_n\,dx\) equals one precisely when \(m+n=0\), and zero otherwise. Keeping track of the conjugation is essential when computing a real wave's quadratic average.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
