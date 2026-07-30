+++
id = "formal-groups/positive-characteristic-warning"
title = "Why tangent Lie algebras do not classify formal groups in positive characteristic"
kind = "comparison"
summary = "In characteristic p, height, the p-series, Frobenius, and restricted structure contain information invisible to the ordinary tangent bracket."
aliases = ["positive-characteristic formal group warning", "failure of formal Lie correspondence in characteristic p", "height of a formal group law"]
domains = ["formal-groups", "lie-groups"]
section_mode = "progressive"
+++

Over a field \(k\) of characteristic \(p>0\), the tangent Lie algebra functor
from finite-dimensional formal groups is **not** an equivalence. Distinct
formal groups can have isomorphic tangent Lie algebras because the tangent
space records only first-order multiplication, while Frobenius and the
\(p\)-series begin at higher order.

## Basic counterexample

For the additive and multiplicative one-dimensional laws,
\[
F_a(X,Y)=X+Y,\qquad F_m(X,Y)=X+Y+XY,
\]
both tangent Lie algebras are the one-dimensional abelian algebra. Yet
\[
[p]_{F_a}(X)=0,
\qquad
[p]_{F_m}(X)=(1+X)^p-1=X^p.
\]
An isomorphism of formal group laws must intertwine the \(p\)-series, so these
two laws are not isomorphic.

## Height

For a one-dimensional commutative formal group law over a field of
characteristic \(p\), either \([p]_F(X)=0\), in which case its height is
\(\infty\), or the first nonzero term has the form
\[
[p]_F(X)=aX^{p^h}+\text{higher terms},\qquad a\neq0.
\]
The integer \(h\) is the **height**. The additive law has height \(\infty\)
and the multiplicative law has height \(1\). Height is invisible in the
ordinary one-dimensional tangent Lie algebra.

## Additional structure is not a complete repair

For suitable group schemes, tangent Lie algebras in characteristic \(p\) carry
a restricted \(p\)-operation. This is an important enrichment, but it still
does not replace the full formal group, its Frobenius and Verschiebung
operators, or its complete \(p\)-series. Cartier–Dieudonné modules and related
theories provide finer classifications under additional commutativity,
finiteness, and perfection hypotheses.

## Consequence for the characteristic-zero theorem

The rational coefficients in the BCH series and formal logarithm are not
cosmetic. Division by integers is precisely what allows higher formal data to
be reconstructed from the bracket in characteristic zero. No such
reconstruction can be asserted after reducing modulo \(p\).

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 3–5, \(p\)-typical laws, height, and Cartier–Dieudonné theory.
2. A. Fröhlich, *Formal Groups*, Lecture Notes in Mathematics 74, Springer, 1968. [Publisher record](https://link.springer.com/book/10.1007/BFb0074373). Relevant: Chapters 3–4, one-dimensional commutative formal groups.
