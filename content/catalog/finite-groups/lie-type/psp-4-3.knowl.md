+++
id = "catalog/finite-groups/lie-type/psp-4-3"
title = "PSp(4,3)"
kind = "definition"
summary = "Symplectic matrices of size 4 over F_3, modulo the scalar center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "linear-algebra/bilinear-form"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(n=2\) and \(q=3\), \(\operatorname{PSp}_{4}(3)\) is the [[algebra-groups/finite-group|finite group]]
\[
 \operatorname{PSp}_{4}(3)=\operatorname{Sp}_{4}(3)/\{\lambda I:\lambda\in\mathbb F_{3}^\times,\lambda^2=1\},
 \quad \operatorname{Sp}_{4}(3)=\{A\in\operatorname{GL}_{4}(\mathbb F_{3}):A^{\mathsf T}JA=J\},
\]
where \(\mathbb F_{3}\) is the [[algebra-fields-galois/finite-field|field with \(3\) elements]]. The matrix \(J=\begin{pmatrix}0&I_{2}\\-I_{2}&0\end{pmatrix}\) gives the [[linear-algebra/bilinear-form|bilinear form]] \(B(v,w)=v^{\mathsf T}Jw\), which is alternating, meaning \(B(v,v)=0\) for every \(v\), and nondegenerate. Multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSp}_{4}(3)|=25920. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]]. The exact order is 25,920.

## Parameter convention

Type \(C_n\) has rank \(n\) and matrix dimension \(2n\). The center has size \(\gcd(2,q-1)\), so the projective quotient does nothing when \(q\) is even. Alternating means \(B(v,v)=0\), also in characteristic two.


## Small-group identification

There is an exceptional isomorphism \(\operatorname{PSp}_4(3)\cong\operatorname{PSU}_4(2)\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§4.2–4.3, pp. 49–54; the Sp(4,2) action on six quadratic forms, p. 51.
2. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§5.2–5.3, pp. 59–63; PSU(2,q), PSU(3,2), and the PSU(4,2) identification.
