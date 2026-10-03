+++
id = "catalog/finite-groups/sporadic/th"
title = "Thompson sporadic group"
kind = "definition"
summary = "The Thompson sporadic group, defined by a fixed pair of 248-dimensional matrices over F2."
aliases = ["Th"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Thompson sporadic group** \(\mathrm{Th}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(248\times248\) [[linear-algebra/matrix|matrices]] \(A,B\) in ATLAS dataset `ThG1-f2r248B0`:
\[
\mathrm{Th}=\langle A,B\rangle\leq\mathrm{GL}_{248}(\mathbb F_{2}).
\]
The files `ThG1-f2r248B0.m1` and `ThG1-f2r248B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_{2}=\mathbb Z/2\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with 2 elements]], \(\mathrm{GL}_{248}(\mathbb F_{2})\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Th}|=90745943887872000=2^{15}\cdot3^{10}\cdot5^{3}\cdot7^{2}\cdot13\cdot19\cdot31.
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## The concrete matrix model

This gives a [[algebra-groups/faithful-action|faithful action]] on \(\mathbb F_{2}^{248}\). The matrix degree \(248\) is distinct from the number of group elements. The two specified matrices determine the group; tests on the orders of unspecified generators would not constitute this definition.

The notation \(\mathrm{Th}\) denotes the finite sporadic group; Thompson’s infinite groups \(F,T,V\) are different objects.

The [[catalog/finite-groups/sporadic/baby-monster-sporadic-subgroups|sporadic subgroups of the Baby Monster]] include copies of \(\mathrm{Fi}_{23}\) and \(\mathrm{Th}\).

## References

1. [ATLAS, Thompson sporadic group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Th/), order heading and “Representations.”
2. [ATLAS, matrix model ThG1-f2r248B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/ThG1-f2r248B0), “About this representation” and “Download”; exact matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/Th/mtx/ThG1-f2r248B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/Th/mtx/ThG1-f2r248B0.m2).
