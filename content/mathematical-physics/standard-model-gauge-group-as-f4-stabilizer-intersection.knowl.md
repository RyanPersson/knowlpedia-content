+++
id = "mathematical-physics/standard-model-gauge-group-as-f4-stabilizer-intersection"
title = "Standard Model gauge group as an F4 stabilizer intersection"
kind = "theorem"
summary = "The effective Standard Model group arises as the intersection of two stabilizers in compact F4 acting on the exceptional Jordan algebra."
aliases = ["F4 stabilizer characterization of the Standard Model group", "Standard Model group from the exceptional Jordan algebra"]
domains = ["mathematical-physics", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/exceptional-jordan-algebra", "lie-groups/compact-exceptional-lie-group-f4", "nonassociative-algebra/automorphism-group-of-a-jordan-algebra", "nonassociative-algebra/jordan-subalgebra", "lie-groups/identity-component-of-a-lie-group", "mathematical-physics/standard-model-gauge-group", "nonassociative-algebra/complex-qubit-jordan-algebra", "nonassociative-algebra/complex-qutrit-jordan-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(J=\mathfrak h_3(\mathbb O)\) be the [[nonassociative-algebra/exceptional-jordan-algebra|exceptional Jordan algebra]], and let the [[lie-groups/compact-exceptional-lie-group-f4|compact group \(F_4\)]] act through its [[nonassociative-algebra/automorphism-group-of-a-jordan-algebra|Jordan-algebra automorphisms]]. Suppose \(X\subset B\subset J\) are [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]] with
\[
X\cong\mathfrak h_2(\mathbb C),
\qquad
B\cong\mathfrak h_3(\mathbb C).
\]
Writing \(\operatorname{Stab}_{F_4}(-)\) for setwise stabilizers and \((-)^0\) for the [[lie-groups/identity-component-of-a-lie-group|identity component]],
\[
\operatorname{Stab}_{F_4}(X)\cap
\operatorname{Stab}_{F_4}(B)^0
\cong S(U(2)\times U(3)),
\]
the effective [[mathematical-physics/standard-model-gauge-group|Standard Model internal symmetry group]]. Here \(\mathfrak h_2(\mathbb C)\) and \(\mathfrak h_3(\mathbb C)\) are the [[nonassociative-algebra/complex-qubit-jordan-algebra|complex-qubit]] and [[nonassociative-algebra/complex-qutrit-jordan-algebra|complex-qutrit Jordan algebras]].

## Equivalent larger-subalgebra formulation

The copy \(X\cong\mathfrak h_2(\mathbb C)\) lies in a unique [[nonassociative-algebra/octonionic-spin-factor|octonionic spin factor]] \(A\cong\mathfrak h_2(\mathbb O)\). Moreover \(X=A\cap B\), and
\[
\operatorname{Stab}_{F_4}(A)\cap
\operatorname{Stab}_{F_4}(B)^0
\cong S(U(2)\times U(3)).
\]
The group on the right is the [[lie-groups/special-block-unitary-group|special block unitary group]].
For a standard pair,
\[
\operatorname{Stab}_{F_4}(A)\cong\operatorname{Spin}(9),
\qquad
\operatorname{Stab}_{F_4}(B)^0
\cong (SU(3)\times SU(3))/\mathbb Z_3.
\]
The proof uses the [[nonassociative-algebra/complex-qutrit-stabilizer-in-f4|complex-qutrit stabilizer calculation]] and transitivity of \(F_4\) on [[nonassociative-algebra/f4-transitivity-on-complex-qutrit-subalgebras|complex-qutrit subalgebras]] and [[nonassociative-algebra/f4-transitivity-on-compatible-jordan-subalgebra-pairs|compatible subalgebra pairs]].

## Why the identity component is essential

The full stabilizer \(\operatorname{Stab}_{F_4}(B)\) is disconnected. Its extra component contains symmetries whose restriction to \(B\cong\mathfrak h_3(\mathbb C)\) has the form \(X\mapsto UXU^{-1}\), where \(U\) is antiunitary on \(\mathbb C^3\). Therefore
\[
\operatorname{Stab}_{F_4}(X)\cap\operatorname{Stab}_{F_4}(B)
\]
is strictly larger than the Standard Model group. The superscript \(0\) is part of the theorem.

## Interpretation and scope

The two complex [[nonassociative-algebra/jordan-algebra|Jordan algebras]] are observable algebras of a [[quantum-foundations/qubit|qubit]] and a [[quantum-foundations/qutrit|qutrit]], motivating an “octonionic qutrit” interpretation of \(J\). The theorem is a precise group-theoretic characterization; by itself it does not construct the Standard Model Lagrangian, select its fermion representation, or prove that \(F_4\) is a physical gauge symmetry.

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: Theorems 1–2 and §§3–5.
2. Ivan Todorov and Michel Dubois-Violette, “Deducing the Symmetry of the Standard Model from the Automorphism and Structure Groups of the Exceptional Jordan Algebra,” *International Journal of Modern Physics A* 33 (2018), 1850118. [DOI record](https://doi.org/10.1142/S0217751X1850118X).
3. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778). Relevant: Chapter IV.
