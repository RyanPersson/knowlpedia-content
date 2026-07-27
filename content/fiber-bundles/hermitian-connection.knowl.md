+++
id = "fiber-bundles/hermitian-connection"
title = "Hermitian connection"
kind = "definition"
summary = "A connection on a Hermitian vector bundle that preserves its fiberwise Hermitian inner product."
aliases = ["unitary connection", "metric-compatible complex connection"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(E\to M\) carry a [[fiber-bundles/hermitian-metric|Hermitian metric]] \(h\), conjugate-linear in its first variable, and let \(\nabla\) be a [[fiber-bundles/connection-on-a-vector-bundle|connection on the complex vector bundle]]. The connection is a **Hermitian connection** if
\[
X\bigl(h(s,t)\bigr)=h(\nabla_Xs,t)+h(s,\nabla_Xt)
\]
for every smooth [[fiber-bundles/vector-field|vector field]] \(X\) and smooth local sections \(s,t\). Thus covariant differentiation is compatible with the fiberwise inner products. A Hermitian connection is also called a unitary connection once \(h\) is fixed. The condition is intrinsic and does not depend on a local frame.

## Equivalent characterizations

The following conditions are equivalent:

1. \(\nabla h=0\), meaning the displayed compatibility identity holds.
2. Parallel transport by \(\nabla\) along every smooth curve is a unitary linear map between the endpoint fibers.
3. The connection on the full frame bundle restricts to a principal connection on the [[fiber-bundles/unitary-frame-bundle-reduction|unitary frame bundle]].
4. In every local unitary frame, the connection one-form takes values in the skew-Hermitian Lie algebra \(\mathfrak u(n)\).

These equivalences are the complex Hermitian analogues of metric compatibility for real vector bundles [Kobayashi, chapter I](https://doi.org/10.1515/9781400858682).

## Standard constructions

Every Hermitian vector bundle over a smooth paracompact manifold admits a Hermitian connection. Starting with any connection, one may correct its failure to preserve \(h\), or equivalently patch local unitary connections using a partition of unity.

On a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] with Hermitian metric there is a unique Hermitian connection whose \((0,1)\)-part equals the bundle's holomorphic structure. This is the [[fiber-bundles/chern-connection|Chern connection]]; its uniqueness uses both the metric and the holomorphic structure [Kobayashi, chapter I, §4](https://doi.org/10.1515/9781400858682).

## Examples

On the trivial bundle \(M\times\mathbb C^n\) with its standard metric, the ordinary derivative \(d\) is Hermitian. More generally, \(d+A\) is Hermitian precisely when the matrix-valued one-form \(A\) is skew-Hermitian.

For a Hermitian [[fiber-bundles/line-bundle|line bundle]], a unitary local frame writes a Hermitian connection as \(d+i\alpha\), where \(\alpha\) is a real one-form. Its parallel transport has unit modulus.

## Conventions and scope

Some authors take a Hermitian form to be linear in the first variable rather than the second. The compatibility identity remains the same in invariant form, but local matrix and curvature sign conventions may change.

**Warning.** “Unitary connection” presupposes a chosen Hermitian metric. A general complex connection need not preserve any specified metric.

## References

1. S. Kobayashi, *Differential Geometry of Complex Vector Bundles*, Princeton University Press, 1987. [DOI record](https://doi.org/10.1515/9781400858682). Relevant: chapter I, Hermitian bundles, connections, and curvature.
