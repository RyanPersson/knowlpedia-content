+++
id = "algebra-category-theory/triangulated-category"
title = "Triangulated category"
kind = "knowl"
summary = "A pretriangulated category satisfying the octahedral axiom."
aliases = ["triangulated category", "triangulated"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/pretriangulated-category", "algebra-category-theory/distinguished-triangle", "algebra-category-theory/octahedral-axiom"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

A **triangulated category** is a [[algebra-category-theory/pretriangulated-category|pretriangulated category]] whose [[algebra-category-theory/distinguished-triangle|distinguished triangles]] also satisfy the [[algebra-category-theory/octahedral-axiom|octahedral axiom]]. Its structure packages an additive shift and a class of triangles behaving like mapping-cone sequences.

Derived categories and homotopy categories of suitable stable settings are central examples. Some authors include the octahedral axiom in the word “pretriangulated”; the terminology here follows mathlib, where `Pretriangulated` supplies the earlier axioms and `IsTriangulated` supplies octahedrality.
