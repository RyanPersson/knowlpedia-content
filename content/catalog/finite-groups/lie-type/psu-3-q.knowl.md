+++
id = "catalog/finite-groups/lie-type/psu-3-q"
title = "PSU(3,q)"
kind = "definition"
summary = "Special unitary 3 by 3 matrices over F_(q²), modulo their scalar center; q is the fixed-field parameter."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "algebra-fields-galois/fixed-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For prime powers \(q\) and fixed matrix size \(3\), \(\operatorname{PSU}_{3}(q)\) is the [[algebra-groups/finite-group|finite group]] defined by
\[
 \operatorname{PSU}_{3}(q)=\operatorname{SU}_{3}(q)/\{\lambda I:\lambda^{q+1}=1,\ \lambda^{3}=1\},
 \quad \operatorname{SU}_{3}(q)=\{A\in M_{3}(\mathbb F_{q^2}): (A^{(q)})^{\mathsf T}A=I,\ \det A=1\}.
\]
Here \(A^{(q)}\) is entrywise \(q\)-th power. The [[algebra-fields-galois/finite-field|matrix field]] has \(q^2\) elements; its involution has [[algebra-fields-galois/fixed-field|fixed field]] of size \(q\). The scalar \(\lambda\) belongs to \(\mathbb F_{q^2}^\times\); multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSU}_{3}(q)|=\frac{q^{3}(q^{2}-1)(q^{3}+1)}{\gcd(3,q+1)}. \]

It is simple exactly when q ≥ 3.

## Parameter convention

The parameter \(q\) is the size of the fixed field, while matrices have entries in \(\mathbb F_{q^2}\). The Hermitian form is \(h(v,w)=\sum_i v_i^q w_i\). All nondegenerate Hermitian forms of this dimension over the finite field give isomorphic groups. Type \({}^2A_{n-1}\) has absolute rank \(n-1\); it is not a unitary group over the real or complex numbers.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§5.2–5.3, pp. 59–63; PSU(2,q), PSU(3,2), and the PSU(4,2) identification.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
