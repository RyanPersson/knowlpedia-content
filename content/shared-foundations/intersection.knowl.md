+++
id = "shared-foundations/intersection"
title = "Intersection"
kind = "knowl"
summary = "The set of elements that belong to all of the given sets."
aliases = ["intersection"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/intersection.md"
prerequisites = ["shared-foundations/set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

The **intersection** of a nonempty set \(\mathcal A\) of [[shared-foundations/set|sets]] is
\[
\bigcap\mathcal A=\{x:\text{for every }A\in\mathcal A,\ x\in A\}.
\]

## Notation

For two sets, write \(A\cap B=\bigcap\{A,B\}\).
For an [[shared-foundations/indexed-family-of-sets|indexed family]] \((A_i)_{i\in I}\), the notation \(\bigcap_{i\in I}A_i\) means the intersection of the sets in its range.

An empty intersection requires an ambient set \(X\): for subsets \(A_i\subseteq X\), set \(\bigcap_{i\in\varnothing}A_i=X\). Without an ambient set, there is no set of all sets.

## Remarks

Intersection is dual to [[shared-foundations/union|union]] and is closely related to [[shared-foundations/subset|containment]]: one has \(A\subseteq B\) exactly when \(A\cap B=A\).

## Examples

- \(\{1,2\}\cap\{2,3\}=\{2\}\).
- If \(A=\{x\in\mathbb{R}: x<0\}\) and \(B=\{x\in\mathbb{R}: x\ge 0\}\), then \(A\cap B=\varnothing\) (see [[shared-foundations/empty-set|empty set]]).
