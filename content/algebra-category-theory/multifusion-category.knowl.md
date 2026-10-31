+++
id = "algebra-category-theory/multifusion-category"
title = "Multifusion category"
kind = "definition"
summary = "The fusion-category axioms without requiring the tensor unit to be simple."
aliases = ["multi-fusion category"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/k-linear-category", "algebra-category-theory/semisimple-category", "algebra-category-theory/rigid-category"]
+++

Over an algebraically closed field \(k\), a **multifusion category** is an essentially small [[algebra-category-theory/k-linear-category|\(k\)-linear]] [[algebra-category-theory/semisimple-category|semisimple abelian category]] with finite-dimensional Hom spaces, finitely many simple isomorphism classes, and a [[algebra-category-theory/rigid-category|rigid monoidal structure]] whose tensor product is \(k\)-bilinear on morphisms. The tensor unit need not be simple. Essentially small means that the isomorphism classes of objects form a set.

## Comparison and example

A nonzero multifusion category with simple unit is a [[algebra-category-theory/fusion-category|fusion category]]. As with fusion categories, some conventions additionally impose characteristic zero.

The product of two categories of finite-dimensional vector spaces, with componentwise tensor product, is multifusion. Its unit \((k,k)\) decomposes as \((k,0)\oplus(0,k)\), so it is not fusion. This example isolates exactly the role of the simple-unit condition.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §4.1; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
