+++
id = "catalog/lie-groups/affine-n-r"
title = "Aff(n,R)"
kind = "definition"
summary = "Aff(n,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\mathrm{Aff}(n,\mathbb R)\) is the [[fiber-bundles/lie-group|Lie group]] of invertible affine maps \(x\mapsto Ax+b\) of \(\mathbb R^{n}\), with \(A\in\mathrm{GL}(n,\mathbb R)\) and \(b\in\mathbb R^{n}\). In coordinates,
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(n^2+n\). The translations form a normal additive subgroup. Projection to the linear part splits by \(A\mapsto(A,0)\), giving \(\mathbb R^{n}\rtimes\mathrm{GL}(n,\mathbb R)\). In dimension one this is the ax+b group.

## Direct verification

Composing the maps x ↦ Ax+b and x ↦ A′x+b′ gives x ↦ AA′x+Ab′+b. The inverse is x ↦ A⁻¹x−A⁻¹b. The underlying manifold is the product of the [[lie-groups/general-linear-group|general linear group]] and the translation [[linear-algebra/vector-space|vector space]].
