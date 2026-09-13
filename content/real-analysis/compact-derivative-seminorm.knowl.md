+++
id = "real-analysis/compact-derivative-seminorm"
title = "Compact derivative seminorm"
kind = "definition"
summary = "A seminorm measuring all derivatives through a fixed order on a compact subset of an open domain."
aliases = ["Ck seminorm on a compact set", "smooth seminorm"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "real-analysis/multi-index-notation", "convex-analysis/seminorm", "topology/compact-set", "real-analysis/supremum-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For open \(U\subseteq\mathbb R^n\), nonempty compact \(K\subset U\), and integer \(k\ge0\), the **compact derivative seminorm** on \(C^\infty(U)\) is
\[
p_{K,k}(f)=\max_{|\alpha|\le k}\sup_{x\in K}|\partial^\alpha f(x)|.
\]
It is finite by continuity and compactness, and satisfies absolute homogeneity and the triangle inequality. It is generally only a [[convex-analysis/seminorm|seminorm]]: a nonzero function supported away from \(K\) can have \(p_{K,k}(f)=0\).

## Smooth convergence

A sequence converges in \(C^\infty(U)\) when every such seminorm of its difference from the limit tends to zero. A countable compact exhaustion and increasing derivative orders suffice to describe this topology, which makes \(C^\infty(U)\) a [[functional-analysis/frechet-space|Fréchet space]].

For vector-valued functions, replace absolute value by a fixed finite-dimensional norm; the resulting notions of convergence agree.
