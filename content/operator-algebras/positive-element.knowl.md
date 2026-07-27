+++
id = "operator-algebras/positive-element"
title = "Positive element of a C*-algebra"
kind = "definition"
summary = "A positive element is a self-adjoint C*-algebra element whose spectrum is contained in the nonnegative real axis."
aliases = ["positive C*-element", "nonnegative element of a C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

An element \(a\) of a \(C^*\)-algebra \(A\) is **positive**, written \(a\geq0\), if it is [[operator-algebras/self-adjoint-element|self-adjoint]] and its [[functional-analysis/banach-algebra-spectrum|spectrum]] satisfies \(\sigma_A(a)\subseteq[0,\infty)\). Equivalently, \(a=b^*b\) for some \(b\in A\). Also equivalently, there is a unique positive element \(a^{1/2}\in A\) such that \((a^{1/2})^2=a\). These characterizations agree in unital and nonunital \(C^*\)-algebras; the square root is constructed by the [[operator-algebras/continuous-functional-calculus|continuous functional calculus]]. The positive elements form the cone \(A_+\), which defines the canonical order on the self-adjoint part: \(x\leq y\) exactly when \(y-x\in A_+\).

## The positive cone and order

The set \(A_+\) of positive elements is a norm-closed convex cone, satisfies \(A_+\cap(-A_+)=\{0\}\), and linearly spans \(A\). It defines an order on the self-adjoint part \(A_{\mathrm{sa}}\) by
\[
x\leq y\quad\Longleftrightarrow\quad y-x\in A_+.
\]
[[operator-algebras/positive-linear-functional|Positive functionals]], [[operator-algebras/state-cstar-algebra|states]], [[operator-algebras/weight-on-von-neumann-algebra|weights]], and [[operator-algebras/positive-linear-map|positive maps]] are defined using this cone.

## Concrete interpretation

Under any faithful representation \(A\subseteq B(H)\), abstract positivity agrees with operator positivity:
\[
\langle a\xi,\xi\rangle\geq0
\qquad\text{for every }\xi\in H.
\]
This criterion is representation-independent. Positivity is stronger than self-adjointness: a self-adjoint element with negative spectrum is not positive. It is also not defined by signs of arbitrary coefficients in a presentation of \(A\).

## References

1. G. J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Section 2.2 on positive elements and square roots.
2. G. K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Section 1.2 on positivity and order.
