+++
id = "differential-geometry/holomorphic-vector-bundle"
title = "Holomorphic vector bundle"
kind = "definition"
summary = "A holomorphic vector bundle is a complex vector bundle whose local trivializations have holomorphic transition functions."
aliases = ["complex analytic vector bundle"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. A **holomorphic vector bundle** of rank \(r\) over \(X\) is a [[fiber-bundles/complex-vector-bundle|complex vector bundle]] \(\pi:E\to X\) whose total space is a complex manifold and which admits [[fiber-bundles/local-trivialization|local trivializations]]
\[
\Phi_i:\pi^{-1}(U_i)\longrightarrow U_i\times\mathbb{C}^r
\]
that are fiberwise complex-linear [[differential-geometry/holomorphic-map|holomorphic maps]] with holomorphic inverses and satisfy \(\operatorname{pr}_1\Phi_i=\pi\). Equivalently, the transition maps have the form \((x,v)\mapsto(x,g_{ij}(x)v)\), where each \(g_{ij}:U_i\cap U_j\to\operatorname{GL}_r(\mathbb{C})\) is holomorphic and the cocycle identities hold.

## Holomorphic sections and morphisms

A [[differential-geometry/holomorphic-section|holomorphic section]] is a section \(s:X\to E\) that is holomorphic as a map of complex manifolds. In a holomorphic trivialization it is represented by a holomorphic map \(U_i\to\mathbb{C}^r\), and the representatives transform by \(g_{ij}\). A morphism of holomorphic vector bundles is a [[fiber-bundles/bundle-map|bundle map]] whose local matrix entries are holomorphic; an isomorphism is such a morphism with a holomorphic inverse.

## Standard constructions

Direct sums, tensor products, duals, exterior powers, and pullbacks along holomorphic maps inherit holomorphic [[fiber-bundles/transition-function|transition functions]] by applying the corresponding matrix operations. The [[fiber-bundles/tangent-bundle|tangent bundle]] of a complex manifold is holomorphic because changes of holomorphic coordinates have holomorphic Jacobian matrices. A [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]] is the rank-one case, with transition functions valued in \(\mathbb{C}^{\times}\).

## Comparison with smooth bundles

Forgetting the complex structures on the total space and transition maps gives an underlying smooth complex vector bundle. The converse is not automatic: smooth transition functions need not be holomorphic, and a fixed smooth complex bundle may support inequivalent holomorphic structures. Holomorphic local triviality is therefore extra analytic structure, not merely complex-linear fiber data.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Definition 2.2.1 and the ensuing discussion of holomorphic bundles.
