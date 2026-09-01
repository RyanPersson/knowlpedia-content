+++
id = "topology/baire-category-theorem"
title = "Baire category theorem"
kind = "knowl"
summary = "In a complete metric space, countable intersections of dense open sets are dense."
aliases = ["baire-category-theorem", "Baire category theorem"]
domains = ["topology"]
prerequisites = ["topology/complete-metric-space", "topology/dense-set", "topology/open-set"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/baire-category-theorem.md"
+++

**Baire category theorem.** Let \((X,d)\) be a nonempty [[topology/complete-metric-space|complete metric space]]. If \((U_n)_{n\in\mathbb{N}}\) is a sequence of [[topology/dense-set|dense]] [[topology/open-set|open sets]] in \(X\), then \(\bigcap_{n\in\mathbb{N}}U_n\) is dense in \(X\).

## Equivalent characterizations

The dense-intersection conclusion is equivalent to saying that no nonempty open subset of \(X\) is [[topology/meager-set|meager]] in \(X\). Consequently, \(X\) is not a countable union of [[topology/nowhere-dense-set|nowhere dense sets]], and every [[topology/residual-set|residual set]] is dense. Thus every complete metric space is a [[topology/baire-space|Baire space]].
