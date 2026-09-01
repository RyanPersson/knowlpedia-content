+++
id = "convex-analysis/distance-function-to-a-set"
title = "Distance function to a set"
kind = "knowl"
summary = "d_Ω(x)=inf{||x−w||: w∈Ω} in a normed space"
aliases = ["distance-function-to-a-set", "Distance function to a set"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/norm-normed-vector-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/distance-function-to-a-set.md"
+++

Let \((X,\|\cdot\|)\) be a [[convex-analysis/norm-normed-vector-space|normed vector space]], and let \(\Omega\subseteq X\) be nonempty. The **distance function** to \(\Omega\) is
\[
d_\Omega(x):=\inf\{\|x-w\|: w\in \Omega\}.
\]

## Properties

- \(d_\Omega(x)=0\) if and only if \(x\in\overline{\Omega}\).
- \(d_\Omega\) is \(1\)-Lipschitz:
  \[
  |d_\Omega(x)-d_\Omega(y)|\leq \|x-y\|.
  \]
- If \(\Omega\) is [[convex-analysis/convex-set|convex]], then \(d_\Omega\) is convex.

Conversely, if \(\Omega\) is closed and \(d_\Omega\) is convex, then \(\Omega\) is convex.

## Examples

- If \(\Omega=\{0\}\), then \(d_\Omega(x)=\|x\|\).
- If \(\Omega\) is the closed ball with center \(x_0\) and radius \(r\), then
  \[
  d_\Omega(x)=\max\{\|x-x_0\|-r,0\}.
  \]
