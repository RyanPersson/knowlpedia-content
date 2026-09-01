+++
id = "algebra-category-theory/initial-object"
title = "Initial object"
kind = "knowl"
summary = "An object admitting a unique morphism to every object of a category."
aliases = ["initial object"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/terminal-object", "algebra-category-theory/zero-object"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. An **initial object** is an object \(0\) such that for every object \(X\), there is exactly one morphism \(0\to X\). Any two initial objects are uniquely isomorphic.

Reversing all arrows gives a [[algebra-category-theory/terminal-object|terminal object]]. An object that is both initial and terminal is a [[algebra-category-theory/zero-object|zero object]]. The empty set is initial in the category of sets, while the trivial group is both initial and terminal in the category of groups.
