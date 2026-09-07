+++
id = "algebra-groups/alternating-group"
title = "Alternating Group"
kind = "knowl"
summary = "The subgroup of even permutations in the symmetric group, equivalently the kernel of the sign homomorphism."
aliases = ["alternating-group", "Alternating Group"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/subgroup", "algebra-groups/kernel-group", "shared-foundations/permutation-sign"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 1
+++

For \(n\geq 2\), the **alternating group** \(A_n\) is the [[algebra-groups/kernel-group|kernel]]
\[
A_n=\ker\bigl(\operatorname{sgn}:S_n\to\{1,-1\}\bigr),
\]
where \(S_n\) is the group of [[shared-foundations/finite-permutation|permutations of \(n\) elements]] under composition and \(\operatorname{sgn}\) is the [[shared-foundations/permutation-sign|sign of a finite permutation]].

## Properties

Thus \(A_n\) consists exactly of the even permutations.

The subgroup \(A_n\) is [[algebra-groups/normal-subgroup|normal]] in \(S_n\) and has index \(2\), hence \(|A_n|=n!/2\). For \(n\geq 5\), \(A_n\) is nonabelian simple.
