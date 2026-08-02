+++
id = "algebra-category-theory/algebra-object"
title = "Algebra object"
kind = "definition"
summary = "An internal associative unital algebra in a monoidal category."
aliases = ["monoid object in a monoidal category", "associative algebra object"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
+++

Let \((\mathcal C,\otimes,\mathbb 1)\) be a [[algebra-category-theory/monoidal-category|monoidal category]]. An **algebra object** in \(\mathcal C\) is an object \(A\) with multiplication and unit morphisms
\[
\mu:A\otimes A\longrightarrow A,\qquad \eta:\mathbb 1\longrightarrow A
\]
for which multiplication is associative, after inserting the associator, and \(\eta\) is a left and right unit, after inserting the unitors. A morphism of algebra objects is a morphism in \(\mathcal C\) that preserves \(\mu\) and \(\eta\).

## Commutative algebra objects

If \(\mathcal C\) is [[algebra-category-theory/symmetric-monoidal-category|symmetric monoidal]] with symmetry \(\beta\), the algebra object is **commutative** when
\[
\mu\circ\beta_{A,A}=\mu.
\]
This formulation makes the meaning of commutativity depend on the ambient symmetry. It produces ordinary commutative algebras in modules and [[supergeometry/supercommutative-algebra|supercommutative algebras]] in [[supergeometry/super-vector-space|super vector spaces]].

## Examples

In the monoidal category of modules over a commutative ring \(R\), algebra objects are precisely unital associative [[algebra-modules/algebra-over-ring|\(R\)-algebras]]. In a category with finite Cartesian products, algebra objects are internal monoids.

## References

1. Pavel Etingof, Shlomo Gelaki, Dmitri Nikshych, and Victor Ostrik, *Tensor Categories*, American Mathematical Society, 2015. [DOI record](https://doi.org/10.1090/surv/205). Relevant: §7.8.
