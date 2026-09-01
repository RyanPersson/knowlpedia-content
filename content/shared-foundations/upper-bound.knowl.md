+++
id = "shared-foundations/upper-bound"
title = "Upper bound"
kind = "knowl"
summary = "An element that is greater than or equal to every element of a subset in an ordered set."
aliases = ["upper-bound", "Upper bound"]
domains = ["shared-foundations"]
prerequisites = ["shared-foundations/partial-order"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shared-foundations/upper-bound.md"
+++

An **upper bound** of a subset \(A\) of a [[shared-foundations/partial-order|partially ordered set]] \((P,\le)\) is an element \(u\in P\) such that \(a\le u\) for all \(a\in A\). The subset \(A\) is **bounded above** if it has at least one upper bound in \(P\).

## Remarks

Upper bounds are paired with [[shared-foundations/lower-bound|lower bounds]] and are used to define least upper bounds (the [[real-analysis/supremum|supremum]] in real analysis).

## Examples

- In \((\mathbb{Z},\le)\), the integer \(10\) is an upper bound for the subset \(\{1,4,7\}\).
- In the poset \((\mathcal P(X),\subseteq)\), the set \(A\cup B\) is an upper bound for \(\{A,B\}\), where \(A\cup B\) is the [[shared-foundations/union|union]] of \(A\) and \(B\).
