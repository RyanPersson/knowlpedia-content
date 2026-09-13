+++
id = "functional-analysis/sobolev-embedding-bounded-derivatives"
title = "Sobolev embedding into bounded continuous derivatives"
kind = "theorem"
summary = "More than half a dimension of additional Sobolev order gives bounded continuous derivatives."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/fourier-sobolev-space", "functional-analysis/fourier-inversion-schwartz-space", "convex-analysis/holder-inequality-integrals", "real-analysis/class-ck-function", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an integer \(k\ge0\) and \(s>n/2+k\), each \(u\in H^s(\mathbb R^n)\) has a representative in \(C^k\) whose derivatives through order \(k\) are bounded and continuous, with
\[
\max_{|\alpha|\le k}\|\partial^\alpha u\|_\infty\le C_{n,s,k}\|u\|_{H^s}.
\]
The space \(H^s\) is the [[functional-analysis/fourier-sobolev-space|inhomogeneous Fourier Sobolev space]].

## Fourier proof

Cauchy–Schwarz bounds \(\int |\xi|^{|\alpha|}|\widehat u(\xi)|\,d\xi\) by a constant times \(\|u\|_{H^s}\), since \(\int |\xi|^{2|\alpha|}(1+4\pi^2|\xi|^2)^{-s}\,d\xi<\infty\). The inverse Fourier integrals for these derivatives therefore converge absolutely and define bounded continuous functions. Approximation, or distributional Fourier inversion, identifies them with the derivatives of \(u\). For example, in three dimensions \(H^3\) controls both the function and its first derivatives in \(L^\infty\).
