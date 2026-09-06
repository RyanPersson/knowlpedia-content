+++
id = "operator-algebras/type-ii-infinity-factor"
title = "Type II∞ factor"
kind = "definition"
summary = "A type II von Neumann factor whose identity projection is infinite."
aliases = ["semifinite infinite factor"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-factor", "operator-algebras/type-ii-von-neumann-algebra", "operator-algebras/properly-infinite-von-neumann-algebra", "operator-algebras/abelian-projection", "operator-algebras/finite-projection", "operator-algebras/faithful-normal-semifinite-trace"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **type \(\mathrm{II}_\infty\) factor** is a [[operator-algebras/von-neumann-factor|von Neumann factor]] \(M\) that is [[operator-algebras/type-ii-von-neumann-algebra|type II]] and whose identity projection \(1_M\) is infinite. Equivalently, it is a semifinite, [[operator-algebras/properly-infinite-von-neumann-algebra|properly infinite]] factor with no nonzero [[operator-algebras/abelian-projection|abelian projection]]. Semifiniteness supplies nonzero [[operator-algebras/finite-projection|finite projections]] below every nonzero projection, while the infinite identity excludes the finite type \(\mathrm{II}_1\) case. A [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] on \(M\) therefore takes the value \(+\infty\) at \(1_M\); unlike the normalized trace on a \(\mathrm{II}_1\) factor, it is determined only up to a positive scalar.

## Projection and trace structure

Every nonzero finite projection \(p\in M\) has a type \(\mathrm{II}_1\) corner \(pMp\) after its trace is normalized. Conversely, the identity can be decomposed into mutually orthogonal finite projections; countable decomposability permits a countable such decomposition. These facts explain how finite corners coexist with a properly infinite ambient algebra.

The defining distinction from a [[operator-algebras/type-iii-factor|type III factor]] is precisely this supply of finite projections. Both classes have infinite identity and no [[operator-algebras/minimal-projection|minimal projections]], but a type III factor has no nonzero finite projection at all.

## Examples and non-examples

If \(N\) is a type \(\mathrm{II}_1\) factor and \(H\) is an infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]], then
\[
N\mathbin{\overline{\otimes}}B(H)
\]
is type \(\mathrm{II}_\infty\). Its tensor-product trace is semifinite and infinite on the identity.

The algebra \(B(H)\) itself is not type \(\mathrm{II}_\infty\): it is a type \(\mathrm{I}_\infty\) factor because it contains minimal projections. A type \(\mathrm{II}_1\) factor is also a near miss, failing only the requirement that its identity be infinite.

## References

1. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on the type decomposition and type \(\mathrm{II}_\infty\) factors.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on finite and semifinite von Neumann algebras.
