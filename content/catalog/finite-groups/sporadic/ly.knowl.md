+++
id = "catalog/finite-groups/sporadic/ly"
title = "Lyons group"
kind = "definition"
summary = "The Lyons sporadic simple group, realized by fixed 111-dimensional matrices over the field with five elements."
aliases = ["Ly", "Lyons sporadic group"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Lyons group** \(\mathrm{Ly}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(111\times111\) [[linear-algebra/matrix|matrices]] \(A,B\) in dataset `LyG1-f5r111B0`:
\[
\mathrm{Ly}=\langle A,B\rangle\leq\mathrm{GL}_{111}(\mathbb F_5).
\]
The files `LyG1-f5r111B0.m1` and `LyG1-f5r111B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_5=\mathbb Z/5\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with five elements]], \(\mathrm{GL}_{111}(\mathbb F_5)\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This group is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Ly}|=51765179004000000=2^8\cdot3^7\cdot5^6\cdot7\cdot11\cdot31\cdot37\cdot67.
\]
It belongs to the pariah display block of sporadic groups.

## Using the concrete model

The realization acts faithfully on \(\mathbb F_5^{111}\). Its matrix degree \(111\) is distinct from the order of the group. The defining data are the specified matrices; conditions on the orders of two unspecified generators do not replace those data. The notation \(\mathrm{Ly}\) names one [[algebra-groups/finite-group|finite group]] and has no rank or field parameter.

## References

1. [ATLAS, Lyons group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Ly/), order heading and “Representations of Ly.”
2. [ATLAS, representation LyG1-f5r111B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/LyG1-f5r111B0), “About this representation” and “Download”; exact MeatAxe text matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/Ly/mtx/LyG1-f5r111B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/Ly/mtx/LyG1-f5r111B0.m2).
3. [ATLAS, sporadic groups](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/), “Pariahs.”
