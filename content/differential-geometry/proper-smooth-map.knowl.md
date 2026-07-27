+++
id = "differential-geometry/proper-smooth-map"
title = "Proper smooth map"
kind = "definition"
summary = "A smooth map for which the inverse image of every compact set is compact."
aliases = ["proper map of manifolds", "proper smooth mapping"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[fiber-bundles/smooth-manifold|smooth manifolds]]. A [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\) is **proper** if \(f^{-1}(K)\) is a [[topology/compact-set|compact set]] in \(M\) for every compact subset \(K\subseteq N\). Properness is a global topological condition on the underlying continuous map; it does not impose a rank condition on its differential. In particular, every fiber \(f^{-1}(y)\) is compact because a singleton in a manifold is compact.

## Equivalent characterizations

For manifolds, properness is equivalent to the sequence criterion: whenever a sequence \((x_j)\) in \(M\) has \(f(x_j)\) converging in \(N\), the sequence \((x_j)\) has a convergent subsequence in \(M\). It is also equivalent to \(f\) being a closed map with compact fibers. These equivalences use the Hausdorff, [[topology/locally-compact-space|locally compact]], second-countable properties built into the manifold convention; they need not hold in arbitrary topological spaces. See [Lee, Appendix A and Chapter 4](https://doi.org/10.1007/978-1-4419-9982-5).

## Stability and geometric consequences

Composites of proper maps are proper, and the base change of a proper smooth map along any smooth map is proper whenever the fiber product is formed in the usual manifold setting. A proper injective immersion is a [[fiber-bundles/smooth-embedding|smooth embedding]]. Properness also prevents points from escaping to infinity while their images remain bounded, which is why it appears in global inverse results, degree theory, and compactness arguments.

## Examples and non-examples

The constant map \(M\to\{\ast\}\) is proper exactly when \(M\) is compact. If \(K\) is a compact manifold, the projection \(M\times K\to M\) from the [[differential-geometry/product-manifold|product manifold]] is proper. By contrast, the projection \(\mathbb R^2\to\mathbb R\), \((x,y)\mapsto x\), is not proper because the inverse image of \(\{0\}\) is a noncompact line. A proper smooth map need not be a submersion, immersion, or injective.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 4 and Appendix A, proper maps and embeddings.
2. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [Publisher record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1, proper maps and differential-topological conventions.
