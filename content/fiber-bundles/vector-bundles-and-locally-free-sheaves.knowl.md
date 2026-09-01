+++
id = "fiber-bundles/vector-bundles-and-locally-free-sheaves"
title = "Vector bundles and locally free sheaves"
kind = "theorem"
summary = "Taking local smooth sections is an equivalence from fixed-base vector bundles to finite-rank locally free smooth-module sheaves."
aliases = ["sheaf-bundle equivalence", "vector bundles as locally free sheaves", "smooth locally free sheaf theorem"]
domains = ["fiber-bundles", "differential-geometry", "algebraic-geometry-foundations"]
prerequisites = ["algebra-category-theory/equivalence-of-categories", "fiber-bundles/category-of-vector-bundles-over-a-manifold", "algebraic-geometry-foundations/locally-free-sheaf", "topology/connected-component"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a smooth manifold and
\(\mathbb F\in\{\mathbb R,\mathbb C\}\). Taking local smooth sections defines
an [[algebra-category-theory/equivalence-of-categories|equivalence of categories]]
\[
\mathbf{Vect}_{\mathbb F}(M)
\;\simeq\;
\mathbf{LocFree}\bigl(C^\infty_M(\mathbb F)\bigr),
\qquad
E\longmapsto\Gamma^\infty(-,E).
\]
The source is the
[[fiber-bundles/category-of-vector-bundles-over-a-manifold|fixed-base
category of finite-rank vector bundles]], and the target consists of
[[algebraic-geometry-foundations/locally-free-sheaf|locally free sheaves]]
of \(C^\infty_M(\mathbb F)\)-modules whose rank is finite and locally
constant. Neither side requires that rank to be globally bounded across the
[[topology/connected-component|connected components]] of \(M\). On morphisms, a bundle map over
\(\operatorname{id}_M\) acts on local sections by postcomposition.

## Reconstruction from a sheaf

Choose local isomorphisms
\(\mathcal E|_{U_i}\cong
(C^\infty_M(\mathbb F)|_{U_i})^{r}\). On overlaps, changes of
frame are smooth maps
\[
g_{ij}:U_i\cap U_j\longrightarrow GL_r(\mathbb F)
\]
satisfying the cocycle identities. Gluing the trivial bundles
\(U_i\times\mathbb F^r\) with these [[fiber-bundles/transition-function|transition functions]] produces a smooth
vector bundle \(E\to M\). Its [[fiber-bundles/sheaf-of-smooth-sections|section sheaf]] is naturally isomorphic to
\(\mathcal E\).

Likewise, a morphism of locally free sheaves is locally a matrix of smooth
functions. These matrices glue to a unique [[fiber-bundles/bundle-morphism|bundle morphism]] over
\(\operatorname{id}_M\), proving full faithfulness.

## No compactness requirement

This equivalence is local and requires no compactness hypothesis. The
[[fiber-bundles/serre-swan-theorem|global smooth Serre–Swan theorem]] over
\(C^\infty(M,\mathbb F)\) likewise needs no compactness when \(M\) is a
finite-dimensional Hausdorff second-countable manifold; its finite generation
uses a finite-dimensional vector-bundle embedding theorem rather than only
local freeness.

The two statements must therefore be separated:

- every finite-rank bundle has a finite-rank locally free **section sheaf**
  on any smooth manifold, with no global bound on ranks across components;
- for connected \(M\), its **global section module** is finitely generated
  projective; on disconnected \(M\), the same holds when the componentwise
  ranks are globally bounded.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: vector bundles, transition functions, and bundle maps.
2. Glen E. Bredon, *Sheaf Theory*, 2nd ed., Springer, 1997. [DOI record](https://doi.org/10.1007/978-1-4612-0647-7). Relevant: sheaves of modules and locally free sheaves.
