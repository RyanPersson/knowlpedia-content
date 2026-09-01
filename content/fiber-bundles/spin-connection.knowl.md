+++
id = "fiber-bundles/spin-connection"
title = "Spin connection"
kind = "definition"
summary = "The lift of the Levi–Civita connection from the oriented orthonormal frame bundle to a chosen spin structure."
aliases = ["lifted Levi–Civita connection", "connection on a spin bundle"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/spin-structure", "fiber-bundles/principal-connection", "fiber-bundles/levicivita-connection-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented [[differential-geometry/riemannian-manifold|Riemannian \(n\)-manifold]] with [[fiber-bundles/spin-structure|spin structure]] \(\Phi:P_{\mathrm{Spin}}\to P_{\mathrm{SO}}\), and let \(\lambda:\mathrm{Spin}(n)\to\mathrm{SO}(n)\) be the double covering. The **spin connection** is the unique [[fiber-bundles/principal-connection|principal connection]] \(\widetilde\omega\) on \(P_{\mathrm{Spin}}\) satisfying
\[
d\lambda\circ\widetilde\omega=\Phi^*\omega_{\mathrm{LC}},
\]
where \(\omega_{\mathrm{LC}}\) is the [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] on \(P_{\mathrm{SO}}\). Since \(d\lambda:\mathfrak{spin}(n)\to\mathfrak{so}(n)\) is an isomorphism, this equation both defines the lift and proves its uniqueness. Thus the spin connection depends on the metric and the chosen spin structure.

## Associated covariant derivative

For a complex spin representation \(\Delta_n\), the spin connection induces a [[fiber-bundles/covariant-derivative-of-a-section|covariant derivative]] \(\nabla^S\) on the associated [[differential-geometry/spinor-bundle|spinor bundle]] \(S=P_{\mathrm{Spin}}\times_{\mathrm{Spin}(n)}\Delta_n\). It is compatible with the spinor metric and [[differential-geometry/clifford-module|Clifford multiplication]]:
\[
\nabla^S_X(Y\mathbin{\cdot}\psi)
=(\nabla_XY)\mathbin{\cdot}\psi+Y\mathbin{\cdot}\nabla^S_X\psi.
\]
This compatibility is the bridge from Riemannian parallel transport to the [[noncommutative-geometry/dirac-operator|Dirac operator]].

## Curvature and local form

The curvature of \(\widetilde\omega\) maps under \(d\lambda\) to the pullback of the Riemannian curvature form. In a local oriented orthonormal frame, if \(\omega_{ij}\) are the Levi–Civita connection one-forms, then the induced spinor derivative has the familiar form
\[
\nabla^S=d+\frac14\sum_{i,j}\omega_{ij}\,e_i\mathbin{\cdot}e_j.
\]
The factor depends on summation conventions, but the invariant lifting equation in the core does not.

## Examples and conventions

On [[linear-algebra/euclidean-space|Euclidean space]] with its standard spin structure and constant orthonormal frame, the spin connection form vanishes and \(\nabla^S\) is ordinary differentiation. An arbitrary principal connection on \(P_{\mathrm{Spin}}\) is not the Riemannian spin connection unless it projects to \(\omega_{\mathrm{LC}}\). In some physics texts “spin connection” denotes a connection built from a more general metric connection, possibly with torsion; the present knowl uses the canonical Levi–Civita convention.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: Chapter II, especially §§4–5 on spinors, connections, and Dirac operators.
2. Thomas Friedrich, *Dirac Operators in Riemannian Geometry*, Graduate Studies in Mathematics 25, American Mathematical Society, 2000. [Publisher record](https://doi.org/10.1090/gsm/025). Relevant: Chapters 2–3 and Appendix B.
