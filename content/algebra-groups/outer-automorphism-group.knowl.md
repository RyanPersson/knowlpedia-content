+++
id = "algebra-groups/outer-automorphism-group"
title = "Outer Automorphism Group"
kind = "knowl"
summary = "Automorphisms modulo inner automorphisms"
aliases = ["outer-automorphism-group", "Outer Automorphism Group"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/inner-automorphism", "algebra-groups/automorphism-group", "algebra-groups/quotient-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-groups/outer-automorphism-group.md"
+++

For a [[algebra-groups/group|group]] \(G\), the subgroup \(\operatorname{Inn}(G)\) of [[algebra-groups/inner-automorphism|inner automorphisms]] is normal in the [[algebra-groups/automorphism-group|automorphism group]] \(\operatorname{Aut}(G)\). The **outer automorphism group** is the [[algebra-groups/quotient-group|quotient group]]
\[
\operatorname{Out}(G) := \operatorname{Aut}(G)\big/\operatorname{Inn}(G),
\]
which measures automorphisms not arising from conjugation.

## Examples

- If \(G\) is abelian, then \(\operatorname{Inn}(G)\) is trivial, so \(\operatorname{Out}(G)=\operatorname{Aut}(G)\).
- If \(\operatorname{Aut}(G)=\operatorname{Inn}(G)\), then \(\operatorname{Out}(G)\) is trivial.

## Remarks

The group \(\operatorname{Out}(G)\) is trivial exactly when every automorphism of \(G\) is inner.
