+++
id = "algebra-category-theory/pretriangulated-category"
title = "Pretriangulated category"
kind = "knowl"
summary = "A shifted preadditive category with distinguished triangles satisfying the first triangle axioms."
aliases = ["pretriangulated category", "pretriangulated"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/preadditive-category", "algebra-category-theory/zero-object", "algebra-category-theory/shift-functor", "algebra-category-theory/distinguished-triangle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In the convention used by mathlib, a **pretriangulated category** is a [[algebra-category-theory/preadditive-category|preadditive category]] with a [[algebra-category-theory/zero-object|zero object]], an additive [[algebra-category-theory/shift-functor|shift]], and a class of [[algebra-category-theory/distinguished-triangle|distinguished triangles]] satisfying the first triangle axioms:

1. distinguishedness is preserved by isomorphism;
2. every morphism extends to a distinguished triangle;
3. a triangle is distinguished exactly when its rotation is;
4. a commuting square on the first maps of two distinguished triangles extends to a morphism of triangles.

This terminology is convention-sensitive. Here “triangulated” means pretriangulated plus the [[algebra-category-theory/octahedral-axiom|octahedral axiom]].
