+++
id = "fiber-bundles/integral-chern-classes"
title = "Integral Chern classes"
kind = "definition"
summary = "The canonical integral characteristic classes of finite-rank complex vector bundles, characterized by the standard normalization and axioms."
aliases = ["integral Chern class", "topological Chern classes"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/topological-complex-vector-bundle", "topology/cup-product-and-cohomology-ring", "fiber-bundles/paracompact-topological-space", "topology/singular-cohomology-group", "differential-geometry/complex-projective-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to X\) be a finite-rank complex [[fiber-bundles/topological-complex-vector-bundle|vector bundle]] over a paracompact Hausdorff space \(X\). Its **integral Chern classes** are the canonical classes
\[
c_k(E)\in H^{2k}(X;\mathbb Z),\qquad k\geq 0,
\]
depending only on the bundle isomorphism class, and characterized as a family over all such bases and bundles by all of the following axioms:

1. **Naturality.** For every continuous map \(f:Y\to X\) with \(Y\) paracompact Hausdorff,
   \[
   c_k(f^*E)=f^*c_k(E).
   \]
2. **Normalization.** \(c_0(E)=1\), and \(c_k(E)=0\) for \(k>\operatorname{rank}_{\mathbb C}E\).
3. **Whitney sum.** For direct sums,
   \[
   c(E\oplus F)=c(E)\smile c(F),\qquad c(E)=1+c_1(E)+c_2(E)+\cdots,
   \]
   with the cup product in integral cohomology.
4. **Line-bundle normalization.** If \(L=\mathcal O(-1)\) is the tautological complex line bundle over \(\mathbb{CP}^{1}\), then
   \[
   c_1(L)=-u,
   \]
   where \(u\in H^2(\mathbb{CP}^{1};\mathbb Z)\) is the positive generator determined by the complex orientation.

These axioms define a stable family: the same class \(c_k(E)\) is used after adding trivial summands, and the Whitney identity determines the components of a direct sum from those of its factors.

## Universal construction and uniqueness

For each rank \(n\), the universal rank-\(n\) bundle over the [[fiber-bundles/classifying-space-bg|classifying space]] \(BU(n)\) has universal classes
\[
c_k\in H^{2k}(BU(n);\mathbb Z).
\]
For a classifying map \(f:X\to BU(n)\), one has \(c_k(E)=f^*c_k\). The classifying-space construction proves existence and uniqueness for paracompact bases because classifying maps are unique up to homotopy. Equivalently, after pulling \(E\) back to a complete flag bundle, the splitting principle writes it as a sum of line bundles; the normalization and the direct-sum axiom then give the elementary symmetric expressions in the line-bundle first classes, and injectivity of the flag-bundle pullback proves uniqueness downstairs.

## Relation to Chern–Weil forms

If \(X\) is a smooth manifold and \(E\) has a Hermitian connection with curvature \(F\), the real image of \(c_k(E)\) is represented by the degree-\(2k\) component of
\[
\det\!\left(I+\frac{i}{2\pi}F\right).
\]
The differential form fixes the image in real cohomology; it does not determine a possible torsion component of the integral class. The sign in the tautological-line normalization agrees with this convention: the tautological bundle has \(c_1(\mathcal O(-1))=-u\).

## Examples

For a trivial rank-\(n\) bundle, \(c(E)=1\). For a sum of line bundles \(L_1\oplus\cdots\oplus L_n\),
\[
c(E)=\prod_{j=1}^{n}\bigl(1+c_1(L_j)\bigr).
\]
Thus \(c_k(E)\) is the \(k\)th elementary symmetric polynomial in the first Chern classes of the summands.

## References

1. Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2 (2017), Chapter 3, §3.1, “Stiefel-Whitney and Chern Classes,” pp. 77–84. [Author's PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf).
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974, Chapter 14. [DOI record](https://doi.org/10.1515/9781400881826).
