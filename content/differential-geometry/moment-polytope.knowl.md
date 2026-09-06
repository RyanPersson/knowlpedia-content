+++
id = "differential-geometry/moment-polytope"
title = "Moment polytope"
kind = "definition"
summary = "The convex-polytope image of the moment map for a compact connected Hamiltonian torus space."
aliases = ["momentum polytope"]
domains = ["differential-geometry", "lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "differential-geometry/symplectic-manifold", "fiber-bundles/moment-map", "differential-geometry/atiyah-guillemin-sternberg-convexity-theorem"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let a compact torus \(T\), with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak t\), act in a Hamiltonian fashion on a compact connected [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), and let \(\mu:M\to\mathfrak t^*\) be a [[fiber-bundles/moment-map|moment map]]. The **moment polytope** is
\[
\Delta(M,\omega,\mu)=\mu(M)\subseteq\mathfrak t^*.
\]
The [[differential-geometry/atiyah-guillemin-sternberg-convexity-theorem|Atiyah–Guillemin–Sternberg convexity theorem]] guarantees that this image is a convex polytope. Because a torus moment map is determined only up to addition of a constant in \(\mathfrak t^*\), the polytope is likewise defined only up to translation unless a normalization of \(\mu\) is chosen.

## Fixed points and lattice structure

The polytope is the [[convex-analysis/convex-hull|convex hull]] of the moment-map values on the [[algebra-groups/fixed-point-set|fixed-point set]] \(M^T\). Every component of \(M^T\) maps to a single point. Its faces and edge directions reflect the isotropy weights of the torus action, hence are rational relative to the weight lattice determined by \(\ker(\exp:\mathfrak t\to T)\).

Translation does not change face directions or the normal fan, but it does change the numerical coordinates of vertices. Integrality of the vertices is an extra prequantization condition, not a consequence of Hamiltonianity alone.

## Standard examples

For the standard \(T^n\)-action on complex [[algebraic-geometry-foundations/projective-space|projective space]] \(\mathbb{CP}^n\), with a normalized Fubini–Study form, the moment polytope is an \(n\)-simplex. Rescaling the symplectic form rescales the simplex, and changing the additive normalization translates it.

For a compact connected symplectic toric manifold, the polytope has dimension \(n=\frac12\dim M\) and satisfies the Delzant smoothness condition. For a noneffective action, the polytope lies in a proper affine subspace corresponding to the effective quotient torus.

## Conventions and scope

Some authors say “moment polytope” for the intersection of a nonabelian moment-map image with a chosen positive Weyl chamber. That is a related nonabelian construction, not the torus image defined here.

Compactness and connectedness matter. For a noncompact Hamiltonian \(T\)-space, the image may be unbounded or fail to be a polytope without properness and convexity hypotheses. A general [[fiber-bundles/smooth-map|smooth map]] into \(\mathfrak t^*\) is not a moment map, so its image does not acquire this structure merely from being compact.

## References

1. V. Guillemin, *Moment Maps and Combinatorial Invariants of Hamiltonian \(T^n\)-Spaces*, Birkhäuser, 1994. [DOI record](https://doi.org/10.1007/978-1-4612-0269-1). Relevant: Chapter 1, moment images, isotropy weights, and rational polytopes.
2. M. Audin, *Torus Actions on Symplectic Manifolds*, 2nd revised ed., Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-3-0348-7960-6). Relevant: Chapter IV, convexity and moment polytopes.
