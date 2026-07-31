+++
id = "lie-groups/riemannian-symmetric-space-noncompact-type"
title = "Riemannian symmetric space of noncompact type"
kind = "definition"
summary = "A simply connected Riemannian symmetric space with nonpositive curvature and no Euclidean factor."
aliases = ["noncompact symmetric space", "G/K symmetric space"]
domains = ["lie-groups", "differential-geometry"]
section_mode = "progressive"
+++

A **Riemannian symmetric space of noncompact type** is a connected, simply
connected, complete [[differential-geometry/riemannian-manifold|Riemannian
manifold]] \(X\) such that every point is an isolated fixed point of an
involutive isometry, all sectional curvatures are nonpositive, and \(X\) has
no nontrivial Euclidean de Rham factor. Equivalently,
\[
X\cong G/K,
\]
where \(G\) is a connected noncompact semisimple [[fiber-bundles/lie-group|Lie group]] with finite center
and no compact factors, and \(K\) is a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]]. The quotient is a
[[lie-groups/homogeneous-space|homogeneous space]], with \(G\) acting by
isometries.

## Infinitesimal model

At the base point \(o=eK\), the [[differential-geometry/tangent-space|tangent space]] identifies with
\(\mathfrak p\) in the
[[lie-groups/cartan-decomposition-real-reductive-lie-algebra|Cartan
decomposition]] \(\mathfrak g=\mathfrak k\oplus\mathfrak p\). A suitably
normalized invariant [[linear-algebra/bilinear-form|bilinear form]] gives the \(G\)-invariant metric. The
relation \([\mathfrak p,\mathfrak p]\subseteq\mathfrak k\) expresses the
symmetry, and curvature is determined by
\[
R(X,Y)Z=-\bigl[ [X,Y],Z \bigr]
\]
up to the chosen curvature-sign convention
[Helgason, Chapters IV–V].

## Rank and flats

A maximal abelian subspace \(\mathfrak a\subseteq\mathfrak p\) exponentiates
to a maximal totally geodesic flat through \(o\). Its dimension is the real
rank of \(X\). The associated
[[lie-groups/restricted-root-system|restricted root system]] controls radial
geometry, invariant differential operators, and the behavior of spherical
functions.

## Examples and boundary of the definition

Real hyperbolic space is
\(\mathrm{SO}_0(n,1)/\mathrm{SO}(n)\), and the space of positive-definite
determinant-one matrices is
\(\mathrm{SL}_n(\mathbb R)/\mathrm{SO}(n)\). [[linear-algebra/euclidean-space|Euclidean space]] is symmetric and
nonpositively curved but is excluded by the no-Euclidean-factor clause.
Compact symmetric spaces, such as round spheres, belong to the compact dual
theory rather than the noncompact type.

## References

1. S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapters IV–V.
2. S. Helgason, *Groups and Geometric Analysis*, American Mathematical Society, 2000. [DOI record](https://doi.org/10.1090/surv/083). Relevant: Chapter I on symmetric spaces and their harmonic analysis.
