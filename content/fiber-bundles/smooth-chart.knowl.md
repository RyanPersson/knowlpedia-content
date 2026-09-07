+++
id = "fiber-bundles/smooth-chart"
title = "Smooth chart"
kind = "knowl"
summary = "A local coordinate map from an open subset of a smooth manifold to an open subset of Euclidean space."
aliases = ["smooth-chart", "Smooth chart"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/smooth-chart.md"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-chart-coordinate-chart"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \((M,\mathcal A)\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], with chosen maximal smooth atlas \(\mathcal A\). A **smooth chart** on \(M\) is a [[fiber-bundles/smooth-chart-coordinate-chart|coordinate chart]] \((U,\varphi)\) belonging to \(\mathcal A\).

## Local coordinates

Writing \(\varphi=(x^1,\ldots,x^n)\), the component functions \(x^i:U\to\mathbb R\) are the associated **local coordinates**.


## Compatibility

Equivalently, a coordinate chart is smooth when its transition maps with every chart in \(\mathcal A\) are [[real-analysis/class-ck-map|\(C^\infty\)]] in both directions. Requiring only one direction to be smooth is insufficient.

The coordinate map of a smooth chart is a [[fiber-bundles/diffeomorphism|diffeomorphism]] from its domain, with the induced smooth structure, onto its Euclidean image. This is a consequence of compatibility, rather than a prerequisite for constructing the smooth structure.
