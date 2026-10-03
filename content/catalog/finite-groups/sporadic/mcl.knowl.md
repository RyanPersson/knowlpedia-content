+++
id = "catalog/finite-groups/sporadic/mcl"
title = "McLaughlin group McL"
kind = "knowl"
summary = "The sporadic simple McLaughlin group in its faithful action on 275 points."
aliases = ["McLaughlin group", "McL"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/symmetric-group", "algebra-groups/generated-subgroup"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **McLaughlin group** \(\mathrm{McL}\) is the [[algebra-groups/generated-subgroup|subgroup generated]] in the [[algebra-groups/symmetric-group|symmetric group]] by the permutations \(a,b\) of \(\{1,\ldots,275\}\) specified by `McLG1-p275B0.g1` and `McLG1-p275B0.g2`, respectively:
\[
\mathrm{McL}=\langle a,b\rangle\le S_{275}.
\]
The exact files are linked in References. They give disjoint-cycle permutations, with omitted points fixed, and define a faithful permutation model under composition.

## Order and simplicity

This is a nonabelian [[algebra-groups/simple-group|simple group]] of order
\[
|\mathrm{McL}|=898\,128\,000=2^7\cdot3^6\cdot5^3\cdot7\cdot11.
\]

## The 275-point action and Conway groups

The action is transitive and a point stabilizer has orbits of sizes \(1,112,162\), giving a rank-three action. The stabilizer is isomorphic to the projective special unitary group \(\mathrm{PSU}_4(3)\).

The group occurs as a maximal subgroup of [[catalog/finite-groups/sporadic/co2|\(\mathrm{Co}_2\)]] of index \(47\,104\), and as a subgroup of [[catalog/finite-groups/sporadic/co3|\(\mathrm{Co}_3\)]] of index \(552\). In the latter case it lies in a larger maximal subgroup \(\mathrm{McL}:2\).

## References

1. [ATLAS: McL](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/McL/), order and representation tables.
2. [Representation `McLG1-p275B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/McLG1-p275B0), “About this representation” and “Checks applied”; exact GAP data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/McL/gap/McLG1-p275B0.g1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/McL/gap/McLG1-p275B0.g2).
3. [ATLAS: Co2](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co2/) and [ATLAS: Co3](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co3/), maximal-subgroup rows McL and McL:2, respectively.
