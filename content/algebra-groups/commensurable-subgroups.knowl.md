+++
id = "algebra-groups/commensurable-subgroups"
title = "Commensurable subgroups"
kind = "definition"
summary = "Two subgroups whose intersection has finite index in each."
aliases = ["commensurability of subgroups", "commensurable up to conjugacy"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/subgroup", "algebra-groups/index-of-subgroup"]
+++

Subgroups \(H,K\) of a group \(G\) are **commensurable** if
\[
[H:H\cap K]<\infty\quad\text{and}\quad[K:H\cap K]<\infty.
\]
Here each bracket is the [[algebra-groups/index-of-subgroup|index of a subgroup]]. They are **commensurable up to conjugacy in \(G\)** if \(H\) and \(gKg^{-1}\) are commensurable for some \(g\in G\).

## Example

Inside \((\mathbb R,+)\), the groups \(\mathbb Z\) and \(2\mathbb Z\) are commensurable. The groups \(\mathbb Z\) and \(\sqrt2\mathbb Z\) are not: their intersection is zero and has infinite index in each.

## Different comparison questions

Conjugacy allows repositioning inside the given ambient group. Abstract commensurability asks only for isomorphic finite-index subgroups and need not respect a specified embedding. Arithmetic Kleinian classification uses the ambient-group, up-to-conjugacy version.
