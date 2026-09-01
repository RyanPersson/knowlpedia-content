+++
id = "real-analysis/chain-rule"
title = "Chain rule"
kind = "knowl"
summary = "Derivative of a composition equals the composition of derivatives."
aliases = ["chain-rule", "Chain rule"]
domains = ["real-analysis"]
prerequisites = ["topology/open-set", "real-analysis/differentiable-map", "shared-foundations/composition", "real-analysis/jacobian-matrix"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "real-analysis/chain-rule.md"
+++

Let \(U\subseteq\mathbb R^k\) and \(V\subseteq\mathbb R^m\) be [[topology/open-set|open sets]]. If \(f:U\to V\) is [[real-analysis/differentiable-map|differentiable]] at \(a\in U\) and \(g:V\to\mathbb R^p\) is differentiable at \(f(a)\), then the [[shared-foundations/composition|composition]] \(g\circ f\) is differentiable at \(a\), and
\[
D(g\circ f)(a)=Dg(f(a))\circ Df(a).
\]

In terms of [[real-analysis/jacobian-matrix|Jacobian matrices]], this is
\[
J_{g\circ f}(a)=J_g(f(a))\,J_f(a).
\]
