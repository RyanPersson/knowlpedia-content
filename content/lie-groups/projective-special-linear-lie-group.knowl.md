+++
id = "lie-groups/projective-special-linear-lie-group"
title = "Projective special linear Lie group"
kind = "definition"
summary = "The real or complex special linear Lie group modulo its finite scalar center."
aliases = ["PSL Lie group", "projective unimodular Lie group"]
domains = ["lie-groups", "algebra-groups"]
section_mode = "progressive"
+++

Let \(\mathbb F=\mathbb R\) or \(\mathbb C\), and let \(n\ge2\). The **projective special linear Lie group** is
\[
\operatorname{PSL}_n(\mathbb F)
=\operatorname{SL}_n(\mathbb F)/
\{\lambda I_n:\lambda\in\mathbb F^\times,\ \lambda^n=1\}.
\]
Its denominator is the finite center of the [[lie-groups/special-linear-group|special linear group]], so this is a [[lie-groups/quotient-lie-group|quotient Lie group]] and the projection is a finite covering homomorphism.

## Lie algebra and dimension

Quotienting by a discrete subgroup does not change the Lie algebra. Hence
\[
\operatorname{Lie}(\operatorname{PSL}_n(\mathbb F))
\cong\mathfrak{sl}_n(\mathbb F).
\]
The real group has real dimension \(n^2-1\); the complex group has complex dimension \(n^2-1\), or real dimension \(2(n^2-1)\) after forgetting its complex structure.

## Connectedness and comparison with \(\operatorname{PGL}\)

Both \(\operatorname{SL}_n(\mathbb R)\) and \(\operatorname{SL}_n(\mathbb C)\) are connected for \(n\ge2\), and a continuous quotient of a connected space is connected. Therefore both corresponding \(\operatorname{PSL}\) groups are connected.

Over \(\mathbb C\), every nonzero complex number has an \(n\)-th root, so
\[
\operatorname{PSL}_n(\mathbb C)\cong
\operatorname{PGL}_n(\mathbb C)
\]
as complex Lie groups. Over \(\mathbb R\), \(\operatorname{PSL}_n(\mathbb R)\) is the identity component of \(\operatorname{PGL}_n(\mathbb R)\). The two groups agree for odd \(n\), while \(\operatorname{PSL}_n(\mathbb R)\) has index \(2\) for even \(n\). In particular,
\[
\operatorname{PSL}_2(\mathbb R)
=\operatorname{PGL}_2(\mathbb R)^\circ
\ne\operatorname{PGL}_2(\mathbb R).
\]

## Center versus simple terminology

The quotient removes the scalar center of \(\operatorname{SL}_n\), but the word “simple” depends on whether one means a Lie algebra, a connected Lie group, an algebraic group, or an abstract group of points. Low-dimensional and small-finite-field exceptions should not be suppressed by a blanket simplicity claim.

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3). Relevant: classical matrix groups and covering homomorphisms.
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0). Relevant: Chapter I, linear Lie groups and their centers.
