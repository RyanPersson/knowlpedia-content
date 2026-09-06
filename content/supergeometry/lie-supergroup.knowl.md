+++
id = "supergeometry/lie-supergroup"
title = "Lie supergroup"
kind = "definition"
summary = "A group object in the category of finite-dimensional smooth real supermanifolds."
aliases = ["smooth Lie supergroup", "super Lie group"]
domains = ["supergeometry", "lie-groups"]
prerequisites = ["algebra-category-theory/group-object", "supergeometry/supermanifold", "fiber-bundles/lie-group", "supergeometry/functor-of-points-of-supermanifold", "supergeometry/super-harish-chandra-pair"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **finite-dimensional smooth real Lie supergroup** is a
[[algebra-category-theory/group-object|group object]] in
\(\mathbf{SMan}_{\mathbb R}^{\mathrm{sm}}\), the category of
[[supergeometry/supermanifold|smooth real supermanifolds]]. It consists of a
supermanifold \(G\) and morphisms
\[
m:G\times G\to G,\qquad
i:G\to G,\qquad
e:* \to G
\]
satisfying the associative, inverse, and unit diagrams.

Taking reduced manifolds gives an ordinary real [[fiber-bundles/lie-group|Lie group]] \(G_{\mathrm{red}}\).
For every test supermanifold \(S\), the
[[supergeometry/functor-of-points-of-supermanifold|set of \(S\)-points]]
\(G(S)\) is a group, naturally in \(S\). The ordinary group
\(G_{\mathrm{red}}\) does not by itself recover the odd directions or their
brackets.

The tangent space at the identity carries a canonical
[[supergeometry/lie-superalgebra-of-lie-supergroup|Lie superalgebra]]. In the
smooth finite-dimensional category, the full Lie supergroup can equivalently
be encoded by a [[supergeometry/super-harish-chandra-pair|super
Harish–Chandra pair]].

## Category warning

Complex-analytic and algebraic Lie supergroups are group objects in different
categories and have different global splitting behavior. The term “Lie
supergroup” on this page always means the smooth real
Berezin–Leites/Kostant version unless another category is stated.

## References

1. B. Kostant, “Graded manifolds, graded Lie theory, and prequantization,” in *Differential Geometrical Methods in Mathematical Physics*, Lecture Notes in Mathematics 570, Springer, 1977, 177–306. [Chapter](https://doi.org/10.1007/BFb0087787).
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of Supersymmetry*, EMS, 2011. [Publisher record](https://doi.org/10.4171/097). Relevant: Chapters 6–7.
