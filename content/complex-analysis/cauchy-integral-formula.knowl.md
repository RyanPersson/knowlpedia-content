+++
id = "complex-analysis/cauchy-integral-formula"
title = "Cauchy integral formula"
kind = "theorem"
summary = "A holomorphic function and all its derivatives are recovered from boundary values."
aliases = ["Cauchy's integral formula"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/winding-number"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be open, let \(f\) be holomorphic on \(D\), and let \(\gamma\) be a closed piecewise \(C^1\) contour whose image lies in \(D\) and whose [[complex-analysis/winding-number|index]] vanishes outside \(D\). For every \(a\in D\setminus\gamma\),
\[
\operatorname{Ind}(\gamma,a)f(a)
=\frac{1}{2\pi i}\int_\gamma\frac{f(z)}{z-a}\,dz.
\]

## Derivatives

Differentiation under the integral gives, for \(n\ge0\),
\[
\operatorname{Ind}(\gamma,a)f^{(n)}(a)
=\frac{n!}{2\pi i}\int_\gamma\frac{f(z)}{(z-a)^{n+1}}\,dz.
\]
For a positively oriented circle contained with its interior in \(D\), the index is \(1\) inside. The derivative formula proves that holomorphic functions are infinitely differentiable and supplies Cauchy estimates.

## Consequences

The formula is the main local engine behind [[complex-analysis/holomorphic-functions-are-analytic|analyticity]], the [[complex-analysis/maximum-modulus-principle|maximum modulus principle]], and [[complex-analysis/liouville-theorem|Liouville's theorem]].

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter IV, §5.
