+++
id = "algebra-category-theory/rigid-category"
title = "Rigid monoidal category"
kind = "definition"
summary = "A monoidal category in which every object has both a left and a right dual."
aliases = ["rigid category", "autonomous category"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/monoidal-category", "algebra-category-theory/dual-object"]
+++

A **rigid monoidal category** is a [[algebra-category-theory/monoidal-category|monoidal category]] in which every object admits both a left and a right [[algebra-category-theory/dual-object|dual]], including evaluation and coevaluation maps satisfying the snake identities. “Rigid category” in the context of fusion categories means rigid with respect to its specified tensor product.

## What rigidity adds

Rigidity makes it possible to move a tensor factor across a Hom expression by replacing it with a suitable dual. It does not assert that every morphism is invertible, or that every object has a tensor inverse. It also does not require a braiding or identify the left and right duals by a chosen isomorphism.

Finite-dimensional vector spaces are rigid under tensor product. The category of all vector spaces is not: a coevaluation tensor is a finite sum, so its snake identity would force the identity map of a dualizable space to have finite rank. Thus its dualizable objects are precisely the finite-dimensional ones.

## Role in fusion categories

[[algebra-category-theory/semisimple-category|Semisimplicity]] describes decomposition under direct sum. Rigidity concerns the different operation \(\otimes\). These conditions play separate roles in a [[algebra-category-theory/fusion-category|fusion category]].

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), Definition 2.10.11; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
