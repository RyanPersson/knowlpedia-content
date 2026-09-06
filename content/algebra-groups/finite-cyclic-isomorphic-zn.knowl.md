+++
id = "algebra-groups/finite-cyclic-isomorphic-zn"
title = "Finite cyclic group is isomorphic to ℤ/nℤ"
kind = "knowl"
summary = "A cyclic group of order n is isomorphic to the additive group ℤ/nℤ."
aliases = ["finite-cyclic-isomorphic-zn", "Finite cyclic group is isomorphic to ℤ/nℤ"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/finite-cyclic-isomorphic-zn.md"
prerequisites = ["algebra-groups/group", "algebra-groups/group-isomorphism", "algebra-groups/cyclic-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Proposition (finite cyclic groups).** Let \(G\) be a [[algebra-groups/group|group]]. Suppose \(G=\langle g\rangle\) is cyclic of finite order \(n\). Then \(G\) is [[algebra-groups/group-isomorphism|isomorphic]] to the additive group \(\mathbb Z/n\mathbb Z\). Concretely, the chosen generator \(g\) determines the isomorphism
\[
\varphi:\mathbb Z/n\mathbb Z \longrightarrow G,\qquad \varphi(\overline{k})=g^k
\]
is a well-defined isomorphism.

## Remarks

This identifies finite cyclic groups up to isomorphism by their order. The displayed isomorphism is not canonical: it depends on the choice of generator \(g\).
