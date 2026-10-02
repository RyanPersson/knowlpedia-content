+++
id = "catalog/relationships/triality-and-central-quotients"
title = "Triality and central quotients of Spin(8)"
kind = "theorem"
summary = "The full triality symmetry preserves Spin(8) but not a chosen SO(8) quotient."
aliases = ["Triality and central quotients of Spin(8)"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["lie-groups/spin8-triality", "algebra-groups/outer-automorphism-group"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For the compact real groups, [[lie-groups/spin8-triality|triality]] gives
\[
\operatorname{Out}(\operatorname{Spin}(8))\cong S_3,
\qquad \operatorname{Out}(SO(8))\cong C_2.
\]
The center of \(\operatorname{Spin}(8)\) is \(C_2\times C_2\). Its three order-two subgroups are the distinct kernels of \(8_v,8_+,8_-\); the triality \(S_3\) permutes them. Only the subgroup fixing the vector kernel descends to automorphisms of the fixed quotient \(SO(8)\).

## Descent criterion

An automorphism \(\phi:G\to G\) induces an automorphism of \(G/K\) precisely when \(\phi(K)=K\). The stabilizer of one item in a three-element permutation action is \(C_2\). Thus an order-three triality automorphism does not descend to this quotient.

## Lie algebra level

The compact real Lie algebra \(\mathfrak{so}(8)\) retains [[algebra-groups/outer-automorphism-group|outer automorphism group]] \(S_3\). Differentiation forgets the central kernel of a covering, so a Lie-algebra symmetry need not integrate to an automorphism of every global group with that Lie algebra.

## References

1. Laura P. Schaposnik and Sebastian Schulz, “Triality for Homogeneous Polynomials,” §2.2, Proposition 2.1 and Remark 2.2, p. 5. [Paper](https://sigma-journal.com/2021/079/sigma21-079.pdf).
