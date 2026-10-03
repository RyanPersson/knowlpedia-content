+++
id = "catalog/finite-groups/lie-type/psu-1-q"
title = "PSU(1,q)"
kind = "definition"
summary = "Special unitary 1 by 1 matrices over F_(q²), modulo their scalar center; q is the fixed-field parameter."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "algebra-fields-galois/fixed-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For prime powers \(q\) and fixed matrix size \(1\), \(\operatorname{PSU}_{1}(q)\) is the [[algebra-groups/finite-group|finite group]] defined by
\[
 \operatorname{PSU}_{1}(q)=\operatorname{SU}_{1}(q)/\{\lambda I:\lambda^{q+1}=1,\ \lambda^{1}=1\},
 \quad \operatorname{SU}_{1}(q)=\{A\in M_{1}(\mathbb F_{q^2}): (A^{(q)})^{\mathsf T}A=I,\ \det A=1\}.
\]
Here \(A^{(q)}\) is entrywise \(q\)-th power. The [[algebra-fields-galois/finite-field|matrix field]] has \(q^2\) elements; its involution has [[algebra-fields-galois/fixed-field|fixed field]] of size \(q\). The scalar \(\lambda\) belongs to \(\mathbb F_{q^2}^\times\); multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSU}_{1}(q)|=1. \]

It is the trivial group, so it is not simple under the nontrivial-group convention. The exact order is 1.

## Parameter convention

The determinant-one condition forces the sole matrix entry to be 1. The resulting group has one element. This is a degenerate matrix-size case, not an additional irreducible Lie-type family.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§5.2–5.3, pp. 59–63; PSU(2,q), PSU(3,2), and the PSU(4,2) identification.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
