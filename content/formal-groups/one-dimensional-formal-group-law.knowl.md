+++
id = "formal-groups/one-dimensional-formal-group-law"
title = "One-dimensional commutative formal group law"
kind = "definition"
summary = "The classical one-variable commutative formal group law F(X,Y) over a commutative ring."
aliases = ["one-dimensional formal group law", "one-parameter formal group law", "commutative formal group law in one dimension"]
domains = ["formal-groups"]
section_mode = "progressive"
+++

Let \(R\) be a commutative ring. A **one-dimensional commutative formal group
law over \(R\)** is a series \(F(X,Y)\in R[[X,Y]]\) satisfying
\[
F(X,0)=X,\qquad F(0,Y)=Y,
\]
\[
F(F(X,Y),Z)=F(X,F(Y,Z)),\qquad F(X,Y)=F(Y,X).
\]
There is then a unique inverse series \(i(X)\in XR[[X]]\) such that
\(F(X,i(X))=0\).

## Convention and scope

In algebraic topology and much of arithmetic geometry, “one-dimensional
formal group law” conventionally includes commutativity. This knowl follows
that convention. The general
[[formal-groups/formal-group-law|\(n\)-dimensional formal group law]] used
elsewhere in this collection does **not** impose commutativity, even when
\(n=1\).

Dimension counts formal parameters, not the number of variables appearing in
the multiplication: a one-dimensional law uses the two inputs \(X\) and
\(Y\), but its underlying formal disc has one coordinate.

## The \(m\)-series

For \(m\in\mathbb Z\), define \([m]_F(X)\) by repeated formal addition, using
the inverse for negative \(m\). The series \([p]_F\) in characteristic \(p\)
determines the
[[formal-groups/height-of-one-dimensional-formal-group-law|height]] of \(F\),
a central invariant that helps explain why
[[formal-groups/positive-characteristic-warning|tangent Lie algebras do not
classify formal groups in positive characteristic]].

## Characteristic zero

Over a \(\mathbb Q\)-algebra, every such law has a unique
[[formal-groups/formal-group-logarithm|strict logarithm]] to the additive law.
This does not trivialize the integral or positive-characteristic theory:
denominators in the logarithm generally prevent descent to the original
coefficient ring.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 1 and 3, one-dimensional commutative laws and \(p\)-typical theory.
2. J. F. Adams, *Stable Homotopy and Generalised Homology*, University of Chicago Press, 1974. Relevant: Part II, formal groups in complex-oriented cohomology.
