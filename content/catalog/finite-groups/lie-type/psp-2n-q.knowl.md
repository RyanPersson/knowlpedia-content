+++
id = "catalog/finite-groups/lie-type/psp-2n-q"
title = "PSp(2n,q)"
kind = "definition"
summary = "Symplectic matrices of size 2n over F_q, modulo the scalar center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "linear-algebra/bilinear-form"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For integers \(n\geq2\) and prime powers \(q\), excluding \((n,q)=(2,2)\), \(\operatorname{PSp}_{2n}(q)\) is the [[algebra-groups/finite-group|finite group]]
\[
 \operatorname{PSp}_{2n}(q)=\operatorname{Sp}_{2n}(q)/\{\lambda I:\lambda\in\mathbb F_{q}^\times,\lambda^2=1\},
 \quad \operatorname{Sp}_{2n}(q)=\{A\in\operatorname{GL}_{2n}(\mathbb F_{q}):A^{\mathsf T}JA=J\},
\]
where \(\mathbb F_{q}\) is the [[algebra-fields-galois/finite-field|field with \(q\) elements]]. The matrix \(J=\begin{pmatrix}0&I_{n}\\-I_{n}&0\end{pmatrix}\) gives the [[linear-algebra/bilinear-form|bilinear form]] \(B(v,w)=v^{\mathsf T}Jw\), which is alternating, meaning \(B(v,v)=0\) for every \(v\), and nondegenerate. Multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSp}_{2n}(q)|=\frac{q^{n^2}\prod_{i=1}^{n}(q^{2i}-1)}{\gcd(2,q-1)}. \]

It is simple for every admitted parameter: n ≥ 2 and (n,q) ≠ (2,2).

## Parameter convention

Type \(C_n\) has rank \(n\) and matrix dimension \(2n\). The center has size \(\gcd(2,q-1)\), so the projective quotient does nothing when \(q\) is even. Alternating means \(B(v,v)=0\), also in characteristic two.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§4.2–4.3, pp. 49–54; the Sp(4,2) action on six quadratic forms, p. 51.
