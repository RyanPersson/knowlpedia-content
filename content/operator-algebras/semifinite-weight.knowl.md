+++
id = "operator-algebras/semifinite-weight"
title = "Semifinite weight"
kind = "definition"
summary = "A weight whose finite positive elements are order-dense in the positive cone."
aliases = ["semifiniteness of a weight"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let
\(\varphi:M_+\to[0,+\infty]\) be a
[[operator-algebras/weight-on-von-neumann-algebra|weight]]. The weight
\(\varphi\) is **semifinite** if its finite part is order-dense in \(M_+\):
for every nonzero \(x\in M_+\), there exists a nonzero \(y\in M_+\) such that
\[
0\leq y\leq x\qquad\text{and}\qquad\varphi(y)<\infty.
\]
Equivalently, the left ideal
\(\mathfrak n_\varphi=\{a\in M:\varphi(a^*a)<\infty\}\) is dense in \(M\) for
the [[operator-algebras/ultraweak-topology|ultraweak topology]].
Semifiniteness is a domain condition; it does not require faithfulness or
normality and does not assert that \(\varphi\) is finite on every positive
element.

## Approximation by finite elements

If \(\varphi\) is also normal, each \(x\in M_+\) can be recovered as the
supremum of finite-weight positive elements below \(x\). Normality then gives
\[
\varphi(x)=\sup\{\varphi(y):0\leq y\leq x,\ \varphi(y)<\infty\}.
\]
The order approximation and the recovery of the value play different roles:
semifiniteness supplies enough finite elements, while normality makes
\(\varphi\) preserve their increasing supremum
[Takesaki, vol. I, Chapter VII, §1](https://doi.org/10.1007/978-1-4612-6188-9).

## Examples and non-examples

The [[operator-algebras/operator-trace|canonical operator trace]] on \(B(H)\)
is semifinite because every nonzero positive operator dominates a nonzero
finite-rank positive operator of finite trace. Every finite
[[operator-algebras/positive-linear-functional|positive functional]] is
automatically a semifinite weight, whether or not it is faithful, because
every positive element already has finite value. The weight taking
\(+\infty\) on every nonzero positive element is not semifinite. These
examples also show that semifiniteness and faithfulness are independent
conditions.

## Role in integration

For a
[[operator-algebras/normal-semifinite-faithful-weight|faithful normal semifinite weight]],
the finite left ideal \(\mathfrak n_\varphi\) is large enough to build the
weight-GNS Hilbert space, normality controls limits, and faithfulness removes
its null ideal. These three independent hypotheses are the standard starting
point for modular theory. A
[[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann algebra]]
is instead an algebra admitting a faithful normal semifinite trace; it should
not be confused with a particular semifinite weight on an arbitrary algebra.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VII, §1 on semifinite weights and their finite ideals.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: the opening chapters on faithful normal semifinite weights and modular theory.
