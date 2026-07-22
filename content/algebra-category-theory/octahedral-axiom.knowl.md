+++
id = "algebra-category-theory/octahedral-axiom"
title = "Octahedral axiom"
kind = "knowl"
summary = "The triangle axiom coherently relating cones of two composable morphisms and their composite."
aliases = ["octahedral axiom", "octahedron axiom", "TR4"]
domains = ["algebra-category-theory", "algebra-homological"]
+++

The **octahedral axiom** concerns composable morphisms \(X\xrightarrow{f}Y\xrightarrow{g}Z\) in a [[algebra-category-theory/pretriangulated-category|pretriangulated category]]. Choose distinguished triangles for \(f\), \(g\), and \(g\circ f\). The axiom requires connecting morphisms between their third objects so that the resulting octahedral diagram commutes and those third objects themselves form a [[algebra-category-theory/distinguished-triangle|distinguished triangle]].

Conceptually, it states that forming cones is coherent with composition. It is often labeled TR4. In mathlib, `IsTriangulated` is precisely the assertion that the required octahedron exists for every such composable pair and choices of distinguished triangles.
