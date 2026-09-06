+++
id = "algebraic-geometry-foundations/projective-geometry"
title = "Projective geometry"
kind = "definition"
summary = "The incidence geometry of lines and subspaces in a vector space, viewed projectively."
aliases = ["Desarguesian projective geometry", "classical projective geometry"]
domains = ["algebraic-geometry-foundations", "linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be a [[linear-algebra/vector-space|vector space]] of dimension at least \(2\) over a field \(k\). The **projective geometry of \(V\)** is the incidence structure whose points are the one-dimensional linear subspaces of \(V\), and whose projective subspaces are the sets
\[
\mathbb P(W)=\{L\subseteq W:\dim_kL=1\}
\]
for nonzero [[convex-analysis/linear-subspace|linear subspaces]] \(W\subseteq V\). Incidence means containment.

## Dimensions and joins

If \(\dim_kW=r+1\), then \(\mathbb P(W)\) has projective dimension \(r\). In particular, projective lines are the \(\mathbb P(W)\) with \(\dim_kW=2\), and projective hyperplanes arise from codimension-one subspaces of \(V\).

Two distinct points represented by lines \(L_1,L_2\subset V\) lie on the unique projective line \(\mathbb P(L_1+L_2)\). More generally, sums and intersections of linear subspaces encode projective spans and projective intersections.

## Coordinates and transformations

Choosing a basis identifies this incidence geometry with the \(k\)-points of [[algebraic-geometry-foundations/projective-space|\(\mathbb P_k^{n}\)]], where \(n=\dim_kV-1\). Its linear symmetries form the [[algebra-groups/projective-general-linear-group|projective general linear group]]. Allowing [[algebra-fields-galois/field-automorphism|field automorphisms]] produces the larger [[algebraic-geometry-foundations/projective-semilinear-group|projective semilinear group]].

This construction is called **Desarguesian** projective geometry. Abstract projective planes need not arise from vector spaces over fields, so the vector-space hypothesis is substantive.

## References

1. Emil Artin, *Geometric Algebra*, Interscience, 1957. Relevant: Chapter II, projective and affine geometry.
2. Peter J. Cameron, *Projective and Polar Spaces*, Queen Mary and Westfield College, 1992. [Author-maintained text](https://www.maths.qmul.ac.uk/~pjc/pps/). Relevant: Chapter 1.
