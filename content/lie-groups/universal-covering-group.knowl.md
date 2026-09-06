+++
id = "lie-groups/universal-covering-group"
title = "Universal covering group"
kind = "knowl"
summary = "A simply connected covering Lie group of a connected Lie group, unique up to isomorphism."
aliases = ["universal-covering-group", "Universal covering group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/universal-covering-group.md"
prerequisites = ["lie-groups/lie-group-homomorphism", "lie-groups/covering-lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected Lie group. A **universal covering group** of \(G\) is a pair \((\widetilde G,p)\) where:

- \(\widetilde G\) is a [[lie-groups/simply-connected-lie-group|simply connected Lie group]];
- \(p:\widetilde G\to G\) is a smooth covering map and a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]];
- \(p\) is universal among connected [[lie-groups/covering-lie-group|covering Lie groups]] of \(G\): for every such covering \(q:H\to G\), there is a unique Lie group homomorphism \(r:\widetilde G\to H\) such that \(q\circ r=p\).

The existence of such a pair is guaranteed by [[lie-groups/universal-covering-group-existence|the existence theorem for universal covering groups]].

## Kernel and fundamental group
The kernel \(\ker(p)\) is a discrete normal subgroup of \(\widetilde G\) and lies in the [[lie-groups/center-of-a-lie-group|center of \(\widetilde G\)]]. After choosing basepoints, \(\ker(p)\) is naturally isomorphic to \(\pi_1(G)\). Consequently,
\[
G \cong \widetilde G / \ker(p)
\]
as a [[lie-groups/quotient-lie-group|quotient Lie group]].

## Lie algebra
The differential \(dp_e:\operatorname{Lie}(\widetilde G)\to \operatorname{Lie}(G)\) is an isomorphism of Lie algebras. Thus passage to the universal cover changes global topology but not the infinitesimal structure.
