+++
id = "noncommutative-geometry/rotation-algebra-derivations"
title = "Canonical derivations of the noncommutative torus"
kind = "construction"
summary = "Two Fourier derivations supplying the coordinate derivatives of the noncommutative torus."
aliases = []
domains = ["noncommutative-geometry"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/rotation-algebra", "algebra-rings/associative-algebra-derivation"]
+++

In [[noncommutative-geometry/rotation-algebra|\(A_\theta\)]], with \(vu=e^{2\pi i\theta}uv\), let \(\mathcal P_\theta\) be the algebra of finite sums of \(v^mu^n\). The **canonical derivations** are the complex-linear maps
\[
\delta_1(v^mu^n)=2\pi im\,v^mu^n,\qquad
\delta_2(v^mu^n)=2\pi in\,v^mu^n.
\]
They obey the Leibniz rule and commute on \(\mathcal P_\theta\).

## Product-rule verification

Multiplying two monomials adds their respective exponents and introduces only a constant phase from the commutation relation. Applying \(\delta_j\) multiplies by the sum of the corresponding frequencies, which equals the two Leibniz terms.

## Smooth algebra

The [[noncommutative-geometry/smooth-noncommutative-torus|smooth noncommutative torus]] is a dense algebra of rapidly decreasing Fourier series, preserved by both derivations. At \(\theta=0\), these derivations become the two usual partial derivatives on the smooth ordinary torus.

## References

1. Alain Connes, [*C*-algebras and differential geometry*](https://arxiv.org/abs/hep-th/0101093), English translation of the 1980 note, pp. 4–5 (torus action, derivations, and rapid-decay series).
