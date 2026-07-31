+++
id = "differential-geometry/symmetric-monoidal-structure-on-the-cobordism-category"
title = "Symmetric monoidal structure on the cobordism category"
kind = "definition"
summary = "The symmetric monoidal structure on a cobordism category whose tensor product is disjoint union and whose unit is the empty manifold."
aliases = ["disjoint-union monoidal structure on cobordisms", "symmetric monoidal bordism category"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

On a fixed \(d\)-dimensional [[differential-geometry/cobordism-category|cobordism category]], the **symmetric monoidal structure under disjoint union** has
\[
M\otimes N=M\sqcup N,\qquad W\otimes W'=W\sqcup W',
\]
for objects \(M,N\) and [[differential-geometry/cobordism|cobordisms]] \(W,W'\). Its monoidal unit is the empty \((d-1)\)-manifold. The associator, left and right unitors, and symmetry are the morphisms induced by the canonical diffeomorphisms among iterated [[differential-geometry/disjoint-union-of-smooth-manifolds|disjoint unions]]. These maps respect boundary identifications and collars, so tensoring is compatible with gluing. In a model formed from diffeomorphism classes, the coherence maps may be represented by canonical identifications or made strict after choosing a strictified model.

## Compatibility with composition

If \(W_{01}:M_0\to M_1\) and \(W_{12}:M_1\to M_2\), and similarly \(W'_{01}\) and \(W'_{12}\), then gluing is componentwise:
\[
(W_{12}\circ W_{01})\sqcup(W'_{12}\circ W'_{01})
\cong
(W_{12}\sqcup W'_{12})\circ(W_{01}\sqcup W'_{01}).
\]
Thus disjoint union defines a bifunctor and satisfies the interchange law with categorical composition. The empty cobordism components supply the unit compatibility. This is the ordinary categorical shadow of the symmetric monoidal bordism categories used for extended field theories [Lurie, §1.1 and §2.2].

## Structured variants

The same construction works for oriented, framed, spin, or otherwise tangentially structured cobordisms: each component carries its given structure, and the disjoint union carries them componentwise. The symmetry exchanges whole components together with their structures. A proposed tensor product that joins components by connected sum is not this monoidal structure: connected sum is not defined for arbitrary objects and cobordisms with the required functoriality.

## Role in field theory

A topological quantum field theory is required to be symmetric monoidal so that disjoint geometric systems are sent to tensor products in the target category. Consequently, the empty manifold is sent to the target unit, and a disjoint union \(M\sqcup N\) is sent coherently to \(Z(M)\otimes Z(N)\). This is precisely why disjoint union, rather than a geometric operation involving interaction between components, is the tensor product in the bordism source [Baez–Dolan, §1].

## References

1. Jacob Lurie, “On the Classification of Topological Field Theories,” 2009. [arXiv record](https://arxiv.org/abs/0905.0465). Relevant: §1.1, classical field theories, and §2.2, bordism categories.
2. John C. Baez and James Dolan, “Higher-dimensional algebra and topological quantum field theory,” in *Category Theory*, Contemporary Mathematics 230, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/conm/230/03340). Relevant: §1, cobordisms and symmetric monoidal functors.
