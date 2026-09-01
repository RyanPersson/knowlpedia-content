+++
id = "differential-geometry/submanifold-chart"
title = "Submanifold chart"
kind = "definition"
summary = "An ambient smooth chart in which an embedded submanifold becomes a coordinate plane."
aliases = ["slice chart", "adapted chart for a submanifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/smooth-manifold", "fiber-bundles/smooth-chart"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(S\) be a \(k\)-dimensional [[differential-geometry/embedded-submanifold|embedded submanifold]] of an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), and let \(p\in S\). A **submanifold chart at \(p\)** is a [[fiber-bundles/smooth-chart|smooth chart]] \((U,\varphi)\) of \(M\), with \(p\in U\), for which
\[
\varphi(U\cap S)=\varphi(U)\cap(\mathbb R^k\times\{0\})\subseteq\mathbb R^k\times\mathbb R^{n-k}.
\]
Thus the first \(k\) coordinate functions restrict to local coordinates on \(S\), while the last \(n-k\) coordinates vanish on \(S\). Reordering the ambient coordinates gives the same notion. The defining local property of embedded submanifolds guarantees such a chart around every point of \(S\).

## Tangent-space description

In a submanifold chart, the coordinate vectors in the first \(k\) directions span \(T_qS\) for every \(q\in U\cap S\). The remaining coordinate directions supply a local complement inside \(T_qM\), although that complement depends on the chart and is not an intrinsic normal subspace.

## Examples and non-examples

For the coordinate plane \(\mathbb R^k\times\{0\}\subset\mathbb R^n\), the identity chart is a submanifold chart. A smooth ambient chart that sends \(S\) to a curved graph is not adapted in this strict sense, even though its restriction may still be a valid chart on \(S\).

## Conventions and scope

“Slice chart” also appears in other contexts, notably proper [[algebra-groups/group-action|group actions]]. Here it means only an ambient chart adapted to an embedded submanifold. Some sources permit an arbitrary coordinate \(k\)-plane rather than the first \(k\) axes; coordinate reordering makes the definitions equivalent.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 5, embedded submanifolds and slice charts.
