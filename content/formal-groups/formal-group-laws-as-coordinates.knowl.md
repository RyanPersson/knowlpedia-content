+++
id = "formal-groups/formal-group-laws-as-coordinates"
title = "Formal group laws as coordinates on formal groups"
kind = "theorem"
summary = "Group structures on a formal disc, expressed in chosen parameters, are exactly formal group laws."
aliases = ["coordinate equivalence for formal groups", "formal groups with parameters", "formal group law coordinate presentation"]
domains = ["formal-groups"]
prerequisites = ["formal-groups/formal-affine-space", "formal-groups/formal-group-law", "formal-groups/formal-group-law-morphism"]
dependency_review_count = 1
section_mode = "progressive"
+++

Fix a commutative base field \(k\) and \(n\geq0\). Giving a group-object
structure on the pointed [[formal-groups/formal-affine-space|formal disc]]
\[
\widehat{\mathbb A}^{\,n}_k
=\operatorname{Spf}k[[X_1,\ldots,X_n]]
\]
is equivalent to giving an \(n\)-dimensional
[[formal-groups/formal-group-law|formal group law]] over \(k\). Under this
equivalence, formal group homomorphisms are exactly
[[formal-groups/formal-group-law-morphism|morphisms of formal group laws]] in
the chosen coordinates.

## The coordinate calculation

The product of two formal \(n\)-discs has coordinate ring \(k[[X,Y]]\).
Because morphisms of formal spectra reverse arrows, multiplication
\[
m:\widehat{\mathbb A}^{\,n}_k\times
\widehat{\mathbb A}^{\,n}_k\longrightarrow
\widehat{\mathbb A}^{\,n}_k
\]
is determined by a continuous homomorphism
\[
m^*:k[[X]]\longrightarrow k[[X,Y]],\qquad
X_i\longmapsto F_i(X,Y).
\]
The unit, associativity, and inverse diagrams dualize exactly to the unit,
associativity, and inverse identities for \(F\).

A pointed formal map \(f\) between two such [[algebra-category-theory/group-object|group objects]] is represented by a
tuple of zero-constant-term series. The group-homomorphism square dualizes to
\[
f(F(X,Y))=G(f(X),f(Y)).
\]
Thus both objects and morphisms agree, not only their isomorphism classes.

## Coordinate Hopf-algebra formula

For a group law \(F=(F_1,\ldots,F_n)\), the coordinate ring
\(A=k[[x_1,\ldots,x_n]]\) has comultiplication
\[
\Delta(x_i)=F_i(x_1,\ldots,x_n,y_1,\ldots,y_n)
\in
A\widehat\otimes_kA\cong k[[x_1,\ldots,x_n,y_1,\ldots,y_n]].
\]
The counit sends \(x_i\) to \(0\), and the antipode sends \(x_i\) to the
\(i\)-th component of the inverse power series. These maps form the
[[formal-groups/coordinate-hopf-algebra|coordinate Hopf algebra]] of the
formal group.

## Chosen coordinates versus intrinsic objects

For a [[formal-groups/formal-group|formal group]] whose underlying pointed
[[algebraic-geometry-foundations/formal-scheme|formal scheme]] is merely *isomorphic* to a formal disc, one must first choose
such an isomorphism. A different choice transports \(F\) by an invertible
pointed substitution. The coordinate-free group is independent of that
choice.

This distinction matters categorically: formal group laws are presentations
by parameters, while the formal group is the represented geometric object.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 2 and 7, power-series and bialgebra descriptions.
2. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). Relevant: the anti-equivalence between affine formal schemes and admissible topological rings.
