+++
id = "functional-analysis/projection-valued-measure"
title = "Projection-valued measure"
kind = "definition"
summary = "A normalized, strongly countably additive measure whose values are orthogonal projections on a Hilbert space."
aliases = ["spectral measure", "resolution of the identity"]
domains = ["functional-analysis", "measure-theory"]
section_mode = "progressive"
+++

Let \((X,\Sigma)\) be a [[measure-theory/measurable-space|measurable space]] and \(H\) a [[linear-algebra/hilbert-space|Hilbert space]]. Write \(\mathcal P(H)\) for the set of [[linear-algebra/orthogonal-projection|orthogonal projections]] on \(H\). A **projection-valued measure** on \((X,\Sigma)\) is a map
\[
E:\Sigma\longrightarrow\mathcal P(H)
\]
such that \(E(X)=I\), \(E(A\cap B)=E(A)E(B)\), and, for every pairwise disjoint sequence \((A_n)\) and every \(\xi\in H\),
\[
E\left(\bigcup_{n=1}^{\infty}A_n\right)\xi
=\sum_{n=1}^{\infty}E(A_n)\xi
\]
with convergence in \(H\). Thus \(E\) is countably additive in the strong operator topology. For \(\xi,\eta\in H\), the scalar function \(A\mapsto\langle E(A)\xi,\eta\rangle\) is a countably additive complex [[measure-theory/measure|measure]].

## Spectral integration

For a bounded [[measure-theory/measurable-function|measurable function]] \(f\), one first sets
\[
\int_X\sum_j c_j1_{A_j}\,dE=\sum_j c_jE(A_j)
\]
and then extends uniformly to define \(\int_X f\,dE\). This construction preserves products, adjoints, and constants, so it is a unital \(*\)-homomorphism from bounded measurable functions into bounded operators. [[measure-theory/indicator-function|Indicator functions]] recover the projections: \(\int_X1_A\,dE=E(A)\).

## Relation to spectral theorems

Every bounded [[quantum-foundations/normal-operator|normal operator]] \(T\) has a unique projection-valued measure on its spectrum for which
\[
T=\int_{\sigma(T)}z\,dE(z).
\]
Conversely, spectral integration of the coordinate function produces a normal operator. For an unbounded self-adjoint operator, define \(\mu_\xi(A)=\langle E(A)\xi,\xi\rangle\); the [[functional-analysis/spectral-integral|spectral integral]] is interpreted on the domain of vectors \(\xi\) satisfying \(\int_{\mathbb R}\lambda^2\,d\mu_\xi(\lambda)<\infty\). These forms of the spectral theorem are developed in [Conway, Chapters IX and X](https://doi.org/10.1007/978-1-4757-4383-8).

## Examples and conventions

If \(H=\bigoplus_nH_n\) is an orthogonal decomposition and \(X=\mathbb N\), then \(E(A)\) projects onto \(\bigoplus_{n\in A}H_n\). This is the discrete model for spectral decomposition.

**Warning.** Some authors allow \(E(X)\neq I\) and call the measure normalized only when equality holds; normalization is part of the definition here. A one-parameter resolution of the identity on \(\mathbb R\) is the cumulative family \(\lambda\mapsto E((-\infty,\lambda])\), not the set-function \(E\) itself.

## References

1. J. B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: chapters on normal operators, spectral measures, and unbounded operators.
