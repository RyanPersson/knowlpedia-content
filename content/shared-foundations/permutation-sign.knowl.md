+++
id = "shared-foundations/permutation-sign"
title = "Permutation sign"
kind = "definition"
summary = "The sign of a finite permutation, determined by the parity of its inversions."
aliases = ["permutation-sign", "sign of a permutation", "parity of a permutation"]
domains = ["shared-foundations"]
prerequisites = ["shared-foundations/finite-permutation"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(\sigma\) be a [[shared-foundations/finite-permutation|finite permutation]] of \([n]\). An **inversion** is a pair of indices \(1\le i<j\le n\) for which \(\sigma(i)>\sigma(j)\). Write \(\operatorname{inv}(\sigma)\) for the number of these pairs.
The **sign** of \(\sigma\) is
\[
\operatorname{sgn}(\sigma)=(-1)^{\operatorname{inv}(\sigma)}\in\{+1,-1\}.
\]
Thus a permutation is even when its inversion number is even and odd otherwise. The empty permutation has sign +1.

## Reference

[Konarovskyi, Mathematics 2, §6.1](https://www.math.uni-leipzig.de/~konarovskyi/teaching/2019/Math2/pdf/notes/notes.pdf).
