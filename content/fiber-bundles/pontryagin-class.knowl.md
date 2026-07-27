+++
id = "fiber-bundles/pontryagin-class"
title = "Pontryagin class via Chern–Weil theory"
kind = "knowl"
summary = "Characteristic cohomology classes of a real vector bundle defined from curvature, using the complexification in Chern–Weil theory."
aliases = ["pontryagin-class", "Pontryagin class via Chern–Weil theory"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/pontryagin-class.md"
+++

Let \(E\to M\) be a real vector bundle. Its \(k\)-th **Pontryagin class** is
\[
p_k(E):=(-1)^k c_{2k}(E\otimes_{\mathbb R}\mathbb C)
\in H^{4k}(M;\mathbb Z).
\]
Here \(c_{2k}\) is the \((2k)\)-th [[fiber-bundles/chern-class|Chern class]].

If \(E\) has a metric-compatible [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\), Chern–Weil theory produces a closed form \(p_k(\nabla)\in\Omega^{4k}(M)\). Its de Rham class is the real image of \(p_k(E)\) and is independent of \(\nabla\).

## Properties

For every [[fiber-bundles/smooth-map|smooth map]] \(f:N\to M\),
\[
p_k(f^*E)=f^*p_k(E).
\]

The de Rham representative detects only the real image of the integral class, not its torsion.

## Examples
1. **Trivial bundle / flat connection.** If \(E\cong M\times\mathbb R^r\) with the flat connection, then \(F_\nabla=0\), hence \(p_k(\nabla)=0\) for all \(k\ge 1\), and thus \(p_k(E)=0\).

2. **Underlying real bundle of a complex line bundle.** Let \(L\to M\) be a complex line bundle with \(c_1(L)=x\in H^2(M;\mathbb Z)\). For the underlying real rank-2 bundle \(L_{\mathbb R}\) one has
   \[
   p_1(L_{\mathbb R})=x^2\in H^4(M;\mathbb Z),
   \]
   because \(p_1=(-1)c_2\big((L_{\mathbb R})^{\mathbb C}\big)\) and \((L_{\mathbb R})^{\mathbb C}\cong L\oplus \overline{L}\).

3. **Dimensional vanishing.** If \(\dim M < 4k\), then every \(4k\)-form vanishes and hence \(p_k(E)=0\) in de Rham cohomology (and therefore in rational cohomology) for degree reasons.
