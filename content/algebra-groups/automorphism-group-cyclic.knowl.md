+++
id = "algebra-groups/automorphism-group-cyclic"
title = "Automorphisms of a cyclic group"
kind = "knowl"
summary = "Aut(C_n) is naturally isomorphic to (ℤ/nℤ)×"
aliases = ["automorphism-group-cyclic", "Automorphisms of a cyclic group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/automorphism-group-cyclic.md"
prerequisites = ["algebra-rings/group-of-units", "algebra-groups/group", "algebra-groups/cyclic-subgroup", "algebra-groups/group-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Proposition.** Let \(G=\langle g\rangle\) be a cyclic group of finite order \(n\). The map sending an automorphism \(\alpha\) to the unique residue class \(k\) satisfying \(\alpha(g)=g^k\) gives an isomorphism
\[
\mathrm{Aut}(G)\ \cong\ (\mathbb Z/n\mathbb Z)^\times,
\]
where \((\mathbb Z/n\mathbb Z)^\times\) is the [[algebra-rings/group-of-units|group of units]].

## Equivalent characterizations

The powers \(g^k\) that generate \(G\) are exactly those with \(\gcd(k,n)=1\), and composition of automorphisms corresponds to multiplication of their exponents modulo \(n\).

## Remarks

This makes automorphisms of cyclic groups completely explicit: an automorphism is exactly the choice of a generator-image. The group \(\mathrm{Aut}(G)\) itself is a central object in extension theory and semidirect products.
