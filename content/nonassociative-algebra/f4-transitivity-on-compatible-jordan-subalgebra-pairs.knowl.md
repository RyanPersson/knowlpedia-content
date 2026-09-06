+++
id = "nonassociative-algebra/f4-transitivity-on-compatible-jordan-subalgebra-pairs"
title = "F4 transitivity on compatible Jordan-subalgebra pairs"
kind = "theorem"
summary = "Compact F_4 acts transitively on incident octonionic-spin-factor and complex-qutrit subalgebra pairs with complex-qubit intersection."
aliases = ["F4 transitivity on compatible H2(O) H3(C) pairs", "transitivity on Albert algebra incidence pairs"]
domains = ["nonassociative-algebra", "lie-groups"]
prerequisites = ["shared-foundations/ordered-pair", "nonassociative-algebra/jordan-subalgebra", "nonassociative-algebra/unique-octonionic-spin-factor-corner"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(J=H_3(\mathbb O)\). The compact group
\(F_4=\operatorname{Aut}(J)\) acts transitively on [[shared-foundations/ordered-pair|ordered pairs]] \((A,B)\) of
[[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]] satisfying
\[
A\cong H_2(\mathbb O),
\qquad B\cong H_3(\mathbb C),
\qquad A\cap B\cong H_2(\mathbb C).
\]
All three hypotheses, including the intersection condition, are part of the
statement.

Equivalently, \(F_4\) acts transitively on incident pairs \((X,B)\) with
\(X\subset B\subset J\), \(X\cong H_2(\mathbb C)\), and
\(B\cong H_3(\mathbb C)\): the passage between the two forms is
\[
X=A\cap B,
\qquad
A=J_1(1_X),
\]
where the second formula is the
[[nonassociative-algebra/unique-octonionic-spin-factor-corner|unique
octonionic spin-factor corner]] containing \(X\).

## Proof outline

Use [[nonassociative-algebra/f4-transitivity-on-complex-qutrit-subalgebras|
transitivity on complex-qutrit subalgebras]] to make the two \(B\)'s equal to
the standard \(H_3(\mathbb C)\). Within this subalgebra,
\(\mathrm{SU}(3)\) acts transitively on trace-two idempotents, equivalently on
complex two-planes in \(\mathbb C^3\), and hence on its
\(H_2(\mathbb C)\)-corners. This action extends through
\(\operatorname{Stab}_{F_4}(B)^0\). Uniqueness of the associated
\(H_2(\mathbb O)\)-corner then carries \(A\) to \(A'\).

## Consequence for stabilizer intersections

The transitivity says that a stabilizer computation for one standard pair
applies to every compatible pair. In particular it is the geometric step
behind the characterization
[[mathematical-physics/standard-model-gauge-group-as-f4-stabilizer-intersection|of
the Standard Model gauge group as an \(F_4\) stabilizer intersection]], where
the [[lie-groups/identity-component-of-a-lie-group|identity component]] of the qutrit stabilizer must be used.

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, Lemma 11 and Theorems 1–2. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Ichirô Yokota, *Exceptional Lie Groups*, 2009, Chapter 2. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431).
