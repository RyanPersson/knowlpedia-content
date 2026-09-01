+++
id = "algebraic-geometry-foundations/projective-space"
title = "Projective space"
kind = "definition"
summary = "The scheme of one-dimensional linear subspaces of a vector space, covered by affine coordinate charts."
aliases = ["projective-space", "projective n-space", "projectivization of a vector space"]
domains = ["algebraic-geometry-foundations", "linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/proj"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
legacy_source_path = "algebraic-geometry-foundations/projective-space.md"
+++

Let \(V\) be a nonzero finite-dimensional [[linear-algebra/vector-space|vector space]] over a field \(k\). Using the convention that points are lines in \(V\), its **projective space** is the [[algebraic-geometry-foundations/scheme|scheme]] obtained by the [[algebraic-geometry-foundations/proj|Proj construction]]
\[
\mathbb P(V):=\operatorname{Proj}\operatorname{Sym}(V^\vee).
\]
Its \(k\)-points are the one-dimensional linear subspaces \(L\subset V\). If \(V=k^{n+1}\), this is **projective \(n\)-space**
\[
\mathbb P_k^n=\operatorname{Proj}k[x_0,\ldots,x_n].
\]

## Homogeneous coordinates and affine charts

A nonzero vector \(a=(a_0,\ldots,a_n)\) spans a point written in **homogeneous coordinates** as \([a_0:\cdots:a_n]\), with
\[
[a_0:\cdots:a_n]=[\lambda a_0:\cdots:\lambda a_n]
\]
for every \(\lambda\in k^\times\). Thus
\[
\mathbb P^n(k)=(k^{n+1}\setminus\{0\})/k^\times.
\]
This formula describes the \(k\)-valued points; the scheme \(\mathbb P_k^n\) contains additional information after extension of the ground field.

For each \(i\), the condition \(a_i\ne0\) defines a standard open subset \(U_i\). Dividing the other coordinates by \(a_i\) gives an isomorphism
\[
U_i\cong\mathbb A_k^n.
\]
Consequently, \(\mathbb P_k^n=\bigcup_{i=0}^nU_i\) is covered by \(n+1\) copies of [[algebraic-geometry-foundations/affine-n-space|affine \(n\)-space]], proving directly that it is a scheme.

## Linear and quotient conventions

The assignment \(L\mapsto L\subset V\) identifies \(\mathbb P(V)\) with the Grassmannian of lines \(\operatorname{Gr}_1(V)\). A linear subspace \(0\ne W\subseteq V\) determines the projective subspace \(\mathbb P(W)\subseteq\mathbb P(V)\), whose projective dimension is \(\dim_kW-1\).

There are two standard projectivization conventions. This knowl uses
\(\operatorname{Proj}\operatorname{Sym}(V^\vee)\), whose points are lines in \(V\). Some algebraic-geometry texts instead write
\(\mathbb P(V)=\operatorname{Proj}\operatorname{Sym}(V)\); that scheme parameterizes one-dimensional quotients of \(V\), equivalently lines in \(V^\vee\). Formulas involving tautological line bundles and duals must be translated when conventions differ.

## Examples and related structures

Projective space is the ambient incidence space of
[[algebraic-geometry-foundations/projective-geometry|projective geometry]]:
its projective lines and higher-dimensional projective subspaces come from
linear subspaces of \(V\).

The [[algebraic-geometry-foundations/projective-line|projective line]] \(\mathbb P_k^1\) is the [[algebraic-geometry-foundations/affine-line|affine line]] together with one point at infinity. For \(k=\mathbb R\) or \(\mathbb C\), the sets of lines carry their familiar smooth structures as [[differential-geometry/real-projective-space|real projective space]] and [[differential-geometry/complex-projective-space|complex projective space]]. Invertible linear maps act through the [[algebra-groups/projective-general-linear-group|projective general linear group]].

Unlike affine space, projective space of positive dimension is not an [[algebraic-geometry-foundations/affine-scheme|affine scheme]].

## References

1. Robin Hartshorne, *Algebraic Geometry*, Springer, 1977. [Publisher record](https://doi.org/10.1007/978-1-4757-3849-0). Relevant: Chapter II, §2, especially the Proj construction and projective space.
2. Joe Harris, *Algebraic Geometry: A First Course*, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-1-4757-2189-8). Relevant: Lecture 1, homogeneous coordinates and projective varieties.
