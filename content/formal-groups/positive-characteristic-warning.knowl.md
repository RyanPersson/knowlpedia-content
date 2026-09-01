+++
id = "formal-groups/positive-characteristic-warning"
title = "Failure of tangent classification in positive characteristic"
kind = "theorem"
summary = "In characteristic p, nonisomorphic formal groups can have isomorphic tangent Lie algebras."
aliases = ["positive-characteristic formal group warning", "failure of formal Lie correspondence in characteristic p"]
domains = ["formal-groups", "lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "formal-groups/formal-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Over a field \(k\) of characteristic \(p>0\), the tangent [[lie-groups/lie-algebra|Lie algebra]] functor
from finite-dimensional [[formal-groups/formal-group|formal groups]] is **not** an equivalence. Distinct
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
An isomorphism of [[formal-groups/formal-group-law|formal group laws]] must intertwine the \(p\)-series, so these
two laws are not isomorphic.

Equivalently, the two laws have different
[[formal-groups/height-of-one-dimensional-formal-group-law|heights]]:
\(F_a\) has height \(\infty\), while \(F_m\) has height \(1\). Height is
invisible in the ordinary one-dimensional tangent Lie algebra.

## Additional structure is not a complete repair

For suitable [[algebraic-geometry-foundations/group-scheme|group schemes]], tangent Lie algebras in characteristic \(p\) carry
a restricted \(p\)-operation. This is an important enrichment, but it still
does not replace the full formal group, its Frobenius and Verschiebung
operators, or its complete \(p\)-series. Cartier–Dieudonné modules and related
theories provide finer classifications under additional commutativity,
finiteness, and perfection hypotheses.

## Consequence for the characteristic-zero theorem

The rational coefficients in the BCH series and [[formal-groups/formal-group-logarithm|formal logarithm]] are not
cosmetic. Division by integers is precisely what allows higher formal data to
be reconstructed from the bracket in characteristic zero. No such
reconstruction can be asserted after reducing modulo \(p\).

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 3–5, \(p\)-typical laws, height, and Cartier–Dieudonné theory.
2. A. Fröhlich, *Formal Groups*, Lecture Notes in Mathematics 74, Springer, 1968. [Publisher record](https://link.springer.com/book/10.1007/BFb0074373). Relevant: Chapters 3–4, one-dimensional commutative formal groups.
