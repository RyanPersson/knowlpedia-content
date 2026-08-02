+++
id = "complex-analysis/open-mapping-theorem"
title = "Open mapping theorem for holomorphic functions"
kind = "theorem"
summary = "A nonconstant holomorphic function on a domain sends open sets to open sets."
aliases = ["holomorphic open mapping theorem"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

If \(D\subseteq\mathbb C\) is a [[complex-analysis/complex-domain|domain]] and \(f:D\to\mathbb C\) is nonconstant and holomorphic, then \(f\) is an open map: \(f(U)\) is open in \(\mathbb C\) for every open \(U\subseteq D\).

## Local mechanism

Near \(a\in D\), factor
\[
f(z)-f(a)=(z-a)^m g(z),\qquad g(a)\ne0.
\]
Small circles around \(a\) therefore wind \(m\) times around \(f(a)\), forcing the image of a small neighborhood to contain a neighborhood of \(f(a)\).

## Consequences

A bijective holomorphic map between plane domains has holomorphic inverse: continuity of the inverse follows because the map is open, and local [[complex-analysis/complex-derivative|complex differentiability]] follows away from critical points; injectivity rules those out. The theorem also gives a short proof of the [[complex-analysis/maximum-modulus-principle|maximum modulus principle]].

## Disambiguation

This result is distinct from the Banach-space [[functional-analysis/open-mapping-theorem|open mapping theorem]] for bounded surjective linear operators. Its hypotheses and proof are specifically complex analytic.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter III, §7.
