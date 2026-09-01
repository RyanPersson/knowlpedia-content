+++
id = "algebra-groups/class-equation-decomposition"
title = "Class equation decomposition"
kind = "knowl"
summary = "A finite group decomposes into its center and nontrivial conjugacy classes"
aliases = ["class-equation-decomposition", "Class equation decomposition"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/conjugation-action-self", "algebra-groups/center-of-group", "algebra-groups/centralizer", "algebra-groups/class-equation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/class-equation-decomposition.md"
+++

**Proposition (Decomposition underlying the class equation).**
Let \(G\) be a finite [[algebra-groups/group|group]], acting on itself by [[algebra-groups/conjugation-action-self|conjugation]]. Then:

1. \(G\) is a disjoint union of its conjugacy classes.
2. The elements with singleton conjugacy class are exactly the [[algebra-groups/center-of-group|center]] \(Z(G)\).
3. For each \(x\in G\), the conjugacy class of \(x\) has size \([G:C_G(x)]\), where \(C_G(x)\) is the [[algebra-groups/centralizer|centralizer]].

Thus, choosing one representative \(x_i\) from each conjugacy class outside the center gives the [[algebra-groups/class-equation|class equation]]
\[
|G| \;=\; |Z(G)| \;+\; \sum_i [G:C_G(x_i)].
\]

## Remarks

The formula follows from the [[algebra-groups/orbit-stabilizer-theorem|orbit–stabilizer theorem]] and is a key counting tool for finite \(p\)-groups.
