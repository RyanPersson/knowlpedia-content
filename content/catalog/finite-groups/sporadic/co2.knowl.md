+++
id = "catalog/finite-groups/sporadic/co2"
title = "Conway group Co2"
kind = "knowl"
summary = "The stabilizer of a minimal Leech-lattice vector, a sporadic simple group."
aliases = ["Conway group Co2", "Co2", "second Conway group"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["catalog/finite-groups/sporadic/leech-lattice", "algebra-groups/stabilizer"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Conway group** \(\mathrm{Co}_2\) is the [[algebra-groups/stabilizer|stabilizer]]
\[
\mathrm{Co}_2=\{g\in O(\Lambda):g(v)=v\}
\]
of a vector \(v\) of squared length \(\langle v,v\rangle=4\) in the [[catalog/finite-groups/sporadic/leech-lattice|Leech lattice]] \(\Lambda\). Here \(O(\Lambda)\) is the group of real linear isometries preserving the lattice. These vectors form one orbit, so all choices give conjugate stabilizers.

## Order and simplicity

This is a nonabelian [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{Co}_2|=42\,305\,421\,312\,000
=2^{18}\cdot3^6\cdot5^3\cdot7\cdot11\cdot23.
\]

## A finite matrix model

The two matrices in `Co2G1-f2r22B0.m1` and `Co2G1-f2r22B0.m2` generate a faithful copy of this group in [[catalog/finite-groups/elementary/gl-n-q|\(\mathrm{GL}_{22}(\mathbb F_2)\)]], the group of [[linear-algebra/matrix-inverse|invertible matrices]] over the [[algebra-fields-galois/finite-field|field]] with two elements. The representation dimension \(22\) is not the dimension \(24\) of the original lattice.

## Subgroup relationships

Projection to [[catalog/finite-groups/sporadic/co1|\(\mathrm{Co}_1\)]] is injective on this vector stabilizer, since \(-I\) does not fix \(v\). Its image is a maximal subgroup of index \(98\,280\).

The [[catalog/finite-groups/sporadic/mcl|McLaughlin group]] is isomorphic to a maximal subgroup of \(\mathrm{Co}_2\), of index \(47\,104\).

## References

1. Robert A. Wilson, [Finite Simple Groups, Chapter 5 notes](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes5.pdf), §5.3.4 and equation (5.16), for vector transitivity and the stabilizer.
2. [ATLAS: Co2](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co2/), order and maximal-subgroup tables; [ATLAS: Co1](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co1/), Co2 maximal-subgroup row.
3. [Representation `Co2G1-f2r22B0`](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/Co2G1-f2r22B0), “About this representation” and “Checks applied”; exact MeatAxe data [generator a](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co2/mtx/Co2G1-f2r22B0.m1) and [generator b](https://brauer.maths.qmul.ac.uk/Atlas/spor/Co2/mtx/Co2G1-f2r22B0.m2).
