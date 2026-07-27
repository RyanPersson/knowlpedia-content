+++
id = "functional-analysis/spectral-integral"
title = "Spectral integral"
kind = "construction"
summary = "An operator obtained by integrating a measurable scalar function against a projection-valued measure."
aliases = ["integration against a projection-valued measure", "operator-valued spectral integral"]
domains = ["functional-analysis", "measure-theory"]
section_mode = "progressive"
+++

Let \(E:\Sigma\to\mathcal B(\mathcal H)\) be a [[functional-analysis/projection-valued-measure|projection-valued measure]] on \(X\), and let \(f:X\to\mathbb C\) be [[measure-theory/measurable-function|measurable]]. The **spectral integral**
\[
\int_X f\,dE
\]
is first defined for simple \(f=\sum_k a_k1_{A_k}\) by \(\sum_k a_kE(A_k)\). For general \(f\), it is the operator obtained by measurable approximation, with domain
\[
D_f=\left\{\xi\in\mathcal H:\int_X|f|^2\,d\langle E(\,\cdot\,)\xi,\xi\rangle<\infty\right\}.
\]
Here the displayed scalar integral is a [[measure-theory/lebesgue-integral|Lebesgue integral]], and this domain is part of the construction. If \(f\) is essentially bounded relative to \(E\), the spectral integral is a bounded operator defined on all of \(\mathcal H\).

## Algebraic and analytic properties

For bounded measurable functions, spectral integration is a unital \(*\)-homomorphism into \(\mathcal B(\mathcal H)\): sums, products, complex conjugation, and uniform limits pass to the corresponding operator operations. Moreover,
\[
\left\|\int_X f\,dE\right\|=\operatorname*{ess\,sup}_{E}|f|.
\]
For unbounded \(f\), the spectral integral is a closed densely defined normal operator, and domain conditions are required before manipulating sums or products.

## Functional calculus

If \(A\) is self-adjoint with spectral measure \(E_A\), then its [[functional-analysis/borel-functional-calculus|measurable functional calculus]] is
\[
f(A)=\int_{\mathbb R}f(\lambda)\,dE_A(\lambda).
\]
In particular, \(A=\int_{\mathbb R}\lambda\,dE_A(\lambda)\), where the unbounded coordinate function determines the domain. Characteristic functions recover spectral projections: \(1_B(A)=E_A(B)\).

## Conventions and scope

The scalar measure \(\langle E(\,\cdot\,)\xi,\xi\rangle\) depends on \(\xi\), so the displayed domain condition is stronger than ordinary scalar integrability against one fixed measure. “Spectral integral” here means integration against a projection-valued measure, not a general integral of Banach-space-valued functions. Equal functions modulo \(E\)-null sets yield the same operator.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [DOI record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VII on spectral measures and functional calculus.
2. Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II: Spectral Theory*, Wiley-Interscience, 1963. [Publisher record](https://www.wiley.com/en-us/Linear+Operators%2C+Part+2%3A+Spectral+Theory-p-9780471608479). Relevant: Chapter X on spectral operators and operator-valued integration.
