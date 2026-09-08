+++
id = "fiber-bundles/tfae-metric-compatible-connections-on-a-metric-vector-bundle"
title = "TFAE: Metric-compatible connections on a metric vector bundle"
kind = "knowl"
summary = "Equivalent conditions for a connection to preserve a fiber metric, including skew connection forms and isometric parallel transport."
aliases = ["tfae-metric-compatible-connections-on-a-metric-vector-bundle", "TFAE: Metric-compatible connections on a metric vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tfae-metric-compatible-connections-on-a-metric-vector-bundle.md"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/bundle-metric", "fiber-bundles/dual-connection", "fiber-bundles/tensor-product-connection", "fiber-bundles/orthonormal-frame-bundle-reduction-of-the-frame-bundle", "fiber-bundles/principal-connection", "fiber-bundles/parallel-transport", "fiber-bundles/local-connection-1-form", "fiber-bundles/section-of-a-vector-bundle", "fiber-bundles/vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let \((E,\langle\cdot,\cdot\rangle)\to M\) be a real [[fiber-bundles/vector-bundle|vector bundle]] of rank \(r\) equipped with a smoothly varying inner product on fibers. Let \(\nabla\) be a [[fiber-bundles/connection-on-a-vector-bundle|connection on a vector bundle]] on \(E\).


The following are equivalent:

**1. Metric preservation (Leibniz rule for the inner product).**
For all smooth vector fields \(X\) on \(M\) and smooth sections \(s,t\) of \(E\),
\[
X\langle s,t\rangle \;=\; \langle \nabla_X s, t\rangle \;+\; \langle s,\nabla_X t\rangle.
\]

**2. Vanishing covariant derivative of the metric.**
The covariant derivative \(\nabla\langle\cdot,\cdot\rangle\) (viewed as a tensor) is identically zero; equivalently, the connection induced by \(\nabla\) on \(E^*\otimes E^*\) annihilates the section representing the metric.

**3. Skew connection \(1\)-forms in orthonormal frames.**
On any open set \(U\) with a local orthonormal frame \((e_1,\dots,e_r)\), the connection is described by matrix-valued \(1\)-forms \(\omega=(\omega^i{}_j)\) via
\[
\nabla e_j = \sum_i \omega^i{}_j\, e_i,
\]
and \(\omega\) takes values in \(\mathfrak{so}(r)\), i.e. \(\omega^i{}_j+\omega^j{}_i=0\).

**4. Isometric parallel transport.**
For every smooth curve \(\gamma:[0,1]\to M\), the parallel transport map on fibers is an isometry:
\[
\langle \mathrm{PT}_\gamma(v), \mathrm{PT}_\gamma(w)\rangle \;=\; \langle v,w\rangle
\quad\text{for all }v,w\in E_{\gamma(0)},
\]
where \(\mathrm{PT}_\gamma\) denotes [[fiber-bundles/parallel-transport|parallel transport]] determined by \(\nabla\).

**5. Orthonormal frame bundle reduction.**
The bundle of orthonormal frames \(O(E)\to M\) is a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group \(\mathrm{O}(r)\), and the connection induced by \(\nabla\) on the full frame bundle restricts to a principal \(\mathrm{O}(r)\)-connection on \(O(E)\).

## Holonomy and the specified metric

These conditions imply that holonomy preserves the given metric in each fiber. The converse statement based only on holonomy at one point requires care: on a connected base, an inner product preserved by holonomy at that point extends by parallel transport to a parallel bundle metric, which need not equal a previously specified metric on the whole bundle. For example, the trivial connection on the real line bundle over \(\mathbb R\) has trivial holonomy, but does not preserve the metric \(h_x(v,w)=e^{2x}vw\).

## Examples

1. **Levi-Civita connection on the tangent bundle.**
   On a [[differential-geometry/riemannian-manifold|Riemannian manifold]], the Levi-Civita connection on the [[fiber-bundles/tangent-bundle|tangent bundle]] is metric-compatible by definition; its parallel transport preserves the Riemannian inner product on tangent spaces.

2. **Trivial bundle with constant metric and trivial connection.**
   If \(E=M\times\mathbb{R}^r\) carries the standard dot product fiberwise and \(\nabla\) is the componentwise derivative in the trivialization, then the connection forms are zero (hence skew), and parallel transport is the identity, so \(\nabla\) is metric-compatible.

3. **Matrix-valued connection with values in so(r).**
   On a trivial rank-\(r\) bundle, define \(\nabla=d+A\) where \(A\) is an \(\mathfrak{so}(r)\)-valued \(1\)-form. Then the connection preserves the standard metric and has holonomy contained in \(\mathrm{O}(r)\); nonzero curvature can occur even though metric compatibility holds.
