+++
id = "operator-algebras/type-i-von-neumann-algebra"
title = "Type I von Neumann algebra"
kind = "definition"
summary = "A von Neumann algebra in which every nonzero central summand contains a nonzero abelian projection."
aliases = ["type I W*-algebra", "discrete von Neumann algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/abelian-projection", "operator-algebras/central-support"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is
**type I** if every nonzero central projection \(z\in M\) dominates a nonzero
[[operator-algebras/abelian-projection|abelian projection]]: there is a
projection \(0\neq p\leq z\) such that the corner \(pMp\) is abelian.
Equivalently, the [[operator-algebras/central-support|central support]] of the
family of abelian projections, meaning the supremum of their central supports,
is \(1\). This definition applies to algebras
with nontrivial center; it does not assert that \(M\) is itself a factor.
The Roman numeral I names the first Murray–von Neumann type and must not be
confused with the separate notion of a type I \(C^*\)-algebra.

## Factor case and homogeneous pieces

A [[operator-algebras/von-neumann-factor|von Neumann factor]] is type I exactly
when it is isomorphic to \(B(H)\) for some [[linear-algebra/hilbert-space|Hilbert space]] \(H\). It is called
type \(\mathrm{I}_n\) when \(\dim H=n<\infty\), and type
\(\mathrm{I}_\infty\) when \(H\) is infinite-dimensional. A general type I
von Neumann algebra is assembled over its center from such homogeneous type I
pieces; the dimensions of the factor fibers need not be constant.

## Abelian and concrete examples

Every [[operator-algebras/commutative-von-neumann-algebra|abelian von Neumann algebra]] is type I because each projection \(p\)
has an abelian corner \(pMp\). Matrix algebras \(M_n(\mathbb C)\) and full
operator algebras \(B(H)\) are [[operator-algebras/type-i-factor|type I factors]]. By contrast, a type II factor
has no nonzero abelian projection, and a [[operator-algebras/type-iii-factor|type III factor]] has no nonzero finite
projection. These contrasts concern factor types; a general von Neumann
algebra may have nonzero central summands of several types.

## Classification convention

The type I, II, and III decomposition is a decomposition by unique central
projections whose sum is \(1\). Thus phrases such as “\(M\) has a type I
part” refer to a central summand, whereas “\(M\) is type I” means that the
other two central parts vanish.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §6.5 on the type decomposition.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on types of von Neumann algebras and traces.
