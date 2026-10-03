+++
id = "catalog/lie-groups/sp-2"
title = "Sp(2)"
kind = "definition"
summary = "Sp(2) as a separately identified real Lie group, with its defining operations and dimension."
aliases = []
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/compact-symplectic-group"]
dependency_heuristic = "catalog-semantic-core-v1"
dependency_review_count = 1
+++

\(\operatorname{Sp}(2)\) is the compact [[lie-groups/compact-symplectic-group|symplectic group]]
\[ \operatorname{Sp}(2)=\{A\in M_{2}(\mathbb H):A^*A=I\}, \]
where \(A^*=\overline A^{\mathsf T}\). Matrices act on the right quaternionic module by left multiplication; the adjoint uses quaternionic conjugation.

## Dimensions and structure

This group has real dimension \(10\). The tangent algebra is formed by skew-Hermitian quaternionic matrices. The parameter counts quaternionic coordinates. Thus Sp(2) is distinct from the real split group Sp(4,R). No ordinary quaternionic determinant is used in the definition.

The scalar field of its matrix entries does not assign a [[lie-groups/complex-lie-group|complex Lie group]] structure to this real [[fiber-bundles/lie-group|Lie group]]. In particular, a [[algebra-groups/group-homomorphism|group homomorphism]] is not called linear merely because the group has a matrix representation.

## References

1. [Pavel Etingof, Lie Groups and Lie Algebras (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §6.2, Proposition 6.7 and Corollary 6.8; §6.3, Lemma 6.10, pp. 40–43.
