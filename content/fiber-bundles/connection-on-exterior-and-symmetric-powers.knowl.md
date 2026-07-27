+++
id = "fiber-bundles/connection-on-exterior-and-symmetric-powers"
title = "Connection on exterior and symmetric powers"
kind = "definition"
summary = "The connections induced on exterior and symmetric power bundles by differentiating one tensor factor at a time."
aliases = ["induced connection on tensor powers", "connection on Lambda^k E", "connection on Sym^k E"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(E\to M\) be a [[fiber-bundles/vector-bundle|real or complex vector bundle]] with connection \(\nabla\). The **induced connections** on the [[fiber-bundles/exterior-power-bundle|exterior power]] \(\Lambda^kE\) and [[fiber-bundles/symmetric-power-bundle|symmetric power]] \(\operatorname{Sym}^kE\) are the unique connections satisfying
\[
\nabla_X(s_1\wedge\cdots\wedge s_k)
=
\sum_{i=1}^k s_1\wedge\cdots\wedge\nabla_Xs_i\wedge\cdots\wedge s_k
\]
and the analogous formula with the symmetric product. Equivalently, take the iterated [[fiber-bundles/tensor-product-connection|tensor-product connection]] on \(E^{\otimes k}\); it preserves alternating and symmetric tensors and therefore descends to both power bundles.
Both constructions use the same scalar field as \(E\) and require \(k\geq0\).

## Parallel transport and curvature

If \(T_\gamma:E_{\gamma(0)}\to E_{\gamma(1)}\) is parallel transport for \(\nabla\), the induced transports are \(\Lambda^kT_\gamma\) and \(\operatorname{Sym}^kT_\gamma\). This characterization immediately shows that a connection preserving a [[fiber-bundles/bundle-metric|bundle metric]] induces metric connections on the corresponding power bundles.

Curvature acts by the derived exterior- or symmetric-power representation. For decomposable exterior tensors,
\[
R^{\Lambda^kE}(X,Y)(s_1\wedge\cdots\wedge s_k)
=
\sum_{i=1}^k
s_1\wedge\cdots\wedge R^E(X,Y)s_i\wedge\cdots\wedge s_k,
\]
and the symmetric formula is identical with \(\wedge\) replaced by the symmetric product. In particular, a flat connection induces flat connections on every exterior and symmetric power.

## Important special cases

The zeroth powers are the trivial [[fiber-bundles/line-bundle|line bundle]] with its trivial connection, and the first powers recover \((E,\nabla)\). If \(E\) has rank \(r\), the connection on \(\Lambda^rE=\det E\) is the determinant connection; in a local frame its connection one-form is the trace of the connection matrix, and its curvature is \(\operatorname{tr}(R^E)\).

For a line bundle \(L\), \(\operatorname{Sym}^kL\cong L^{\otimes k}\), and the induced local connection one-form is \(k\) times that of \(L\). A connection chosen independently on \(\Lambda^kE\) is a near miss: it need not arise from any connection on \(E\).

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Graduate Texts in Mathematics 176, Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 4, connections and induced connections on tensor bundles.
2. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Chapter record](https://doi.org/10.1515/9781400883912-005). Relevant: Chapter II, induced connections and their curvature actions on associated tensor and Clifford modules.
