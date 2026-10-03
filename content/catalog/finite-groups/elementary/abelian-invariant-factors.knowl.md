+++
id = "catalog/finite-groups/elementary/abelian-invariant-factors"
title = "Finite abelian group with specified invariant factors"
kind = "definition"
summary = "A product of cyclic groups with specified invariant factors."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/direct-product-groups"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(r\geq0\), and for \(r>0\) let \(2\leq d_1\mid d_2\mid\cdots\mid d_r\) be integers. The **finite abelian group with these invariant factors** is the [[algebra-groups/direct-product-groups|direct product]]
\[
C_{d_1}\times\cdots\times C_{d_r},
\]
where each factor is the additive group of residue classes modulo \(d_i\). The empty product for \(r=0\) is the trivial group.

## Classification and order

Its order is \(\prod_{i=1}^r d_i\), with empty product \(1\). The [[algebra-groups/classification-finite-abelian-groups|classification of finite abelian groups]] says that every finite [[algebra-groups/abelian-group|abelian group]] occurs up to isomorphism, with a unique such list of invariant factors.

## Simplicity

For \(r=0\) the group is trivial. For \(r\geq2\), a coordinate factor is proper nontrivial normal. For \(r=1\), the cyclic group \(C_{d_1}\) is simple exactly when \(d_1\) is prime.

## References

- [J. S. Milne, Group Theory, v4.01](https://www.jmilne.org/math/CourseNotes/GT.pdf), Theorem 1.57, p. 26: invariant-factor classification of finite abelian groups.
