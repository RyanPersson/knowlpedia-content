+++
id = "fiber-bundles/chern-class"
title = "Chern class via Chern–Weil theory"
kind = "knowl"
summary = "Characteristic cohomology classes of a complex vector bundle defined from curvature using invariant polynomials."
aliases = ["chern-class", "Chern class via Chern–Weil theory"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/chern-class.md"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], and let \(E\to M\) be a rank-\(n\) complex vector bundle with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\). If \(F_\nabla\in\Omega^2(M;\operatorname{End}(E))\) is its [[fiber-bundles/curvature|curvature]], the **total Chern form** is
\[
c(\nabla)\;:=\;\det\!\Big(I+\frac{i}{2\pi}F_\nabla\Big)\;\in\;\Omega^{\mathrm{even}}(M),
\]
where the determinant is computed in local frames. Its homogeneous components are
\[
c(\nabla)=1+c_1(\nabla)+\cdots+c_n(\nabla),
\qquad c_k(\nabla)\in\Omega^{2k}(M).
\]
Each \(c_k(\nabla)\) is closed, and its de Rham class is independent of \(\nabla\). The **\(k\)th Chern class** is the canonical class \(c_k(E)\in H^{2k}(M;\mathbb Z)\); its image under
\[
H^{2k}(M;\mathbb Z)\longrightarrow H^{2k}(M;\mathbb R)\cong H^{2k}_{\mathrm{dR}}(M)
\]
is \([c_k(\nabla)]\). The Chern–Weil form determines this real image, but by itself need not detect torsion in integral cohomology.

Equivalently, \(c_k(E)\) is the characteristic class obtained by the Chern–Weil construction for the structure group \(U(n)\) of a Hermitian bundle (or the corresponding [[fiber-bundles/principal-g-bundle|principal bundle]] of unitary frames) using the invariant polynomial given by the \(k\)th elementary symmetric function of eigenvalues.

The Chern classes are natural under pullback: for any [[fiber-bundles/smooth-map|smooth map]] \(f:N\to M\),
\[
c_k(f^*E)=f^*c_k(E)\in H^{2k}(N;\mathbb Z).
\]

## Examples
1. **Trivial bundle.** If \(E\cong M\times\mathbb C^n\) admits the flat connection (\(F_\nabla=0\)), then \(c(\nabla)=1\) and hence \(c_k(E)=0\) for all \(k\ge 1\).

2. **Complex line bundle.** If \(\mathrm{rank}_{\mathbb C}E=1\), then
   \[
   c(\nabla)=1+\frac{i}{2\pi}F_\nabla,
   \]
   so \(c_1(E)\) is represented in de Rham cohomology by the real 2-form \(\frac{i}{2\pi}F_\nabla\).

3. **Whitney sum behavior (curvature-level).** If \(E=E_1\oplus E_2\) with a block-diagonal connection \(\nabla=\nabla_1\oplus\nabla_2\), then \(F_\nabla\) is block-diagonal and
   \[
   c(\nabla)=c(\nabla_1)\wedge c(\nabla_2),
   \]
   recovering the usual multiplicativity of total Chern classes under direct sum.
