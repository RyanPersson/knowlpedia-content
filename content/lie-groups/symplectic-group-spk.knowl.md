+++
id = "lie-groups/symplectic-group-spk"
title = "Symplectic Group Sp(K)"
kind = "knowl"
summary = "Bounded invertible real-linear maps preserving the symplectic form B"
aliases = ["symplectic-group-spk", "Symplectic Group Sp(K)"]
domains = ["lie-groups"]
legacy_source_path = "shale-paper/symplectic-group-spk.md"
prerequisites = ["functional-analysis/symplectic-hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a [[functional-analysis/symplectic-hilbert-space|symplectic Hilbert space]] \((K,B)\), let \(\operatorname{GL}_{\mathbb R}(K)\) denote the group of bounded invertible real-[[linear-algebra/linear-operator|linear operators]] on \(K\). The **[[lie-groups/symplectic-group|symplectic group]]** is
\[
\operatorname{Sp}(K)
=\{T\in\operatorname{GL}_{\mathbb R}(K):B(Tx,Ty)=B(x,y)
\text{ for all }x,y\in K\}.
\]

## Remarks

Each \(T\in\operatorname{Sp}(K)\) preserves the Weyl relations and hence acts on Weyl operators by \(V(z)\mapsto V(Tz)\). Only the [[lie-groups/restricted-symplectic-group-rspk|restricted symplectic subgroup]] is unitarily implementable in the associated Fock representation.

## Examples

- \(Sp(\mathbb R^{2n})\) is the classical real symplectic group.
