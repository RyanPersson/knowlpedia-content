+++
id = "catalog/arithmetic/adeles-function-field"
title = "Adeles of a global function field"
kind = "definition"
summary = "Adeles of K with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/global-function-field", "algebra-fields-galois/adeles-restricted-product"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

Let \(F=K\) be a global function field. Write \(F_v\) for its completion at \(v\), and \(\mathcal O_v\) for the valuation ring at a nonarchimedean place. At any archimedean places put \(\mathcal O_v=F_v\).

Let \(K\) be the specified [[algebra-fields-galois/global-function-field|global function field]]. the **adele ring of K** is the [[algebra-fields-galois/adeles-restricted-product|restricted product]]

\[
\mathbb A_{K}=\prod_{v}{}'(F_v,\mathcal O_v),
\]
An adele is integral at all but finitely many nonarchimedean places. No integrality condition is imposed at archimedean places.

## Topology

A basic open set is \(\prod_v U_v\), with each \(U_v\) open in the corresponding [[algebra-fields-galois/local-field|local field]] and \(U_v=\mathcal O_v\) for all but finitely many nonarchimedean places. Operations are coordinatewise. This restricted-product topology is part of the object; the topology inherited from the unrestricted direct product is different.

## Scope of the places

For a [[algebra-fields-galois/number-field|number field]] the archimedean factors are included; for a function field every place is nonarchimedean. In particular, the place at infinity of \(\mathbb F_q(t)\) is still included and is nonarchimedean.

## Units

An adele is a unit exactly when every coordinate is nonzero and its inverse is again an adele. The resulting [[catalog/arithmetic/ideles-function-field|idele group]] carries its own restricted-product group topology.

## References

1. [J. S. Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, §4, Ideles, pp. 169–172, especially restricted-product topology and Notes.
