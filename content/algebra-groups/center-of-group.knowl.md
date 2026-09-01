+++
id = "algebra-groups/center-of-group"
title = "Center of a Group"
kind = "knowl"
summary = "The subgroup of elements that commute with every element of a group."
aliases = ["center-of-group", "Center of a Group"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/center-of-group.md"
+++

Let \(G\) be a [[algebra-groups/group|group]]. The **center** of \(G\) is the subgroup
\[
Z(G)=\{z\in G:zx=xz\text{ for every }x\in G\}.
\]

## Remarks

The group \(G\) is abelian if and only if \(Z(G)=G\). Moreover, \(Z(G)\) is always a [[algebra-groups/characteristic-subgroup|characteristic subgroup]] (hence normal), and it is the intersection of the [[algebra-groups/centralizer|centralizers]] of all elements of \(G\).

## Examples

- If \(G\) is abelian, then \(Z(G)=G\).
- In \(S_3\), \(Z(S_3)=\{e\}\).
- In the quaternion group \(Q_8\), the center is \(\{\pm 1\}\).
