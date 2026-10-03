+++
id = "catalog/finite-groups/sporadic/hs"
title = "Higman–Sims group HS"
kind = "knowl"
summary = "The sporadic simple group HS in its faithful action on 100 points."
aliases = ["Higman-Sims group", "Higman–Sims group", "HS"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/symmetric-group", "algebra-groups/generated-subgroup"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Higman–Sims group** \(\mathrm{HS}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] in the [[algebra-groups/symmetric-group|symmetric group]] by the permutations \(a,b\) of \(\{1,\ldots,100\}\) specified by the data files `HSG1-p100B0.g1` and `HSG1-p100B0.g2`, respectively:
\[
\mathrm{HS}=\langle a,b\rangle\le S_{100}.
\]
The exact files are linked in References. Each file gives a permutation in disjoint-cycle notation; omitted points are fixed. This specifies a concrete faithful permutation model, with group multiplication given by composition.

## Order and simplicity

This is a nonabelian [[algebra-groups/simple-group|simple group]] of order
\[
|\mathrm{HS}|=44\,352\,000=2^9\cdot3^2\cdot5^3\cdot7\cdot11.
\]
It belongs to the Leech-lattice cluster of the sporadic groups.

## Geometry and neighboring groups

The action on 100 points is transitive. A point stabilizer has orbits of sizes \(1,22,77\); the invariant graph from the orbit of length 22 is the Higman–Sims graph. Its full automorphism group is \(\mathrm{HS}:2\), so \(\mathrm{HS}\) has index two in that larger group.

There is a maximal subgroup isomorphic to \(\mathrm{HS}\) in [[catalog/finite-groups/sporadic/co3|\(\mathrm{Co}_3\)]], of index \(11\,178\).

## References

1. [ATLAS of Finite Group Representations: HS](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HS/), order and representation tables.
2. [Representation `HSG1-p100B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/HSG1-p100B0), “About this representation” and “Checks applied”; exact GAP data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/HS/gap/HSG1-p100B0.g1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/HS/gap/HSG1-p100B0.g2).
3. Peter J. Cameron, [Scenes from mathematical life](https://maths.qmul.ac.uk/~pjc/travel/forder/scenes2.pdf), slide “From Higman–Sims to Urysohn,” for the graph automorphism group.
4. [ATLAS: Co3](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co3/), “Maximal subgroups of Co3,” HS row.
