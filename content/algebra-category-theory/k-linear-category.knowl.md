+++
id = "algebra-category-theory/k-linear-category"
title = "k-linear category"
kind = "definition"
summary = "A category whose morphisms form vector spaces and whose composition is bilinear."
aliases = ["linear category over a field"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "linear-algebra/vector-space"]
+++

A **\(k\)-linear category**, for a field \(k\), is a [[algebra-category-theory/category|category]] \(\mathcal C\) with a \(k\)-[[linear-algebra/vector-space|vector space]] structure on each \(\operatorname{Hom}_{\mathcal C}(X,Y)\), such that composition is \(k\)-bilinear. Thus, whenever the composites are defined,
\[
g\circ(af+bf')=a(g\circ f)+b(g\circ f'),\qquad
(ag+bg')\circ f=a(g\circ f)+b(g'\circ f)
\]
for \(a,b\in k\). The vector space structures are part of the data.

## What linearity does and does not supply

One can add parallel arrows and multiply them by scalars. In particular the category is [[algebra-category-theory/preadditive-category|preadditive]]. This does not by itself provide direct sums of objects, kernels, or finite-dimensional Hom spaces. Some authors include additivity in their convention for “linear category”; here it is a separate condition.

For example, a unital \(k\)-algebra gives a one-object \(k\)-linear category with composition given by multiplication. It need not have a zero object. The category of finite-dimensional vector spaces has all these additional additive structures.

## Compatibility with a tensor product

When a \(k\)-linear category is also [[algebra-category-theory/monoidal-category|monoidal]], compatibility requires the map on arrows \((f,g)\mapsto f\otimes g\) to be \(k\)-bilinear. Linearity of composition alone does not impose that compatibility. It is included in the definition of a [[algebra-category-theory/fusion-category|fusion category]].

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §1.2; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
