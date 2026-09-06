+++
id = "fiber-bundles/tangent-bundle-cocycle-from-coordinate-changes"
title = "Tangent-bundle cocycle from coordinate changes"
kind = "theorem"
summary = "Differentiating coordinate transitions produces the GL(n,R)-valued cocycle of the tangent bundle."
aliases = ["tangent bundle transition functions from an atlas", "Jacobian cocycle of a smooth atlas"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/smooth-atlas", "fiber-bundles/smooth-g-valued-cech-1-cocycle", "fiber-bundles/tangent-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\{(U_i,\varphi_i)\}\) be a [[fiber-bundles/smooth-atlas|smooth atlas]] on
an \(n\)-manifold \(M\). On \(U_i\cap U_j\), define the change from \(j\)-th
coordinate components to \(i\)-th coordinate components by

\[
A_{ij}(x)
=D(\varphi_i\circ\varphi_j^{-1})_{\varphi_j(x)}
\in\operatorname{GL}(n,\mathbb R).
\]

Then

\[
A_{ii}=I,
\qquad
A_{ji}=A_{ij}^{-1},
\qquad
A_{ik}=A_{ij}A_{jk}.
\]

Thus the Jacobians form a smooth
[[fiber-bundles/smooth-g-valued-cech-1-cocycle|
\(\operatorname{GL}(n,\mathbb R)\)-valued Čech \(1\)-cocycle]], and the vector
bundle obtained by gluing \(U_i\times\mathbb R^n\) with this cocycle is the
[[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\).

## Why the cocycle law holds

On a triple overlap,

\[
\varphi_i\circ\varphi_k^{-1}
=(\varphi_i\circ\varphi_j^{-1})
\circ(\varphi_j\circ\varphi_k^{-1}).
\]

The chain rule therefore gives \(A_{ik}=A_{ij}A_{jk}\). In this example, the
bundle cocycle is not extra arbitrary data: it is functorially derived from
the smooth atlas.

## Frame-bundle interpretation

Coordinate vector fields give local frames of \(TM\). Their
[[fiber-bundles/transition-matrix-of-a-local-frame|transition matrices]] are
the same Jacobian data, subject to the chosen direction convention. The
associated [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] is a
principal \(\operatorname{GL}(n,\mathbb R)\)-bundle.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: tangent bundles, coordinate frames, and transformation laws.
