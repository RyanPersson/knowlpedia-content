+++
id = "shared-foundations/finite-sum"
title = "Finite sum"
kind = "definition"
summary = "Addition over a finite ordered list, with empty sum zero and order independence in an abelian group."
aliases = ["summation", "empty sum"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/function", "algebra-groups/abelian-group", "shared-foundations/finite-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For elements \(a_1,\ldots,a_n\) of an additive [[algebra-groups/abelian-group|abelian group]], the **finite sum** is defined recursively by
\[
\sum_{j=1}^{0}a_j=0,\qquad
\sum_{j=1}^{n+1}a_j=\left(\sum_{j=1}^{n}a_j\right)+a_{n+1}.
\]
Associativity makes parenthesization immaterial, and commutativity permits arbitrary reordering. Hence for a family \((a_i)_{i\in I}\) indexed by a [[shared-foundations/finite-set|finite set]], the notation \(\sum_{i\in I}a_i\) does not require an ordering of \(I\).

## Grouping

Splitting a finite index set into disjoint subsets splits the sum into the sum over those subsets. No convergence condition is required for a finite sum. An infinite series instead requires a definition of convergence of its partial sums.
