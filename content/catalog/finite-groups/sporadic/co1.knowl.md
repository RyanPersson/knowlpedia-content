+++
id = "catalog/finite-groups/sporadic/co1"
title = "Conway group Co1"
kind = "knowl"
summary = "The simple quotient of the Leech lattice isometry group by its central sign."
aliases = ["Conway group Co1", "Co1", "first Conway group"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["catalog/finite-groups/sporadic/leech-lattice", "algebra-groups/quotient-group"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Conway group** \(\mathrm{Co}_1\) is the [[algebra-groups/quotient-group|quotient]]
\[
\mathrm{Co}_1=O(\Lambda)/\{I,-I\},
\]
where \(\Lambda\) is the [[catalog/finite-groups/sporadic/leech-lattice|Leech lattice]] and \(O(\Lambda)\) consists of the real linear isometries of \(\mathbb R^{24}\) that preserve \(\Lambda\). The subgroup \(\{I,-I\}\) is central, so the quotient is a group.

## Order and simplicity

The group is nonabelian and [[algebra-groups/simple-group|simple]], with
\[
|\mathrm{Co}_1|=4\,157\,776\,806\,543\,360\,000
=2^{21}\cdot3^9\cdot5^4\cdot7^2\cdot11\cdot13\cdot23.
\]
The full lattice isometry group is often denoted \(\mathrm{Co}_0=2.\mathrm{Co}_1\). It has twice this order and is not the simple group \(\mathrm{Co}_1\).

## A finite matrix model

The two binary matrices in `Co1G1-f2r24B0.m1` and `Co1G1-f2r24B0.m2` generate a faithful copy of \(\mathrm{Co}_1\) in [[catalog/finite-groups/elementary/gl-n-q|\(\mathrm{GL}_{24}(\mathbb F_2)\)]], the group of [[linear-algebra/matrix-inverse|invertible matrices]] over the [[algebra-fields-galois/finite-field|field]] with two elements. The files specify all entries row by row after their format header.

## Neighboring Conway groups

There are maximal subgroups isomorphic to [[catalog/finite-groups/sporadic/co2|\(\mathrm{Co}_2\)]] and [[catalog/finite-groups/sporadic/co3|\(\mathrm{Co}_3\)]], of indices \(98\,280\) and \(8\,386\,560\), respectively.

## References

1. Robert A. Wilson, [Finite Simple Groups, Chapter 5 notes](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes5.pdf), §5.3.2 for the central quotient and §5.3.3 for simplicity.
2. [ATLAS: Co1](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co1/), order and maximal-subgroup tables.
3. [Representation `Co1G1-f2r24B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/Co1G1-f2r24B0), “About this representation”; exact MeatAxe data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co1/mtx/Co1G1-f2r24B0.m1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co1/mtx/Co1G1-f2r24B0.m2).
