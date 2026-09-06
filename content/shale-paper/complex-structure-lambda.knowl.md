+++
id = "shale-paper/complex-structure-lambda"
title = "Complex Structure Λ on K"
kind = "knowl"
summary = "A bounded real-linear operator Λ with Λ² = −I; when orthogonal, it equips a real Hilbert space with a compatible complex Hilbert structure."
aliases = ["complex-structure-lambda", "Complex Structure Λ on K"]
domains = ["shale-paper"]
prerequisites = ["linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "shale-paper/complex-structure-lambda.md"
+++

A **complex structure** on a real Hilbert space \(K\) is a bounded real-linear operator \(\Lambda:K\to K\) satisfying \(\Lambda^2=-I\). It defines complex scalar multiplication by
\[
(a+ib)z=az+b\Lambda z.
\]
When \(\Lambda\) is orthogonal, this complex structure is compatible with the real Hilbert-space inner product.

## Remarks

In the paper, \(\Lambda z=iz\) on \(K=H\) viewed as a real Hilbert space. It relates symplectic and adjoint operations: a regular \(T\) is symplectic if and only if \(\Lambda T\Lambda^{-1}=T^{*-1}\).

- The compatible unitary group is \(U(H)=O(K)\cap Sp(K)\).

## Examples

- On \(\mathbb R^{2n}\), \(\Lambda(p,q)=(-q,p)\).
