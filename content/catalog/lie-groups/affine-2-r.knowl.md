+++
id = "catalog/lie-groups/affine-2-r"
title = "Aff(2,R)"
kind = "definition"
summary = "Aff(2,R) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{Aff}(2,\mathbb R)\) is the [[fiber-bundles/lie-group|Lie group]] of invertible affine maps \(x\mapsto Ax+b\) of \(\mathbb R^{2}\), with \(A\in\mathrm{GL}(2,\mathbb R)\) and \(b\in\mathbb R^{2}\). In coordinates,
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(6\). The translations form a normal additive subgroup. Projection to the linear part splits by \(A\mapsto(A,0)\), giving \(\mathbb R^{2}\rtimes\mathrm{GL}(2,\mathbb R)\). In dimension one this is the ax+b group.

## Direct verification

Composing the maps x ↦ Ax+b and x ↦ A′x+b′ gives x ↦ AA′x+Ab′+b. The inverse is x ↦ A⁻¹x−A⁻¹b. The underlying manifold is the product of the [[lie-groups/general-linear-group|general linear group]] and the translation [[linear-algebra/vector-space|vector space]].
