+++
id = "fiber-bundles/chern-class"
title = "Chern class via Chern–Weil theory"
kind = "knowl"
summary = "Characteristic cohomology classes of a complex vector bundle defined from curvature using invariant polynomials."
aliases = ["chern-class", "Chern class via Chern–Weil theory"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/chern-class.md"
prerequisites = ["fiber-bundles/complex-vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/curvature-of-a-vector-bundle-connection", "linear-algebra/determinant", "fiber-bundles/wedge-product-of-differential-forms", "fiber-bundles/de-rham-cohomology-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 2
+++

Let \(E\to M\) be a smooth [[fiber-bundles/complex-vector-bundle|complex vector bundle]] of rank \(n\), with a complex-linear [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\) and [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature]] \(F_\nabla\). Its **total Chern form** is
\[
c(\nabla)=\det\!\left(I+\frac{i}{2\pi}F_\nabla\right)
=1+c_1(\nabla)+\cdots+c_n(\nabla),
\qquad c_k(\nabla)\in\Omega^{2k}(M;\mathbb C).
\]
Here the [[linear-algebra/determinant|determinant]] uses its usual permutation formula, with multiplication replaced by the [[fiber-bundles/wedge-product-of-differential-forms|wedge product]] of forms. The even-degree entries commute, so this formula is well defined and invariant under changes of frame. Complex forms mean forms \(\alpha+i\beta\) with real forms \(\alpha,\beta\), with exterior derivative extended complex-linearly.

The forms \(c_k(\nabla)\) are closed and their [[fiber-bundles/de-rham-cohomology-group|de Rham classes]] are independent of \(\nabla\). The **Chern–Weil Chern class** is this class
\[
c_k^{\mathrm{dR}}(E)=[c_k(\nabla)]\in H^{2k}_{\mathrm{dR}}(M;\mathbb C).
\]
It lies in the image of real de Rham cohomology: choosing a Hermitian metric and a compatible connection gives real Chern forms representing the same class. For an arbitrary complex connection the forms themselves need not be real. Set \(c_0^{\mathrm{dR}}=1\) and \(c_k^{\mathrm{dR}}=0\) for \(k>n\).

## Integral classes and naturality

The [[fiber-bundles/integral-chern-classes|integral Chern classes]] \(c_k(E)\in H^{2k}(M;\mathbb Z)\) are defined topologically by naturality, the Whitney sum axiom, rank normalization, and the tautological-line normalization. Their images in complex cohomology, identified with de Rham cohomology, are \(c_k^{\mathrm{dR}}(E)\). Curvature alone does not define the integral classes, since change of coefficients can lose integral information, including torsion.

For any smooth map \(f:N\to M\),
\[
c_k^{\mathrm{dR}}(f^*E)=f^*c_k^{\mathrm{dR}}(E).
\]
The integral classes satisfy the corresponding integral naturality identity.

## Examples
1. **Trivial bundle.** If \(E\cong M\times\mathbb C^n\) admits the flat connection (\(F_\nabla=0\)), then \(c(\nabla)=1\) and hence \(c_k(E)=0\) for all \(k\ge 1\).

2. **[[fiber-bundles/line-bundle|Complex line bundle]].** If \(\mathrm{rank}_{\mathbb C}E=1\), then
   \[
   c(\nabla)=1+\frac{i}{2\pi}F_\nabla,
   \]
   so \(c_1(E)\) is represented in de Rham cohomology by the complex 2-form \(\frac{i}{2\pi}F_\nabla\), which is real when the connection is Hermitian.

3. **Whitney sum behavior (curvature-level).** If \(E=E_1\oplus E_2\) with a block-diagonal connection \(\nabla=\nabla_1\oplus\nabla_2\), then \(F_\nabla\) is block-diagonal and
   \[
   c(\nabla)=c(\nabla_1)\wedge c(\nabla_2),
   \]
   recovering the usual multiplicativity of total Chern classes under direct sum.
