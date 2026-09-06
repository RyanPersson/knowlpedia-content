+++
id = "fiber-bundles/symmetric-power-bundle"
title = "Symmetric power bundle"
kind = "knowl"
summary = "The vector bundle whose fiber at each point is the k-th symmetric power of the original fiber."
aliases = ["symmetric-power-bundle", "Symmetric power bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/symmetric-power-bundle.md"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/smooth-manifold", "fiber-bundles/tensor-product-vector-bundle", "fiber-bundles/bundle-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] of rank \(r\) over a [[fiber-bundles/smooth-manifold|smooth manifold]]. For an integer \(k\ge 0\), the **k-th symmetric power bundle** of \(E\) is the vector bundle
\[
S^k E \to M
\]
defined fiberwise by
\[
(S^k E)_x := S^k(E_x),
\]
the \(k\)-th symmetric power of the vector space \(E_x\) (i.e. the quotient of \(E_x^{\otimes k}\) by the action of the symmetric group permuting factors).

In local frames, if \((e_1,\dots,e_r)\) is a local frame of \(E|_U\), then the symmetrized tensors built from the \(e_i\) give a local frame of \((S^kE)|_U\). Under a change of frame with transition matrix \(g\), the induced transition on \(S^kE\) is the symmetric power representation \(S^k g\). This can be constructed systematically from the local description of the [[fiber-bundles/tensor-product-vector-bundle|tensor product bundle]] \(E^{\otimes k}\).

Functoriality holds: a [[fiber-bundles/bundle-map|bundle map]] \(\Phi:E\to F\) over \(\mathrm{id}_M\) induces \(S^k\Phi:S^kE\to S^kF\) fiberwise.

## Examples
1. **Symmetric 2-tensors.** For \(E=T^*M\), the bundle \(S^2T^*M\) has sections given by symmetric covariant 2-tensor fields; a Riemannian metric is an everywhere positive-definite section of this bundle.

2. **[[fiber-bundles/line-bundle|Line bundles]].** If \(L\to M\) is a line bundle, then \(S^k L \cong L^{\otimes k}\) canonically (since there is no nontrivial symmetrization in rank 1).

3. **Trivial bundle case.** If \(E\cong M\times \mathbb F^r\), then \(S^kE\cong M\times S^k(\mathbb F^r)\).
