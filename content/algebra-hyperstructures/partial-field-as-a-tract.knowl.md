+++
id = "algebra-hyperstructures/partial-field-as-a-tract"
title = "Tract associated with a partial field"
kind = "construction"
summary = "The tract whose null sums are the formal sums vanishing in the ambient ring of a partial field."
aliases = ["partial field tract"]
domains = ["algebra-hyperstructures", "matroid-theory"]
prerequisites = ["algebra-hyperstructures/partial-field", "algebra-hyperstructures/tract"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P=(G,R)\) be a
[[algebra-hyperstructures/partial-field|partial field]]. Its associated
[[algebra-hyperstructures/tract|tract]] has multiplicative group \(G\) and
null set
\[
N_P=
\left\{\sum_i g_i\in\mathbb N[G]:
\sum_i g_i=0\text{ in }R\right\}.
\]

The distinguished element \(\epsilon\) of the tract is \(-1\in G\).
A morphism of partial fields carries ring-null formal sums to ring-null
formal sums and therefore induces a morphism of the associated tracts.

## What the construction retains

The tract remembers every finite additive relation among elements of \(G\),
including relations whose intermediate binary sums leave \(G\cup\{0\}\).
It does not retain the ambient ring \(R\) as an object; different ambient
presentations can therefore determine the same tract.

## References
Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,”
*Advances in Mathematics* 343 (2019), 821–863.
[arXiv:1709.09707](https://arxiv.org/abs/1709.09707).
