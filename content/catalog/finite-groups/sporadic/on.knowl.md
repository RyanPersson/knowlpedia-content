+++
id = "catalog/finite-groups/sporadic/on"
title = "O'Nan group"
kind = "definition"
summary = "The O'Nan sporadic simple group, realized by fixed 154-dimensional matrices over the field with three elements."
aliases = ["ON", "O'N", "O'Nan sporadic group"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **O'Nan group** \(\mathrm{O'N}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(154\times154\) [[linear-algebra/matrix|matrices]] \(A,B\) in dataset `ONG1-f3r154B0`:
\[
\mathrm{O'N}=\langle A,B\rangle\leq\mathrm{GL}_{154}(\mathbb F_3).
\]
The files `ONG1-f3r154B0.m1` and `ONG1-f3r154B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_3=\mathbb Z/3\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with three elements]], \(\mathrm{GL}_{154}(\mathbb F_3)\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This group is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{O'N}|=460815505920=2^9\cdot3^4\cdot5\cdot7^3\cdot11\cdot19\cdot31.
\]
It belongs to the pariah display block of sporadic groups. The selected matrices represent the simple group itself; the triple [[algebra-groups/central-extension|central extension]] denoted \(3.\mathrm{O'N}\) is a different group.

## A sporadic subgroup

There is a maximal subgroup isomorphic to the [[catalog/finite-groups/sporadic/j1|first Janko group]]:
\[
J_1\hookrightarrow\mathrm{O'N},\qquad [\mathrm{O'N}:J_1]=2624832.
\]
This is an existence statement for an embedding, not a classification of all homomorphisms between the two groups.

## Using the concrete model

The realization acts faithfully on \(\mathbb F_3^{154}\). Its matrix degree \(154\) is distinct from the order of the group. The defining data are the specified matrices; conditions on the orders of two unspecified generators do not replace those data.

## References

1. [ATLAS, O'Nan group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/ON/), order heading, “Representations of O'N,” and “Maximal subgroups of O'N,” row J1.
2. [ATLAS, representation ONG1-f3r154B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/ONG1-f3r154B0), “About this representation” and “Download”; exact MeatAxe text matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/ON/mtx/ONG1-f3r154B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/ON/mtx/ONG1-f3r154B0.m2).
3. [ATLAS, sporadic groups](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/), “Pariahs.”
