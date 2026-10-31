+++
id = "algebra-category-theory/strict-monoidal-category"
title = "Strict monoidal category"
kind = "definition"
summary = "A monoidal category whose associator and unitors are identity morphisms."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/monoidal-category"]
+++

A **strict monoidal category** is a [[algebra-category-theory/monoidal-category|monoidal category]] whose associator and left and right unitors are identities. Thus \((X\otimes Y)\otimes Z=X\otimes(Y\otimes Z)\) and \(\mathbb1\otimes X=X=X\otimes\mathbb1\) hold as equalities of objects and functors, with the specified coherence maps equal to identity arrows.

## Why strict notation is useful

Endofunctors of a category, with composition as tensor product and the identity functor as unit, form a strict monoidal category. Ordinary vector-space tensor products come with canonical associativity isomorphisms rather than literal equalities.

Every monoidal category is monoidally equivalent to a strict one. This permits coherent calculations without parentheses, but does not make the original category's associators literally identities. In particular, one should not discard associator data when specifying a particular fusion category.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §§2.8–2.9; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
