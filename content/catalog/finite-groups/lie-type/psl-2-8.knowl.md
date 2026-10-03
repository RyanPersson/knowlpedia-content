+++
id = "catalog/finite-groups/lie-type/psl-2-8"
title = "PSL(2,8)"
kind = "definition"
summary = "Determinant-one 2 by 2 matrices over F_8, modulo scalar matrices of determinant one."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-groups/projective-special-linear-group", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

\(\operatorname{PSL}_{2}(8)\) is the following [[algebra-groups/finite-group|finite group]], with \(n=2\) and \(q=8\):
\[ \operatorname{PSL}_{2}(8)=\operatorname{SL}_{2}(\mathbb F_{8})/\{\lambda I:\lambda\in\mathbb F_{8}^\times,\ \lambda^{2}=1\}, \qquad
 \operatorname{SL}_{2}(\mathbb F_{8})=\{A\in M_{2}(\mathbb F_{8}):\det A=1\}. \]
This is the [[algebra-groups/projective-special-linear-group|projective special linear group]]; multiplication is multiplication of scalar cosets. Here \(\mathbb F_{8}\) is the [[algebra-fields-galois/finite-field|field with \(8\) elements]].

## Order and simplicity

Its order is
\[ |\operatorname{PSL}_{2}(8)|=504. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]]. The exact order is 504.

## Parameter convention

Type \(A_{n-1}\) uses matrix size \(n\), so the Lie rank is \(n-1\). The simple family omits \(\operatorname{PSL}_2(2)\cong S_3\) and \(\operatorname{PSL}_2(3)\cong A_4\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§2.4–2.5, pp. 19–21; Theorem 2.11.
