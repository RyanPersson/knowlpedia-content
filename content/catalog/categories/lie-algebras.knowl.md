+++
id = "catalog/categories/lie-algebras"
title = "Category of Lie algebras over a field"
kind = "definition"
summary = "Lie algebras over a fixed field and bracket-preserving linear maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "lie-groups/lie-algebra"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Fix a field \(k\). The **category \(k\text{-}\mathbf{LieAlg}\)** has [[lie-groups/lie-algebra|Lie algebras]] over \(k\) as objects and \(k\)-linear maps \(f:\mathfrak g\to\mathfrak h\) satisfying
\[
f([x,y])=[f(x),f(y)]
\]
as morphisms. Identities and composition preserve linearity and the bracket.

## Scalars and invertibility

A complex Lie algebra has both a complex-linear and an underlying real-linear Lie-algebra view. Forgetting the bracket gives still larger linear Hom-spaces. In either Lie-algebra category, automorphisms are the invertible bracket-preserving maps. The zero map is an endomorphism, but is an automorphism only for the zero Lie algebra.

## Groups are different objects

Differentiation sends a Lie-group homomorphism to a Lie-algebra homomorphism. Integrating a Lie-algebra map requires global information about the groups; equal Lie algebras do not imply isomorphic [[fiber-bundles/lie-group|Lie groups]].
