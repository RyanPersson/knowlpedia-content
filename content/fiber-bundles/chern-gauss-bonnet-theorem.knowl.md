+++
id = "fiber-bundles/chern-gauss-bonnet-theorem"
title = "Chern–Gauss–Bonnet theorem"
kind = "theorem"
summary = "The integral of the Euler curvature form of a closed oriented even-dimensional Riemannian manifold equals its Euler characteristic."
aliases = ["Gauss–Bonnet–Chern theorem", "generalized Gauss–Bonnet theorem"]
domains = ["fiber-bundles", "differential-geometry", "topology"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/levicivita-connection-connection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a closed oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] of dimension \(2m\), and let \(\Omega\) be the curvature matrix of its [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] in a local oriented orthonormal frame. With the Chern–Weil normalization
\[
e(TM,\nabla^{\mathrm{LC}})=\operatorname{Pf}\!\left(\frac{\Omega}{2\pi}\right),
\]
the **Chern–Gauss–Bonnet theorem** states
\[
\int_M e(TM,\nabla^{\mathrm{LC}})
=\left\langle e(TM),[M]\right\rangle
=\chi(M).
\]
Thus the integral of this metric-dependent curvature form is the topological Euler characteristic of \(M\).
The middle expression uses the topological Euler class and the chosen
orientation.

## Why the equality is topological

The Pfaffian is an invariant polynomial on the even-dimensional [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebra]]. Chern–Weil theory therefore makes the displayed Euler form closed and identifies its de Rham class with the [[fiber-bundles/euler-class|Euler class]] of \(TM\). Evaluation on the [[topology/fundamental-class|fundamental class]] is independent of the metric and connection. The remaining equality with \(\chi(M)\) is the topological characterization of the Euler number.

Chern’s intrinsic proof transgresses the Euler form to the unit tangent
[[fiber-bundles/sphere-bundle|sphere bundle]] and applies Stokes’s theorem
around the isolated zeros of a [[fiber-bundles/vector-field|vector field]];
their local indices sum to the Euler characteristic.

## Surface case

For an oriented closed Riemannian surface, the curvature matrix has Pfaffian \(K\,dA\), where \(K\) is Gaussian curvature. The theorem becomes the classical formula
\[
\frac{1}{2\pi}\int_M K\,dA=\chi(M).
\]
For the round \(2\)-sphere, \(K=1\) and the area is \(4\pi\), so the integral gives \(2=\chi(S^2)\).

## Conventions and scope

**Warning.** The sign in a local Pfaffian formula depends on the curvature-matrix convention, while the normalized Euler form must represent the chosen oriented Euler class. Stating both conventions prevents a spurious sign change.

Closedness is essential to the displayed formula. A
[[differential-geometry/manifold-with-boundary|manifold with boundary]]
requires a boundary transgression term. In odd dimensions the Pfaffian
expression above is not present; a closed odd-dimensional manifold has Euler
characteristic zero.

## References

1. Shiing-Shen Chern, “A Simple Intrinsic Proof of the Gauss–Bonnet Formula for Closed Riemannian Manifolds,” *Annals of Mathematics* 45 (1944), 747–752. [DOI record](https://doi.org/10.2307/1969302). Relevant: §§1–3, construction of the intrinsic form and proof of the integral formula.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: chapter 11, Euler forms and Chern–Weil theory.
