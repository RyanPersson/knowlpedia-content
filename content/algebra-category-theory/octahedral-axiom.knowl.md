+++
id = "algebra-category-theory/octahedral-axiom"
title = "Octahedral axiom"
kind = "knowl"
summary = "The triangle axiom coherently relating cones of two composable morphisms and their composite."
aliases = ["octahedral axiom", "octahedron axiom", "TR4"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/pretriangulated-category", "algebra-category-theory/distinguished-triangle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal T\) be a [[algebra-category-theory/pretriangulated-category|pretriangulated category]], and let \(X\xrightarrow{f}Y\xrightarrow{g}Z\) be composable morphisms. Complete \(f\), \(g\), and \(gf\) to distinguished triangles, with third objects \(C_f\), \(C_g\), and \(C_{gf}\). The **octahedral axiom** asserts that these triangles can be connected by morphisms
\[
C_f\longrightarrow C_{gf}\longrightarrow C_g
\]
so that the standard octahedral diagram commutes and
\[
C_f\longrightarrow C_{gf}\longrightarrow C_g\longrightarrow \Sigma C_f
\]
is a [[algebra-category-theory/distinguished-triangle|distinguished triangle]].

## Interpretation

The axiom says that forming cones is coherent with composition. It is often labeled TR4.
