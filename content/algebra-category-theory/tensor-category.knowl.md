+++
id = "algebra-category-theory/tensor-category"
title = "Tensor category"
kind = "definition"
summary = "A locally finite linear abelian rigid monoidal category with simple unit."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/k-linear-category", "algebra-category-theory/rigid-category", "algebra-category-theory/simple-object"]
+++

Fix an algebraically closed field \(k\). Here a **tensor category over \(k\)** is a [[algebra-category-theory/k-linear-category|\(k\)-linear]] [[algebra-category-theory/abelian-category|abelian category]] with finite-dimensional Hom spaces and finite-length objects, equipped with a [[algebra-category-theory/rigid-category|rigid monoidal structure]] whose tensor product is \(k\)-bilinear on morphisms and whose unit is [[algebra-category-theory/simple-object|simple]]. Finite length means admitting a finite filtration with simple successive quotients.

## Terminology and nearby conditions

Some authors use “tensor category” simply for a monoidal category. The stronger convention here records the linear, abelian, finiteness, and duality hypotheses explicitly. Neither a braiding nor semisimplicity is part of this definition.

A [[algebra-category-theory/finite-tensor-category|finite tensor category]] additionally has a finite underlying abelian category. A [[algebra-category-theory/fusion-category|fusion category]] is a semisimple finite tensor category in this convention.

## Example

Finite-dimensional representations of a group, with equivariant linear maps and the diagonal action on tensor products, form a tensor category over \(k\). The dual action is \((g\varphi)(v)=\varphi(g^{-1}v)\). The group need not be finite; finiteness of the underlying abelian category is a separate requirement.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §4.1; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
