+++
id = "harmonic-analysis/torus-cover-preserves-average"
title = "Torus coverings preserve normalized averages"
kind = "theorem"
summary = "Pulling a smooth function back by a nonsingular integer torus map preserves its average."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/normalized-torus-average", "topology/integer-matrix-torus-cover", "harmonic-analysis/fourier-character", "harmonic-analysis/smooth-fourier-reconstruction"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(A\) is a nonsingular integer matrix and \(f\in C^\infty(\mathbb T^n)\), then
\[
\langle f\circ p_A\rangle=\langle f\rangle.
\]
Both [[harmonic-analysis/normalized-torus-average|averages]] use probability normalization; no factor of \(|\det A|\) occurs.

## Fourier proof

A character \(e^{2\pi i m\cdot x}\) pulls back to \(e^{2\pi i(A^Tm)\cdot x}\). Because \(A^T\) is injective, its average vanishes for every \(m\ne0\), while the constant character is unchanged. The smooth Fourier series converges uniformly, so its integral is the sum of its termwise integrals. This proves the formula and, in particular, preservation of the zero-mean condition.
