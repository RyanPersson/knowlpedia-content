+++
id = "complex-analysis/log-modulus-subharmonic"
title = "Subharmonicity of the logarithmic modulus"
kind = "theorem"
summary = "The logarithm of the modulus of a nonzero holomorphic function is subharmonic, with Laplacian equal to its zero-counting measure."
aliases = ["log modulus is subharmonic", "Poincaré–Lelong formula in one variable"]
domains = ["complex-analysis", "potential-theory"]
section_mode = "progressive"
prerequisites = ["complex-analysis/subharmonic-function", "functional-analysis/distribution", "complex-analysis/holomorphic-functions-are-analytic", "complex-analysis/order-of-zero-or-pole"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f\) be a holomorphic function on a planar domain \(U\), not identically
zero. Extending \(\log|f|\) by \(-\infty\) at zeros, the function
\(\log|f|\) is [[complex-analysis/subharmonic-function|subharmonic]]. Moreover,
in the sense of [[functional-analysis/distribution|distributions]],
\[
\Delta\log|f|=2\pi\sum_{a\in U}\operatorname{ord}_a(f)\,\delta_a.
\]

## Away from the zeros

Where \(f\ne0\), a local holomorphic logarithm exists and
\(\log|f|\) is the real part of that logarithm, hence harmonic. All positive
Laplacian mass is concentrated at the zeros.

## Multiplicity

If \(f(z)=(z-a)^m g(z)\) with \(g(a)\ne0\), then the contribution at \(a\) is
\(2\pi m\delta_a\). Thus the Riesz measure of \(\log|f|\) is exactly the
zero-counting measure with multiplicity.

## References

1. Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511623776).
