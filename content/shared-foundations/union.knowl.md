+++
id = "shared-foundations/union"
title = "Union"
kind = "knowl"
summary = "The set of elements that belong to at least one of the given sets."
aliases = ["union"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/union.md"
prerequisites = ["shared-foundations/set", "shared-foundations/zfc-axioms"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 3
+++

The **union** of a set \(\mathcal A\) of [[shared-foundations/set|sets]] is
\[
\bigcup\mathcal A=\{x:\text{there exists }A\in\mathcal A\text{ with }x\in A\}.
\]

## Notation

For two sets, write \(A\cup B=\bigcup\{A,B\}\).
For an [[shared-foundations/indexed-family-of-sets|indexed family]] \((A_i)_{i\in I}\), the notation \(\bigcup_{i\in I}A_i\) means the union of the sets in its range.

## Remarks

Union is dual to [[shared-foundations/intersection|intersection]] and interacts with [[shared-foundations/complement|complement]] via De Morgan’s laws in an ambient universe.

## Examples

- \(\{1,2\}\cup\{2,3\}=\{1,2,3\}\).
- If \(A_n=\{n\}\) for \(n\in\mathbb{N}\), then \(\bigcup_{n\in\mathbb{N}} A_n=\mathbb{N}\).
