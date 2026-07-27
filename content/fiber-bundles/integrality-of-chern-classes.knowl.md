+++
id = "fiber-bundles/integrality-of-chern-classes"
title = "Integrality of Chern classes"
kind = "knowl"
summary = "Chern–Weil forms representing Chern classes have integral periods and come from integral cohomology classes."
aliases = ["integrality-of-chern-classes", "Integrality of Chern classes"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/integrality-of-chern-classes.md"
+++

**Theorem (integrality of Chern classes).** Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(E\to M\) be a complex vector bundle of rank \(r\), equipped with a Hermitian [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\) with [[fiber-bundles/curvature|curvature]] \(F_\nabla\).

Form the total Chern–Weil representative
\[
c(E,\nabla)\;=\;\det\!\left(I+\frac{i}{2\pi}F_\nabla\right)
\;=\;1+c_1(E,\nabla)+\cdots+c_r(E,\nabla),
\]
where each \(c_k(E,\nabla)\) is a closed differential form of degree \(2k\). Then its de Rham class is independent of \(\nabla\) and is the image of the integral Chern class
\[
c_k(E)\in H^{2k}(M;\mathbb Z)
\]
under \(H^{2k}(M;\mathbb Z)\to H^{2k}(M;\mathbb R)\cong H_{\mathrm{dR}}^{2k}(M)\).

## Periods

For every smooth singular \(2k\)-cycle \(\Sigma\) in \(M\),
\[
\int_\Sigma c_k(E,\nabla)\in\mathbb{Z}.
\]
This period condition expresses that the de Rham class comes from integral cohomology. It does not make the integral lift unique: torsion classes vanish after changing coefficients to \(\mathbb R\).

## Examples

1. **Complex line bundles over the 2-sphere.**
   For a complex line bundle \(L\to S^2\) with a Hermitian connection, the form \(c_1(L,\nabla)=\frac{i}{2\pi}F_\nabla\) satisfies
   \[
   \int_{S^2} \frac{i}{2\pi}F_\nabla \in \mathbb{Z},
   \]
   and that integer is the degree of \(L\).

2. **The tautological line bundle over complex projective space.**
   For the tautological line bundle \(\mathcal O(-1)\to\mathbb{CP}^n\), the class \(c_1(\mathcal O(-1))\) generates \(H^2(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z\).

3. **Direct sums preserve integrality.**
   If \(E=L_1\oplus\cdots\oplus L_r\) is a sum of line bundles, then
   \[
   c(E)=\prod_{j=1}^r \bigl(1+c_1(L_j)\bigr),
   \]
   so each \(c_k(E)\) is an integral cohomology class.
