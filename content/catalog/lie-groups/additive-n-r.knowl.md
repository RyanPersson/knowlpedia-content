+++
id = "catalog/lie-groups/additive-n-r"
title = "Additive R^n"
kind = "definition"
summary = "Additive R^n as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), the additive [[fiber-bundles/lie-group|Lie group]] \((\mathbb R^{n},+)\) has coordinatewise addition, identity zero, and inversion \(x\mapsto-x\).

## Dimensions and structure

This group has real dimension \(n\). It is connected, [[topology/simply-connected-space|simply connected]] and abelian; its Lie bracket is zero. Its additive structure is one view of a [[linear-algebra/vector-space|vector space]], and forgetting scalar multiplication permits more homomorphisms.

## Direct verification

Coordinatewise addition is associative and commutative, zero is the identity, and negation is inversion. These polynomial operations give the stated Lie group, and its coordinate space gives the dimension.
