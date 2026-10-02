+++
id = "catalog/finite-groups/sporadic/hn"
title = "Harada–Norton group"
kind = "definition"
summary = "The Harada–Norton group, defined by a fixed pair of 133-dimensional matrices over F5."
aliases = ["HN"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Harada–Norton group** \(\mathrm{HN}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(133\times133\) [[linear-algebra/matrix|matrices]] \(A,B\) in ATLAS dataset `HNG1-f5r133B0`:
\[
\mathrm{HN}=\langle A,B\rangle\leq\mathrm{GL}_{133}(\mathbb F_{5}).
\]
The files `HNG1-f5r133B0.m1` and `HNG1-f5r133B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_{5}=\mathbb Z/5\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with 5 elements]], \(\mathrm{GL}_{133}(\mathbb F_{5})\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{HN}|=273030912000000=2^{14}\cdot3^{6}\cdot5^{6}\cdot7\cdot11\cdot19.
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## The concrete matrix model

This gives a [[algebra-groups/faithful-action|faithful action]] on \(\mathbb F_{5}^{133}\). The matrix degree \(133\) is distinct from the number of group elements. The two specified matrices determine the group; tests on the orders of unspecified generators would not constitute this definition.

## References

1. [ATLAS, Harada–Norton group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HN/), order heading and “Representations.”
2. [ATLAS, matrix model HNG1-f5r133B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/HNG1-f5r133B0), “About this representation” and “Download”; exact matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/HN/mtx/HNG1-f5r133B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/HN/mtx/HNG1-f5r133B0.m2).
