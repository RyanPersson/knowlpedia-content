+++
id = "harmonic-analysis/smooth-fourier-reconstruction"
title = "Smooth periodic Fourier reconstruction"
kind = "theorem"
summary = "The Fourier series of a smooth periodic function converges uniformly with every derivative."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-series", "harmonic-analysis/smooth-fourier-coefficient-decay", "real-analysis/uniform-convergence", "real-analysis/multi-index-notation", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

If \(f\) is smooth and \(\mathbb Z^d\)-periodic, its [[harmonic-analysis/fourier-series|Fourier series]] reconstructs it:
\[
f(x)=\sum_{m\in\mathbb Z^d}\widehat f(m)e^{2\pi i m\cdot x},
\]
and the series may be differentiated term by term to every fixed order, with absolute and uniform convergence of each resulting series.

## Convergence and identification

For a derivative of order \(k\), [[harmonic-analysis/smooth-fourier-coefficient-decay|coefficient decay]] bounds the summands by \(C_N(1+|m|)^{k-2N}\). Choose \(2N>k+d\) to make the lattice sum convergent. This produces a smooth function with the same coefficients as \(f\).

To identify it with \(f\), use uniqueness of coefficients for continuous periodic functions. One proof convolves their difference with the product Fejér kernels: these averages are zero because all its coefficients vanish, and the positive normalized kernels concentrate at zero, so their convolution converges uniformly to the continuous difference. The difference is therefore zero.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
