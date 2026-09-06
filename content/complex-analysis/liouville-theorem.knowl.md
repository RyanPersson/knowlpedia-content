+++
id = "complex-analysis/liouville-theorem"
title = "Liouville's theorem in complex analysis"
kind = "theorem"
summary = "Every bounded entire function is constant."
aliases = ["Liouville theorem for entire functions"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/entire-function"]
dependency_review_count = 1
section_mode = "progressive"
+++

If \(f:\mathbb C\to\mathbb C\) is an [[complex-analysis/entire-function|entire function]] and bounded, then \(f\) is constant.

## Cauchy-estimate proof

If \(|f|\le M\), the derivative form of the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]] on the circle \(|z-a|=R\) gives
\[
|f'(a)|\le\frac{M}{R}.
\]
Letting \(R\to\infty\) yields \(f'(a)=0\) for every \(a\), hence \(f\) is constant.

## Consequences

The theorem gives a complex-analytic proof of the [[complex-analysis/fundamental-theorem-of-algebra-complex-analysis|fundamental theorem of algebra]]. More generally, an entire function satisfying \(|f(z)|\le C(1+|z|^m)\) is a polynomial of degree at most \(m\), by the higher Cauchy estimates.

## Disambiguation

This theorem is unrelated to Liouville's theorem in Hamiltonian mechanics or the [[differential-geometry/liouville-arnold-theorem|Liouville–Arnold theorem]].

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 4, §3.
