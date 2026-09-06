+++
id = "algebra-hyperstructures/hyperfield-as-a-tract"
title = "Tract associated with a hyperfield"
kind = "construction"
summary = "The tract whose null formal sums are precisely the hypersums containing zero."
aliases = ["hyperfield tract"]
domains = ["algebra-hyperstructures", "matroid-theory"]
prerequisites = ["algebra-hyperstructures/hyperfield", "algebra-hyperstructures/tract"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a [[algebra-hyperstructures/hyperfield|hyperfield]]. Its
associated [[algebra-hyperstructures/tract|tract]] has multiplicative group
\(F^\times\) and null set
\[
N_F=
\left\{\sum_i a_i\in\mathbb N[F^\times]:
0\in\mathop{\boxplus}_i a_i\right\}.
\]
The unique hyper-additive inverse of \(1\) is the tract's distinguished
element \(\epsilon=-1\).

A weak hyperfield homomorphism preserves null hypersums, so restriction to
the nonzero multiplicative groups induces a tract morphism.

## Scope

This construction forgets the individual values of a non-null hyper-sum and
retains its null relations. Every hyperfield therefore determines a tract,
but an arbitrary tract need not carry a binary hyperaddition from which its
null set can be recovered.

## References
Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,”
*Advances in Mathematics* 343 (2019), 821–863.
[arXiv:1709.09707](https://arxiv.org/abs/1709.09707).
