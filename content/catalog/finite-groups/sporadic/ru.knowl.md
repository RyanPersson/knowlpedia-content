+++
id = "catalog/finite-groups/sporadic/ru"
title = "Rudvalis group"
kind = "definition"
summary = "The Rudvalis sporadic simple group, realized by fixed 28-dimensional matrices over the field with two elements."
aliases = ["Ru", "Rudvalis sporadic group"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/generated-subgroup", "linear-algebra/matrix", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Rudvalis group** \(\mathrm{Ru}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] by the fixed pair of \(28\times28\) [[linear-algebra/matrix|matrices]] \(A,B\) in dataset `RuG1-f2r28B0`:
\[
\mathrm{Ru}=\langle A,B\rangle\leq\mathrm{GL}_{28}(\mathbb F_2).
\]
The files `RuG1-f2r28B0.m1` and `RuG1-f2r28B0.m2` specify \(A\) and \(B\), respectively; their entries are part of this concrete definition. Here \(\mathbb F_2=\mathbb Z/2\mathbb Z\) is the [[algebra-fields-galois/finite-field|field with two elements]], \(\mathrm{GL}_{28}(\mathbb F_2)\) consists of invertible matrices, and the group operation is matrix multiplication over that field. The exact generator files are linked in References.

## Order and structure

This group is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Ru}|=145926144000=2^{14}\cdot3^3\cdot5^3\cdot7\cdot13\cdot29.
\]
It belongs to the pariah display block of sporadic groups. The selected matrices represent \(\mathrm{Ru}\) itself; the double [[algebra-groups/central-extension|central extension]] denoted \(2.\mathrm{Ru}\) is a different group.

## Using the concrete model

The realization acts faithfully on \(\mathbb F_2^{28}\). Its matrix degree \(28\) is distinct from the order of the group. In particular, changing the field of a representation requires separate data; the 28-dimensional representations of \(2.\mathrm{Ru}\) in odd characteristic do not define this same matrix group. Conditions on the orders of two unspecified generators do not replace the defining matrix files.

## References

1. [ATLAS, Rudvalis group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Ru/), order heading, “Representations of Ru,” and “Representations of 2.Ru.”
2. [ATLAS, representation RuG1-f2r28B0](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/RuG1-f2r28B0), “About this representation” and “Download”; exact MeatAxe text matrices [A](https://brauer.maths.qmul.ac.uk/Atlas/spor/Ru/mtx/RuG1-f2r28B0.m1) and [B](https://brauer.maths.qmul.ac.uk/Atlas/spor/Ru/mtx/RuG1-f2r28B0.m2).
3. [ATLAS, sporadic groups](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/), “Pariahs.”
