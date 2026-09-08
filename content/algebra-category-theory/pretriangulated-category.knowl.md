+++
id = "algebra-category-theory/pretriangulated-category"
title = "Pretriangulated category"
kind = "knowl"
summary = "A shifted preadditive category with distinguished triangles satisfying the first triangle axioms."
aliases = ["pretriangulated category", "pretriangulated"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/preadditive-category", "algebra-category-theory/zero-object", "algebra-category-theory/shift-functor", "algebra-category-theory/triangle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In the convention used by mathlib, a **pretriangulated category** is a [[algebra-category-theory/preadditive-category|preadditive category]] with a [[algebra-category-theory/zero-object|zero object]], an additive [[algebra-category-theory/shift-functor|shift]] \([1]\) (so \((f+g)[1]=f[1]+g[1]\) and \(0[1]=0\)), and a class Δ of [[algebra-category-theory/triangle|triangles]], whose members are called **distinguished**, satisfying:

1. distinguishedness is preserved by isomorphism;
2. every contractible triangle \(X\xrightarrow{\mathrm{id}_X}X\to0\to X[1]\) is distinguished;
3. every morphism extends to a distinguished triangle;
4. \(X\xrightarrow fY\xrightarrow gZ\xrightarrow hX[1]\) is distinguished exactly when its rotation \(Y\xrightarrow gZ\xrightarrow hX[1]\xrightarrow{-f[1]}Y[1]\) is;
5. a commuting square on the first maps of two distinguished triangles extends to a morphism of triangles.

## Convention

This terminology is convention-sensitive. Here “triangulated” means pretriangulated plus the [[algebra-category-theory/octahedral-axiom|octahedral axiom]].
