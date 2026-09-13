+++
id = "measure-theory/bochner-integral"
title = "Bochner integral"
kind = "definition"
summary = "The norm limit of integrals of simple Banach-valued functions approximating in integral norm."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "measure-theory/simple-function", "measure-theory/lebesgue-integral", "measure-theory/almost-everywhere", "measure-theory/strongly-measurable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(X\) be a [[linear-algebra/banach-space|Banach space]]. For an integrable simple function \(s=\sum_jx_j\mathbf1_{E_j}\), set \(\int s\,d\mu=\sum_jx_j\mu(E_j)\). A [[measure-theory/strongly-measurable-function|strongly measurable]] function \(f\) is **Bochner integrable** if it admits such simple functions \(s_n\) with
\[
\int\|f-s_n\|_X\,d\mu\longrightarrow0.
\]
Its integral is \(\lim_n\int s_n\,d\mu\) in \(X\). The estimate \(\|\int s\|\le\int\|s\|\) shows that this limit exists and is independent of the approximations.

## Criterion and bound

Equivalently, \(f\) is an almost-everywhere pointwise norm limit of measurable simple functions and \(\int\|f\|_X\,d\mu<\infty\). This is [[measure-theory/strongly-measurable-function|strong measurability]]. The integral satisfies \(\|\int f\|_X\le\int\|f\|_X\), and bounded linear operators commute with it.

## References

- [John K. Hunter, Notes on Partial Differential Equations, Appendix 6.A](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
