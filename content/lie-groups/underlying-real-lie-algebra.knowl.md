+++
id = "lie-groups/underlying-real-lie-algebra"
title = "Underlying real Lie algebra"
kind = "construction"
summary = "A complex Lie algebra regarded as a real Lie algebra by restricting scalars."
aliases = ["realification of a complex Lie algebra", "restriction of scalars of a complex Lie algebra"]
domains = ["lie-groups", "linear-algebra"]
section_mode = "progressive"
+++

For a complex [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), the **underlying real Lie algebra** \(\mathfrak g_{\mathbb R}\) is obtained by [[linear-algebra/realification-of-a-complex-vector-space|realifying its vector space]]: it has the same additive group and bracket, but scalar multiplication is restricted along \(\mathbb R\hookrightarrow\mathbb C\). If \(\dim_{\mathbb C}\mathfrak g=n\), then
\[
\dim_{\mathbb R}\mathfrak g_{\mathbb R}=2n.
\]
Complex-linear [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphisms]] become real-linear homomorphisms, so \((-)_{\mathbb R}\) is a functor.

## Complex structure retained as extra data

Multiplication by \(i\) defines a real-linear endomorphism \(J\) of \(\mathfrak g_{\mathbb R}\) satisfying \(J^2=-1\) and
\[
[JX,Y]=J[X,Y]=[X,JY].
\]
Forgetting \(J\) can lose information: an isomorphism of the underlying real Lie algebras need not be complex-linear.

This scalar restriction is not the inverse of [[lie-groups/complexification-of-a-real-lie-algebra|complexification]]. In fact,
\[
\mathfrak g_{\mathbb R}\otimes_{\mathbb R}\mathbb C
\cong \mathfrak g\oplus\overline{\mathfrak g}
\]
as complex Lie algebras.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Nathan Jacobson, *Lie Algebras*, Dover, 1979, Chapter I.
