+++
id = "catalog/finite-groups/elementary/klein-4"
title = "Klein four-group"
kind = "definition"
summary = "The product C_2 \u00d7 C_2 with coordinatewise addition."
aliases = ["Klein four-group", "four-group"]
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/direct-product-groups"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **Klein four-group** \(V_4\) is the [[algebra-groups/direct-product-groups|direct product]] \(C_2\times C_2\), with coordinatewise addition modulo two. It has four elements, and every nonidentity element has order two.

## Permutation realization

The subgroup \(\{1,(12)(34),(13)(24),(14)(23)\}\) of \(A_4\) is isomorphic to \(V_4\). Multiplying any two distinct double transpositions gives the third. Conjugation preserves cycle type, so this subgroup is normal in both \(A_4\) and \(S_4\).

## Nonsimplicity

Each nonidentity element generates a subgroup of order two. The group is abelian, so these subgroups are normal; it is not simple.

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), §4, symmetric and alternating groups; Theorem 4.33 and Remark 4.34, p. 69.
