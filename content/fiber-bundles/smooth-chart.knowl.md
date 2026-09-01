+++
id = "fiber-bundles/smooth-chart"
title = "Smooth chart"
kind = "knowl"
summary = "A local coordinate map from an open subset of a smooth manifold to an open subset of Euclidean space."
aliases = ["smooth-chart", "Smooth chart"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/diffeomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "fiber-bundles/smooth-chart.md"
+++

Let \(M\) be an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. A **smooth chart** on \(M\) is a pair \((U,\varphi)\) in which \(U\subseteq M\) is open and \(\varphi:U\to V\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]] onto an open set \(V\subseteq\mathbb R^n\).

Writing \(\varphi=(x^1,\ldots,x^n)\), the component functions \(x^i:U\to\mathbb R\) are the associated **local coordinates**.

## Compatibility

Equivalently, \((U,\varphi)\) is a topological chart compatible with the smooth structure: for every chart \((U',\varphi')\) in that structure, the transition map
\[
\varphi'\circ \varphi^{-1}:\varphi(U\cap U')\longrightarrow \varphi'(U\cap U')
\]
is smooth wherever defined.
