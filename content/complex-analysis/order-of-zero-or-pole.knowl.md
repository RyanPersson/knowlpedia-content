+++
id = "complex-analysis/order-of-zero-or-pole"
title = "Order of a zero or pole"
kind = "definition"
summary = "The integer exponent in the local factorization of a meromorphic function."
aliases = ["multiplicity of a zero", "order of vanishing", "pole order"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/meromorphic-function", "complex-analysis/laurent-series"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f\) be [[complex-analysis/meromorphic-function|meromorphic]] near \(a\) and not identically zero. There is a unique integer \(m\in\mathbb Z\) and a holomorphic function \(u\) near \(a\), with \(u(a)\ne0\), such that
\[
f(z)=(z-a)^m u(z).
\]
The integer \(\operatorname{ord}_a(f)=m\) is the **order** of \(f\) at \(a\): \(m>0\) is a zero of multiplicity \(m\), \(m<0\) is a pole of order \(-m\), and \(m=0\) means \(f\) is holomorphic and nonzero at \(a\).

## Arithmetic

Whenever the expressions are defined,
\[
\operatorname{ord}_a(fg)=\operatorname{ord}_a(f)+\operatorname{ord}_a(g),
\qquad
\operatorname{ord}_a(f/g)=\operatorname{ord}_a(f)-\operatorname{ord}_a(g).
\]
Thus order behaves as a local additive valuation on nonzero meromorphic germs.

## Logarithmic derivative

The [[complex-analysis/logarithmic-derivative|logarithmic derivative]] gives, for a small positively oriented circle around \(a\),
\[
\operatorname{ord}_a(f)
=\frac{1}{2\pi i}\int\frac{f'(z)}{f(z)}\,dz.
\]
This local identity is the building block of the [[complex-analysis/argument-principle|argument principle]].

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§8–9.
