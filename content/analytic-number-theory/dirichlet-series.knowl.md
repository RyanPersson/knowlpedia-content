+++
id = "analytic-number-theory/dirichlet-series"
title = "Dirichlet series"
kind = "definition"
summary = "A series of complex coefficients weighted by inverse powers of their positive integer indices."
aliases = []
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "real-analysis/natural-logarithm"]
+++

An **ordinary Dirichlet series** has the form
\[
F(s)=\sum_{n=1}^{\infty}a_n n^{-s},
\qquad n^{-s}=\exp(-s\log n),
\]
where \(s\) and the coefficients \(a_n\) are [[shared-foundations/complex-numbers-c|complex numbers]] and \(\log\) is the [[real-analysis/natural-logarithm|natural logarithm]]. At each \(s\) where the partial sums converge, their limit defines \(F(s)\).

## The boundary of convergence

If a Dirichlet series converges at \(s_0\), it converges at every \(s\) with \(\operatorname{Re}s>\operatorname{Re}s_0\). The *abscissa of convergence* \(\sigma_c\) separates the open half-plane of convergence from the open half-plane of divergence. The values \(-\infty\) and \(+\infty\) allow for series converging everywhere or nowhere. For \(a_n=1\) the series gives the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]] on \(\operatorname{Re}s>1\). Its abscissa is \(1\), where the harmonic series diverges.

## References

- Kiran Kedlaya, [Notes on analytic number theory, §2.1, Dirichlet series](https://kskedlaya.org/ant/part-1-3.html).
