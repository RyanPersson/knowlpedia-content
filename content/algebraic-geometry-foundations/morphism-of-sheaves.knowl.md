+++
id = "algebraic-geometry-foundations/morphism-of-sheaves"
title = "Morphism of sheaves"
kind = "definition"
summary = "Compatible maps between the sections of two sheaves."
aliases = ["morphism of sheaves", "sheaf morphism", "map of sheaves"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/sheaf", "topology/topological-space", "algebraic-geometry-foundations/stalk"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal F\) and \(\mathcal G\) be [[algebraic-geometry-foundations/sheaf|sheaves]] on a [[topology/topological-space|topological space]] \(X\). A **morphism of sheaves** \(\varphi:\mathcal F\to\mathcal G\) consists of a map

\[
\varphi_U:\mathcal F(U)\longrightarrow\mathcal G(U)
\]

for every open subset \(U\subseteq X\), compatible with restriction: whenever \(V\subseteq U\), restricting after applying \(\varphi_U\) gives the same result as applying \(\varphi_V\) after restricting.

These maps induce maps on every [[algebraic-geometry-foundations/stalk|stalk]],

\[
\varphi_x:\mathcal F_x\longrightarrow\mathcal G_x.
\]

## Morphisms along a map

More generally, if \(f:X\to Y\), \(\mathcal F\) is a sheaf on \(Y\), and \(\mathcal G\) is a sheaf on \(X\), a morphism of sheaves **along \(f\)** is a morphism into the [[algebraic-geometry-foundations/direct-image-sheaf|direct image sheaf]]:

\[
\mathcal F\longrightarrow f_*\mathcal G.
\]

When the sheaves take values in rings, groups, or modules, every component map preserves the corresponding algebraic structure.
