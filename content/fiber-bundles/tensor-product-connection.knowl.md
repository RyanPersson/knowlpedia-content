+++
id = "fiber-bundles/tensor-product-connection"
title = "Tensor product connection"
kind = "definition"
summary = "The connection on a tensor product bundle obtained by differentiating each factor."
aliases = ["product connection on vector bundles", "connection on E tensor F"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(E\to M\) and \(F\to M\) be smooth [[fiber-bundles/vector-bundle|real vector bundles]] or [[fiber-bundles/complex-vector-bundle|complex vector bundles]] with [[fiber-bundles/connection-on-a-vector-bundle|connections]] \(\nabla^E\) and \(\nabla^F\). The **tensor product connection** is the unique connection \(\nabla^{E\otimes F}\) on the [[fiber-bundles/tensor-product-vector-bundle|tensor product bundle]] satisfying
\[
\nabla^{E\otimes F}_X(s\otimes t)
=
(\nabla^E_Xs)\otimes t+s\otimes(\nabla^F_Xt)
\]
for every [[fiber-bundles/vector-field|vector field]] \(X\) and [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] \(s\) of \(E\) and \(t\) of \(F\). Equivalently,
\[
\nabla^{E\otimes F}(s\otimes t)
=
\nabla^Es\otimes t+s\otimes\nabla^Ft.
\]

## Why the formula is well defined

Sections of \(E\otimes F\) are locally finite sums of decomposable sections \(s\otimes t\). The displayed rule is balanced over smooth functions: replacing \(s\otimes ft\) by \(fs\otimes t\) gives the same result because the two occurrences of \(\mathrm df\) agree. It therefore descends from pairs of sections to their tensor product and obeys the Leibniz rule required of a connection.

In local frames, if
\[
\nabla^E=\mathrm d+A
\qquad\text{and}\qquad
\nabla^F=\mathrm d+B,
\]
then the product connection has connection matrix
\[
A\otimes I_F+I_E\otimes B.
\]
This expression explains why both factors are differentiated.

## Curvature

The [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature of the tensor product connection]] contains no mixed term:
\[
R^{E\otimes F}
=
R^E\otimes I_F+I_E\otimes R^F.
\]
Consequently, the tensor product of two flat connections is flat. The converse need not hold, since scalar curvature contributions from the two factors can cancel.

## Related induced connections

The same Leibniz principle defines connections on tensor powers, exterior powers, symmetric powers, dual bundles, and bundles of homomorphisms. For example, the [[fiber-bundles/dual-connection|dual connection]] is characterized by
\[
X\bigl(\lambda(s)\bigr)
=
(\nabla_X\lambda)(s)+\lambda(\nabla_Xs),
\]
and the connection on \(\operatorname{Hom}(E,F)\) satisfies
\[
(\nabla_XT)(s)=\nabla^F_X(Ts)-T(\nabla^E_Xs).
\]

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 5, connections and induced connections on tensor bundles.
