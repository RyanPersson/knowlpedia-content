+++
id = "lie-groups/projective-general-linear-lie-group"
title = "Projective general linear Lie group"
kind = "definition"
summary = "The real or complex general linear Lie group modulo its closed central subgroup of scalar matrices."
aliases = ["PGL Lie group", "projective linear Lie group"]
domains = ["lie-groups", "algebra-groups"]
prerequisites = ["lie-groups/quotient-lie-group", "algebra-groups/projective-general-linear-group", "fiber-bundles/smooth-submersion"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathbb F=\mathbb R\) or \(\mathbb C\), and let \(n\ge2\). The **projective general linear Lie group** is the [[lie-groups/quotient-lie-group|quotient Lie group]]
\[
\operatorname{PGL}_n(\mathbb F)
=\operatorname{GL}_n(\mathbb F)/(\mathbb F^\times I_n).
\]
The scalar subgroup is closed and central. Therefore the abstract [[algebra-groups/projective-general-linear-group|projective general linear group]] carries the unique quotient manifold structure for which the projection is a [[fiber-bundles/smooth-submersion|smooth submersion]].

## Dimension and Lie algebra

The scalar subgroup has dimension \(1\) over \(\mathbb F\), so
\[
\dim_{\mathbb R}\operatorname{PGL}_n(\mathbb R)=n^2-1,
\qquad
\dim_{\mathbb C}\operatorname{PGL}_n(\mathbb C)=n^2-1.
\]
The complex group consequently has underlying real dimension \(2(n^2-1)\). Its [[lie-groups/lie-algebra|Lie algebra]] is
\[
\mathfrak{pgl}_n(\mathbb F)
=\mathfrak{gl}_n(\mathbb F)/(\mathbb F I_n).
\]
Because \(\mathbb F\) has characteristic zero, \(X\mapsto X-\frac{\operatorname{tr}X}{n}I_n\) identifies this quotient with \(\mathfrak{sl}_n(\mathbb F)\).

## Connected components over \(\mathbb R\) and \(\mathbb C\)

The [[lie-groups/complex-lie-group|complex Lie group]] \(\operatorname{PGL}_n(\mathbb C)\) is connected. For the real group, scalar multiplication changes determinant by \(\lambda^n\). It follows that
\[
\pi_0(\operatorname{PGL}_n(\mathbb R))\cong
\begin{cases}
1,&n\ \text{odd},\\
\mathbb Z/2,&n\ \text{even}.
\end{cases}
\]
Indeed, for odd \(n\), a negative scalar identifies the two determinant-sign components of \(\operatorname{GL}_n(\mathbb R)\); for even \(n\), scalar matrices always have positive determinant and the sign survives the quotient.

The identity component is the image of \(\operatorname{SL}_n(\mathbb R)\), namely \(\operatorname{PSL}_n(\mathbb R)\). Thus it is the whole group for odd \(n\) and has index \(2\) for even \(n\).

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3). Relevant: matrix Lie groups, quotient Lie groups, and classical Lie algebras.
2. James S. Milne, *Lie Algebras, Algebraic Groups, and Lie Groups*, 2013. [Author-maintained course notes](https://www.jmilne.org/math/CourseNotes/ala.html). Relevant: classical groups and their Lie algebras.
