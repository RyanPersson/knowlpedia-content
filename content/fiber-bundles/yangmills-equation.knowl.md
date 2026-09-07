+++
id = "fiber-bundles/yangmills-equation"
title = "Yang–Mills equation"
kind = "knowl"
summary = "The Euler–Lagrange equation for the Yang–Mills functional, expressed as a covariant divergence-free condition on curvature."
aliases = ["yangmills-equation", "Yang–Mills equation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-equation.md"
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/principal-connection", "fiber-bundles/curvature", "differential-geometry/hodge-star-operator", "fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to M\) be a principal \(G\)-bundle over an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]], and let \(A\) be a [[fiber-bundles/principal-connection|principal connection]] with [[fiber-bundles/curvature|curvature]] \(F_A\).

The **Yang–Mills equation** is
\[
d_A(*F_A)=0.
\]
Here \(*\) is the [[differential-geometry/hodge-star-operator|Hodge star]], and \(d_A\) is the [[fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms|covariant exterior derivative]] on \(\operatorname{ad}(P)\)-valued forms, which extends the [[fiber-bundles/exterior-derivative|exterior derivative]] on ordinary forms and satisfies the Bianchi identity \(d_A F_A=0\).

A connection \(A\) satisfying \(d_A(*F_A)=0\) is called a Yang–Mills connection.

## Variational interpretation

If the Lie algebra carries an Ad-invariant positive-definite inner product, this is the Euler–Lagrange equation of the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] on a closed manifold. On a noncompact manifold the same local equation follows for finite-energy connections under compactly supported variations; boundaries require boundary conditions or variations supported away from the boundary.

## Examples
1. **Flat connections.** If \(F_A=0\) then \(d_A(*F_A)=0\) automatically.
2. **Abelian reduction.** For \(G=U(1)\), the equation becomes \(d(*F)=0\), the source-free Maxwell equation for the curvature 2-form \(F\).
3. **Instantons in dimension 4.** On a 4-manifold, any connection with self-dual or anti-self-dual curvature satisfies the Yang–Mills equation because \(*F_A=\pm F_A\) and the Bianchi identity gives \(d_A(*F_A)=\pm d_AF_A=0\).
