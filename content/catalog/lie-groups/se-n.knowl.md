+++
id = "catalog/lie-groups/se-n"
title = "SE(n)"
kind = "definition"
summary = "SE(n) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = []
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\mathrm{SE}(n)\) is the group of orientation-preserving Euclidean isometries of \(\mathbb R^{n}\). Each element is \(x\mapsto Ax+b\) with \(A\in\mathrm{SO}(n,\mathbb R)\) and \(b\in\mathbb R^{n}\), and
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(n(n+1)/2\). This gives the [[algebra-groups/semidirect-product|semidirect product]] of translations by the indicated [[lie-groups/orthogonal-group|orthogonal group]].

## Direct verification

The determinant-one condition is preserved by composition and inversion. Its [[lie-groups/lie-algebra|Lie algebra]] has a skew-symmetric block and an arbitrary translation vector, giving n(n−1)/2+n dimensions.
