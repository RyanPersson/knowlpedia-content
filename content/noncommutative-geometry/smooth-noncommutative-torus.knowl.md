+++
id = "noncommutative-geometry/smooth-noncommutative-torus"
title = "Smooth noncommutative torus"
kind = "definition"
summary = "The dense algebra of rapidly decreasing Fourier series in the noncommutative two-torus."
aliases = ["smooth rotation algebra"]
domains = ["noncommutative-geometry"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/rotation-algebra"]
+++

The **smooth noncommutative torus** \(A_\theta^\infty\) is the subalgebra of the [[noncommutative-geometry/rotation-algebra|rotation algebra \(A_\theta\)]] consisting of series
\[
\sum_{m,n\in\mathbb Z}c_{m,n}v^mu^n
\]
whose coefficients are rapidly decreasing: for every integer \(N\geq0\),
\[
\sup_{m,n}(1+|m|+|n|)^N|c_{m,n}|<\infty.
\]
Here \(vu=e^{2\pi i\theta}uv\). The series converge in the \(C^*\)-norm and define a dense \(*\)-subalgebra.

## Smoothness and differentiation

Multiplication is twisted convolution of coefficients, which preserves rapid decrease. The [[noncommutative-geometry/rotation-algebra-derivations|canonical derivations]] multiply coefficients by \(2\pi im\) and \(2\pi in\), respectively, and also preserve rapid decrease. At \(\theta=0\), this algebra is \(C^\infty(\mathbb T^2)\).

## References

1. Alain Connes, [*C*-algebras and differential geometry*](https://arxiv.org/abs/hep-th/0101093), English translation of the 1980 note, pp. 4–5 (torus action, derivations, and rapid-decay series).
