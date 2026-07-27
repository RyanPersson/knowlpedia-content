+++
id = "functional-analysis/spectral-theorem-unbounded-self-adjoint"
title = "Spectral theorem for unbounded self-adjoint operators"
kind = "theorem"
summary = "Every self-adjoint operator is uniquely represented as a spectral integral against a projection-valued measure on the real line."
aliases = ["unbounded spectral theorem", "spectral resolution theorem"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(A\) be a [[functional-analysis/self-adjoint-unbounded-operator|self-adjoint
operator]] on a complex [[linear-algebra/hilbert-space|Hilbert space]] \(H\). There is a unique
[[functional-analysis/projection-valued-measure|projection-valued measure]]
\(E_A\) on the Borel subsets of \(\mathbb R\) such that
\[
A=\int_{\mathbb R}\lambda\,dE_A(\lambda)
\]
as an unbounded [[functional-analysis/spectral-integral|spectral integral]].
Precisely,
\[
\mathcal D(A)=\left\{\xi\in H:
\int_{\mathbb R}\lambda^2\,d\langle E_A(\lambda)\xi,\xi\rangle<\infty\right\},
\]
and the integral defines \(A\xi\) on this domain. The measure is supported on
the real spectrum of \(A\), so the spectral resolution determines both the
operator and its domain.

## Borel functional calculus

For a Borel function \(f:\mathbb R\to\mathbb C\), the theorem defines
\[
f(A)=\int_{\mathbb R}f(\lambda)\,dE_A(\lambda)
\]
on the vectors \(\xi\) satisfying
\(\int |f(\lambda)|^2\,d\langle E_A(\lambda)\xi,\xi\rangle<\infty\).
Bounded \(f\) give bounded operators on all of \(H\); real-valued \(f\) give
self-adjoint operators. [[measure-theory/indicator-function|Indicator functions]] yield
[[functional-analysis/spectral-projection|spectral projections]], and this
construction extends the continuous calculus to the
[[functional-analysis/borel-functional-calculus|Borel functional calculus]].

## Resolvents and reconstruction

For \(z\in\mathbb C\setminus\mathbb R\),
\[
(A-z)^{-1}=\int_{\mathbb R}(\lambda-z)^{-1}\,dE_A(\lambda).
\]
Conversely, the spectral projections can be recovered from boundary behavior
of the resolvent. The support of \(E_A\) is
[[functional-analysis/spectrum-closed-operator|\(\sigma(A)\)]], and a Borel
set disjoint from the spectrum has zero spectral projection. Conversely, if
an open set \(U\) satisfies \(E_A(U)=0\), then \(U\) is disjoint from the
spectrum. These relations connect the measure-theoretic and resolvent forms of
spectral theory
[Schmüdgen, Chapter 5](https://doi.org/10.1007/978-94-007-4753-1).

## Self-adjointness convention

**Warning.** The theorem requires self-adjointness
\(A=A^*\), including equality of domains. A densely defined [[functional-analysis/symmetric-operator|symmetric operator]]
need not have a real spectrum or a spectral resolution of this form. An
essentially self-adjoint symmetric operator acquires the resolution only after
passing to its self-adjoint closure. For skew-adjoint generators, the theorem
is applied to the self-adjoint operator obtained by multiplication by \(i\) or
\(-i\), according to the generator convention.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VIII on the spectral theorem and functional calculus for self-adjoint operators.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapters 4–5 on spectral measures, spectral integrals, and spectral decompositions.
