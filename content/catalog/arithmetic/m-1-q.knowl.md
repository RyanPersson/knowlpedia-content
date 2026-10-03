+++
id = "catalog/arithmetic/m-1-q"
title = "Rational matrix algebra M_1(Q)"
kind = "definition"
summary = "A rational matrix algebra with fixed size and ordinary matrix multiplication."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "shared-foundations/rational-numbers"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **rational matrix algebra \(M_1(\mathbb Q)\)** is the [[linear-algebra/vector-space|vector space]] of \(1\times 1\) matrices with [[shared-foundations/rational-numbers|rational]] entries, with entrywise addition and scalar multiplication, and the associative product
\[
(AB)_{ij}=\sum_{r=1}^{1} A_{ir}B_{rj}.
\]
Its multiplicative unit is the identity matrix \(I_1\).

## Basis and dimensions

The matrix units \(E_{ij}\) form a rational basis of size \(1^2\), with \(E_{ij}E_{rs}=\delta_{jr}E_{is}\). Thus its rational dimension is 1. The center consists of scalar matrices.

## Endomorphism interpretation

After choosing a basis of \(\mathbb Q^1\), this algebra identifies with \(\operatorname{End}_{\mathbb Q}(\mathbb Q^1)\), with matrix product corresponding to composition. Its units form \(\mathrm{GL}_1(\mathbb Q)\). These are units of this algebra; an automorphism of the matrix algebra is a different sort of map.

## Low-dimensional boundary

For size one, scalar matrices give \(M_1(\mathbb Q)\cong\mathbb Q\) as unital rational algebras. For every size at least two, \(E_{11}\) and \(E_{22}\) are nonzero with zero product, so the matrix algebra is not a division algebra.
