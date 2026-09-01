+++
id = "differential-geometry/smooth-maps-from-smooth-function-algebras"
title = "Full faithfulness of the smooth-function functor"
kind = "theorem"
summary = "Pullback identifies smooth maps with C-infinity-ring morphisms in the opposite direction."
aliases = ["smooth maps from smooth-function algebras", "full faithfulness of smooth functions", "reconstruction of smooth maps from C-infinity rings", "C∞ functor is fully faithful"]
domains = ["differential-geometry", "category-theory"]
prerequisites = ["fiber-bundles/smooth-manifold", "algebra-category-theory/opposite-category", "differential-geometry/category-of-smooth-manifolds", "algebra-category-theory/contravariant-functor"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For finite-dimensional Hausdorff second-countable [[fiber-bundles/smooth-manifold|smooth manifolds]] \(M,N\),
pullback gives a natural bijection
\[
\operatorname{Hom}_{\mathbf{Man}}(M,N)
\;\cong\;
\operatorname{Hom}_{C^\infty\mathbf{Ring}}
\bigl(C^\infty(N),C^\infty(M)\bigr),
\qquad F\longmapsto F^*.
\]
Thus the assignment
\[
C^\infty(-):
\mathbf{Man}^{\mathrm{op}}
\longrightarrow C^\infty\mathbf{Ring}
\]
is a covariant fully faithful functor from the
[[algebra-category-theory/opposite-category|opposite category]] of the
[[differential-geometry/category-of-smooth-manifolds|smooth-manifold
category]]. Equivalently, \(M\mapsto C^\infty(M)\) is a fully faithful
[[algebra-category-theory/contravariant-functor|contravariant functor]] on
\(\mathbf{Man}\). One should not call the displayed functor on
\(\mathbf{Man}^{\mathrm{op}}\) itself contravariant.

## Why a homomorphism determines a map

For each \(x\in M\), composing a \(C^\infty\)-ring morphism
\(\varphi:C^\infty(N)\to C^\infty(M)\) with evaluation at \(x\) gives a
character \(C^\infty(N)\to\mathbb R\). Such characters are evaluations at
unique points of \(N\). Writing that point as \(F(x)\) defines a set map
\(F:M\to N\). In local coordinates, the coordinate functions pull back to
smooth functions, which proves that \(F\) is smooth and
\(\varphi=F^*\).

## Essential image and limitations

The theorem is full faithfulness, not an equivalence with all
[[differential-geometry/c-infinity-ring|\(C^\infty\)-rings]]. Its essential
image consists precisely of those \(C^\infty\)-rings isomorphic to
\(C^\infty(M)\) for manifolds \(M\). Quotients with singular or infinitesimal
behavior generally lie outside that image.

## References

1. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: “Algebras and Points,” “Smooth Manifolds,” and “Smooth Maps.”
2. Ieke Moerdijk and Gonzalo E. Reyes, *Models for Smooth Infinitesimal Analysis*, Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4757-4148-6). Relevant: Chapter I, \(C^\infty\)-rings and smooth loci.
