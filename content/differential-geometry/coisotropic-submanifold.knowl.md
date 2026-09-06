+++
id = "differential-geometry/coisotropic-submanifold"
title = "Coisotropic submanifold"
kind = "definition"
summary = "A submanifold whose tangent spaces contain their symplectic orthogonal complements."
aliases = ["co-isotropic submanifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/embedded-submanifold", "differential-geometry/coisotropic-subspace", "fiber-bundles/smooth-embedding"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]] and \(C\subseteq M\) an [[differential-geometry/embedded-submanifold|embedded submanifold]]. For \(p\in C\), let
\[
(T_pC)^\omega=\{v\in T_pM:\omega_p(v,w)=0\text{ for all }w\in T_pC\}.
\]
The submanifold \(C\) is **coisotropic** if
\[
(T_pC)^\omega\subseteq T_pC
\]
at every \(p\in C\); equivalently, every \(T_pC\) is a [[differential-geometry/coisotropic-subspace|coisotropic subspace]] of \(T_pM\). The kernel of the restricted form \(\omega|_{T_pC}\) is exactly \((T_pC)^\omega\). Thus coisotropy says that all null directions of the restricted form are tangent to \(C\). It depends on the ambient form, not only on the [[fiber-bundles/smooth-embedding|smooth embedding]].

## Dimension and local structure

If \(\dim M=2n\) and \(C\) has codimension \(k\), then the characteristic space \((T_pC)^\omega\) has dimension \(k\). Coisotropy forces \(k\leq n\), or equivalently \(\dim C\geq n\). A hypersurface in a symplectic manifold is automatically coisotropic because its one-dimensional [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal]] lies in the hyperplane.

The spaces \((T_pC)^\omega\) assemble into the [[differential-geometry/characteristic-distribution-coisotropic|characteristic distribution]] on \(C\). Since the restricted two-form is closed, this distribution is involutive and hence determines the [[differential-geometry/characteristic-foliation|characteristic foliation]].

## Examples and contrasts

The whole manifold \(M\) is coisotropic. Every [[differential-geometry/lagrangian-submanifold|Lagrangian submanifold]] is coisotropic because its [[differential-geometry/tangent-space|tangent spaces]] equal their symplectic orthogonals. If a Hamiltonian Lie-group action has [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\), then a [[differential-geometry/regular-level-set|regular level set]] \(\mu^{-1}(\xi)\) is coisotropic under the usual hypotheses when \(\xi\) is fixed by the coadjoint action relevant to the reduction.

A proper [[differential-geometry/symplectic-submanifold|symplectic submanifold]] is not coisotropic: the restricted form has zero kernel, whereas a positive-codimension coisotropic submanifold has a positive-dimensional characteristic space.

## Role in reduction

The leaf space of the characteristic foliation is the candidate [[differential-geometry/symplectic-quotient|reduced phase space]]. When that leaf space is a [[fiber-bundles/smooth-manifold|smooth manifold]] and the quotient map is a submersion, there is a unique symplectic form downstairs whose pullback is \(\omega|_C\). Without these regularity hypotheses, the quotient may be singular or non-Hausdorff, even though \(C\) is a perfectly smooth coisotropic submanifold.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: symplectic reduction and the characteristic directions of constraint sets.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 5, constraints and symplectic reduction.
