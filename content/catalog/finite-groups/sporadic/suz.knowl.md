+++
id = "catalog/finite-groups/sporadic/suz"
title = "Sporadic Suzuki group Suz"
kind = "knowl"
summary = "The sporadic simple Suzuki group in its faithful action on 1782 points."
aliases = ["sporadic Suzuki group", "Suz", "Suzuki sporadic group"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/symmetric-group", "algebra-groups/generated-subgroup"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **sporadic Suzuki group** \(\mathrm{Suz}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] in the [[algebra-groups/symmetric-group|symmetric group]] by the permutations \(a,b\) of \(\{1,\ldots,1782\}\) specified by `SuzG1-p1782B0.g1` and `SuzG1-p1782B0.g2`, respectively:
\[
\mathrm{Suz}=\langle a,b\rangle\le S_{1782}.
\]
The exact files are linked in References. They specify disjoint-cycle permutations, fixing all omitted points, and give a faithful model under composition. The symbol \(\mathrm{Suz}\) denotes this single group.

## Order and simplicity

This is a nonabelian [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Suz}|=448\,345\,497\,600
=2^{13}\cdot3^7\cdot5^2\cdot7\cdot11\cdot13.
\]

## The 1782-point action

The action is transitive with point-stabilizer orbits of sizes \(1,416,1365\), hence has rank three. Its point stabilizer is \(G_2(4)\).

There is also a maximal subgroup \(J_2:2\), of index \(370\,656\), containing the [[catalog/finite-groups/sporadic/j2|Hall–Janko group]] with index two.

## Naming convention

The finite simple groups of Lie type \({}^2B_2(q)\), for \(q=2^{2m+1}\) with integer \(m\ge1\), are also called Suzuki groups. That parameterized family is distinct from the sporadic group \(\mathrm{Suz}\). Likewise, the central covers \(2.\mathrm{Suz}\), \(3.\mathrm{Suz}\), and \(6.\mathrm{Suz}\) are distinct groups.

## References

1. [ATLAS: Suz](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Suz/), order, group/cover labels, and maximal-subgroup tables.
2. [Representation `SuzG1-p1782B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/SuzG1-p1782B0), “About this representation” and “Checks applied”; exact GAP data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/Suz/gap/SuzG1-p1782B0.g1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/Suz/gap/SuzG1-p1782B0.g2).
