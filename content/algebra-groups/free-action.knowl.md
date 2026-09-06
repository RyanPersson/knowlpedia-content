+++
id = "algebra-groups/free-action"
title = "Free Action"
kind = "knowl"
summary = "An action in which only the identity can fix a point"
aliases = ["free-action", "Free Action"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group-action", "algebra-groups/stabilizer"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/free-action.md"
+++

A [[algebra-groups/group-action|group action]] of a group \(G\) on a set \(X\) is **free** if every [[algebra-groups/stabilizer|stabilizer]] is trivial:
\[
G_x=\{e\}\qquad(x\in X).
\]
Equivalently, if \(g\cdot x=x\) for some \(x\in X\), then \(g=e\).

## Remarks

Free actions are one half of the definition of a [[algebra-groups/regular-action|regular action]] (free + transitive).

## Examples

- The left translation action of \(G\) on itself is free.
- The action of \(G\) on the coset space \(G/H\) by left multiplication is free iff \(H=\{e\}\).
- The action of \(C_n\) on the vertices of a regular \(n\)-gon by rotation is free when restricted to the vertex set (no nontrivial rotation fixes a vertex).
