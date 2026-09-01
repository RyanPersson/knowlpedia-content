+++
id = "differential-geometry/symplectic-leaf"
title = "Symplectic leaf"
kind = "definition"
summary = "A symplectic leaf is a maximal connected integral manifold of the characteristic distribution of a Poisson manifold."
aliases = ["leaf of a Poisson manifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/poisson-manifold", "differential-geometry/immersed-submanifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\pi)\) be a [[differential-geometry/poisson-manifold|Poisson manifold]], and define its characteristic subspace at \(p\) by
\[
\mathcal D_p=\pi^\sharp_p(T_p^*M)\subseteq T_pM.
\]
A **symplectic leaf** through \(p\) is the maximal connected [[differential-geometry/immersed-submanifold|immersed submanifold]] \(L\subseteq M\) containing \(p\) and satisfying \(T_qL=\mathcal D_q\) for every \(q\in L\). Its symplectic form is determined by
\[
\omega_L(\pi^\sharp\alpha,\pi^\sharp\beta)=\pi(\alpha,\beta).
\]
This is well-defined, closed, and nondegenerate. The Poisson integrability theorem guarantees that every point lies on a unique such leaf, even when the rank of \(\pi\) varies.

## Why the leaf form is canonical

If \(\pi^\sharp\alpha=0\), then \(\pi(\alpha,\beta)=0\) for every \(\beta\), so the displayed formula is independent of the covectors representing tangent vectors. It is nondegenerate because the [[differential-geometry/tangent-space|tangent space]] is exactly the image of \(\pi^\sharp\). Closedness and integrability ultimately follow from the Jacobi identity for the Poisson bracket.

## Structure and consequences

The leaf dimension equals the rank of \(\pi\) along the leaf and is therefore even and locally constant on that leaf. Different leaves may have different dimensions, so the decomposition is generally a singular foliation rather than a [[differential-geometry/regular-level-set|regular fiber]] bundle.

[[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] are tangent to every leaf. Conversely, their values span the characteristic distribution, so a leaf is the region reachable by piecewise [[differential-geometry/hamiltonian-flow|Hamiltonian flows]]. The inclusion \(L\hookrightarrow M\) is a Poisson immersion when \(L\) is equipped with the bracket induced by \(\omega_L\).

## Examples and non-examples

For \(\mathbb R^3\) with \(\pi=\partial_x\wedge\partial_y\), the leaves are the planes \(z=c\), each with its standard symplectic form. If \(\pi=0\), every leaf is a single point. The [[differential-geometry/coadjoint-orbit|coadjoint orbits]] in the dual of a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] are the leaves of its linear Poisson structure.

A proper open disk in one plane \(z=c\) is an integral [[differential-geometry/symplectic-submanifold|symplectic submanifold]], but it is not a leaf because it is not maximal.

## Conventions and scope

**Warning.** The sign of \(\omega_L\) depends on the convention for \(\pi^\sharp\) and for passing between a symplectic form and a Poisson bivector. The formula in the core fixes the convention used here. “Leaf” always means connected and maximal; an arbitrary integral submanifold is not automatically a leaf.

## References

1. Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds*, Progress in Mathematics 118, Birkhäuser, 1994. [Publisher record](https://doi.org/10.1007/978-3-0348-8495-2). Relevant: “The Symplectic Foliation of a Poisson Manifold,” pp. 19–30.
2. Alan Weinstein, “The Local Structure of Poisson Manifolds,” *Journal of Differential Geometry* 18, no. 3 (1983), 523–557. [DOI record](https://doi.org/10.4310/jdg/1214437787). Relevant: §1, Poisson manifolds and mappings, and §2, the splitting theorem.
