+++
id = "catalog/finite-groups/lie-type/psp-2-q"
title = "PSp(2,q)"
kind = "definition"
summary = "Symplectic matrices of size 2 over F_q, modulo the scalar center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/finite-group", "algebra-fields-galois/finite-field", "linear-algebra/bilinear-form"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(n=1\) and prime powers \(q\), \(\operatorname{PSp}_{2}(q)\) is the [[algebra-groups/finite-group|finite group]]
\[
 \operatorname{PSp}_{2}(q)=\operatorname{Sp}_{2}(q)/\{\lambda I:\lambda\in\mathbb F_{q}^\times,\lambda^2=1\},
 \quad \operatorname{Sp}_{2}(q)=\{A\in\operatorname{GL}_{2}(\mathbb F_{q}):A^{\mathsf T}JA=J\},
\]
where \(\mathbb F_{q}\) is the [[algebra-fields-galois/finite-field|field with \(q\) elements]]. The matrix \(J=\begin{pmatrix}0&I_{1}\\-I_{1}&0\end{pmatrix}\) gives the [[linear-algebra/bilinear-form|bilinear form]] \(B(v,w)=v^{\mathsf T}Jw\), which is alternating, meaning \(B(v,v)=0\) for every \(v\), and nondegenerate. Multiplication is multiplication of scalar cosets.

## Order and simplicity

Its order is
\[ |\operatorname{PSp}_{2}(q)|=\frac{q(q^{2}-1)}{\gcd(2,q-1)}. \]

It is simple exactly when q ≥ 4.

## Parameter convention

Type \(C_n\) has rank \(n\) and matrix dimension \(2n\). The center has size \(\gcd(2,q-1)\), so the projective quotient does nothing when \(q\) is even. Alternating means \(B(v,v)=0\), also in characteristic two.

In dimension two, preservation of \(J\) is equivalent to determinant one, so \(\operatorname{PSp}_2(q)\cong\operatorname{PSL}_2(q)\). See [[catalog/finite-groups/lie-type/psl-2-q|the dimension-two projective linear group]].

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§4.2–4.3, pp. 49–54; the Sp(4,2) action on six quadratic forms, p. 51.
