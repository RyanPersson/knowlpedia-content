+++
id = "catalog/lie-groups/se-2"
title = "SE(2)"
kind = "definition"
summary = "SE(2) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = []
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\mathrm{SE}(2)\) is the group of orientation-preserving Euclidean isometries of \(\mathbb R^{2}\). Each element is \(x\mapsto Ax+b\) with \(A\in\mathrm{SO}(2,\mathbb R)\) and \(b\in\mathbb R^{2}\), and
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(3\). This gives the [[algebra-groups/semidirect-product|semidirect product]] of translations by the indicated [[lie-groups/orthogonal-group|orthogonal group]].

## Direct verification

The determinant-one condition is preserved by composition and inversion. Its [[lie-groups/lie-algebra|Lie algebra]] has a skew-symmetric block and an arbitrary translation vector, giving n(n−1)/2+n dimensions.
