+++
id = "algebra-hyperstructures/partial-field"
title = "Partial field"
kind = "definition"
summary = "A multiplicative group of ring units on which addition is only partially defined."
aliases = ["Semple-Whittle partial field"]
domains = ["algebra-hyperstructures", "algebra-rings", "matroid-theory"]
section_mode = "progressive"
+++

A **partial field** in normalized ambient form is a pair \(P=(G,R)\), where
\(R\) is a commutative unital ring and \(G\leq R^\times\) is a subgroup such
that \(-1\in G\) and \(G\) generates \(R\) as a ring. Its underlying pointed
set is
\[
\underline P=G\cup\{0\}.
\]
Multiplication is inherited from \(R\), while \(a+b\) is defined in
\(\underline P\) exactly when the ring sum \(a+b\) again belongs to
\(\underline P\).

## Why addition is partial

Multiplication and division by nonzero elements stay inside \(G\), but a ring
sum of two selected units can leave \(G\cup\{0\}\). When the sum is defined,
it has one value; this differs from a hyperfield, where every pair has a
nonempty set of possible sums.

## Fields and the regular partial field

Every field \(K\) gives the partial field
\((K^\times,K)\), for which addition is defined everywhere and recovers the
field. The **regular partial field**
\[
\mathbb U_0=(\{1,-1\},\mathbb Z)
\]
has only \(0,\pm1\) as coefficients; for example \(1+(-1)=0\) is defined,
while \(1+1=2\) is not a coefficient and is therefore undefined.

## Associated tract

A partial field determines a [[algebra-hyperstructures/tract|tract]] with
multiplicative group \(G\) by declaring
\[
\sum_i g_i\in N_G
\quad\Longleftrightarrow\quad
\sum_i g_i=0\text{ in }R.
\]
The tract remembers all finite null relations, including ones whose
intermediate binary sums leave the partial field. Partial fields also have
associated pastures, but not every tract or pasture comes from a partial
field.

## Convention warning

Some definitions omit the requirement that \(G\) generate \(R\) and identify
ambient presentations that produce the same partial field. The generation
condition is used here to remove irrelevant ambient ring elements.

## References

1. Charles Semple and Geoff Whittle, “Partial fields and matroid representation,” *Advances in Applied Mathematics* 17 (1996), 184–208. [Institutional record and text](https://ir.canterbury.ac.nz/items/c820a2ab-c8f6-4316-83fb-5f36804fac7c). Relevant: the original partial-field framework.
2. Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,” *Advances in Mathematics* 343 (2019), 821–863. [arXiv:1709.09707](https://arxiv.org/abs/1709.09707). Relevant: Definition 2.24 and the associated tract.
