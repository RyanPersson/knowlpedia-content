+++
id = "analytic-number-theory/character-projection"
title = "Projection onto a character by weighting"
kind = "construction"
summary = "An average weighted by the conjugate character extracts its Fourier coefficient."
aliases = ["choice of weights", "character isolation"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/finite-fourier-inversion"]
+++

Suppose \(f(g)=\sum_{\chi}a_\chi\chi(g)\) on a finite abelian group \(G\). To **isolate a character** \(\eta\), give \(f(g)\) weight \(\overline{\eta(g)}/|G|\) and sum over \(g\). By [[analytic-number-theory/finite-fourier-inversion|finite Fourier orthogonality]] the result is \(a_\eta\).

## Two weights by hand

If \(f(1)=a+b\) and \(f(c)=a-b\), their average extracts the trivial coefficient \(a\). Half their difference extracts \(b\). The post describes a more constrained averaging step. Its chosen weights keep a family of target characters, while additional twisted sums require estimates.

## References

- Siniša Slijepčević, [Proposition 4.8 and the averaging over translates](https://hexagonmath.org/pdf/2611.00812).
