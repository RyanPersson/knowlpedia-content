+++
id = "catalog/arithmetic/ideles-number-field"
title = "Ideles of a number field"
kind = "definition"
summary = "Ideles of K with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/adeles-number-field"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

Let \(F=K\) be a number field. For each place \(v\), write \(F_v\) for its completion. At nonarchimedean places let \(\mathcal O_v\) be the valuation ring; at any archimedean places put \(\mathcal O_v=F_v\).

The **idele group of \(K\)** is the multiplicative restricted product
\[
\mathbb A_{K}^\times=\prod_{v}{}'(F_v^\times,\mathcal O_v^\times).
\]

Its elements have nonzero coordinates everywhere and unit coordinates at almost every nonarchimedean place. Algebraically this is the unit group of the [[catalog/arithmetic/adeles-number-field|corresponding adele ring]].

## Topology

Basic opens are products of local multiplicative open sets that equal \(\mathcal O_v^\times\) at almost all nonarchimedean places. This gives a locally compact abelian topological group. The idele topology is not the subspace topology inherited from the adele ring; continuity of inversion is one reason the distinction matters.

## Operations and scope

The operation is coordinatewise multiplication and the identity has every coordinate equal to one. These objects belong to categories of groups, rather than to categories of fields or rings. A group homomorphism need not preserve an ambient additive operation.

## Global elements

Every element of \(K^\times\) embeds diagonally: a nonzero global element is a unit at almost every finite place. For full ideles the global subgroup is discrete. Its quotient is the idele class group, a further construction.

## References

1. [J. S. Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, §4, Ideles, pp. 169–172, especially restricted-product topology and Notes.
