+++
id = "catalog/finite-groups/lie-type/psu-4-2"
title = "PSU(4,2)"
kind = "definition"
summary = "Special unitary 4 by 4 matrices over F_(2²), modulo their scalar center; 2 is the fixed-field parameter."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "algebra-fields-galois/fixed-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

\(\operatorname{PSU}_{4}(2)\) is the following [[algebra-groups/finite-group|finite group]], with \(n=4\) and \(q=2\):
\[
 \operatorname{PSU}_{4}(2)=\operatorname{SU}_{4}(2)/\{\lambda I:\lambda^{2+1}=1,\ \lambda^{4}=1\},
 \quad \operatorname{SU}_{4}(2)=\{A\in M_{4}(\mathbb F_{2^2}): (A^{(2)})^{\mathsf T}A=I,\ \det A=1\}.
\]
Here \(A^{(2)}\) is entrywise \(2\)-th power. The [[algebra-fields-galois/finite-field|matrix field]] has \(2^2\) elements; its involution has [[algebra-fields-galois/fixed-field|fixed field]] of size \(2\). The scalar \(\lambda\) belongs to \(\mathbb F_{2^2}^\times\); multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSU}_{4}(2)|=25920. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]]. The exact order is 25,920.

## Parameter convention

The parameter \(q\) is the size of the fixed field, while matrices have entries in \(\mathbb F_{q^2}\). The Hermitian form is \(h(v,w)=\sum_i v_i^q w_i\). All nondegenerate Hermitian forms of this dimension over the finite field give isomorphic groups. Type \({}^2A_{n-1}\) has absolute rank \(n-1\); it is not a unitary group over the real or complex numbers.

## Small-group identification

The exceptional isomorphism is \(\operatorname{PSU}_4(2)\cong\operatorname{PSp}_4(3)\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§5.2–5.3, pp. 59–63; PSU(2,q), PSU(3,2), and the PSU(4,2) identification.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
