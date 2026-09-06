+++
id = "algebra-groups/kernel-group"
title = "Kernel of a group homomorphism"
kind = "knowl"
summary = "The subgroup of elements mapped to the identity by a group homomorphism."
aliases = ["kernel-group", "Kernel of a group homomorphism"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group-homomorphism"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/kernel-group.md"
+++

Let \(\varphi\colon G\to H\) be a [[algebra-groups/group-homomorphism|group homomorphism]]. The **kernel** of \(\varphi\) is the subgroup
\[
\ker(\varphi)=\{g\in G:\varphi(g)=e_H\}.
\]

## Equivalent characterizations

Equivalently, \(\ker(\varphi)\) is the [[shared-foundations/preimage|preimage]] of \(\{e_H\}\) under \(\varphi\).

## Remarks

The kernel is a [[algebra-groups/normal-subgroup|normal subgroup]] of \(G\), and \(\varphi\) is injective if and only if \(\ker(\varphi)=\{e_G\}\). The [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]] identifies \(G/\ker(\varphi)\) with the image of \(\varphi\).

## Examples

- For the reduction map \(\pi\colon\mathbb Z\to\mathbb Z/n\mathbb Z\), one has \(\ker(\pi)=n\mathbb Z\).
- For \(\operatorname{sgn}\colon S_n\to\{\pm1\}\), the kernel is \(A_n\).
- For \(\det\colon GL_m(\mathbb R)\to\mathbb R^\times\), the kernel is \(SL_m(\mathbb R)\).
