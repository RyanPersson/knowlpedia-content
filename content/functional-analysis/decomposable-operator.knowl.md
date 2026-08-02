+++
id = "functional-analysis/decomposable-operator"
title = "Decomposable operator"
kind = "definition"
summary = "A bounded operator on direct integrals that is given almost everywhere by a measurable essentially bounded field of fiber operators."
aliases = ["fiberwise operator", "direct-integral decomposable operator"]
domains = ["functional-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let
\(\mathcal H=\int_X^\oplus H_x\,d\mu(x)\) and
\(\mathcal K=\int_X^\oplus K_x\,d\mu(x)\) be
[[functional-analysis/direct-integral-hilbert-spaces|direct integrals of
Hilbert spaces]]. A bounded operator \(T:\mathcal H\to\mathcal K\) is
**decomposable** if there is a measurable field of bounded operators
\(x\mapsto T_x:H_x\to K_x\), with
\(\operatorname*{ess\,sup}_x\lVert T_x\rVert<\infty\), such that
\[
(T\xi)(x)=T_x\xi(x)
\]
for [[measure-theory/almost-everywhere|almost every]] \(x\) and every
measurable square-integrable section \(\xi\). One writes
\(T=\int_X^\oplus T_x\,d\mu(x)\). The field \(T_x\) is determined up to
equality almost everywhere, and
\(\lVert T\rVert=\operatorname*{ess\,sup}_x\lVert T_x\rVert\).

## Algebraic operations

Sums, products of composable decomposable operators, and adjoints are
decomposable and are computed fiberwise:
\[
(ST)_x=S_xT_x,\qquad (T^*)_x=T_x^*
\]
almost everywhere. Consequently, decomposable operators on a fixed direct
integral form a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
Fiberwise properties such as
self-adjointness, positivity, or unitarity pass to the global operator and
back, modulo [[measure-theory/null-set|null sets]].

## Characterization by diagonal operators

For \(f\in L^\infty(X,\mu)\), let \(M_f\) act diagonally by
\((M_f\xi)(x)=f(x)\xi(x)\). Under the standard separability and
\(\sigma\)-finiteness hypotheses used in direct-integral theory, the
decomposable operators are precisely the bounded operators commuting with
every \(M_f\). Thus decomposability is an intrinsic commutant condition, not
a claim that the fibers \(T_x\) are diagonalizable.

## Examples and scope

A diagonal multiplication operator is decomposable with
\(T_x=f(x)I_{H_x}\). More generally, a measurable essentially bounded family
of matrices defines a decomposable operator on a direct integral of
finite-dimensional fibers. An operator that mixes values at different base
points, such as translation on \(L^2(\mathbb R)\), is generally not
decomposable over the usual position-space decomposition.

**Warning.** Measurability of every matrix coefficient and essential
boundedness require the measurable structures and measure class to be fixed.
A bare pointwise family \(T_x\) need not define an operator on a direct
integral.

## References

1. Jacques Dixmier, *Von Neumann Algebras*, North-Holland, 1981. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/27/suppl/C). Relevant: Chapter II, §2 on decomposable operators.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §8 on direct integrals and decomposable operators.
