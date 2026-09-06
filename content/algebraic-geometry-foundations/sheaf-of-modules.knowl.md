+++
id = "algebraic-geometry-foundations/sheaf-of-modules"
title = "Sheaf of modules"
kind = "definition"
summary = "A sheaf carrying module structures over a fixed sheaf of rings, compatibly with restriction."
aliases = ["module sheaf", "O-module sheaf", "sheaf of O-modules"]
domains = ["algebraic-geometry-foundations", "algebra-modules"]
prerequisites = ["algebraic-geometry-foundations/ringed-space", "algebra-groups/abelian-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((X,\mathcal O_X)\) be a
[[algebraic-geometry-foundations/ringed-space|ringed space]]. A **sheaf of
\(\mathcal O_X\)-modules**, or an **\(\mathcal O_X\)-module**, is a sheaf
\(\mathcal F\) such that \(\mathcal F(U)\) is an
\(\mathcal O_X(U)\)-module for every open \(U\subseteq X\), and restriction
commutes with scalar multiplication:
\[
(a s)|_V=(a|_V)(s|_V)
\qquad(V\subseteq U).
\]
Equivalently, \(\mathcal F\) is a module object over the ring object
\(\mathcal O_X\) in sheaves of [[algebra-groups/abelian-group|abelian groups]].

## Morphisms and stalks

A morphism \(\varphi:\mathcal F\to\mathcal G\) of
\(\mathcal O_X\)-modules is a morphism of sheaves whose map on every open set
is \(\mathcal O_X(U)\)-linear. It induces an
\(\mathcal O_{X,x}\)-linear map
\[
\varphi_x:\mathcal F_x\longrightarrow\mathcal G_x
\]
on every stalk. Kernels are computed sectionwise, while a cokernel is the
sheafification of the sectionwise presheaf cokernel. These constructions make
the category of \(\mathcal O_X\)-modules an [[algebra-category-theory/abelian-category|abelian category]].

## Examples

The structure sheaf \(\mathcal O_X\) is a module over itself, as is every
finite direct sum \(\mathcal O_X^{\oplus r}\). Ideals of \(\mathcal O_X\)
form subsheaves of modules. On a smooth manifold, smooth sections of a vector
bundle form a sheaf of modules over the [[differential-geometry/sheaf-of-smooth-functions|sheaf of smooth functions]].

A sheaf of modules is not merely one module with a topology attached. Its
sections and scalar rings vary over all open sets and retain gluing data that
the global module \(\mathcal F(X)\) can lose.

## References

1. The Stacks Project Authors, *The Stacks Project*. [Tag 01AG](https://stacks.math.columbia.edu/tag/01AG). Relevant: sheaves of modules on ringed spaces.
2. Robin Hartshorne, *Algebraic Geometry*, Springer, 1977. [DOI record](https://doi.org/10.1007/978-1-4757-3849-0). Relevant: Chapter II, §1, sheaves of modules.
