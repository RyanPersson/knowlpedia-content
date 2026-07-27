+++
id = "fiber-bundles/dual-vector-bundle"
title = "Dual vector bundle"
kind = "knowl"
summary = "The vector bundle whose fiber at each point is the linear dual of the original fiber."
aliases = ["dual-vector-bundle", "Dual vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/dual-vector-bundle.md"
+++

Let \(\pi:E\to M\) be a smooth vector bundle of rank \(r\) over \(\mathbb F=\mathbb R\) or \(\mathbb C\). The **dual vector bundle** of \(E\) is the vector bundle
\[
\pi_{E^*}:E^*\to M
\]
defined fiberwise by
\[
E_x^* := \mathrm{Hom}_{\mathbb F}(E_x,\mathbb F),
\]
whose smooth structure is characterized by requiring each local trivialization \(E|_U\cong U\times\mathbb F^r\) to induce
\[
E^*|_U \cong U\times (\mathbb F^r)^*
\]
via fiberwise duality.

A [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] \(\Phi:E\to F\) over \(\mathrm{id}_M\) induces a dual morphism \(\Phi^*:F^*\to E^*\) by precomposition on each fiber.

## Equivalent characterizations

If \((e_1,\dots,e_r)\) is a local frame on \(U\), the dual local frame \((e^1,\dots,e^r)\) is determined by \(e^i(e_j)=\delta^i_j\). Under a change of frame by a matrix \(A\), the dual frame changes by \(A^{-T}\), over both \(\mathbb R\) and \(\mathbb C\). A conjugate transpose belongs instead to Hermitian duality, which uses conjugate-linear functionals.

## Examples
1. **Cotangent bundle.** The [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*M\) is the dual vector bundle of the [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\).

2. **Dual of a trivial bundle.** \((M\times \mathbb F^r)^*\cong M\times (\mathbb F^r)^*\) canonically.

3. **Dual line bundle.** If \(L\to M\) is a real or complex line bundle, then \(L^*\) is again a line bundle; fiberwise, it consists of linear functionals on \(L_x\). The tensor product \(L\otimes L^*\) has a canonical nowhere-zero section given by evaluation, so it is canonically trivial.
