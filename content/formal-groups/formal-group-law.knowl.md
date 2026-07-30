+++
id = "formal-groups/formal-group-law"
title = "Formal group law"
kind = "definition"
summary = "An n-dimensional, not necessarily commutative group multiplication encoded by tuples of formal power series."
aliases = ["n-dimensional formal group law", "multidimensional formal group law"]
domains = ["formal-groups", "algebra-rings"]
section_mode = "progressive"
+++

Let \(R\) be a commutative ring and write
\(X=(X_1,\ldots,X_n)\), \(Y=(Y_1,\ldots,Y_n)\). An
**\(n\)-dimensional formal group law over \(R\)** is a tuple
\[
F(X,Y)=(F_1(X,Y),\ldots,F_n(X,Y))
\in R[[X,Y]]^n
\]
satisfying the identities
\[
F(X,0)=X,\qquad F(0,Y)=Y,
\]
\[
F(F(X,Y),Z)=F(X,F(Y,Z)),
\]
and admitting a tuple \(i(X)\in(X)R[[X]]^n\) with
\[
F(X,i(X))=0=F(i(X),X).
\]
All identities are identities of
[[algebra-rings/multivariable-formal-power-series-ring|formal power series]],
interpreted using [[algebra-rings/substitution-of-formal-power-series|formal
substitution]].

## Linear and higher-order terms

The unit identities force
\[
F(X,Y)=X+Y+\text{terms of total degree at least \(2\)}.
\]
They also make the inverse tuple exist uniquely by recursive degree. Including
the inverse axiom in the definition emphasizes the group structure.

No commutativity axiom is imposed here. A law is **commutative** when
\(F(X,Y)=F(Y,X)\). In particular, the
[[formal-groups/one-dimensional-formal-group-law|classical one-dimensional
commutative convention]] is a narrower use of “formal group law.”

## Geometric meaning

The tuple \(F\) is the coordinate expression for multiplication on a pointed
[[formal-groups/formal-affine-space|formal \(n\)-disc]]. Choosing coordinates
turns a suitable [[formal-groups/formal-group|formal group]] into a formal
group law, and changing coordinates produces an isomorphic law. This
relationship is made exact by
[[formal-groups/formal-group-laws-as-coordinates|the coordinate equivalence]].

## Tangent bracket

Write
\[
F(X,Y)=X+Y+B(X,Y)+O(3),
\]
where \(B\) is bilinear. The antisymmetric part
\[
[u,v]=B(u,v)-B(v,u)
\]
is the bracket on the
[[formal-groups/tangent-lie-algebra|tangent Lie algebra]]. Over a
characteristic-zero field this tangent algebra determines the isomorphism
class of the finite-dimensional law. More precisely, every specified
homomorphism of tangent Lie algebras integrates to a unique formal-group-law
homomorphism; an isomorphism of tangent Lie algebras therefore integrates to a
unique isomorphism of laws.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 1–2, one- and higher-dimensional formal group laws.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, second edition, Springer, 1992. [Publisher record](https://link.springer.com/book/10.1007/978-3-540-70634-2). Relevant: Part I, formal groups and Lie algebras.
