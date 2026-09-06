+++
id = "shared-foundations/finite-permutation"
title = "Finite permutation"
kind = "definition"
summary = "A bijection from a finite initial segment of the natural numbers to itself."
aliases = ["finite-permutation", "Finite permutation", "permutation of n elements"]
domains = ["shared-foundations"]
prerequisites = ["shared-foundations/bijective-function", "shared-foundations/natural-numbers"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

For \(n\in\mathbb N\), write \([n]=\{1,\ldots,n\}\) (with \([0]=\varnothing\)). A **finite permutation of size \(n\)** is a [[shared-foundations/bijective-function|bijective function]] \(\sigma:[n]\to[n]\). The set of all such permutations is denoted \(S_n\).

In one-line notation, \(\sigma\) is recorded as \((\sigma(1),\ldots,\sigma(n))\), which contains each element of \([n]\) exactly once.

## Reference

[Konarovskyi, Mathematics 2, §6.1](https://www.math.uni-leipzig.de/~konarovskyi/teaching/2019/Math2/pdf/notes/notes.pdf).
