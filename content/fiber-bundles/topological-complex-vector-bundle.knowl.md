+++
id = "fiber-bundles/topological-complex-vector-bundle"
title = "Topological complex vector bundle"
kind = "definition"
summary = "A topological bundle whose fibers are complex vector spaces and whose local trivializations are fiberwise complex linear."
aliases = ["complex topological vector bundle", "topological C-vector bundle"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/continuous-map", "topology/homeomorphism", "topology/product-topology", "linear-algebra/vector-space", "convex-analysis/image-and-kernel-linear-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a topological space and let \(r\geq 0\). A **topological complex vector bundle of rank \(r\)** over \(X\) is a topological space \(E\), a continuous surjection \(\pi:E\to X\), and a complex vector-space structure on every fiber \(E_x=\pi^{-1}(x)\), such that every \(x\in X\) has an open neighborhood \(U\) and a homeomorphism
\[
\varphi:\pi^{-1}(U)\xrightarrow{\cong} U\times\mathbb C^r
\]
with \(\operatorname{pr}_1\circ\varphi=\pi\) and such that each restricted map
\[
\varphi_x:E_x\longrightarrow\{x\}\times\mathbb C^r
\]
is a complex-linear isomorphism. The bundle has constant rank \(r\); the fibers and the transition maps are complex-linear.

A bundle map \(E\to F\) over \(X\) is continuous and restricts on each fiber to a complex-linear map. A continuous map \(f:Y\to X\) pulls \(E\) back to the fiber product
\[
f^*E=\{(y,e)\in Y\times E:f(y)=\pi(e)\}\to Y,
\]
which is again a topological complex vector bundle of rank \(r\). Pullback is the operation used in the naturality axiom for integral Chern classes.

## Direct sums

For bundles \(E\to X\) and \(F\to X\), their direct sum is the topological complex vector bundle
\[
E\oplus F=\coprod_{x\in X}(E_x\oplus_{\mathbb C}F_x)\to X.
\]
On trivializing neighborhoods for both bundles, the product trivialization identifies this with \(U\times\mathbb C^{r+s}\), using the standard complex-linear isomorphism \(\mathbb C^r\oplus\mathbb C^s\cong\mathbb C^{r+s}\). For smooth bundles on a smooth manifold this agrees with the corresponding [[fiber-bundles/direct-sum-vector-bundle|smooth direct sum]].

## Examples

The product \(X\times\mathbb C^r\to X\) is the trivial rank-\(r\) bundle. A complex line bundle is the rank-one case. The tautological line bundle \(\mathcal O(-1)\to\mathbb{CP}^n\) has fiber the line represented by a point \([z]\in\mathbb{CP}^n\), and is a basic normalization example for integral Chern classes.

## Scope

No smooth structure on \(X\) or \(E\) is part of this definition. A smooth complex vector bundle on a smooth manifold has an underlying topological complex vector bundle, but the topological definition applies to arbitrary bases.
