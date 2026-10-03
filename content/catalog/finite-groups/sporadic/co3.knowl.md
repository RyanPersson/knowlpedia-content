+++
id = "catalog/finite-groups/sporadic/co3"
title = "Conway group Co3"
kind = "knowl"
summary = "The stabilizer of a squared-length-six Leech-lattice vector, a sporadic simple group."
aliases = ["Conway group Co3", "Co3", "third Conway group"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["catalog/finite-groups/sporadic/leech-lattice", "algebra-groups/stabilizer"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Conway group** \(\mathrm{Co}_3\) is the [[algebra-groups/stabilizer|stabilizer]]
\[
\mathrm{Co}_3=\{g\in O(\Lambda):g(v)=v\}
\]
of a vector \(v\) of squared length \(\langle v,v\rangle=6\) in the [[catalog/finite-groups/sporadic/leech-lattice|Leech lattice]] \(\Lambda\). Here \(O(\Lambda)\) is the group of real linear isometries preserving the lattice. These vectors form one orbit, so all choices give conjugate stabilizers.

## Order and simplicity

This is a nonabelian [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Co}_3|=495\,766\,656\,000
=2^{10}\cdot3^7\cdot5^3\cdot7\cdot11\cdot23.
\]

## A finite matrix model

The two matrices in `Co3G1-f2r22B0.m1` and `Co3G1-f2r22B0.m2` generate a faithful copy in [[catalog/finite-groups/elementary/gl-n-q|\(\mathrm{GL}_{22}(\mathbb F_2)\)]], the group of [[linear-algebra/matrix-inverse|invertible matrices]] over the [[algebra-fields-galois/finite-field|field]] with two elements.

## Subgroup relationships

Projection to [[catalog/finite-groups/sporadic/co1|\(\mathrm{Co}_1\)]] is injective on this vector stabilizer, since \(-I\) does not fix \(v\). Its image is maximal of index \(8\,386\,560\).

The [[catalog/finite-groups/sporadic/hs|Higman–Sims group]] occurs as a maximal subgroup of index \(11\,178\). A maximal subgroup \(\mathrm{McL}:2\), containing the [[catalog/finite-groups/sporadic/mcl|McLaughlin group]] with index two, has index \(276\). Consequently the embedded \(\mathrm{McL}\) has index \(552\) and is not maximal.

## References

1. Robert A. Wilson, [Finite Simple Groups, Chapter 5 notes](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes5.pdf), §5.3.4 and equation (5.17), for vector transitivity and the stabilizer.
2. [ATLAS: Co3](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co3/), order and maximal-subgroup tables; [ATLAS: Co1](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co1/), Co3 maximal-subgroup row.
3. [Representation `Co3G1-f2r22B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/Co3G1-f2r22B0), “About this representation”; exact MeatAxe data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co3/mtx/Co3G1-f2r22B0.m1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co3/mtx/Co3G1-f2r22B0.m2).
