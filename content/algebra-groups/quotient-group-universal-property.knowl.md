+++
id = "algebra-groups/quotient-group-universal-property"
title = "Universal Property of Quotient Groups"
kind = "knowl"
summary = "A homomorphism that kills a normal subgroup factors uniquely through the corresponding quotient group."
aliases = ["quotient-group-universal-property", "Universal Property of Quotient Groups"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/normal-subgroup", "algebra-groups/quotient-group", "algebra-groups/group-homomorphism"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/quotient-group-universal-property.md"
+++

Let \(G\) be a [[algebra-groups/group|group]], \(N\trianglelefteq G\) a [[algebra-groups/normal-subgroup|normal subgroup]], and \(\pi:G\to G/N\) the canonical map to the [[algebra-groups/quotient-group|quotient group]]. If \(f:G\to K\) is a [[algebra-groups/group-homomorphism|group homomorphism]] with \(N\subseteq\ker(f)\), then there is a unique homomorphism \(\bar f:G/N\to K\) such that
\[
f=\bar f\circ\pi.
\]
It is given by \(\bar f(gN)=f(g)\).

## Equivalent characterizations

Thus composition with \(\pi\) gives a bijection between homomorphisms \(G/N\to K\) and homomorphisms \(G\to K\) that send every element of \(N\) to the identity of \(K\).
