+++
id = "fiber-bundles/bogomolny-monopole-equation"
title = "Bogomolny monopole equation"
kind = "definition"
summary = "A first-order gauge equation equating the curvature of a connection on a three-manifold with the Hodge dual of the covariant derivative of a Higgs field."
aliases = ["Bogomolny equation", "magnetic monopole equation"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(P\to Y\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over an oriented Riemannian three-manifold. A **Bogomolny monopole** is a pair \((A,\Phi)\) consisting of a [[fiber-bundles/principal-connection|connection]] \(A\) and a Higgs field \(\Phi\in\Omega^0(Y;\operatorname{ad}P)\) satisfying the **Bogomolny monopole equation**
\[
F_A=*d_A\Phi.
\]
Here \(F_A\in\Omega^2(Y;\operatorname{ad}P)\) is the [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]], \(d_A\Phi\) is the covariant derivative, and \(*:\Omega^1(Y)\to\Omega^2(Y)\) is the [[differential-geometry/hodge-star-operator|Hodge star]]. The equation is imposed modulo [[fiber-bundles/gauge-transformation|gauge transformations]] acting simultaneously on \(A\) and \(\Phi\).

## Energy decomposition

On a compact domain, or under decay conditions making every integral finite, the Yang–Mills–Higgs energy satisfies
\[
\frac12\int_Y\left(|F_A|^2+|d_A\Phi|^2\right)
=
\frac12\int_Y|F_A-*d_A\Phi|^2
+\int_Y\langle F_A\wedge d_A\Phi\rangle.
\]
The final term becomes a boundary or topological charge after the [[fiber-bundles/bianchi-identity|Bianchi identity]] is used. Solutions therefore saturate the associated Bogomolny bound. This completion-of-squares argument is the origin of the first-order equation [Bogomolny, pp. 449–454](https://cds.cern.ch/record/406760).

## Dimensional reduction

Let \(X=Y\times\mathbb R\) with the product metric and consider a translation-invariant connection
\[
\widetilde A=A+\Phi\,dt.
\]
Its curvature is \(F_{\widetilde A}=F_A+d_A\Phi\wedge dt\). With compatible product-orientation conventions, one of the four-dimensional self-duality equations reduces to \(F_A=*d_A\Phi\). This explains why monopoles inherit ellipticity modulo gauge and many structural features of instantons.

## Examples and conventions

The abelian Dirac monopole satisfies the equation away from its singular point, with \(\Phi\) proportional to the reciprocal radial coordinate. Smooth finite-energy \(SU(2)\) monopoles provide the basic nonabelian examples.

**Warning.** Reversing orientation, choosing the opposite four-dimensional self-duality convention, or replacing \(\Phi\) by \(-\Phi\) changes the displayed sign. Both \(F_A=*d_A\Phi\) and \(F_A=-*d_A\Phi\) occur in the literature.

## References

1. Evgeny B. Bogomolny, “The Stability of Classical Solutions,” *Soviet Journal of Nuclear Physics* 24 (1976), 449–454. [CERN record](https://cds.cern.ch/record/406760). Relevant: the energy bound and first-order monopole equations.
2. Michael Atiyah and Nigel Hitchin, *The Geometry and Dynamics of Magnetic Monopoles*, Princeton University Press, 1988. [Publisher record](https://press.princeton.edu/books/paperback/9780691084800/the-geometry-and-dynamics-of-magnetic-monopoles). Relevant: Chapter 1, Bogomolny equations, gauge action, and dimensional reduction.
