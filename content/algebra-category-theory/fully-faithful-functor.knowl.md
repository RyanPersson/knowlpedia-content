+++
id = "algebra-category-theory/fully-faithful-functor"
title = "Fully faithful functor"
kind = "definition"
summary = "A functor that induces bijections on all hom-sets."
aliases = ["fully faithful functor", "fully faithful", "full and faithful functor", "full and faithful"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/functor"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 1
+++

Let \(F:\mathcal C\to\mathcal D\) be a [[algebra-category-theory/functor|functor]]. It is **fully faithful** if, for every pair of objects \(X,Y\) in \(\mathcal C\), the induced map
\[
\operatorname{Hom}_{\mathcal C}(X,Y)\longrightarrow
\operatorname{Hom}_{\mathcal D}(F(X),F(Y)),\qquad
f\longmapsto F(f)
\]
is a bijection.

## Consequences

A fully faithful functor is [[algebra-category-theory/faithful-functor|faithful]] and is full: every morphism \(F(X)\to F(Y)\) is \(F(f)\) for a unique morphism \(f:X\to Y\).

## Example

The inclusion of a [[algebra-category-theory/full-subcategory|full subcategory]] into its ambient category is fully faithful.
