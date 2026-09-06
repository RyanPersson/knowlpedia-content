+++
id = "fiber-bundles/smooth-compatibility-of-charts-and-atlases"
title = "Smooth compatibility of charts and atlases"
kind = "definition"
summary = "The condition that overlapping coordinate charts have smooth transition maps, extended to compatibility of smooth atlases."
aliases = ["smoothly compatible charts", "compatible smooth charts", "compatible smooth atlases", "smooth atlas compatibility"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/coordinate-transition-map", "fiber-bundles/smooth-atlas"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Two coordinate charts \((U,\varphi)\) and \((V,\psi)\) on the same
topological manifold are **smoothly compatible** if either \(U\cap V\) is
empty or the coordinate transition map

\[
\psi\circ\varphi^{-1}:\varphi(U\cap V)\longrightarrow\psi(U\cap V)
\]

is smooth with smooth inverse. Two [[fiber-bundles/smooth-atlas|smooth
atlases]] are **compatible** if every chart in one is smoothly compatible
with every chart in the other; equivalently, their union is a smooth atlas.

## Equivalent formulations

Because the two transition maps are inverses, compatibility can equivalently
be stated by requiring \(\psi\circ\varphi^{-1}\) to be a
[[fiber-bundles/diffeomorphism|diffeomorphism]]. Compatibility of smooth
atlases is an equivalence relation, and two smooth atlases are compatible
exactly when they generate the same [[fiber-bundles/maximal-smooth-atlas|maximal
smooth atlas]].

## Scope of the terminology

Compatibility depends on the regularity category. Smooth atlases require
smooth coordinate changes, while \(C^k\), real-analytic, complex, and other
atlases impose their corresponding transition-map conditions. Thus the bare
phrase “compatible atlases” should be interpreted only after the category has
been specified.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth structures and smoothly compatible charts.
