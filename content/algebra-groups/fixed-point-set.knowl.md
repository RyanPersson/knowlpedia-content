+++
id = "algebra-groups/fixed-point-set"
title = "Fixed-Point Set"
kind = "knowl"
summary = "The subset of points fixed by every group element in an action."
aliases = ["fixed-point-set", "Fixed-Point Set"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group-action"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/fixed-point-set.md"
+++

Let a [[algebra-groups/group-action|group action]] of a group \(G\) on a set \(X\) be given. The **fixed-point set** of the action is
\[
X^G := \{x\in X : g\cdot x = x \text{ for all } g\in G\}.
\]

## Equivalent characterizations

Equivalently, \(x\in X^G\) iff its [[algebra-groups/stabilizer|stabilizer]] is all of \(G\), i.e. \(G_x=G\).

## Examples

- For the trivial action \(g\cdot x=x\) for all \(g,x\), one has \(X^G=X\).
- For the conjugation action of \(G\) on itself, the fixed-point set is the [[algebra-groups/center-of-group|center]] \(Z(G)\).
- For the action of \(C_n\) on the vertices of a regular \(n\)-gon by rotation, the fixed-point set is empty if \(n>1\) (no vertex is fixed by all rotations).
