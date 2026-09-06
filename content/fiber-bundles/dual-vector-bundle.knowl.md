+++
id = "fiber-bundles/dual-vector-bundle"
title = "Dual vector bundle"
kind = "knowl"
summary = "The vector bundle whose fiber over each point is the dual space of the original fiber."
aliases = ["dual-vector-bundle", "Dual vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/dual-vector-bundle.md"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/smooth-manifold", "fiber-bundles/local-trivialization", "fiber-bundles/vector-bundle-morphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] (real or complex) over a [[fiber-bundles/smooth-manifold|smooth manifold]]. The **dual vector bundle** of \(E\) is the vector bundle
\[
\pi^*:E^*\to M
\]
defined fiberwise by
\[
E_x^* := \mathrm{Hom}_{\mathbb F}(E_x,\mathbb F),
\]
with smooth structure characterized by the property that any [[fiber-bundles/local-trivialization|local trivialization]] \(E|_U\cong U\times \mathbb F^r\) induces a local trivialization
\[
E^*|_U \cong U\times (\mathbb F^r)^*
\]
via fiberwise duality.

A [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] \(\Phi:E\to F\) over \(\mathrm{id}_M\) induces a dual morphism \(\Phi^*:F^*\to E^*\) over \(\mathrm{id}_M\) by precomposition on each fiber.

## Equivalent characterizations

Equivalently, if \((e_1,\dots,e_r)\) is a local frame on \(U\), then there is a uniquely determined dual local frame \((e^1,\dots,e^r)\) of \(E^*|_U\) such that \(e^i(e_j)=\delta^i_j\) pointwise. If the original frame changes by a matrix \(A\), then the dual frame changes by \(A^{-T}\) over both \(\mathbb R\) and \(\mathbb C\). An inverse conjugate transpose belongs instead to Hermitian duality, which uses conjugate-linear functionals.

## Examples
1. **Cotangent bundle.** The [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*M\) is the dual vector bundle of the [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\).

2. **Dual of a trivial bundle.** \((M\times \mathbb F^r)^*\cong M\times (\mathbb F^r)^*\) canonically.

3. **Dual [[fiber-bundles/line-bundle|line bundle]].** If \(L\to M\) is a real or complex line bundle, then \(L^*\) is again a line bundle; fiberwise, it consists of linear functionals on \(L_x\). The tensor product \(L\otimes L^*\) has a canonical [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]] given by evaluation, so it is canonically trivial.
