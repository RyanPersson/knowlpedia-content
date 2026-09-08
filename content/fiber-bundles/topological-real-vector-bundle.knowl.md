+++
id = "fiber-bundles/topological-real-vector-bundle"
title = "Topological real vector bundle"
kind = "definition"
summary = "A topological bundle whose fibers are real vector spaces and whose local trivializations are fiberwise real linear."
aliases = ["real topological vector bundle", "topological R-vector bundle"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/continuous-map", "topology/homeomorphism", "topology/product-topology", "linear-algebra/vector-space", "convex-analysis/image-and-kernel-linear-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a topological space and let \(r\ge 0\) be an integer. A **topological real vector bundle of rank \(r\)** over \(X\) is a topological space \(E\), a continuous surjection \(\pi:E\to X\), and a real vector-space structure on every fiber \(E_x=\pi^{-1}(x)\), such that every \(x\in X\) has an open neighborhood \(U\) and a homeomorphism

\[
\varphi:\pi^{-1}(U)\xrightarrow{\cong} U\times\mathbb R^r
\]

with \(\operatorname{pr}_1\circ\varphi=\pi\) and such that each restricted map

\[
\varphi_x:E_x\longrightarrow\{x\}\times\mathbb R^r
\]

is a real-linear isomorphism. The bundle has constant rank \(r\); its fibers are real vector spaces and its transition maps are real-linear. No smooth structure on \(X\) or \(E\) is part of this definition.

## Bundle maps and pullbacks

A bundle map \(E\to F\) over \(X\) is continuous and restricts on each fiber to a real-linear map. A continuous map \(f:Y\to X\) pulls \(E\) back to the fiber product

\[
f^*E=\{(y,e)\in Y\times E:f(y)=\pi(e)\}\longrightarrow Y,
\]

which is again a topological real vector bundle of rank \(r\).

## Examples

The product \(X\times\mathbb R^r\to X\) is the trivial rank-\(r\) bundle. A real line bundle is the rank-one case. The Möbius bundle is a nontrivial real line bundle over the circle. A smooth real vector bundle on a smooth manifold has an underlying topological real vector bundle.


## Direct sums and complexification

For two bundles on the same base, \((E\oplus F)_x=E_x\oplus F_x\). Simultaneous local trivializations give charts \((E\oplus F)|_U\cong U\times\mathbb R^{r+s}\), which define its topology. The complexification has fibers \(E_x\otimes_{\mathbb R}\mathbb C\); its charts use the same real transition matrices regarded as complex matrices. Thus \(E^{\mathbb C}\) is a topological complex vector bundle of complex rank \(r\).
