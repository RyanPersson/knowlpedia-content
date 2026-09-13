+++
id = "complex-analysis/cauchy-derivative-estimate"
title = "Cauchy estimate for holomorphic derivatives"
kind = "theorem"
summary = "A bound on a complex neighborhood controls all derivatives on a smaller set with factorial constants."
aliases = ["Cauchy inequality", "Cauchy derivative bound"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/cauchy-integral-formula", "shared-foundations/factorial", "real-analysis/modulus-on-c"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(f\) is holomorphic on a neighborhood of the closed disc \(\overline D(a,R)\), then
\[
|f^{(m)}(a)|\le \frac{m!}{R^m}\max_{|z-a|=R}|f(z)|,
\qquad m\ge0.
\]
This **Cauchy estimate** follows from the derivative form of the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]]: bound the integrand and use the circle length \(2\pi R\).

## Uniform neighborhoods

If every point of a compact real interval has its closed radius-\(R\) disc in a common complex domain where \(|f|\le M\), then \(\sup_I|f^{(m)}|\le M m!R^{-m}\) for every \(m\). The same domain supplies all orders at once. In a polydisc, iterating the formula gives \(|\partial^\alpha f(a)|\le\alpha!M\prod_jR_j^{-\alpha_j}\).

## Room for polynomial factors

If a norm includes an extra factor such as \((m+1)^2\), choosing a strictly smaller radius absorbs it: for \(0<r<R\), the sequence \((m+1)^2(r/R)^m\) is bounded. A positive gap between radii is therefore useful even when each fixed derivative already has a Cauchy bound.

## References

- [Dan Romik, Complex Analysis, Cauchy inequalities](https://www.math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/complex-analysis-2018.pdf).
