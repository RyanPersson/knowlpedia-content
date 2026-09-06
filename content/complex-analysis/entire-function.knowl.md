+++
id = "complex-analysis/entire-function"
title = "Entire function"
kind = "definition"
summary = "A complex-valued function holomorphic on the whole complex plane."
aliases = ["entire holomorphic function"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/complex-derivative", "differential-geometry/holomorphic-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **entire function** is a function \(f:\mathbb C\to\mathbb C\) that is [[differential-geometry/holomorphic-map|holomorphic]] at every point of the complex plane.

## Power-series form

By [[complex-analysis/holomorphic-functions-are-analytic|analyticity of holomorphic functions]], an entire function has a Taylor expansion about every \(a\in\mathbb C\) with infinite radius of convergence:
\[
f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(z-a)^n.
\]
Conversely, any complex [[real-analysis/power-series|power series]] of infinite radius defines an entire function.

## Growth and rigidity

Polynomials, \(e^z\), \(\sin z\), and \(\cos z\) are entire. [[complex-analysis/rational-function|Rational functions]] with poles are not. The [[complex-analysis/liouville-theorem|Liouville theorem]] says that a bounded entire function is constant. More generally, if \(|f(z)|\le C(1+|z|^m)\), then \(f\) is a polynomial of degree at most \(m\).

## Behavior at infinity

Regard \(f\) near \(\infty\) through \(g(w)=f(1/w)\). The point \(\infty\) is removable exactly when \(f\) is constant, a pole exactly when \(f\) is a nonconstant polynomial, and an essential singularity exactly when \(f\) is transcendental entire.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapters III and V.
