+++
id = "algebra-category-theory/finite-tensor-category"
title = "Finite tensor category"
kind = "definition"
summary = "A tensor category whose underlying linear abelian category is finite."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/tensor-category", "algebra-category-theory/finite-abelian-category"]
+++

A **finite tensor category** over an algebraically closed field \(k\) is a [[algebra-category-theory/tensor-category|tensor category]] whose underlying \(k\)-linear abelian category is [[algebra-category-theory/finite-abelian-category|finite abelian]]. In particular, its Hom spaces are finite-dimensional, its objects have finite length, it has finitely many simple isomorphism classes and enough projectives, and its monoidal structure is rigid with simple unit and \(k\)-bilinear tensor product.

## Why this is broader than fusion

A [[algebra-category-theory/fusion-category|fusion category]] is precisely a semisimple finite tensor category under these conventions. Finite tensor categories may have nonsplit extensions of simple objects.

For example, over an algebraically closed field of characteristic \(p>0\), finite-dimensional representations of the cyclic group of order \(p\) form a finite tensor category that is not semisimple. Its group algebra is \(k[t]/((t-1)^p)\), whose regular module has nontrivial extensions. This example is outside the often-adopted characteristic-zero convention for fusion categories.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §4.1 and Chapter 6; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
