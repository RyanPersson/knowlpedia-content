+++
id = "algebra-groups/centralizer"
title = "Centralizer"
kind = "knowl"
summary = "The subgroup of elements that commute with every element of a given subset."
aliases = ["centralizer"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/centralizer.md"
+++

Let \(G\) be a [[algebra-groups/group|group]] and \(S\subseteq G\) a subset. The **centralizer of \(S\) in \(G\)** is the [[algebra-groups/subgroup|subgroup]]
\[
C_G(S)=\{g\in G:gs=sg\text{ for every }s\in S\}.
\]
For \(x\in G\), one writes \(C_G(x)\) for \(C_G(\{x\})\).

## Remarks

For the conjugation action, \(C_G(x)\) is the stabilizer of \(x\), so it controls the size of the [[algebra-groups/conjugacy-class|conjugacy class]] of \(x\). The center satisfies \(Z(G)=C_G(G)\).

## Examples

- If \(G\) is abelian, then \(C_G(S)=G\) for every \(S\subseteq G\).
- In \(S_3\), \(C_{S_3}((12))=\{e,(12)\}\).
- In \(S_3\), \(C_{S_3}((123))=\{e,(123),(132)\}\).
