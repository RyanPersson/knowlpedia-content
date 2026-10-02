+++
id = "catalog/finite-groups/lie-type/omega-3-q"
title = "PΩ(3,q)"
kind = "definition"
summary = "Projective commutator subgroup of the isometry group of a odd-type quadratic form in dimension 3."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/finite-orthogonal-derived-group", "linear-algebra/linear-map", "algebra-groups/commutator-subgroup", "linear-algebra/quadratic-form"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(n=1\) and prime powers \(q\geq 4\), \(\operatorname{P}\Omega_{3}(q)\) is the [[catalog/finite-groups/lie-type/finite-orthogonal-derived-group|projective orthogonal derived group]] of \(Q(x,y,z)=\sum_{i=1}^{1}x_i y_i+z^2\) on \(\mathbb F_q^{3}\):
\[
 \Omega=\operatorname O(Q)',\qquad \operatorname{P}\Omega_{3}(q)=\Omega/(\Omega\cap\{\lambda I:\lambda\in\mathbb F_q^\times\}).
\]
Here \(\operatorname O(Q)\) is the group of invertible [[linear-algebra/linear-map|linear maps]] preserving \(Q\), and its prime denotes the [[algebra-groups/commutator-subgroup|commutator subgroup]]. Multiplication is multiplication of scalar cosets. The displayed [[linear-algebra/quadratic-form|quadratic form]], not merely its polar form, is part of the definition.

## Order and simplicity

Its order is
\[ |\operatorname{P}\Omega_{3}(q)|=\frac{q^{1^2}\prod_{i=1}^{1}(q^{2i}-1)}{\gcd(2,q-1)}. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted parameter.

## Rank and form convention

The ambient quadratic-space dimension is \(3\), and the absolute rank is \(1\). The Witt index is \(n\). For even \(q\), the polar form has a one-dimensional radical and passage to its quotient gives \(\operatorname{P}\Omega_{2n+1}(q)\cong\operatorname{PSp}_{2n}(q)\) in this stated range. For odd \(q\) and \(n\geq3\), the two groups have equal orders but are not isomorphic.

## Low-rank identification

\(\operatorname{P}\Omega_3(q)\cong\operatorname{PSL}_2(q)\) for \(q\geq4\). The lower parameters are excluded here because the full orthogonal commutator subgroup can differ from the usual small Chevalley-group convention.

## References

1. [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §6, pp. 64–74, especially Theorems 6.3 and 6.6; §7 introduction, p. 75.
2. [Robert A. Wilson, Classical groups (lecture notes)](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes3.pdf), §3.1.7, pp. 5–6; §§3.2–3.4, pp. 7–17.
