+++
id = "algebra-category-theory/group-object"
title = "Group object"
kind = "definition"
summary = "An object carrying multiplication, identity, and inverse morphisms that satisfy the group axioms internally."
aliases = ["internal group"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/categorical-product", "algebra-category-theory/terminal-object"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] with finite [[algebra-category-theory/categorical-product|products]] and [[algebra-category-theory/terminal-object|terminal object]] \(1\). A **group object** in \(\mathcal C\) is an object \(G\) with morphisms
\[
m:G\times G\to G,\qquad e:1\to G,\qquad i:G\to G
\]
that satisfy the associativity, identity, and inverse diagrams obtained by writing the ordinary group axioms using products, the diagonal \(G\to G\times G\), and the unique map \(G\to1\).

## Generalized elements

For every object \(T\), composition with \(m,e,i\) makes
\[
\operatorname{Hom}_{\mathcal C}(T,G)
\]
a group, naturally in \(T\). This is a reliable way to read the internal axioms, although ordinary elements alone may not detect all morphisms in every category.

## Examples

- Group objects in sets are ordinary [[algebra-groups/group|groups]].
- Group objects in topological spaces are [[topology/topological-group|topological groups]].
- Group objects in smooth manifolds are [[fiber-bundles/lie-group|Lie groups]].
- Group objects in schemes are [[algebraic-geometry-foundations/group-scheme|group schemes]].

## References

1. Francis Borceux, *Handbook of Categorical Algebra 2: Categories and Structures*, Cambridge University Press, 1994. [DOI record](https://doi.org/10.1017/CBO9780511525865). Relevant: internal algebraic structures.
