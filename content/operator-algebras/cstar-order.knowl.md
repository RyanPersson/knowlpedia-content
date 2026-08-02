+++
id = "operator-algebras/cstar-order"
title = "Order on self-adjoint elements"
kind = "definition"
summary = "The partial order whose nonnegative elements are the positive elements of a C-star algebra."
aliases = ["C*-algebra order"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]], and write
\(A_{\mathrm{sa}}\) for its
self-adjoint part. The **\(C^*\)-algebra order** on \(A_{\mathrm{sa}}\) is
defined by
\[
a\leq b\quad\Longleftrightarrow\quad b-a\in A_+.
\]
Here \(A_+\) is the [[operator-algebras/positive-cone|positive cone]] of
\(A\).
Equivalently, \(a\leq b\) when \(b-a=c^*c\) for some \(c\in A\). This is a
[[shared-foundations/partial-order|partial order]] compatible with addition and multiplication by nonnegative real
scalars. Positivity therefore supplies the order intrinsically; no external
cone is chosen. The order is defined on self-adjoint elements; arbitrary
elements of \(A\) are not compared unless a separate convention is supplied.

## Order-preserving operations

If \(a\leq b\), then \(x^*ax\leq x^*bx\) for every \(x\in A\). Consequently,
every [[operator-algebras/positive-linear-map|positive linear map]] is
order-preserving on self-adjoint elements, and every \(*\)-homomorphism is
positive. The
[[operator-algebras/continuous-functional-calculus|continuous functional calculus]]
also makes increasing
operator-monotone functions order preserving on their domains.

## Examples and incomparability

For \(A=C_0(X)\), the order is pointwise:
\(f\leq g\) exactly when \(f(x)\leq g(x)\) for all \(x\in X\). In
\(M_2(\mathbb C)\), the projections
\(\operatorname{diag}(1,0)\) and \(\operatorname{diag}(0,1)\) are
incomparable, since their difference has both a positive and a negative
eigenvalue. Thus this order is usually not total.

## Noncommutative caution

Multiplication need not preserve order. Even if \(0\leq a\leq b\), the product
\(xa\) need not be self-adjoint and hence need not be comparable with \(xb\).
The conjugated inequality \(x^*ax\leq x^*bx\) is the valid replacement. The
order should also not be confused with an ordering of the complex [[linear-algebra/vector-space|vector space]]
\(A\); it lives on the real vector space \(A_{\mathrm{sa}}\).

## References

1. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the introductory chapters on positive elements and the order of the self-adjoint part.
2. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: the chapter on positive elements and positive maps.
