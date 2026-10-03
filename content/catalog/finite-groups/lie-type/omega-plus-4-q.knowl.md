+++
id = "catalog/finite-groups/lie-type/omega-plus-4-q"
title = "PΩ+(4,q)"
kind = "definition"
summary = "Projective commutator subgroup of the isometry group of a plus-type quadratic form in dimension 4."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/finite-orthogonal-derived-group", "linear-algebra/linear-map", "algebra-groups/commutator-subgroup", "linear-algebra/quadratic-form"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(n=2\) and prime powers \(q\geq 3\), \(\operatorname{P}\Omega_{4}^{+}(q)\) is the [[catalog/finite-groups/lie-type/finite-orthogonal-derived-group|projective orthogonal derived group]] of \(Q(x,y)=\sum_{i=1}^{2}x_i y_i\) on \(\mathbb F_q^{4}\):
\[
 \Omega=\operatorname O(Q)',\qquad \operatorname{P}\Omega_{4}^{+}(q)=\Omega/(\Omega\cap\{\lambda I:\lambda\in\mathbb F_q^\times\}).
\]
Here \(\operatorname O(Q)\) is the group of invertible [[linear-algebra/linear-map|linear maps]] preserving \(Q\), and its prime denotes the [[algebra-groups/commutator-subgroup|commutator subgroup]]. Multiplication is multiplication of scalar cosets. The displayed [[linear-algebra/quadratic-form|quadratic form]], not merely its polar form, is part of the definition.

## Order and simplicity

Its order is
\[ |\operatorname{P}\Omega_{4}^{+}(q)|=\frac{q^{2(2-1)}(q^{2}-1)\prod_{i=1}^{2-1}(q^{2i}-1)}{\gcd(4,q^{2}-1)}. \]

It is never simple: it is a direct product of two nontrivial copies of PSL(2,q).

## Rank and form convention

The ambient quadratic-space dimension is \(4\), and the absolute rank is \(2\). The plus sign has Witt index \(n\); the minus sign has Witt index \(n-1\), because the norm plane is anisotropic. The order denominator is \(\gcd(4,q^n-1)\) in plus type and \(\gcd(4,q^n+1)\) in minus type.

## Low-rank identification

\(\operatorname{P}\Omega_4^+(q)\cong\operatorname{PSL}_2(q)\times\operatorname{PSL}_2(q)\) for \(q\geq3\). This is the reducible root-system case \(D_2=A_1\sqcup A_1\). The lower parameters are excluded here because the full orthogonal commutator subgroup can differ from the usual small Chevalley-group convention.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §6, pp. 64–74, especially Theorems 6.3 and 6.6; §7 introduction, p. 75.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
