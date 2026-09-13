+++
id = "harmonic-analysis/smooth-fourier-coefficient-decay"
title = "Decay of smooth periodic Fourier coefficients"
kind = "lemma"
summary = "Integration by parts gives decay faster than every inverse power of frequency."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-coefficient", "real-analysis/integration-by-parts", "real-analysis/laplacian", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a smooth \(\mathbb Z^d\)-periodic function \(f\) and an integer \(N\ge0\),
\[
|\widehat f(m)|\le(1+4\pi^2|m|^2)^{-N}
\|(1-\Delta)^N f\|_{L^1([0,1]^d)}.
\]
In particular, the [[harmonic-analysis/fourier-coefficient|coefficients]] decay faster than every inverse power of \(1+|m|\).

## Proof and parameters

Periodic integration by parts has canceling boundary terms and gives
\(\widehat{(1-\Delta)^N f}(m)=(1+4\pi^2|m|^2)^N\widehat f(m)\). Bound the coefficient of \((1-\Delta)^N f\) by its \(L^1\) norm. Uniform bounds on the indicated derivatives of a parameter family give uniform coefficient decay; no uniform conclusion follows without those bounds.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
