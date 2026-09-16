+++
id = "ergodic-theory/oseledets-multiplicative-ergodic-theorem"
title = "Oseledets multiplicative ergodic theorem"
kind = "theorem"
summary = "An integrable invertible linear cocycle over an ergodic base has a measurable splitting into spaces of definite exponential growth."
aliases = ["Oseledets theorem", "multiplicative ergodic theorem"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/linear-cocycle", "ergodic-theory/lyapunov-exponent", "ergodic-theory/ergodic-transformation", "measure-theory/standard-probability-space"]
+++

Let \(T\) be an invertible [[ergodic-theory/ergodic-transformation|ergodic]] transformation of a [[measure-theory/standard-probability-space|standard probability space]] and let \(A:X\to GL_d(\mathbb R)\) be measurable with
\[
\log^+\|A\|,\ \log^+\|A^{-1}\|\in L^1,
\qquad\log^+t=\max(0,\log t).
\]
There are real numbers \(\lambda_1>\cdots>\lambda_r\) and, on an invariant conull set, a measurable direct sum
\[
\mathbb R^d=E_1(x)\oplus\cdots\oplus E_r(x),\qquad
A(x)E_i(x)=E_i(Tx),
\]
such that for every nonzero \(v\in E_i(x)\),
\[
\lim_{n\to\pm\infty}\frac1n\log\|A^{(n)}(x)v\|=\lambda_i.
\]
This is the invertible finite-dimensional form of the **multiplicative ergodic theorem**.

## Applications and hypotheses

The theorem makes Lyapunov exponents and invariant growth directions available in smooth dynamics and random matrix products. Integrability of the inverse is used for the two-sided finite-exponent splitting stated here. Versions with weaker assumptions give filtrations or allow infinite exponents.

## References

1. Simion Filip, [*Notes on the Multiplicative Ergodic Theorem*](https://math.uchicago.edu/~sfilip/public_files/MET_lectures.pdf), Theorem 2.2.6 and Variant 2.2.10.
