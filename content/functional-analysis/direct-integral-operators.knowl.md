+++
id = "functional-analysis/direct-integral-operators"
title = "Direct integral of operators"
kind = "definition"
summary = "A direct integral operator acts fiberwise by a measurable family of closed operators on a direct integral Hilbert space."
aliases = ["direct integral operator", "fiber integral of operators"]
domains = ["functional-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let \(\{H_x\}_{x\in X}\) be a
[[functional-analysis/measurable-field-hilbert-spaces|measurable field of Hilbert spaces]] over \((X,\mu)\), and let \(A_x\) be a measurable family of
closed [[functional-analysis/densely-defined-operator|densely defined operators]] on the fibers. The **direct integral**
\[
A=\int_X^\oplus A_x\,d\mu(x)
\]
has domain consisting of measurable sections \(\xi\) such that
\(\xi(x)\in\operatorname{Dom}(A_x)\)
[[measure-theory/almost-everywhere|almost everywhere]] and
\(x\mapsto A_x\xi(x)\) is square-integrable; it acts by
\((A\xi)(x)=A_x\xi(x)\). Here measurability of the family can be expressed by
measurability of the graph projections. Operators and families that agree
almost everywhere define the same direct integral.

## Bounded and unbounded cases

If the \(A_x\) are bounded and
\(\operatorname*{ess\,sup}_x\lVert A_x\rVert<\infty\), then \(A\) is the
bounded [[functional-analysis/decomposable-operator|decomposable operator]]
determined by the field. Without a uniform essential bound, the same formula
usually defines an unbounded operator with the stated maximal natural domain.
The graph of \(A\) is the direct integral of the fiber graphs, so closedness
passes from the fibers to \(A\).

## Fiberwise spectral properties

Adjoints and standard operator properties are computed fiberwise under the
measurability hypotheses:
\[
A^*=\int_X^\oplus A_x^*\,d\mu(x).
\]
In particular, \(A\) is self-adjoint when \(A_x\) is self-adjoint almost
everywhere. Fiberwise functional calculus then gives
\[
f(A)=\int_X^\oplus f(A_x)\,d\mu(x)
\]
for bounded Borel \(f\). These results are part of the direct-integral

## Examples and scope

For one-dimensional fibers \(H_x=\mathbb C\), the direct integral of scalar
operators \(A_x z=a(x)z\) is the multiplication operator by the measurable
function \(a\) on \(L^2(X,\mu)\), possibly unbounded. A bare family of closed
operators need not be measurable and therefore need not define a direct
integral.

**Warning.** The measurable-family condition has several equivalent
formulations only under standard separability assumptions. These hypotheses
and the choice of measure class must not be suppressed in applications.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §8, direct integrals and decomposable operators.
2. Jacques Dixmier, *Von Neumann Algebras*, North-Holland, 1981. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/27/suppl/C). Relevant: Chapter II, measurable fields and direct integrals of operators.
