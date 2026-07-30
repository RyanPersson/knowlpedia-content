+++
id = "algebra-category-theory/symmetric-monoidal-category"
title = "Symmetric monoidal category"
kind = "definition"
summary = "A monoidal category whose tensor factors can be exchanged by a coherent involutive braiding."
aliases = ["symmetric tensor category"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
+++

A **symmetric monoidal category** is a [[algebra-category-theory/monoidal-category|monoidal category]] \((\mathcal C,\otimes,\mathbb 1)\) equipped with natural isomorphisms
\[
\beta_{X,Y}:X\otimes Y\overset{\sim}{\longrightarrow}Y\otimes X
\]
such that \(\beta_{Y,X}\circ\beta_{X,Y}=\operatorname{id}_{X\otimes Y}\) and the two hexagon coherence diagrams relating \(\beta\) to the associator commute. The maps \(\beta_{X,Y}\) form the **symmetry** or **symmetric braiding**.

## Examples

For modules over a commutative ring, \(\beta(x\otimes y)=y\otimes x\). For super vector spaces the symmetry instead includes the Koszul sign:
\[
\beta(v\otimes w)=(-1)^{|v||w|}w\otimes v
\]
on homogeneous vectors. This is symmetric because applying it twice gives the identity.

## Related structures

A braided monoidal category has coherent maps \(\beta_{X,Y}\) but does not require \(\beta_{Y,X}\beta_{X,Y}\) to be the identity. Thus every symmetric monoidal category is braided, but not conversely.

## References

1. Pavel Etingof, Shlomo Gelaki, Dmitri Nikshych, and Victor Ostrik, *Tensor Categories*, American Mathematical Society, 2015. [DOI record](https://doi.org/10.1090/surv/205). Relevant: §2.1.
