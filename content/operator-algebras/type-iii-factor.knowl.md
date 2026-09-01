+++
id = "operator-algebras/type-iii-factor"
title = "Type III factor"
kind = "definition"
summary = "A von Neumann factor having no nonzero finite projection."
aliases = ["type III von Neumann factor"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-factor", "operator-algebras/type-iii-von-neumann-algebra", "operator-algebras/finite-projection", "operator-algebras/infinite-projection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **type III factor** is a [[operator-algebras/von-neumann-factor|von Neumann
factor]] \(M\) that is a
[[operator-algebras/type-iii-von-neumann-algebra|type III von Neumann algebra]].
Thus \(M\) has no nonzero [[operator-algebras/finite-projection|finite
projection]]: every nonzero projection \(p\in M\) is
[[operator-algebras/infinite-projection|infinite]]. The factor condition
separately requires that the center of \(M\) consist only of scalars. Neither
condition follows from the other. This is the factorial case of the
Murray–von Neumann type III class; the finer labels
\(\mathrm{III}_0\), \(\mathrm{III}_\lambda\), and
\(\mathrm{III}_1\) require modular invariants and are not part of this
definition.

## Projection and corner structure

Every nonzero corner \(pMp\) of a type III factor is again a type III factor.
Indeed, its center remains scalar and any [[operator-algebras/finite-projection|finite projection]] in the corner
would be finite in \(M\). Nonzero projections have central support \(1\), and
the absence of finite projections makes them properly infinite. These
projection properties distinguish type III factors from both finite factors
and [[operator-algebras/type-ii-infinity-factor|semifinite infinite factors]].

## Traces and modular structure

A type III factor admits no nonzero normal semifinite trace: semifiniteness
would produce nonzero finite projections.
[[operator-algebras/normal-state|Normal states]] can nevertheless exist, and
[[operator-algebras/faithful-normal-state|faithful normal states]] exist under standard countable decomposability
hypotheses. Their [[operator-algebras/modular-automorphism-group|modular automorphism groups]] carry structure that cannot
generally be removed by choosing a trace. The resulting modular invariants
underlie Connes's finer classification.

## Examples and scope

Type III factors arise from infinite tensor products, nonsingular group
actions, and local algebras in algebraic quantum field theory. Merely being
infinite-dimensional is not enough: \(B(\ell^2)\) is an infinite-dimensional
[[operator-algebras/type-i-factor|type I factor]], and the hyperfinite
\(\mathrm{II}_1\) factor is infinite-dimensional but finite.

**Warning.** “Type III” for a general [[operator-algebras/von-neumann-algebra|von Neumann algebra]] does not imply
factoriality. A type III algebra may have nontrivial center and decompose into
type III factors only after an appropriate central decomposition.

## References

1. M. Takesaki, *Theory of Operator Algebras III*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10453-8). Relevant: Chapter XII on type III factors and their classification.
2. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on the Murray–von Neumann types.
