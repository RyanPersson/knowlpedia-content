+++
id = "catalog/finite-groups/elementary/sym-4"
title = "Symmetric group S_4"
kind = "definition"
summary = "Permutations of 4 letters under composition."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group", "shared-foundations/bijective-function"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **symmetric group \(S_4\)** is the [[algebra-groups/group|group]] of all [[shared-foundations/bijective-function|bijections]] of \(\{1,\ldots,4\}\), with composition as multiplication.

## Order and normal subgroup

There are 24 permutations: choose the images of the 4 letters successively. The even permutations form the proper nontrivial [[algebra-groups/normal-subgroup|normal subgroup]] \(A_4\), the kernel of the sign map. Therefore \(S_4\) is not simple.

## Klein subgroup

The identity and the three double transpositions form a normal [[catalog/finite-groups/elementary/klein-4|Klein four-group]]. Conjugation permutes these three nonidentity elements.

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), §4, symmetric and alternating groups; Theorem 4.33 and Remark 4.34, p. 69.
