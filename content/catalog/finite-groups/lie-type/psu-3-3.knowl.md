+++
id = "catalog/finite-groups/lie-type/psu-3-3"
title = "PSU(3,3)"
kind = "definition"
summary = "Special unitary 3 by 3 matrices over F_(3²), modulo their scalar center; 3 is the fixed-field parameter."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "algebra-fields-galois/fixed-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

\(\operatorname{PSU}_{3}(3)\) is the following [[algebra-groups/finite-group|finite group]], with \(n=3\) and \(q=3\):
\[
 \operatorname{PSU}_{3}(3)=\operatorname{SU}_{3}(3)/\{\lambda I:\lambda^{3+1}=1,\ \lambda^{3}=1\},
 \quad \operatorname{SU}_{3}(3)=\{A\in M_{3}(\mathbb F_{3^2}): (A^{(3)})^{\mathsf T}A=I,\ \det A=1\}.
\]
Here \(A^{(3)}\) is entrywise \(3\)-th power. The [[algebra-fields-galois/finite-field|matrix field]] has \(3^2\) elements; its involution has [[algebra-fields-galois/fixed-field|fixed field]] of size \(3\). The scalar \(\lambda\) belongs to \(\mathbb F_{3^2}^\times\); multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSU}_{3}(3)|=6048. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]]. The exact order is 6,048.

## Parameter convention

The parameter \(q\) is the size of the fixed field, while matrices have entries in \(\mathbb F_{q^2}\). The Hermitian form is \(h(v,w)=\sum_i v_i^q w_i\). All nondegenerate Hermitian forms of this dimension over the finite field give isomorphic groups. Type \({}^2A_{n-1}\) has absolute rank \(n-1\); it is not a unitary group over the real or complex numbers.

## Small-group identification

This group is isomorphic to the index-two [[algebra-groups/commutator-subgroup|commutator subgroup]] \(G_2(2)'\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§5.2–5.3, pp. 59–63; PSU(2,q), PSU(3,2), and the PSU(4,2) identification.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
3. [ATLAS of Finite Group Representations: U3(3) and G2(2) derived group](https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/U33/), Heading and Standard generators: U3(3) = G2(2)′ has order 6048; U3(3):2 = G2(2).
