+++
id = "catalog/finite-groups/lie-type/psl-2-q2"
title = "PSL(2,q²)"
kind = "definition"
summary = "Determinant-one two by two matrices over F_(q²), modulo scalar matrices."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/projective-special-linear-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a prime power \(q\), \(\operatorname{PSL}_2(q^2)\) is the [[algebra-groups/projective-special-linear-group|projective special linear group]]
\[
 \operatorname{PSL}_2(q^2)=\{A\in M_2(\mathbb F_{q^2}):\det A=1\}/\{\lambda I:\lambda\in\mathbb F_{q^2}^\times,\lambda^2=1\}.
\]
Multiplication is multiplication of scalar cosets. Here the matrix field has size \(q^2\), not \(q\).

## Order and simplicity

Its order is
\[ |\operatorname{PSL}_2(q^2)|=\frac{q^2(q^4-1)}{\gcd(2,q^2-1)}. \]

It is simple for every admitted prime power q, since q² ≥ 4.

## Orthogonal identification

The low-rank identification is \(\operatorname{P}\Omega_4^-(q)\cong\operatorname{PSL}_2(q^2)\). For example \(q=2\) gives \(\operatorname{PSL}_2(4)\cong A_5\).

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §§2.4–2.5, pp. 19–21; Theorem 2.11.
2. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §6, pp. 64–74, especially Theorems 6.3 and 6.6; §7 introduction, p. 75.
