+++
id = "differential-geometry/coordinate-chart-isomorphism-in-smooth-manifolds"
title = "Coordinate chart as an isomorphism of smooth manifolds"
kind = "theorem"
summary = "The coordinate map of a smooth chart is a diffeomorphism between two open smooth manifolds."
aliases = ["chart isomorphism in Diff", "coordinate chart is a diffeomorphism"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth
manifold]] and let \((U,\varphi)\) be a
[[fiber-bundles/smooth-chart-coordinate-chart|smooth coordinate chart]]. Give
\(U\subseteq M\) its open-submanifold structure and
\(\varphi(U)\subseteq\mathbb R^n\) its standard smooth structure. Then

\[
\varphi:U\longrightarrow\varphi(U)
\]

is a [[fiber-bundles/diffeomorphism|diffeomorphism]], hence an isomorphism in
the [[differential-geometry/category-of-smooth-manifolds|category of smooth
manifolds]].

## What the chart itself is

Strictly, a chart is the pair \((U,\varphi)\), not only the arrow \(\varphi\).
The coordinate map is generally not a morphism with domain all of \(M\); its
domain is the open submanifold \(U\). It sits beside the smooth inclusion

\[
U\xrightarrow{\ \varphi\ }\varphi(U),
\qquad
U\hookrightarrow M.
\]

Thus charts provide local isomorphisms, not usually global isomorphisms
\(M\cong\mathbb R^n\).

## Transition maps

For overlapping charts \((U,\varphi)\) and \((V,\psi)\), the transition map

\[
\psi\circ\varphi^{-1}:
\varphi(U\cap V)\longrightarrow\psi(U\cap V)
\]

is likewise an isomorphism between open submanifolds of Euclidean space. The
pairwise smoothness of these local isomorphisms is the compatibility condition
in a [[fiber-bundles/smooth-atlas|smooth atlas]].

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth structures, charts, and smooth maps.
