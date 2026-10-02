+++
id = "catalog/finite-groups/sporadic/fi24-prime"
title = "Fischer group Fi24′"
kind = "definition"
summary = "The Fischer group Fi24′, defined by a fixed pair of 781-dimensional matrices over F3."
aliases = ["Fi_24'"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Fischer group Fi24′** \(\mathrm{Fi}_{24}'\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(781\times781\) [[linear-algebra/matrix|matrices]] \(A,B\) in ATLAS dataset `F24G1-f3r781B0`:
\[
\mathrm{Fi}_{24}'=\langle A,B\rangle\leq\mathrm{GL}_{781}(\mathbb F_{3}).
\]
The files `F24G1-f3r781B0.m1` and `F24G1-f3r781B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_{3}=\mathbb Z/3\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with 3 elements]], \(\mathrm{GL}_{781}(\mathbb F_{3})\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
\begin{aligned}|\mathrm{Fi}_{24}'|&=2^{21}\cdot3^{16}\cdot5^{2}\cdot7^{3}\cdot11\cdot13\cdot17\\
&\quad{}\cdot23\cdot29.\end{aligned}
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## The concrete matrix model

This gives a [[algebra-groups/faithful-action|faithful action]] on \(\mathbb F_{3}^{781}\). The matrix degree \(781\) is distinct from the number of group elements. The two specified matrices determine the group; tests on the orders of unspecified generators would not constitute this definition.

The prime in \(\mathrm{Fi}_{24}'\) is essential: this is the simple [[algebra-groups/commutator-subgroup|derived subgroup]] of the larger Fischer group \(\mathrm{Fi}_{24}=\mathrm{Fi}_{24}':2\), which has twice its order. The central cover \(3.\mathrm{Fi}_{24}'\) is also a different group.

## References

1. [ATLAS, Fischer group Fi24′](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/F24/), order heading and “Representations.”
2. [ATLAS, matrix model F24G1-f3r781B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/F24G1-f3r781B0), “About this representation” and “Download”; exact matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/F24/mtx/F24G1-f3r781B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/F24/mtx/F24G1-f3r781B0.m2).
