+++
id = "real-analysis/gamma-function"
title = "Gamma function on positive real arguments"
kind = "definition"
summary = "Euler’s convergent integral interpolates factorials on the positive real axis."
aliases = ["Gamma function", "Euler gamma integral"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integral", "real-analysis/exponential-function", "real-analysis/real-power", "shared-foundations/factorial", "real-analysis/integration-by-parts", "measure-theory/differentiation-under-integral", "real-analysis/natural-logarithm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(a>0\), the **Gamma function** is
\[
\Gamma(a)=\int_0^\infty e^{-v}v^{a-1}\,dv.
\]
The integral converges: \(v^{a-1}\) is integrable near zero, and the [[real-analysis/exponential-function|exponential]] dominates every fixed power at infinity. In particular \(\Gamma(a)>0\).

## Recurrence and smoothness

Integration by parts gives \(\Gamma(a+1)=a\Gamma(a)\), and \(\Gamma(1)=1\), so \(\Gamma(n+1)=n!\) for nonnegative integers. Differentiating under the integral gives smoothness for \(a>0\); powers of \(\log v\) are integrable against a common bound when \(a\) ranges over a compact positive interval. This entry uses only the positive real restriction; complex arguments require the corresponding analytic extension.

## References

- [NIST DLMF, §5.2(i), Euler’s integral for the Gamma function](https://dlmf.nist.gov/5.2#i).
