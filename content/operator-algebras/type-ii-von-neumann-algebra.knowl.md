+++
id = "operator-algebras/type-ii-von-neumann-algebra"
title = "Type II von Neumann algebra"
kind = "definition"
summary = "A type II von Neumann algebra is semifinite and has no nonzero abelian projection."
aliases = ["type II W*-algebra", "continuous semifinite von Neumann algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/semifinite-von-neumann-algebra", "operator-algebras/abelian-projection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is **type II** if it is [[operator-algebras/semifinite-von-neumann-algebra|semifinite]] and has no nonzero [[operator-algebras/abelian-projection|abelian projection]]. Here a projection \(p\in M\) is abelian when the corner \(pMp\) is a commutative algebra. Thus type II algebras possess enough [[operator-algebras/finite-projection|finite projections]] or, equivalently in the standard formulation, a [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]], but none of their nonzero projection corners is type I and abelian. This definition applies to general von Neumann algebras, not only to factors.

## The subdivisions \(\mathrm{II}_1\) and \(\mathrm{II}_\infty\)

A type II factor is of type \(\mathrm{II}_1\) when its identity is finite; it then has a unique normalized faithful normal trace. It is of type \(\mathrm{II}_\infty\) when its identity is infinite; it has a faithful normal semifinite trace but no finite trace normalized on the identity. A general type II algebra admits a canonical central decomposition into \(\mathrm{II}_1\) and \(\mathrm{II}_\infty\) parts.

## Distinguishing nearby conditions

Having no nonzero [[operator-algebras/minimal-projection|minimal projections]] does not by itself imply type II: a diffuse [[operator-algebras/commutative-von-neumann-algebra|abelian von Neumann algebra]] also has no minimal projections, but it has nonzero abelian projections and is type I. The no-abelian-projection condition is what excludes this case. [[operator-algebras/type-iii-von-neumann-algebra|Type III algebras]] are also non-type-I, but, unlike type II algebras, they have no nonzero finite projections.

## References

1. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: Section 6.5 on the type decomposition.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on finite, semifinite, and type II von Neumann algebras.
