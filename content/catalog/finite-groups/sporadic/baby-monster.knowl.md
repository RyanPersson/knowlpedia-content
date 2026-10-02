+++
id = "catalog/finite-groups/sporadic/baby-monster"
title = "Baby Monster group"
kind = "definition"
summary = "The Baby Monster group, defined by a fixed pair of 4370-dimensional matrices over F2."
aliases = ["B"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Baby Monster group** \(\mathbb B\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(4370\times4370\) [[linear-algebra/matrix|matrices]] \(A,B\) in ATLAS dataset `BG1-f2r4370B0`:
\[
\mathbb B=\langle A,B\rangle\leq\mathrm{GL}_{4370}(\mathbb F_{2}).
\]
The files `BG1-f2r4370B0.m1` and `BG1-f2r4370B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_{2}=\mathbb Z/2\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with 2 elements]], \(\mathrm{GL}_{4370}(\mathbb F_{2})\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
\begin{aligned}|\mathbb B|&=2^{41}\cdot3^{13}\cdot5^{6}\cdot7^{2}\cdot11\cdot13\cdot17\\
&\quad{}\cdot19\cdot23\cdot31\cdot47.\end{aligned}
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## The concrete matrix model

This gives a [[algebra-groups/faithful-action|faithful action]] on \(\mathbb F_{2}^{4370}\). The matrix degree \(4370\) is distinct from the number of group elements. The two specified matrices determine the group; tests on the orders of unspecified generators would not constitute this definition.

The [[catalog/finite-groups/sporadic/baby-monster-sporadic-subgroups|sporadic subgroups of the Baby Monster]] include copies of \(\mathrm{Fi}_{23}\) and \(\mathrm{Th}\).

## References

1. [ATLAS, Baby Monster group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/B/), order heading and “Representations.”
2. [ATLAS, matrix model BG1-f2r4370B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/BG1-f2r4370B0), “About this representation” and “Download”; exact matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/B/mtx/BG1-f2r4370B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/B/mtx/BG1-f2r4370B0.m2).
