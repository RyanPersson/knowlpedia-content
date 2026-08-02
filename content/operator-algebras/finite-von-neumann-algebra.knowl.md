+++
id = "operator-algebras/finite-von-neumann-algebra"
title = "Finite von Neumann algebra"
kind = "definition"
summary = "A von Neumann algebra whose identity is a finite projection."
aliases = ["finite W*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is
**finite** if its identity \(1_M\) is a
[[operator-algebras/finite-projection|finite projection]] in \(M\). Explicitly,
whenever \(v\in M\) satisfies \(v^*v=1_M\), one must also have
\(vv^*=1_M\); thus every isometry belonging to \(M\) is unitary. Equivalently,
no proper subprojection of \(1_M\) is
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann equivalent]]
to \(1_M\). Finiteness is an internal comparison property of projections. It
does not require \(M\) to be finite-dimensional, a factor, or represented on a
finite-dimensional [[linear-algebra/hilbert-space|Hilbert space]].

## Equivalent formulations and structure

Finiteness of the identity forces every projection in \(M\) to be finite.
Conversely, that condition plainly includes the identity. A major structure
theorem supplies every finite von Neumann algebra with a unique faithful normal
center-valued trace normalized at \(1_M\); its scalar specializations organize
the ordinary finite traces. See
for the projection-comparison and trace formulations.

Finite factors split into two classes. A
[[operator-algebras/type-i-n-factor|finite type I factor]] is a matrix algebra,
whereas a finite factor without nonzero
[[operator-algebras/abelian-projection|abelian projections]] is of type
\(\mathrm{II}_1\). A finite von Neumann algebra with nontrivial center can
have both sorts of central summands.

## Examples and non-examples

Every matrix algebra \(M_n(\mathbb C)\) is finite. An infinite-dimensional
[[operator-algebras/commutative-von-neumann-algebra|commutative von Neumann algebra]] is also finite: a [[functional-analysis/partial-isometry|partial isometry]] in an
abelian algebra has equal initial and final projections.

By contrast, \(B(H)\) for an infinite-dimensional Hilbert space \(H\) is not
finite. A unilateral shift is an isometry whose range projection is strictly
smaller than the identity.

## Conventions and scope

**Warning.** A finite von Neumann algebra need not admit a faithful normal
[[operator-algebras/tracial-state|tracial state]] when its center is not suitably countably decomposable. The
center-valued trace is the representation-free general statement. “Finite”
also differs from “semifinite”: every finite algebra is semifinite, but
infinite type \(\mathrm{II}_\infty\) algebras are semifinite without being
finite.

## References

1. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on finite von Neumann algebras, comparison, and center-valued traces.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §2 on finite von Neumann algebras.
