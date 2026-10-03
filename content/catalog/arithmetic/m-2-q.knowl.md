+++
id = "catalog/arithmetic/m-2-q"
title = "Rational matrix algebra M_2(Q)"
kind = "definition"
summary = "A rational matrix algebra with fixed size and ordinary matrix multiplication."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "shared-foundations/rational-numbers"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **rational matrix algebra \(M_2(\mathbb Q)\)** is the [[linear-algebra/vector-space|vector space]] of \(2\times 2\) matrices with [[shared-foundations/rational-numbers|rational]] entries, with entrywise addition and scalar multiplication, and the associative product
\[
(AB)_{ij}=\sum_{r=1}^{2} A_{ir}B_{rj}.
\]
Its multiplicative unit is the identity matrix \(I_2\).

## Basis and dimensions

The matrix units \(E_{ij}\) form a rational basis of size \(2^2\), with \(E_{ij}E_{rs}=\delta_{jr}E_{is}\). Thus its rational dimension is 4. The center consists of scalar matrices.

## Endomorphism interpretation

After choosing a basis of \(\mathbb Q^2\), this algebra identifies with \(\operatorname{End}_{\mathbb Q}(\mathbb Q^2)\), with matrix product corresponding to composition. Its units form \(\mathrm{GL}_2(\mathbb Q)\). These are units of this algebra; an automorphism of the matrix algebra is a different sort of map.

## Low-dimensional boundary

For size one, scalar matrices give \(M_1(\mathbb Q)\cong\mathbb Q\) as unital rational algebras. For every size at least two, \(E_{11}\) and \(E_{22}\) are nonzero with zero product, so the matrix algebra is not a division algebra.

## Quadratic-field example

Using the basis \(1,i\) identifies the rational-linear endomorphisms of [[catalog/arithmetic/qi|\(\mathbb Q(i)\)]] with this matrix algebra. Multiplication by \(a+bi\) corresponds to \(\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)\), a two-dimensional subalgebra of the four-dimensional matrix algebra.
