+++
id = "differential-geometry/cobordism-category"
title = "Cobordism category"
kind = "definition"
summary = "A category whose objects are closed manifolds and whose morphisms are cobordisms composed by gluing."
aliases = ["bordism category", "category of cobordisms"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

For \(d\geq1\), the **\(d\)-dimensional cobordism category** \(\mathbf{Cob}_d\) has [[topology/closed-manifold|closed smooth manifolds]] of dimension \(d-1\) as objects. A [[algebra-category-theory/morphism|morphism]] \(M_0\to M_1\) is a diffeomorphism class, relative to the boundary, of compact \(d\)-dimensional [[differential-geometry/cobordism|cobordisms]] \(W\) equipped with boundary identifications \(\partial W\cong M_0\sqcup M_1\) and collars of those boundary components. Composition is smooth gluing along the identified common boundary, disjoint union is the symmetric monoidal product, and the cylinder represents the [[algebra-category-theory/identity-morphism|identity morphism]]. All diffeomorphisms used in the quotient must preserve the specified boundary data.

## Why collars enter

A [[differential-geometry/collar-neighborhood-theorem|collar]] identifies a neighborhood of each boundary component with a product. Product coordinates make two cobordisms glue to a [[fiber-bundles/smooth-manifold|smooth manifold]] and show that different compatible collar choices produce diffeomorphic composites. Passing to diffeomorphism classes removes the remaining choices and makes composition associative. Keeping embeddings and collars instead leads naturally to a topological category.

## Structured variants

The oriented cobordism category uses oriented objects and [[differential-geometry/oriented-cobordism|oriented cobordisms]], with incoming [[differential-geometry/boundary-orientation|boundary orientation]] reversed. Tangential structures give framed, spin, complex, and other bordism categories. One may also require maps to a fixed background space. In every case, composition is permitted only when the structure on the common boundary matches and extends across the glued manifold.

## Topological enrichment

The category used in homotopy theory often retains spaces of embedded manifolds and cobordisms rather than collapsing morphisms to diffeomorphism classes. Galatius–Madsen–Tillmann–Weiss define such a topological category and identify the weak homotopy type of its classifying space with an infinite loop space associated to a Thom spectrum. This enriched category and the ordinary quotient category encode related but different information.

## Relation to field theory

A \(d\)-dimensional topological quantum field theory in the Atiyah–Segal sense is a symmetric monoidal functor from an appropriately structured cobordism category to a category such as [[linear-algebra/vector-space|vector spaces]]. Gluing cobordisms becomes composition of [[linear-algebra/linear-map|linear maps]], while disjoint union becomes tensor product. The categorical formulation makes locality under cutting and gluing an algebraic axiom.

## References

1. Søren Galatius, Ib Madsen, Ulrike Tillmann, and Michael Weiss, “The homotopy type of the cobordism category,” *Acta Mathematica* 202 (2009), 195–239. [DOI record](https://doi.org/10.1007/s11511-009-0036-9). Relevant: §2 and the main theorem.
2. John C. Baez and James Dolan, “Higher-dimensional algebra and topological quantum field theory,” in *Category Theory*, Contemporary Mathematics 230, AMS, 1998. [DOI record](https://doi.org/10.1090/conm/230/03340). Relevant: §1, cobordisms and symmetric monoidal functors.
