+++
id = "catalog/lie-groups/affine-3-c"
title = "Aff(3,C)"
kind = "definition"
summary = "Aff(3,C) as a separately identified complex Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{Aff}(3,\mathbb C)\) is the [[fiber-bundles/lie-group|Lie group]] of invertible affine maps \(x\mapsto Ax+b\) of \(\mathbb C^{3}\), with \(A\in\mathrm{GL}(3,\mathbb C)\) and \(b\in\mathbb C^{3}\). In coordinates,
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(24\), complex dimension \(12\). The translations form a normal additive subgroup. Projection to the linear part splits by \(A\mapsto(A,0)\), giving \(\mathbb C^{3}\rtimes\mathrm{GL}(3,\mathbb C)\). In dimension one this is the ax+b group.

Its [[lie-groups/complex-lie-group|complex Lie group]] structure uses holomorphic multiplication and inversion. Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]]; real and holomorphic homomorphisms belong to different categories.

## Direct verification

Composing the maps x ↦ Ax+b and x ↦ A′x+b′ gives x ↦ AA′x+Ab′+b. The inverse is x ↦ A⁻¹x−A⁻¹b. The underlying manifold is the product of the [[lie-groups/general-linear-group|general linear group]] and the translation [[linear-algebra/vector-space|vector space]].
