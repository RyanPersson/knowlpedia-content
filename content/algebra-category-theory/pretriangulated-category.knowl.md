+++
id = "algebra-category-theory/pretriangulated-category"
title = "Pretriangulated category"
kind = "knowl"
summary = "A shifted preadditive category with distinguished triangles satisfying the first triangle axioms."
aliases = ["pretriangulated category", "pretriangulated"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/preadditive-category", "algebra-category-theory/zero-object", "algebra-category-theory/shift-functor", "algebra-category-theory/triangle"]
dependency_review_count = 1
+++

In the convention used by mathlib, a **pretriangulated category** is a [[algebra-category-theory/preadditive-category|preadditive category]] with a [[algebra-category-theory/zero-object|zero object]], an additive [[algebra-category-theory/shift-functor|shift]], and a class Δ of [[algebra-category-theory/triangle|triangles]], whose members are called **distinguished**, satisfying:

1. distinguishedness is preserved by isomorphism;
2. every contractible triangle \(X\xrightarrow{\mathrm{id}_X}X\to0\to X[1]\) is distinguished;
3. every morphism extends to a distinguished triangle;
4. a triangle is distinguished exactly when its rotation is;
5. a commuting square on the first maps of two distinguished triangles extends to a morphism of triangles.

This terminology is convention-sensitive. Here “triangulated” means pretriangulated plus the [[algebra-category-theory/octahedral-axiom|octahedral axiom]].
