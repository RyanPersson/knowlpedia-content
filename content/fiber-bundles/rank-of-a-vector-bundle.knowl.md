+++
id = "fiber-bundles/rank-of-a-vector-bundle"
title = "Rank of a vector bundle"
kind = "knowl"
summary = "The fiber dimension of a real or complex vector bundle, which is locally constant on the base."
aliases = ["rank-of-a-vector-bundle", "Rank of a vector bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "fiber-bundles/rank-of-a-vector-bundle.md"
+++

Let \(\pi:E\to M\) be a smooth real or complex vector bundle. The **rank of \(E\) at \(x\in M\)** is
\[
\mathrm{rank}_x(E):=\dim_{\mathbb F}(E_x),
\]
where \(\mathbb F=\mathbb R\) for real bundles and \(\mathbb F=\mathbb C\) for [[fiber-bundles/complex-vector-bundle|complex vector bundles]].

Local triviality makes \(x\mapsto\operatorname{rank}_x(E)\) locally constant. If \(M\) is connected, its common value is the **rank of \(E\)**, denoted \(\operatorname{rank}(E)\).

## Examples
1. If \(\dim M=n\), then \(\operatorname{rank}(TM)=\operatorname{rank}(T^*M)=n\).

2. The trivial bundle \(M\times\mathbb F^r\to M\) has rank \(r\).

3. If \(E\) and \(F\) are bundles over the same connected base, then
   \[
   \mathrm{rank}(E\oplus F)=\mathrm{rank}(E)+\mathrm{rank}(F),\qquad
   \mathrm{rank}(E\otimes F)=\mathrm{rank}(E)\,\mathrm{rank}(F),
   \]
   where \(\oplus\) and \(\otimes\) denote the fiberwise direct sum and tensor product.
