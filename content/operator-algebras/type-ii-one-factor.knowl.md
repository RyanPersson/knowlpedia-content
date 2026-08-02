+++
id = "operator-algebras/type-ii-one-factor"
title = "Type II₁ factor"
kind = "definition"
summary = "A finite type II von Neumann factor, equivalently a continuous factor with finite identity."
aliases = ["finite continuous factor", "Type II_1 factor"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A **type \(\mathrm{II}_1\) factor** is a
[[operator-algebras/von-neumann-factor|von Neumann factor]] \(M\) that is
[[operator-algebras/type-ii-von-neumann-algebra|type II]] and whose identity
is a [[operator-algebras/finite-projection|finite projection]]. Equivalently,
it is a type II [[operator-algebras/finite-von-neumann-algebra|finite von
Neumann algebra]] with trivial center. Thus \(M\) has no nonzero abelian
projection, but all its projections are finite. It possesses a unique
normalized faithful normal trace \(\tau\), characterized by
\(\tau(1_M)=1\) and \(\tau(xy)=\tau(yx)\). Infinite-dimensionality is automatic:
a finite-dimensional factor is a matrix algebra and hence type I.

## Continuous dimension

The trace classifies projections up to
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalence]]:
\[
p\sim q\quad\Longleftrightarrow\quad \tau(p)=\tau(q).
\]
Moreover every value in \([0,1]\) occurs as \(\tau(p)\) for some projection
\(p\). This continuous range of projection dimensions explains the older name
“finite continuous factor.” These statements are part of the basic dimension
theory of finite factors.

## Examples and contrasts

The hyperfinite type \(\mathrm{II}_1\) factor is obtained as the weak closure,
in its tracial representation, of an increasing union of matrix algebras.
[[operator-algebras/group-von-neumann-algebra|Group von Neumann algebras]] of many infinite [[algebra-groups/conjugacy-class|conjugacy class]] discrete groups
give further examples.

The [[operator-algebras/type-i-n-factor|matrix factor]]
\(M_n(\mathbb C)\) is finite but type I, not type \(\mathrm{II}_1\), because
it has minimal [[operator-algebras/abelian-projection|abelian projections]]. A
type \(\mathrm{II}_\infty\) factor has no nonzero abelian projections but its
identity is infinite.

## Conventions and scope

**Warning.** Some authors define a finite factor first and then call it type
\(\mathrm{II}_1\) only after excluding matrix factors. Both the type II
condition and finiteness of the identity are essential. The trace is unique
only after normalization; positive scalar multiples are also faithful normal
traces.

## References

1. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on finite continuous factors and dimension theory.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on finite factors and traces.
