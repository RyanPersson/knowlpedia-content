+++
id = "catalog/finite-groups/lie-type/psl-2-5"
title = "PSL(2,5)"
kind = "definition"
summary = "Determinant-one 2 by 2 matrices over F_5, modulo scalar matrices of determinant one."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-groups/projective-special-linear-group", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

\(\operatorname{PSL}_{2}(5)\) is the following [[algebra-groups/finite-group|finite group]], with \(n=2\) and \(q=5\):
\[ \operatorname{PSL}_{2}(5)=\operatorname{SL}_{2}(\mathbb F_{5})/\{\lambda I:\lambda\in\mathbb F_{5}^\times,\ \lambda^{2}=1\}, \qquad
 \operatorname{SL}_{2}(\mathbb F_{5})=\{A\in M_{2}(\mathbb F_{5}):\det A=1\}. \]
This is the [[algebra-groups/projective-special-linear-group|projective special linear group]]; multiplication is multiplication of scalar cosets. Here \(\mathbb F_{5}\) is the [[algebra-fields-galois/finite-field|field with \(5\) elements]].

## Order and simplicity

Its order is
\[ |\operatorname{PSL}_{2}(5)|=60. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]]. The exact order is 60.

## Parameter convention

Type \(A_{n-1}\) uses matrix size \(n\), so the Lie rank is \(n-1\). The simple family omits \(\operatorname{PSL}_2(2)\cong S_3\) and \(\operatorname{PSL}_2(3)\cong A_4\).

## Small-group identification

The exceptional isomorphism is \(\operatorname{PSL}_2(5)\cong A_5\cong\operatorname{PSL}_2(4)\). Its projective-line action has six points, so the five-letter identification is not that natural action.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§2.4–2.5, pp. 19–21; Theorem 2.11.
