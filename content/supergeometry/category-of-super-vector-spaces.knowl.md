+++
id = "supergeometry/category-of-super-vector-spaces"
title = "Category of super vector spaces"
kind = "definition"
summary = "The symmetric monoidal category of Z/2-graded vector spaces and even linear maps."
aliases = ["SuperVect", "category of Z/2-graded vector spaces"]
domains = ["supergeometry", "algebra-category-theory"]
prerequisites = ["supergeometry/super-vector-space", "algebra-category-theory/symmetric-monoidal-category", "supergeometry/koszul-sign-rule"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic different from \(2\). The **category of
super vector spaces** \(\mathbf{SuperVect}_k\) has
[[supergeometry/super-vector-space|super vector spaces]] as objects and even
linear maps as morphisms. Its tensor product is graded by
\[
(V\otimes W)_{\bar r}
=\bigoplus_{\bar i+\bar j=\bar r}V_{\bar i}\otimes W_{\bar j},
\]
and its symmetry is the **Koszul braiding**
\[
\tau_{V,W}(v\otimes w)=(-1)^{|v||w|}w\otimes v
\]
for homogeneous \(v,w\). With this tensor product, unit \(k\) in even degree,
and braiding, \(\mathbf{SuperVect}_k\) is a
[[algebra-category-theory/symmetric-monoidal-category|symmetric monoidal
category]]. The signs forced by this braiding are recorded in the
[[supergeometry/koszul-sign-rule|Koszul sign rule]].

## Odd maps

Only even maps are ordinary morphisms in \(\mathbf{SuperVect}_k\). The internal
mapping object, which includes both even and odd maps, is the
[[supergeometry/super-internal-hom|super internal Hom]]. The
[[supergeometry/parity-shift|parity shift]] turns an odd map into an even map
to or from a shifted object.

## Why the morphism convention matters

Allowing all homogeneous maps as ungraded morphisms does not produce the
ordinary symmetric monoidal category used to define
[[supergeometry/superalgebra|superalgebras]]: composition and tensoring must
retain degrees and Koszul signs. Keeping even maps as the categorical
morphisms and all degrees in the internal Hom makes those roles explicit.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph
   Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*,
   Volume 1, American Mathematical Society, 1999, pp. 41–97. Relevant:
   Sections 1–2.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of
   Supersymmetry*, European Mathematical Society, 2011. [DOI
   record](https://doi.org/10.4171/097). Relevant: Chapter 1.
