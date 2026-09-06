+++
id = "algebra-groups/conjugation-action"
title = "Conjugation Action"
kind = "knowl"
summary = "The action of a group on itself or its subgroups by conjugation."
aliases = ["conjugation-action", "Conjugation Action"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/group-action"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/conjugation-action.md"
+++

Let \(G\) be a [[algebra-groups/group|group]]. The **conjugation action** of \(G\) on itself is the [[algebra-groups/group-action|group action]]
\[
g\cdot x := gxg^{-1}.
\]

## Remarks

Under this action, two elements lie in the same orbit exactly when they are [[algebra-groups/conjugate-element|conjugate]], so the orbits are the [[algebra-groups/conjugacy-class|conjugacy classes]]. The stabilizer of \(x\) is its [[algebra-groups/centralizer|centralizer]], and the kernel is the [[algebra-groups/center-of-group|center]].

More generally, \(G\) acts on its subgroups by \(g\cdot H := gHg^{-1}\). The stabilizer of \(H\) is its [[algebra-groups/normalizer|normalizer]], and \(H\) is normal if and only if every element of \(G\) fixes it.

## Examples

- In \(S_3\), the conjugacy classes are \(\{e\}\), the three transpositions, and the two \(3\)-cycles.
- If \(G\) is abelian, every conjugacy class is a singleton.
