+++
id = "catalog/finite-groups/lie-type/psl-n-q"
title = "PSL(n,q)"
kind = "definition"
summary = "Determinant-one n by n matrices over F_q, modulo scalar matrices of determinant one."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-groups/projective-special-linear-group", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For integers \(n\geq2\) and prime powers \(q\), excluding \((n,q)=(2,2),(2,3)\), \(\operatorname{PSL}_{n}(q)\) is the [[algebra-groups/finite-group|finite group]] defined by
\[ \operatorname{PSL}_{n}(q)=\operatorname{SL}_{n}(\mathbb F_{q})/\{\lambda I:\lambda\in\mathbb F_{q}^\times,\ \lambda^{n}=1\}, \qquad
 \operatorname{SL}_{n}(\mathbb F_{q})=\{A\in M_{n}(\mathbb F_{q}):\det A=1\}. \]
This is the [[algebra-groups/projective-special-linear-group|projective special linear group]]; multiplication is multiplication of scalar cosets. Here \(\mathbb F_{q}\) is the [[algebra-fields-galois/finite-field|field with \(q\) elements]].

## Order and simplicity

Its order is
\[ |\operatorname{PSL}_{n}(q)|=\frac{q^{n(n-1)/2}\prod_{i=2}^{n}(q^i-1)}{\gcd(n,q-1)}. \]

It is simple for every admitted parameter: n ≥ 2, with (n,q) different from (2,2) and (2,3).

## Parameter convention

Type \(A_{n-1}\) uses matrix size \(n\), so the Lie rank is \(n-1\). The simple family omits \(\operatorname{PSL}_2(2)\cong S_3\) and \(\operatorname{PSL}_2(3)\cong A_4\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§2.4–2.5, pp. 19–21; Theorem 2.11.
