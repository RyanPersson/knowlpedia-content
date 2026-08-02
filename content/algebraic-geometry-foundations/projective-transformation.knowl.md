+++
id = "algebraic-geometry-foundations/projective-transformation"
title = "Projective transformation"
kind = "definition"
summary = "A transformation of projective space induced by an invertible linear map."
aliases = ["projectivity", "linear projective transformation", "homography"]
domains = ["algebraic-geometry-foundations", "linear-algebra"]
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional [[linear-algebra/vector-space|vector space]] over a field \(k\). An invertible [[linear-algebra/linear-map|linear map]] \(A:V\to V\) induces a **projective transformation**
\[
\mathbb P(A):\mathbb P(V)\longrightarrow\mathbb P(V),
\qquad [v]\longmapsto[Av].
\]
More generally, a linear isomorphism \(V\to W\) induces a projective isomorphism \(\mathbb P(V)\to\mathbb P(W)\).

## Scalar ambiguity

Two invertible linear maps \(A,B\) induce the same transformation exactly when \(B=\lambda A\) for some \(\lambda\in k^\times\), provided \(V\ne0\). Thus the group of projective transformations is
\[
\operatorname{GL}(V)/(k^\times I)
=\operatorname{PGL}(V),
\]
the [[algebra-groups/projective-general-linear-group|projective general linear group]].

## Incidence preservation

Projective transformations send projective subspaces to projective subspaces and preserve incidence. A bijection with this line-preserving property is called a **collineation**. Projective transformations are collineations, but over a field with nontrivial automorphisms there can also be collineations induced by non-linear [[linear-algebra/semilinear-map|semilinear maps]]. The [[algebraic-geometry-foundations/fundamental-theorem-of-projective-geometry|fundamental theorem of projective geometry]] accounts for all of them in projective dimension at least two.

## References

1. Emil Artin, *Geometric Algebra*, Interscience, 1957. Relevant: Chapter II, §§3–4.
2. Joe Harris, *Algebraic Geometry: A First Course*, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-1-4757-2189-8). Relevant: Lecture 1, projective linear transformations.
