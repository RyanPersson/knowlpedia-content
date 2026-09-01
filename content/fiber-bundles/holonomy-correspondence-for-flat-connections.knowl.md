+++
id = "fiber-bundles/holonomy-correspondence-for-flat-connections"
title = "Holonomy correspondence for flat connections"
kind = "theorem"
summary = "The classification of flat principal bundles by conjugacy classes of fundamental-group representations."
aliases = ["Riemann–Hilbert correspondence for smooth flat bundles", "monodromy correspondence"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/lie-group", "fiber-bundles/principal-g-bundle", "fiber-bundles/holonomy-representation", "algebra-groups/conjugation-action"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a connected [[fiber-bundles/smooth-manifold|smooth manifold]] with basepoint \(x\), and let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. The **holonomy correspondence for flat connections** is the bijection
\[
\left\{
\begin{array}{c}
\text{flat principal \(G\)-bundles over \(M\)}\\
\text{up to connection-preserving isomorphism}
\end{array}
\right\}
\longleftrightarrow
\operatorname{Hom}(\pi_1(M,x),G)/G .
\]
Here a flat principal bundle means a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] with a flat connection. The correspondence sends it to its [[fiber-bundles/holonomy-representation|holonomy representation]] after choosing a point over \(x\); changing that point conjugates the representation. Conversely, a homomorphism \(\rho\) produces the quotient \(\widetilde M\times_\rho G\) with the flat connection descended from the product connection.
The right-hand quotient is by the [[algebra-groups/conjugation-action|conjugation action]] of \(G\).

## Construction from monodromy

Let \(\pi_1(M,x)\) act on the universal cover by deck transformations and on \(G\) by left multiplication through \(\rho\):
\[
\gamma\cdot(\widetilde x,g)
=
(\gamma\widetilde x,\rho(\gamma)g).
\]
This action commutes with the principal right \(G\)-action, so
\[
P_\rho=(\widetilde M\times G)/\pi_1(M,x)
\]
is a principal \(G\)-bundle. The [[fiber-bundles/horizontal-distribution|horizontal distribution]] tangent to \(\widetilde M\) descends and is flat. Its holonomy is \(\rho\), up to the inverse or conjugation dictated by path-lifting conventions. This construction and its converse are the classification content behind the standard equivalences for [[fiber-bundles/tfae-flat-principal-bundles-principal-g-bundle-pm|flat principal bundles]].

## Passage to moduli

The correspondence is a bijection of isomorphism classes. With suitable topologies and hypotheses, it refines to a comparison between the [[fiber-bundles/moduli-space-of-flat-connections|moduli space of flat connections]] and a topological representation quotient. For compact \(G\) over a closed surface, every conjugacy orbit is closed and the quotient behaves well topologically; for noncompact or complex reductive groups, one often replaces the naive [[lie-groups/orbit-space|orbit space]] by a closed-orbit or geometric-invariant-theory quotient.

On a fixed principal bundle \(P\), only the representations for which \(P_\rho\) is isomorphic to \(P\) occur. Thus the correspondence does not say that every representation lies in the flat moduli of one preselected bundle.

## Example

For \(M=S^1\), a representation is determined by one element \(g\in G\). Two resulting flat bundles with connection are isomorphic exactly when their elements are conjugate. If \(G=U(1)\), conjugation is trivial and the moduli is \(U(1)\).

## Conventions and scope

For [[fiber-bundles/complex-vector-bundle|complex vector bundles]], the same construction is often called the smooth Riemann–Hilbert or monodromy correspondence. It should not be confused with the analytic Riemann–Hilbert correspondence involving regular singular differential equations or perverse sheaves.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley.com/en-us/Foundations+of+Differential+Geometry%2C+Volume+1-p-9780471157335). Relevant: Chapter II, holonomy, flat connections, and bundle reconstruction from monodromy.
2. William M. Goldman, “The Symplectic Nature of Fundamental Groups of Surfaces,” *Advances in Mathematics* 54 (1984), 200–225. [DOI record](https://doi.org/10.1016/0001-8708%2884%2990040-9). Relevant: §§1–2, surface-group representations and flat-bundle moduli.
