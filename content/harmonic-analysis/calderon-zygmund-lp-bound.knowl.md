+++
id = "harmonic-analysis/calderon-zygmund-lp-bound"
title = "Lp boundedness of Calderón–Zygmund operators"
kind = "theorem"
summary = "A standard singular kernel together with L2 boundedness gives boundedness for every interior Lebesgue exponent."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/calderon-zygmund-operator", "measure-theory/lp-space", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Every [[harmonic-analysis/calderon-zygmund-operator|Calderón–Zygmund operator]] \(T\) extends uniquely from \(L^2\cap L^p\) to a bounded operator on \(L^p(\mathbb R^n)\) for \(1<p<\infty\), with
\[
\|Tf\|_p\le C_p\|f\|_p.
\]
The constant depends on dimension, \(p\), the kernel size and regularity bounds, its Hölder exponent, and the \(L^2\) operator norm.

## Proof mechanism and endpoints

The Calderón–Zygmund decomposition splits an integrable input into a bounded part and localized pieces of mean zero. The \(L^2\) bound handles the bounded part; cancellation and kernel regularity control the others off enlarged supporting cubes. This gives the distribution-function estimate \(|\{|Tf|>\lambda\}|\le C\|f\|_1/\lambda\). Interpolation gives \(1<p<2\), and applying the same argument to the adjoint and using duality gives \(2<p<\infty\). The cited lecture notes supply the full decomposition and interpolation proof.

Neither strong \(L^1\) nor strong \(L^\infty\) boundedness is part of this conclusion.

## References

- [Tao, Fourier analysis lecture notes 4, §2](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
