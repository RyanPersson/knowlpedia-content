+++
id = "real-analysis/power-series"
title = "Power series"
kind = "definition"
summary = "A real or complex series in powers of a variable about a chosen center."
aliases = ["power-series", "Power series", "convergent power series"]
domains = ["real-analysis", "complex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/power-series.md"
section_mode = "progressive"
+++

A **power series** over \(\mathbb K=\mathbb R\) or \(\mathbb C\), with coefficients \(c_n\in\mathbb K\) and center \(a\in\mathbb K\), is an expression
\[
\sum_{n=0}^\infty c_n(z-a)^n.
\]
There is a radius \(R\in[0,\infty]\) such that the series converges absolutely for \(|z-a|<R\) and diverges for \(|z-a|>R\). It defines a function on the interval \((a-R,a+R)\) over \(\mathbb R\), or on the open disc \(\{z:|z-a|<R\}\) over \(\mathbb C\).

## Radius and boundary

The Cauchy–Hadamard formula is
\[
\frac1R=\limsup_{n\to\infty}|c_n|^{1/n},
\]
with the usual conventions for \(0\) and \(\infty\). When \(R<\infty\), points satisfying \(|z-a|=R\) must be checked separately; different boundary points of a complex disc may have different convergence behavior.

## Calculus inside the radius

Inside its radius of convergence, a power series may be differentiated and integrated term by term:
\[
\left(\sum_{n=0}^{\infty}c_n(z-a)^n\right)'
=\sum_{n=1}^{\infty}n c_n(z-a)^{n-1}.
\]
The differentiated series has the same radius. Convergence is uniform on every smaller closed interval or disc, which justifies these operations.

## Convergent versus formal

A convergent power series is both a coefficient sequence and a function on a neighborhood of its center. A [[algebra-rings/formal-power-series-ring|formal power series]] is instead an algebraic object whose coefficients are manipulated without any convergence requirement. Two convergent complex power series centered at the same point define the same germ exactly when their coefficients agree, but this analytic uniqueness does not erase the distinction between the two settings.

## Complex analyticity

Every complex power series defines a holomorphic function inside its disc of convergence. Conversely, [[complex-analysis/holomorphic-functions-are-analytic|every holomorphic function is locally given by its Taylor series]], a rigidity absent for general smooth real functions.

## Examples

- The geometric series \(\sum_{n=0}^\infty z^n\) has radius \(1\) and equals \(1/(1-z)\) for \(|z|<1\).
- The exponential series \(\sum_{n=0}^\infty z^n/n!\) has infinite radius of convergence over either \(\mathbb R\) or \(\mathbb C\).

## References

1. Walter Rudin, *Real and Complex Analysis*, 3rd ed., McGraw–Hill, 1987. Relevant: Chapters 3 and 10.
2. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter III.
