+++
id = "formal-groups/formal-affine-space"
title = "Formal affine space"
kind = "definition"
summary = "The formal n-disc with its origin, coordinates, and n-dimensional tangent space."
aliases = ["formal n-disc", "formal disk", "formal disc", "formal affine n-space"]
domains = ["formal-groups", "algebraic-geometry-foundations"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a field. The **formal affine \(n\)-space**, or **formal
\(n\)-disc**, over \(k\) is
\[
\widehat{\mathbb A}^{\,n}_k
:=
\operatorname{Spf}k[[X_1,\ldots,X_n]],
\]
where the power-series ring has its
\((X_1,\ldots,X_n)\)-adic topology. Its distinguished origin is induced by
the augmentation \(k[[X_1,\ldots,X_n]]\to k\), \(X_i\mapsto0\).

## Coordinates and tangent space

The elements \(X_1,\ldots,X_n\) are formal coordinates. If
\(\mathfrak m=(X_1,\ldots,X_n)\), the cotangent space at the origin is
\(\mathfrak m/\mathfrak m^2\), and the [[differential-geometry/tangent-space|tangent space]] is
\[
T_0\widehat{\mathbb A}^{\,n}_k
=\operatorname{Hom}_k(\mathfrak m/\mathfrak m^2,k)
\cong k^n.
\]
Thus the dimension \(n\) is the dimension of the tangent space, even though
the underlying topological space of the [[algebraic-geometry-foundations/formal-spectrum|formal spectrum]] has only one point.

## Pointed maps

A pointed morphism
\[
\widehat{\mathbb A}^{\,n}_k\longrightarrow
\widehat{\mathbb A}^{\,m}_k
\]
is represented contravariantly by an \(m\)-tuple of series in
\((X_1,\ldots,X_n)k[[X_1,\ldots,X_n]]\). Composition of maps is
[[algebra-rings/substitution-of-formal-power-series|formal substitution]].
The map is an isomorphism exactly when its linear term is invertible.

## Products

The product of formal discs is again a formal disc:
\[
\widehat{\mathbb A}^{\,n}_k\times_k
\widehat{\mathbb A}^{\,m}_k
\cong
\widehat{\mathbb A}^{\,n+m}_k.
\]
On coordinate rings this uses the [[algebra-topological/completed-tensor-product|completed tensor product]]
\(k[[X]]\widehat\otimes_k k[[Y]]\cong k[[X,Y]]\).
Consequently a multiplication map on a formal \(n\)-disc is represented by an
\(n\)-tuple of series in the \(2n\) variables \(X,Y\).

## References

1. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). Relevant: affine formal schemes from adic rings.
2. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Appendix A and Chapter 2.
