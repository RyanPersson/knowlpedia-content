+++
id = "lie-groups/tfae-semisimplicity-lie-algebra"
title = "Equivalent characterizations of semisimplicity for Lie algebras"
kind = "knowl"
summary = "Semisimplicity is equivalent to nondegeneracy of the Killing form and to decomposition into simple ideals."
aliases = ["tfae-semisimplicity-lie-algebra", "Equivalent characterizations of semisimplicity for Lie algebras"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/killing-form", "lie-groups/killing-form-nondegenerate-iff-semisimple", "lie-groups/direct-sum-of-lie-algebras", "lie-groups/simple-lie-algebra", "lie-groups/semisimple-direct-sum-simple"]
dependency_review_count = 1
legacy_source_path = "lie-groups/tfae-semisimplicity-lie-algebra.md"
+++

Let \(\mathfrak g\) be a finite-dimensional Lie algebra over a field of characteristic \(0\). The following are equivalent.

1. **No nonzero solvable ideals:** \(\mathfrak g\) is [[lie-groups/semisimple-lie-algebra|semisimple]], i.e. it has no nonzero solvable ideal (equivalently, its radical is \(0\)).

2. **Nondegenerate Killing form:** the [[lie-groups/killing-form|Killing form]] \(\kappa(X,Y)=\mathrm{tr}(\mathrm{ad}_X\mathrm{ad}_Y)\) is nondegenerate; compare [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegeneracy of the Killing form]].

3. **Direct sum of simple ideals:** \(\mathfrak g\) is a (finite) [[lie-groups/direct-sum-of-lie-algebras|direct sum]] of [[lie-groups/simple-lie-algebra|simple Lie algebras]]; see [[lie-groups/semisimple-direct-sum-simple|semisimple equals direct sum of simple ideals]].

## Remarks

Nondegeneracy of the Killing form is [[lie-groups/cartans-criterion-semisimplicity|Cartan's criterion for semisimplicity]]. Complete reducibility of every finite-dimensional representation is a consequence of semisimplicity by [[lie-groups/weyls-theorem-complete-reducibility|Weyl's theorem]], but complete reducibility of the adjoint module alone is not an equivalent condition: an abelian Lie algebra has a completely reducible trivial adjoint module and is not semisimple.
