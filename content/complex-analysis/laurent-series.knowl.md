+++
id = "complex-analysis/laurent-series"
title = "Laurent series"
kind = "theorem"
summary = "The unique expansion of a holomorphic function in positive and negative powers on an annulus."
aliases = ["Laurent expansion"]
domains = ["complex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

If \(f\) is holomorphic on an annulus
\[
A=\{z:r<|z-a|<R\},
\]
then there is a unique **Laurent series**
\[
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-a)^n
\]
converging absolutely and locally uniformly on \(A\). For any positively oriented circle \(|\zeta-a|=\rho\subset A\),
\[
c_n=\frac{1}{2\pi i}\int_{|\zeta-a|=\rho}
\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta.
\]

## Two-sided convergence

The nonnegative powers form an ordinary [[real-analysis/power-series|power series]] converging for \(|z-a|<R\); the negative powers become a power series in \(1/(z-a)\) converging for \(|z-a|>r\). Their common annulus is the natural domain of the Laurent expansion.

## Principal part

The sum of negative-power terms is the principal part at \(a\). Its pattern classifies an [[complex-analysis/isolated-singularity-classification|isolated singularity]], while \(c_{-1}\) is the [[complex-analysis/residue|residue]].

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 5, §1.
