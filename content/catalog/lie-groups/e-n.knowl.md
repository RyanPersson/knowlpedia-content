+++
id = "catalog/lie-groups/e-n"
title = "E(n)"
kind = "definition"
summary = "E(n) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = []
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

For every integer \(n\ge1\), \(\mathrm{E}(n)\) is the group of Euclidean isometries of \(\mathbb R^{n}\). Each element is \(x\mapsto Ax+b\) with \(A\in\mathrm{O}(n,\mathbb R)\) and \(b\in\mathbb R^{n}\), and
\[ (A,b)(A^{\prime},b^{\prime})=(AA^{\prime},Ab^{\prime}+b). \]

## Dimensions and structure

This group has real dimension \(n(n+1)/2\). This gives the [[algebra-groups/semidirect-product|semidirect product]] of translations by the indicated [[lie-groups/orthogonal-group|orthogonal group]].

## Direct verification

The displayed product is composition of affine maps. Orthogonal matrices preserve the Euclidean distance, and any Euclidean isometry is a translation followed by an orthogonal map. Adding the translation dimension to n(n−1)/2 gives n(n+1)/2.
