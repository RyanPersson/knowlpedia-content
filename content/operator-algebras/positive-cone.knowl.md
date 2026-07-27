+++
id = "operator-algebras/positive-cone"
title = "Positive cone of a C*-algebra"
kind = "definition"
summary = "The closed convex cone of positive self-adjoint elements in a C*-algebra."
aliases = ["C*-positive cone", "positive cone A_+"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Its **positive cone** is
\[
A_+=\{a\in A:a=a^*,\ \sigma(a)\subseteq[0,\infty)\}.
\]
Equivalently,
\[
A_+=\{b^*b:b\in A\}=\{c^2:c=c^*\in A\}.
\]
It is a norm-closed [[convex-analysis/convex-set|convex]] cone: \(a,b\in A_+\) and \(s,t\geq0\) imply \(sa+tb\in A_+\). It is proper, meaning \(A_+\cap(-A_+)=\{0\}\). The order on the self-adjoint part \(A_{\mathrm{sa}}\) is defined by \(a\leq b\) exactly when \(b-a\in A_+\).
This cone and the involution recover the distinction between positive,
negative, and incomparable self-adjoint elements; no separate ordering is
chosen as extra structure.

## Square roots and decomposition

Every \(a\in A_+\) has a unique positive square root \(a^{1/2}\in A_+\), obtained from [[operator-algebras/continuous-functional-calculus|continuous functional calculus]], and this proves \(a=(a^{1/2})^*a^{1/2}\). Every self-adjoint element has positive and [[operator-algebras/positive-negative-parts|negative parts]]
\[
a_+=\frac{|a|+a}{2},\qquad a_-=\frac{|a|-a}{2},
\]
with \(a=a_+-a_-\), \(a_+a_-=0\), and \(a_\pm\in A_+\).

## Order-theoretic role

The cone determines the order structure used to define [[operator-algebras/positive-linear-functional|positive functionals]] and [[operator-algebras/positive-linear-map|positive maps]]. A \(*\)-homomorphism preserves the cone because it sends \(b^*b\) to \(\phi(b)^*\phi(b)\). The order is compatible with translation and multiplication by nonnegative scalars, but it is an order only on \(A_{\mathrm{sa}}\), not a total order on all of \(A\).

## Noncommutative caution

Positive elements need not have a positive product. If \(a,b\in A_+\), then \(ab\) is positive exactly when \(a\) and \(b\) commute: positivity forces \(ab=(ab)^*=ba\), while commuting positive elements have a positive product by functional calculus. Thus the cone is closed under addition, not under arbitrary multiplication. It should also not be confused with the set of nonzero or invertible positive elements.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Elsevier DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.2 on positive elements, square roots, and order.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [Elsevier DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §§1.4–1.5 on positivity and functional calculus.
