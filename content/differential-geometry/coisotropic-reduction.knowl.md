+++
id = "differential-geometry/coisotropic-reduction"
title = "Coisotropic reduction"
kind = "theorem"
summary = "A smooth quotient of a coisotropic submanifold by its characteristic leaves inherits a unique symplectic form."
aliases = ["characteristic reduction", "presymplectic reduction"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(C\) be a [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]] of \((M,\omega)\), with inclusion \(i:C\hookrightarrow M\). Suppose the leaf space \(C/\mathcal K\) of its [[differential-geometry/characteristic-foliation|characteristic foliation]] is a [[fiber-bundles/smooth-manifold|smooth manifold]] \(B\), and the quotient map \(\pi:C\to B\) is a surjective submersion whose fibers are the characteristic leaves. Then there is a unique two-form \(\omega_B\) satisfying
\[
\pi^*\omega_B=i^*\omega.
\]
This form is closed and nondegenerate, so \((B,\omega_B)\) is a [[differential-geometry/symplectic-manifold|symplectic manifold]]. It is the **coisotropic reduction** of \(C\). Smoothness and the submersion condition are hypotheses, not consequences of coisotropy.

## Descent and nondegeneracy

The kernel of \(i^*\omega\) is exactly \(\mathcal K\). The form is horizontal because it annihilates every vector tangent to a leaf. It is also invariant along leafwise [[fiber-bundles/vector-field|vector fields]]: if \(X\) is tangent to \(\mathcal K\), then Cartan's formula gives
\[
\mathcal L_X(i^*\omega)=d\iota_X(i^*\omega)+\iota_Xd(i^*\omega)=0.
\]
Thus \(i^*\omega\) is basic and descends uniquely through the surjective submersion \(\pi\). If a tangent vector downstairs pairs to zero with every other tangent vector, any lift lies in \(\ker i^*\omega=\ker d\pi\), so the original vector is zero. This proves nondegeneracy [Cannas da Silva, §1.4].

## Linear model and Hamiltonian reduction

For a [[differential-geometry/coisotropic-subspace|coisotropic subspace]] \(W\) of a [[differential-geometry/symplectic-vector-space|symplectic vector space]], the theorem becomes [[differential-geometry/linear-coisotropic-reduction|linear coisotropic reduction]]:
\[
W_{\mathrm{red}}=W/W^\omega.
\]
There are no global leaf-space pathologies in this linear case.

Regular Hamiltonian reduction is the principal nonlinear example. Under the hypotheses of the [[differential-geometry/marsden-weinstein-meyer-reduction-theorem|Marsden–Weinstein–Meyer theorem]], the moment-map level set is coisotropic, its characteristic leaves are group orbits, and its coisotropic reduction is the usual [[differential-geometry/symplectic-quotient|symplectic quotient]].

## Failure of the hypotheses

The characteristic foliation may have dense leaves, nonclosed leaves, or a non-Hausdorff leaf space. Even when the underlying quotient is Hausdorff, it may not admit a smooth structure for which \(\pi\) is a submersion. In these cases the pullback equation still describes the desired geometry formally, but it does not produce an ordinary symplectic manifold.

**Warning.** Some authors call the quotient of any presymplectic manifold by its null foliation “presymplectic reduction.” The theorem here uses the restricted form on a coisotropic submanifold; a more general presymplectic quotient has the same descent argument when its null distribution has constant rank and a smooth leaf space.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.4, characteristic foliations and symplectic reduction.
2. Paulette Libermann and Charles-Michel Marle, *Symplectic Geometry and Analytical Mechanics*, Mathematics and Its Applications 35, D. Reidel, 1987. [DOI record](https://doi.org/10.1007/978-94-009-3807-6). Relevant: Chapter III, reduction of presymplectic and coisotropic manifolds.
