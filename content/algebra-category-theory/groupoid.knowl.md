+++
id = "algebra-category-theory/groupoid"
title = "Groupoid"
kind = "definition"
summary = "A category in which every morphism is invertible."
aliases = ["category with only invertible morphisms"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/isomorphism-category"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **groupoid** is a [[algebra-category-theory/category|category]] \(\mathcal G\) in which every morphism is an [[algebra-category-theory/isomorphism-category|isomorphism]]. Thus for every \(f:x\to y\) there is a morphism \(f^{-1}:y\to x\) satisfying \(f^{-1}f=\operatorname{id}_x\) and \(ff^{-1}=\operatorname{id}_y\).

## Groups and equivalence relations

A group is the same thing as a groupoid with one object: its morphisms are the group elements and composition is multiplication. An [[shared-foundations/equivalence-relation|equivalence relation]] on a set determines a groupoid having one arrow \(x\to y\) exactly when \(x\) and \(y\) are equivalent. General groupoids allow several arrows between two objects and nontrivial automorphism groups.

## Geometric role

Groupoids record objects together with reversible identifications. They arise from [[algebra-groups/group-action|group actions]], atlases, moduli problems, and the isomorphisms inside any category. Keeping the arrows retains symmetry information that the set of isomorphism classes discards.

## References

1. Ronald Brown, *Topology and Groupoids*, BookSurge, 2006. [Author-hosted record](https://groupoids.org.uk/topgpds.html). Relevant: Chapters 1–2.
