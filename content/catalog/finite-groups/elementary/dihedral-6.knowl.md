+++
id = "catalog/finite-groups/elementary/dihedral-6"
title = "Dihedral group D_6"
kind = "definition"
summary = "Cyclic rotations extended by an involution acting by inversion."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/semidirect-product"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

the **dihedral group \(D_{6}\)** is the [[algebra-groups/semidirect-product|semidirect product]] \(C_3\rtimes C_2\) in which the nontrivial element of \(C_2\) acts by inversion. Equivalently, its elements are pairs \((a,\epsilon)\in(\mathbb Z/3\mathbb Z)\times(\mathbb Z/2\mathbb Z)\), with
\[
(a,\epsilon)(b,\delta)=(a+(-1)^\epsilon b,\epsilon+\delta).
\]
The coordinates are reduced modulo \(3\) and \(2\), respectively; the subscript records the group order.

## Order and simplicity

The group has \(6\) elements. The first factor is a proper nontrivial [[algebra-groups/normal-subgroup|normal subgroup]], so this group is not simple.

## Notation and small cases

This catalogue uses \(D_{2n}\) for a group of order \(2n\); another common convention calls the same group \(D_n\). The abstract definition admits \(n=1,2\): it gives \(C_2\) and the [[catalog/finite-groups/elementary/klein-4|Klein four-group]], respectively. For \(n\geq3\), it is the symmetry group of a regular \(n\)-gon.

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), §1.17, pp. 13–14: dihedral groups (there denoted D_n with order 2n).
