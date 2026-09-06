+++
id = "operator-algebras/left-ideal-of-weight"
title = "Left ideal of a weight"
kind = "definition"
summary = "The elements whose positive square has finite value under a weight."
aliases = ["square-integrable ideal of a weight"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/weight-on-von-neumann-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\varphi\) be a
[[operator-algebras/weight-on-von-neumann-algebra|weight]] on a von Neumann
algebra \(M\). The **left ideal of \(\varphi\)** is
\[
\mathfrak n_\varphi
=\{x\in M:\varphi(x^*x)<\infty\}.
\]
It is a complex vector subspace and a left ideal: if \(a\in M\) and
\(x\in\mathfrak n_\varphi\), then
\[
(ax)^*(ax)\leq\|a\|^2x^*x,
\]
so \(ax\in\mathfrak n_\varphi\). It need not be self-adjoint or two-sided.
The terminology “square-integrable” reflects the commutative model, where
\(\varphi\) is integration and the condition says that \(x\) has finite
\(L^2\)-norm.

## Associated finite algebra

The products \(y^*x\), with \(x,y\in\mathfrak n_\varphi\), form the linear
domain
\[
\mathfrak m_\varphi
=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\}.
\]
The weight has a linear extension to this \(*\)-algebra. The
[[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] for weights ensures that
\(\varphi(y^*x)\) is finite on such products.

## Examples and non-examples

For the usual [[operator-algebras/operator-trace|operator trace]] on
\(\mathcal B(H)\), \(\mathfrak n_\varphi\) is the ideal of
[[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operators]], while
\(\mathfrak m_\varphi\) is the
[[functional-analysis/schatten-class-operator|trace-class ideal]]. If
\(\varphi\) is a bounded
[[operator-algebras/positive-linear-functional|positive functional]], then
\(\mathfrak n_\varphi=M\). By contrast, the finite positive domain
\(\{x\in M_+:\varphi(x)<\infty\}\) contains only positive elements and is not
the left ideal used in the
[[operator-algebras/gns-construction-for-weight|GNS construction for the weight]].

## Role in the weight GNS construction

The formula
\[
\langle x,y\rangle_\varphi=\varphi(y^*x)
\]
defines a positive semidefinite [[linear-algebra/inner-product|inner product]] on
\(\mathfrak n_\varphi\). After quotienting by its null space and completing,
left multiplication by \(M\) gives the GNS representation of the weight.
Thus the left-ideal property is precisely what makes the representation
action well defined.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VII, §1 on weights, their left ideals, and semi-cyclic representations.
