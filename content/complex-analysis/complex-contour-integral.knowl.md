+++
id = "complex-analysis/complex-contour-integral"
title = "Complex contour integral"
kind = "definition"
summary = "The integral of a complex-valued function along an oriented parametrized curve."
aliases = ["contour integral", "complex line integral"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(\gamma:[a,b]\to\mathbb C\) be piecewise \(C^1\), and let \(f\) be continuous on the image of \(\gamma\). The **complex contour integral** of \(f\) along \(\gamma\) is
\[
\int_\gamma f(z)\,dz
=\int_a^b f(\gamma(t))\gamma'(t)\,dt,
\]
with the ordinary integral taken separately in real and imaginary parts on each smooth piece.

## Invariance and orientation

The integral is invariant under orientation-preserving piecewise \(C^1\) reparametrization. Reversing orientation changes its sign, and concatenating compatible curves adds their integrals. The value depends on the parametrized oriented contour, not merely on its image.

## Basic estimate

If \(L(\gamma)\) is the length of the contour, then
\[
\left|\int_\gamma f(z)\,dz\right|
\le L(\gamma)\max_{z\in\gamma([a,b])}|f(z)|.
\]
This estimate underlies convergence arguments and the derivative estimates obtained from the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]].

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter IV, §1.
