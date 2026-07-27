+++
id = "differential-geometry/characteristic-foliation"
title = "Characteristic foliation"
kind = "definition"
summary = "The foliation integrating the null distribution of the symplectic form restricted to a coisotropic submanifold."
aliases = ["null foliation"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(C\) be a [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]] of a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\). Its **characteristic foliation** is the regular foliation whose tangent distribution is the [[differential-geometry/characteristic-distribution-coisotropic|characteristic distribution]]
\[
\mathcal K_p=(T_pC)^\omega=\ker\!\left((\iota^*\omega)_p:T_pC\longrightarrow T_p^*C\right).
\]
The closedness of \(\iota^*\omega\) makes \(\mathcal K\) involutive, so the Frobenius theorem supplies a unique maximal connected integral manifold through every point of \(C\). These integral manifolds are the **characteristic leaves**. The leaf space \(C/\mathcal K\) is only a set in general; it need not be Hausdorff or carry a smooth-manifold structure.

## Why the distribution integrates

For vector fields \(X,Y\) tangent to \(\mathcal K\), one has \(\iota_X\iota^*\omega=\iota_Y\iota^*\omega=0\). Cartan's formula and \(d(\iota^*\omega)=0\) then imply
\[
\iota_{[X,Y]}\iota^*\omega=0.
\]
Thus \(\mathcal K\) is closed under Lie brackets. Its rank is constant because coisotropy gives \(\dim\mathcal K_p=\operatorname{codim}_M C\). Frobenius therefore applies as a regular-foliation theorem, not merely as a statement about a possibly singular distribution [Cannas da Silva, §1.4](https://doi.org/10.1007/978-3-540-45330-7).

## Examples and geometry of the leaves

If \(C\) is a coisotropic hypersurface, its characteristic foliation is one-dimensional. For a regular energy surface \(C=H^{-1}(c)\), its leaves are the unparameterized trajectories of the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] \(X_H\) restricted to \(C\). If \(C\) is [[differential-geometry/lagrangian-submanifold|Lagrangian]], then \(\mathcal K=TC\), so the leaves are the connected components of \(C\).

By contrast, a positive-dimensional [[differential-geometry/symplectic-submanifold|symplectic submanifold]] has zero null distribution. Its point leaves form a trivial foliation, but the submanifold is not coisotropic unless it is open in \(M\).

## Leaf space and reduction

The restricted form \(\iota^*\omega\) annihilates directions tangent to the leaves and is invariant along them. If the leaf space is a smooth manifold and the quotient map is a surjective submersion, these facts allow the form to descend. The resulting symplectic manifold is the [[differential-geometry/coisotropic-reduction|coisotropic reduction]] of \(C\).

**Warning.** “Characteristic foliation” also occurs for contact hypersurfaces and for singular Poisson structures. Here it specifically means the regular null foliation of a coisotropic submanifold in a symplectic manifold.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.4, coisotropic submanifolds, characteristic distributions, and reduction.
2. Paulette Libermann and Charles-Michel Marle, *Symplectic Geometry and Analytical Mechanics*, Mathematics and Its Applications 35, D. Reidel, 1987. [DOI record](https://doi.org/10.1007/978-94-009-3807-6). Relevant: Chapter III, characteristic systems of presymplectic forms.
