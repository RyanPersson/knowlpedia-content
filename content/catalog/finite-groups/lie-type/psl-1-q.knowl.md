+++
id = "catalog/finite-groups/lie-type/psl-1-q"
title = "PSL(1,q)"
kind = "definition"
summary = "Determinant-one 1 by 1 matrices over F_q, modulo scalar matrices of determinant one."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For prime powers \(q\) and fixed matrix size \(1\), \(\operatorname{PSL}_{1}(q)\) is the [[algebra-groups/finite-group|finite group]] defined by
\[ \operatorname{PSL}_{1}(q)=\operatorname{SL}_{1}(\mathbb F_{q})/\{\lambda I:\lambda\in\mathbb F_{q}^\times,\ \lambda^{1}=1\}, \qquad
 \operatorname{SL}_{1}(\mathbb F_{q})=\{A\in M_{1}(\mathbb F_{q}):\det A=1\}. \]
This extends the projective special linear convention to matrix size one; multiplication is multiplication of scalar cosets. Here \(\mathbb F_{q}\) is the [[algebra-fields-galois/finite-field|field with \(q\) elements]].

## Order and simplicity

Its order is
\[ |\operatorname{PSL}_{1}(q)|=1. \]

It is the trivial group, so it is not simple under the nontrivial-group convention. The exact order is 1.

## Parameter convention

The determinant-one condition forces the sole matrix entry to be 1. The resulting group has one element. This is a degenerate matrix-size case, not an additional irreducible Lie-type family.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§2.4–2.5, pp. 19–21; Theorem 2.11.
