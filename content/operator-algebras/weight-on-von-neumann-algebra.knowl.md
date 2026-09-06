+++
id = "operator-algebras/weight-on-von-neumann-algebra"
title = "Weight on a von Neumann algebra"
kind = "definition"
summary = "An extended nonnegative additive and positively homogeneous functional on the positive cone of a von Neumann algebra."
aliases = ["positive weight", "extended positive functional"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/positive-cone", "operator-algebras/positive-linear-functional"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
with [[operator-algebras/positive-cone|positive cone]] \(M_+\). A **weight on
\(M\)** is a map
\[
\varphi:M_+\longrightarrow[0,+\infty]
\]
such that \(\varphi(x+y)=\varphi(x)+\varphi(y)\) and
\(\varphi(\lambda x)=\lambda\varphi(x)\) for all \(x,y\in M_+\) and
\(\lambda\geq0\), with \(0\cdot(+\infty)=0\). No boundedness, normality,
faithfulness, or semifiniteness is implicit. If \(\varphi\) is finite on all
of \(M_+\), it extends uniquely to a
[[operator-algebras/positive-linear-functional|positive linear functional]] on
\(M\); otherwise it is genuinely extended-valued and is not a linear
functional on all of \(M\).

## Finite domains

Three domains organize the part of \(M\) on which a weight behaves finitely:
\[
\mathfrak m_\varphi^+=\{x\in M_+:\varphi(x)<\infty\},\qquad
\mathfrak n_\varphi=\{a\in M:\varphi(a^*a)<\infty\},
\]
and \(\mathfrak m_\varphi=\operatorname{span}\mathfrak m_\varphi^+\).
The set \(\mathfrak n_\varphi\) is a left ideal, while
\[
\mathfrak m_\varphi
=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\}
\]
is a \(*\)-subalgebra on which \(\varphi\) has a linear extension. This
extension need not be bounded or defined on all of \(M\).

## Regularity properties

Faithfulness, normality, and semifiniteness impose independent conditions. A
[[operator-algebras/faithful-weight|faithful weight]] detects every nonzero
positive element. A [[operator-algebras/normal-weight|normal weight]] preserves
suprema of increasing nets in \(M_+\). A
[[operator-algebras/semifinite-weight|semifinite weight]] has enough
finite-weight positive elements to be order-dense in \(M_+\). A weight having
all three properties is called faithful, normal, and semifinite, often
abbreviated FNS; this is a hypothesis, not part of the word “weight.”

## Examples and scope

Every positive linear functional on \(M\) restricts to a finite weight on
\(M_+\). On \(B(H)\), the
[[operator-algebras/operator-trace|canonical operator trace]] is a weight that
may take the value \(+\infty\); it is faithful, normal, and semifinite. By
contrast, assigning \(0\) to \(0\) and \(+\infty\) to every nonzero positive
element is a weight, but it is neither semifinite nor useful as a linear
functional. Weights are defined on positive elements so that extended values
can be added without trying to form undefined expressions such as
\(+\infty-(+\infty)\).

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VII, §1 on weights and their finite domains.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the chapters on densely defined weights and positive functionals.
