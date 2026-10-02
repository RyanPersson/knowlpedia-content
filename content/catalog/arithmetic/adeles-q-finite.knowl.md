+++
id = "catalog/arithmetic/adeles-q-finite"
title = "Finite adeles of Q"
kind = "definition"
summary = "Finite adeles of Q with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["shared-foundations/rational-numbers", "algebra-fields-galois/adeles-restricted-product"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

Put \(F=\mathbb Q\). Write \(F_v\) for its completion at \(v\), and \(\mathcal O_v\) for the valuation ring at a nonarchimedean place. At any archimedean places put \(\mathcal O_v=F_v\).

For the [[shared-foundations/rational-numbers|rational field]] \(\mathbb Q\), the **finite adele ring of \(\mathbb Q\)** is the [[algebra-fields-galois/adeles-restricted-product|restricted product]]

\[
\mathbb A_{\mathbb Q,f}=\prod_{v\nmid\infty}{}'(F_v,\mathcal O_v),
\]
An adele is integral at all but finitely many nonarchimedean places. No integrality condition is imposed at archimedean places.

## Topology

A basic open set is \(\prod_v U_v\), with each \(U_v\) open in the corresponding [[algebra-fields-galois/local-field|local field]] and \(U_v=\mathcal O_v\) for all but finitely many nonarchimedean places. Operations are coordinatewise. This restricted-product topology is part of the object; the topology inherited from the unrestricted direct product is different.

## Scope of the places

The omitted archimedean factor is \(\prod_{v\mid\infty}\mathbb Q_v\). For \(\mathbb Q\) it is \(\mathbb R\), so \(\mathbb A_{\mathbb Q}=\mathbb R\times\mathbb A_{\mathbb Q,f}\). Finite adeles must not be identified with the full adele ring.

## Units

An adele is a unit exactly when every coordinate is nonzero and its inverse is again an adele. The resulting [[catalog/arithmetic/ideles-q-finite|idele group]] carries its own restricted-product group topology.

## References

1. [J. S. Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, §4, Ideles, pp. 169–172, especially restricted-product topology and Notes.
