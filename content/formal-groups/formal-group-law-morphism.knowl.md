+++
id = "formal-groups/formal-group-law-morphism"
title = "Morphism of formal group laws"
kind = "definition"
summary = "A pointed tuple of power series intertwining two formal group laws, with isomorphisms and strict isomorphisms distinguished by their linear terms."
aliases = ["formal group law homomorphism", "homomorphism of formal group laws", "strict isomorphism of formal group laws", "coordinate change of formal group laws"]
domains = ["formal-groups"]
section_mode = "progressive"
+++

Let \(F\) be an \(n\)-dimensional [[formal-groups/formal-group-law|formal group
law]] over \(R\), and let \(G\) be \(m\)-dimensional. A **morphism of formal
group laws**
\[
f:F\longrightarrow G
\]
is a tuple \(f(X)\in(X)R[[X_1,\ldots,X_n]]^m\) satisfying
\[
f(F(X,Y))=G(f(X),f(Y)).
\]
Composition is [[algebra-rings/substitution-of-formal-power-series|formal
substitution]], and the identity morphism is the coordinate tuple \(X\).

## Isomorphisms and strict isomorphisms

When \(m=n\), the morphism \(f\) is an **isomorphism** precisely when its
linear coefficient matrix \(Df(0)\) lies in \(\operatorname{GL}_n(R)\).
The [[algebra-rings/formal-inverse-function-theorem|formal inverse function
theorem]] then supplies a unique compositional inverse, and the homomorphism
identity shows that inverse also respects the laws.

An isomorphism is **strict** when
\[
Df(0)=I_n.
\]
Thus every strict isomorphism preserves the chosen tangent coordinates to first
order, while a general isomorphism may also change the tangent basis.

## Coordinate changes

An invertible pointed tuple \(f\) transports a law \(F\) to a law \(G\) by
requiring
\[
f(F(X,Y))=G(f(X),f(Y)).
\]
This is a change of coordinates on the same coordinate-free formal group.
Accordingly, properties invariant under formal-group-law isomorphism do not
depend on the selected parameters.

## Tangent functor

Taking linear terms sends \(f\) to
\[
Df(0):T_0F\longrightarrow T_0G.
\]
It is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]] for
the tangent brackets. Over a characteristic-zero field, every
finite-dimensional Lie algebra homomorphism integrates to one and only one
formal-group-law morphism.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 1, 2, and 4, homomorphisms and strict isomorphisms.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, second edition, Springer, 1992. [Publisher record](https://link.springer.com/book/10.1007/978-3-540-70634-2). Relevant: Part I, morphisms in formal Lie theory.
