+++
id = "algebra-groups/center-is-characteristic"
title = "Center is characteristic"
kind = "knowl"
summary = "The center of a group is invariant under every automorphism."
aliases = ["center-is-characteristic", "Center is characteristic"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/center-of-group", "algebra-groups/characteristic-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-groups/center-is-characteristic.md"
+++

**Proposition (Center is characteristic).**
Let \(G\) be a [[algebra-groups/group|group]] and let \(Z(G)\) denote its [[algebra-groups/center-of-group|center]]. Then \(Z(G)\) is a [[algebra-groups/characteristic-subgroup|characteristic subgroup]] of \(G\): for every \(\varphi\in\operatorname{Aut}(G)\),
\[
\varphi(Z(G))=Z(G).
\]

## Remarks

Every characteristic subgroup is normal, but the converse need not hold. The center is preserved because automorphisms preserve commutation: if \(z\in Z(G)\), then \(\varphi(z)\varphi(g)=\varphi(g)\varphi(z)\) for every \(g\in G\).
