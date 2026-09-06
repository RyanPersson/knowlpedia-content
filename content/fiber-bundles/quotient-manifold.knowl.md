+++
id = "fiber-bundles/quotient-manifold"
title = "Quotient manifold (for a free proper action)"
kind = "knowl"
summary = "The smooth manifold structure on an orbit space arising from a free and proper Lie group action."
aliases = ["quotient-manifold", "Quotient manifold (for a free proper action)"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/lie-group", "fiber-bundles/smooth-manifold", "fiber-bundles/principal-g-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "fiber-bundles/quotient-manifold.md"
+++

Let a [[fiber-bundles/lie-group|Lie group]] \(G\) act smoothly, freely, and properly on a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\). Then the orbit space \(M/G\) admits a unique smooth manifold structure for which the quotient map \(\pi:M\to M/G\) is a smooth submersion. Moreover:

1. The fibers of \(\pi\) are the orbits, and \(\dim(M/G)=\dim(M)-\dim(G)\).
2. With this structure, \(\pi:M\to M/G\) is a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], after converting a given left action to the corresponding right action if necessary.

In particular, local differential geometry on \(M/G\) can be studied through \(G\)-invariant data on \(M\).

## Examples
1. **Hopf fibration.** The free proper \(S^1\)-action on \(S^{2n+1}\) by scalar multiplication yields the quotient manifold \(S^{2n+1}/S^1 \cong \mathbb{CP}^n\).
2. **Positive scalings.** The action of \(\mathbb{R}_{>0}\) on \(\mathbb{R}^n\setminus\{0\}\) by \(t\cdot x = tx\) is free and proper; the quotient is diffeomorphic to \(S^{n-1}\).
3. **Covering space quotient.** The free proper action of \(\mathbb{Z}\) on \(\mathbb{R}\) by translations gives the quotient manifold \(\mathbb{R}/\mathbb{Z}\cong S^1\).
