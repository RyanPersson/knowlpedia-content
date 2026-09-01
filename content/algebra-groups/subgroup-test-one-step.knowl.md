+++
id = "algebra-groups/subgroup-test-one-step"
title = "Subgroup Test (one-step)"
kind = "knowl"
summary = "A nonempty subset H of a group is a subgroup exactly when xy⁻¹ belongs to H for all x,y in H."
aliases = ["subgroup-test-one-step", "Subgroup Test (one-step)"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "shared-foundations/subset", "algebra-groups/subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/subgroup-test-one-step.md"
+++

**One-step subgroup test.** Let \(G\) be a [[algebra-groups/group|group]] and let \(H\) be a nonempty [[shared-foundations/subset|subset]] of \(G\). Then \(H\) is a [[algebra-groups/subgroup|subgroup]] of \(G\) if and only if
\[
x,y\in H\quad\Longrightarrow\quad xy^{-1}\in H.
\]

## Remarks

Taking \(x=y\) gives the identity, taking \(x=e\) gives inverses, and the displayed condition then gives closure under products.
