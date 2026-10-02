+++
id = "catalog/finite-groups/elementary/sym-3"
title = "Symmetric group S_3"
kind = "definition"
summary = "Permutations of 3 letters under composition."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group", "shared-foundations/bijective-function"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **symmetric group \(S_3\)** is the [[algebra-groups/group|group]] of all [[shared-foundations/bijective-function|bijections]] of \(\{1,\ldots,3\}\), with composition as multiplication.

## Order and normal subgroup

There are 6 permutations: choose the images of the 3 letters successively. The even permutations form the proper nontrivial [[algebra-groups/normal-subgroup|normal subgroup]] \(A_3\), the kernel of the sign map. Therefore \(S_3\) is not simple.

## Triangle symmetries

The generators \((123)\) and \((12)\) satisfy the dihedral relations. The action on three vertices identifies this group with [[catalog/finite-groups/elementary/dihedral-6|\(D_6\)]].

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), §4, symmetric and alternating groups; Theorem 4.33 and Remark 4.34, p. 69.
