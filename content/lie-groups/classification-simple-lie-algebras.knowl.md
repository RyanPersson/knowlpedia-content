+++
id = "lie-groups/classification-simple-lie-algebras"
title = "Classification of complex simple Lie algebras"
kind = "knowl"
summary = "Complex simple Lie algebras are classified by connected Dynkin diagrams of types A–G."
aliases = ["classification-simple-lie-algebras", "Classification of complex simple Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/classification-simple-lie-algebras.md"
prerequisites = ["lie-groups/simple-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Theorem (classification).** Every finite-dimensional complex [[lie-groups/simple-lie-algebra|simple Lie algebra]] is isomorphic to exactly one of the Lie algebras in the following families:
- Type \(A_n\) (\(n\ge 1\)): \(\mathfrak{sl}_{n+1}(\mathbb{C})\),
- Type \(B_n\) (\(n\ge 2\)): \(\mathfrak{so}_{2n+1}(\mathbb{C})\),
- Type \(C_n\) (\(n\ge 3\)): \(\mathfrak{sp}_{2n}(\mathbb{C})\),
- Type \(D_n\) (\(n\ge 4\)): \(\mathfrak{so}_{2n}(\mathbb{C})\),
- Exceptional types: \(E_6,E_7,E_8,F_4,G_2\).

These ranges avoid duplication: \(\mathfrak{sp}_4(\mathbb C)\cong\mathfrak{so}_5(\mathbb C)\) is counted as \(B_2\). The type \(C_2\) remains a valid name for that same isomorphism class.

## Equivalent characterizations

Equivalently, complex simple Lie algebras are classified by connected [[lie-groups/dynkin-diagram|Dynkin diagrams]], or by indecomposable [[lie-groups/cartan-matrix|Cartan matrices]] satisfying the Cartan axioms.

**Semisimple corollary.** Every complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] is a [[lie-groups/semisimple-direct-sum-simple|direct sum of simple ideals]], so its isomorphism type is determined by a (finite) multiset of Dynkin diagram types.

## Remarks

**Context.** The classification proceeds by choosing a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] \(\mathfrak{h}\), analyzing the associated [[lie-groups/root-system|root system]] in \(\mathfrak{h}^*\), and encoding the relative geometry of [[lie-groups/simple-root|simple roots]] in the Dynkin diagram. The root-system combinatorics precisely controls the [[fiber-bundles/lie-bracket|Lie bracket]] via the [[lie-groups/root-space-decomposition|root space decomposition]].

For selected global Lie groups with these types, see the [Lie-group table](/catalog/lie-groups/table/) and its [[catalog/lie-groups-table-guide|guide to forms and coverings]].

## References

- Pavel Etingof, [Lie Groups and Lie Algebras](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §23.2, Theorem 23.7; §23.8, Remark 23.18; §24.2. The low-rank identification \(B_2\cong C_2\) is stated in Remark 23.18, printed p. 128.
