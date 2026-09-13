+++
id = "real-analysis/compactly-supported-function"
title = "Compactly supported function"
kind = "definition"
summary = "A function whose nonzero set has compact closure in its specified domain."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/support-of-a-function", "topology/compact-set", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A function \(f:U\to\mathbb R^m\) is **compactly supported in \(U\)** when its [[shared-foundations/support-of-a-function|support]]
\[
\operatorname{supp}_U f=\overline{\{x\in U:f(x)\ne0\}}^{\,U}
\]
is a [[topology/compact-set|compact subset]] of \(U\). For open \(U\subseteq\mathbb R^n\), the notation \(C_c^k(U;\mathbb R^m)\) denotes compactly supported [[real-analysis/class-ck-map|class \(C^k\) maps]], and \(C_c^\infty\) denotes the smooth ones.

## The domain matters

If \(U=(0,1)\), the constant function \(1\) has bounded support but does not have compact support in \(U\). Compact support in an open Euclidean domain leaves a positive distance from its boundary. A smooth function with such support extends smoothly by zero to \(\mathbb R^n\), since it already vanishes in a neighborhood of each boundary point.

## Relation to bump functions

A [[differential-geometry/bump-function|bump function]] is a smooth compactly supported scalar function. Compact support itself is a condition on support and does not imply continuity or differentiability.
