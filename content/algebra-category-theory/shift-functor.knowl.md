+++
id = "algebra-category-theory/shift-functor"
title = "Shift functor"
kind = "knowl"
summary = "An autoequivalence representing an integral degree shift in a category."
aliases = ["shift functor", "shift autoequivalence", "translation functor"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/equivalence-of-categories"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **shift functor** on a category \(\mathcal C\) is an [[algebra-category-theory/equivalence-of-categories|autoequivalence]]
\[
[1]:\mathcal C\longrightarrow\mathcal C.
\]
Its inverse is denoted \([-1]\), and for \(n\in\mathbb Z\), the notation \([n]\) denotes the corresponding iterate, with \([0]=\operatorname{id}_{\mathcal C}\).

## Common settings

For cochain complexes, \(X[1]\) shifts the grading and changes the sign of the differential according to the chosen convention. In a [[algebra-category-theory/preadditive-category|preadditive category]], one usually requires the shift to be additive. Shifted objects supply the fourth vertex of a [[algebra-category-theory/triangle|triangle]].
