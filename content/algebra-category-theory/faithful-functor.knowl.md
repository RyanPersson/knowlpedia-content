+++
id = "algebra-category-theory/faithful-functor"
title = "Faithful functor"
kind = "definition"
summary = "A functor that is injective on every hom-set."
aliases = ["faithful functor"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/functor"]
+++

Let \(F:\mathcal C\to\mathcal D\) be a [[algebra-category-theory/functor|functor]]. It is **faithful** if, for every pair of objects \(X,Y\) in \(\mathcal C\), the induced map
\[
\operatorname{Hom}_{\mathcal C}(X,Y)\longrightarrow
\operatorname{Hom}_{\mathcal D}(F(X),F(Y)),\qquad
f\longmapsto F(f)
\]
is injective.

## Interpretation

A faithful functor can identify distinct objects, but it never identifies two morphisms having the same source and target.

## Example

The forgetful functor from groups to sets is faithful: a group homomorphism is determined by its underlying function.
