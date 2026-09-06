+++
id = "differential-geometry/characteristic-distribution-coisotropic"
title = "Characteristic distribution of a coisotropic submanifold"
kind = "definition"
summary = "The null distribution of the restricted symplectic form on a coisotropic submanifold."
aliases = ["null distribution", "characteristic subbundle"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/coisotropic-submanifold", "differential-geometry/symplectic-manifold", "fiber-bundles/vector-subbundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(C\) be a [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]] of a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), and write \(\omega_C=\iota^*\omega\) for the restricted two-form. The **characteristic distribution** on \(C\) is the [[fiber-bundles/vector-subbundle|vector subbundle]] \(\mathcal K\subseteq TC\) whose fiber at \(p\in C\) is
\[
\mathcal K_p=(T_pC)^\omega
=\ker\!\left(\omega_C^\flat:T_pC\to T_p^*C\right).
\]
Coisotropy ensures \((T_pC)^\omega\subseteq T_pC\), while symplectic linear algebra gives \(\operatorname{rank}\mathcal K=\operatorname{codim}_M C\). Thus these null spaces have constant rank and form a smooth distribution. It is also called the null distribution of the restricted form.

## Involutivity

The characteristic distribution is involutive. If \(X\) and \(Y\) are [[fiber-bundles/vector-field|vector fields]] tangent to \(\mathcal K\), then \(\iota_X\omega_C=\iota_Y\omega_C=0\). Because \(d\omega_C=0\), Cartan's formula gives
\[
\iota_{[X,Y]}\omega_C
=\mathcal L_X(\iota_Y\omega_C)-\iota_Y(\mathcal L_X\omega_C)=0.
\]
Hence \([X,Y]\) is again tangent to \(\mathcal K\). The Frobenius theorem therefore integrates \(\mathcal K\) to the **[[differential-geometry/characteristic-foliation|characteristic foliation]]** of \(C\).

## Examples

For a coisotropic hypersurface, \(\mathcal K\) is a line field. If the hypersurface is a regular energy level \(H^{-1}(c)\), its characteristic line is spanned by the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] \(X_H\) wherever \(dH\ne0\). At the opposite extreme, if \(C\) is Lagrangian, then \(\mathcal K=TC\), so each [[topology/connected-component|connected component]] is a characteristic leaf.

## Role in reduction

The restricted form \(\omega_C\) is horizontal along \(\mathcal K\) and invariant under vector fields tangent to \(\mathcal K\). Consequently it is the candidate pullback of a two-form on the leaf space \(C/\mathcal K\). If that quotient is a [[fiber-bundles/smooth-manifold|smooth manifold]] and the projection is a submersion, the descended form is symplectic. The distribution alone does not guarantee that the leaf space is Hausdorff or even a manifold.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: characteristic foliations and symplectic reduction.
2. Paulette Libermann and Charles-Michel Marle, *Symplectic Geometry and Analytical Mechanics*, Mathematics and Its Applications 35, D. Reidel, 1987. [Springer DOI record](https://doi.org/10.1007/978-94-009-3807-6). Relevant: Chapter III, coisotropic submanifolds and characteristic distributions.
