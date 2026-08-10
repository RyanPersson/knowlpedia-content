+++
id = "lie-groups/exterior-algebra-of-a-direct-sum"
title = "Exterior algebra of a direct sum"
kind = "theorem"
summary = "The canonical graded-algebra isomorphism between the exterior algebra of a direct sum and a graded tensor product."
aliases = ["exterior algebra direct-sum formula", "wedge algebra of a direct sum", "Lambda of V direct sum W"]
domains = ["lie-groups", "algebra-modules", "linear-algebra"]
section_mode = "progressive"
+++

Let \(V\) and \(W\) be modules over a commutative ring. There is a canonical isomorphism of graded algebras
\[
\Lambda(V\oplus W)\cong \Lambda V\,\widehat\otimes\,\Lambda W,
\]
where \(\widehat\otimes\) is the graded tensor product. Under this isomorphism,
\[
(v,0)\longmapsto v\otimes1,
\qquad
(0,w)\longmapsto1\otimes w.
\]

The multiplication on the right uses the Koszul sign rule
\[
(a\otimes b)(a'\otimes b')
=(-1)^{\deg(b)\deg(a')}(a\wedge a')\otimes(b\wedge b')
\]
for homogeneous elements.

## Degree-by-degree form

Taking the homogeneous part of degree \(k\) gives a canonical decomposition
\[
\Lambda^k(V\oplus W)
\cong
\bigoplus_{p+q=k}\Lambda^pV\otimes\Lambda^qW.
\]
Explicitly, the summand indexed by \((p,q)\) maps
\[
(v_1\wedge\cdots\wedge v_p)\otimes
(w_1\wedge\cdots\wedge w_q)
\]
to the wedge of the corresponding vectors in \(V\oplus W\), with all \(V\)-vectors written before the \(W\)-vectors. The graded sign rule makes this prescription independent of how products are regrouped.

## Equivariance

If a group or Lie algebra acts on both \(V\) and \(W\), the direct sum carries the diagonal action and the displayed isomorphisms are equivariant. In terms of [[lie-groups/exterior-power-representation|exterior-power representations]],
\[
\Lambda^k(V\oplus W)
\cong
\bigoplus_{p+q=k}\Lambda^pV\otimes\Lambda^qW
\]
is therefore an isomorphism of representations.

Setting \(k=\dim V+\dim W\) recovers the determinant identity
\[
\det(V\oplus W)\cong\det(V)\otimes\det(W).
\]

## Why the tensor product must be graded

Using the ordinary ungraded tensor-product multiplication would make elements from \(V\) commute with elements from \(W\). In \(\Lambda(V\oplus W)\) they anticommute in degree one, so the Koszul sign is essential.

## References

1. Nicolas Bourbaki, *Algebra I: Chapters 1–3*, Springer, 1989, Chapter III. [Publisher record](https://doi.org/10.1007/978-3-642-61698-3).
2. Christian Kassel, *Quantum Groups*, Springer, 1995, Chapter XI, §1. [Publisher record](https://doi.org/10.1007/978-1-4612-0783-2).
