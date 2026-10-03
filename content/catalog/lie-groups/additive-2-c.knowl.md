+++
id = "catalog/lie-groups/additive-2-c"
title = "Additive C^2"
kind = "definition"
summary = "Additive C^2 as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

the additive [[fiber-bundles/lie-group|Lie group]] \((\mathbb C^{2},+)\) has coordinatewise addition, identity zero, and inversion \(x\mapsto-x\).

## Dimensions and structure

This group has real dimension \(4\), complex dimension \(2\). It is connected, [[topology/simply-connected-space|simply connected]] and abelian; its Lie bracket is zero. Its additive structure is one view of a [[linear-algebra/vector-space|vector space]], and forgetting scalar multiplication permits more homomorphisms.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## Direct verification

Coordinatewise addition is associative and commutative, zero is the identity, and negation is inversion. These polynomial operations give the stated Lie group, and its coordinate space gives the dimension.
