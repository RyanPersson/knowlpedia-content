+++
id = "operator-algebras/type-i-n-factor"
title = "Type Iₙ factor"
kind = "definition"
summary = "A type I factor isomorphic to the algebra of complex n by n matrices for a positive integer n."
aliases = ["finite type I factor", "matrix factor", "Type I_n factor"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(n\geq 1\) be an integer. A **type \(\mathrm{I}_n\) factor** is a
[[operator-algebras/type-i-factor|type I factor]] isomorphic, as a von Neumann
algebra, to the matrix algebra \(M_n(\mathbb C)\). Equivalently, it is a type I
factor whose maximal families of nonzero mutually orthogonal equivalent
[[operator-algebras/minimal-projection|minimal projections]] have exactly
\(n\) members. Its identity is finite, so it is a
[[operator-algebras/finite-von-neumann-algebra|finite von Neumann
algebra]].
The integer \(n\) is intrinsic: it is the complex dimension of the
[[linear-algebra/hilbert-space|Hilbert space]] \(K\) in the realization
\(M\cong B(K)\), not the vector-space dimension \(n^2\) of the algebra.

## Matrix-unit description

A type \(\mathrm{I}_n\) factor contains matrix units
\(\{e_{ij}\}_{1\leq i,j\leq n}\) satisfying
\[
e_{ij}e_{kl}=\delta_{jk}e_{il},\qquad e_{ij}^*=e_{ji},\qquad
\sum_{i=1}^n e_{ii}=1.
\]
The diagonal projections \(e_{ii}\) are mutually equivalent and minimal.
Conversely, such a full system of matrix units identifies the algebra with
\(M_n(\mathbb C)\). The classification follows from the type I factor theorem
[Takesaki, Chapter V, §1](https://doi.org/10.1007/978-1-4612-6188-9).

## Trace and examples

There is a unique normalized [[operator-algebras/tracial-state|tracial state]],
\[
\tau(x)=\frac{1}{n}\operatorname{Tr}(x).
\]
For projections, \(\tau(p)=\operatorname{rank}(p)/n\), so the possible trace
values form the finite set \(\{0,1/n,\ldots,1\}\).

The case \(n=1\) is \(\mathbb C\). The case \(n=2\) is the algebra of
\(2\times2\) complex matrices. An [[operator-algebras/type-i-infinity-factor|infinite type I factor]] \(B(H)\) is not type
\(\mathrm{I}_n\) for any finite \(n\), even though it contains many corners
isomorphic to finite matrix algebras.

## Conventions and scope

**Warning.** The subscript records Hilbert-space dimension, not algebra
dimension. Some texts write \(I_n\) without typesetting the Roman numeral;
“type 1” is not the standard terminology.

## References

1. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §1 on type I factors and their dimension.
2. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on finite type I factors.
