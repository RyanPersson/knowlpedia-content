+++
id = "algebra-category-theory/finite-abelian-category"
title = "Finite abelian category"
kind = "definition"
summary = "A linear abelian category equivalent to finite-dimensional modules over a finite-dimensional algebra."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/k-linear-category", "algebra-category-theory/equivalence-of-categories", "algebra-modules/module"]
+++

A **finite abelian category over \(k\)** is a [[algebra-category-theory/k-linear-category|\(k\)-linear]] [[algebra-category-theory/abelian-category|abelian category]] that is \(k\)-linearly [[algebra-category-theory/equivalence-of-categories|equivalent]] to the category of finite-dimensional left [[algebra-modules/module|modules]] over some finite-dimensional associative unital \(k\)-algebra.

## Intrinsic conditions

Equivalently, Hom spaces are finite-dimensional, every object has finite length, there are finitely many simple isomorphism classes, and there are enough projectives. Finite length means that an object has a finite filtration with simple successive quotients. Having enough projectives means that every object is the target of an epimorphism from a projective object; an object is projective when maps from it lift across every epimorphism.

“Finite” does not mean finitely many objects or finitely many arrows. Finite-dimensional vector spaces form a finite abelian category, but their dimensions are unbounded.

## Semisimplicity is extra

Finite-dimensional modules over \(k[\varepsilon]/(\varepsilon^2)\) form a finite abelian category which is not semisimple. The regular module has the submodule \((\varepsilon)\), and its resulting short exact sequence does not split. In contrast, a Hom-finite semisimple \(k\)-linear category with finitely many simple isomorphism classes is finite abelian.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), Definitions 1.8.5–1.8.6; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
