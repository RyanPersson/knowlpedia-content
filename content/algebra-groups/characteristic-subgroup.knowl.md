+++
id = "algebra-groups/characteristic-subgroup"
title = "Characteristic Subgroup"
kind = "knowl"
summary = "A subgroup preserved by every automorphism of the ambient group."
aliases = ["characteristic-subgroup", "Characteristic Subgroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/characteristic-subgroup.md"
prerequisites = ["algebra-groups/group", "algebra-groups/subgroup", "algebra-groups/automorphism-group", "algebra-groups/normal-subgroup", "algebra-groups/inner-automorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[algebra-groups/group|group]] and let \(H\le G\) be a [[algebra-groups/subgroup|subgroup]]. The subgroup \(H\) is **characteristic** in \(G\) if, for every automorphism \(\varphi:G\to G\), one has
\[
\varphi(H)=H.
\]

## Equivalent characterizations

Equivalently, \(H\) is invariant under the action of the [[algebra-groups/automorphism-group|automorphism group]] \(\mathrm{Aut}(G)\) on the underlying set of \(G\). Every characteristic subgroup is [[algebra-groups/normal-subgroup|normal]], since conjugations are [[algebra-groups/inner-automorphism|inner automorphisms]].

## Examples

- The [[algebra-groups/center-of-group|center]] \(Z(G)\) is characteristic in \(G\).
- The [[algebra-groups/commutator-subgroup|commutator subgroup]] \([G,G]\) is characteristic in \(G\).
- In a cyclic group of order \(n\), the unique subgroup of each divisor \(d\mid n\) is characteristic.
- *(Non-example)* In \((\mathbb{Z}/2\mathbb{Z})^2\), any subgroup of order \(2\) is not characteristic (automorphisms permute the three such subgroups).
