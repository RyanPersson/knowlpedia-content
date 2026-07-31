+++
id = "algebra-hyperstructures/partial-hyperfield-as-a-tract"
title = "Tract associated with a partial hyperfield"
kind = "construction"
summary = "The tract obtained from the ambient null hypersums of a partial hyperfield."
aliases = ["partial hyperfield tract"]
domains = ["algebra-hyperstructures", "matroid-theory"]
section_mode = "progressive"
+++

Let \(P=(G,R)\) be a
[[algebra-hyperstructures/partial-hyperfield|partial hyperfield]], with
\(G\) a subgroup of the units of the ambient integral hyperring \(R\). Its
associated [[algebra-hyperstructures/tract|tract]] has multiplicative group
\(G\) and null set
\[
N_P=
\left\{\sum_i g_i\in\mathbb N[G]:
0\in\mathop{\boxplus}_i g_i\text{ in }R\right\}.
\]

The construction uses the ambient hypersum in \(R\), not only binary partial
sums that remain visible in \(G\cup\{0\}\). It therefore records null
relations even when every attempted parenthesization passes through elements
outside the selected coefficient set.

For an ordinary ambient ring this specializes to the
[[algebra-hyperstructures/partial-field-as-a-tract|partial-field
construction]]. Taking \(G=R^\times\) with \(R\) a hyperfield specializes to
the [[algebra-hyperstructures/hyperfield-as-a-tract|hyperfield
construction]].

## Reference

Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,”
*Advances in Mathematics* 343 (2019), 821–863.
[arXiv:1709.09707](https://arxiv.org/abs/1709.09707).
