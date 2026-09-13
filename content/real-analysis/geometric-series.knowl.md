+++
id = "real-analysis/geometric-series"
title = "Geometric series"
kind = "definition"
summary = "A series with constant ratio, with sum a/(1-r) for |r|<1."
aliases = ["geometric progression", "geometric sum"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/convergent-series", "shared-foundations/complex-numbers-c", "real-analysis/monotone-sequence-convergence-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For complex numbers \(a,r\), the **geometric series** with initial term \(a\) and ratio \(r\) is the [[real-analysis/series|series]]
\[
\sum_{n=0}^{\infty} ar^n.
\]
Its [[real-analysis/partial-sums|partial sum]] through index \(N\) is
\[
\sum_{n=0}^{N} ar^n=
\begin{cases}
a(1-r^{N+1})/(1-r),&r\ne1,\\
a(N+1),&r=1.
\end{cases}
\]
For \(r\ne1\), subtracting \(r\) times the finite sum from the sum proves this identity by cancellation.

## Convergence and remainder

For \(0<|r|<1\), the nonnegative decreasing sequence \(|r|^n\) has a limit \(L\) by the [[real-analysis/monotone-sequence-convergence-theorem|monotone sequence convergence theorem]]. Passing to the limit in \(|r|^{n+1}=|r|\,|r|^n\) gives \(L=|r|L\), hence \(L=0\). The case \(r=0\) is immediate. Thus if \(|r|<1\), then \(r^{N+1}\to0\), and the series [[real-analysis/convergent-series|converges]] to \(a/(1-r)\). Its tail satisfies
\[
\sum_{n=N+1}^{\infty}ar^n=\frac{ar^{N+1}}{1-r},\qquad
\left|\sum_{n=N+1}^{\infty}ar^n\right|
\le\frac{|a|\,|r|^{N+1}}{1-|r|}.
\]
If \(a\ne0\) and \(|r|\ge1\), the terms do not tend to zero, so the series diverges. When \(a=0\), every term is zero for every \(r\), taking the zeroth power as \(1\).

## Example

The series \(1+\tfrac12+\tfrac14+\cdots\) has sum \(2\). More generally, if \(|u_n|\le Cr^n\) for \(C\ge0\) and \(0\le r<1\), the [[real-analysis/comparison-test|comparison test]] gives \(\sum_n|u_n|\le C/(1-r)\).
