+++
id = "differential-geometry/transverse-preimage-theorem"
title = "Transverse preimage theorem"
kind = "theorem"
summary = "The inverse image of an embedded submanifold under a transverse map is an embedded submanifold of the same codimension."
aliases = ["preimage theorem for transverse maps", "transversality preimage theorem"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, and let \(S\subseteq N\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. If \(f\) is [[differential-geometry/map-transverse-to-a-submanifold|transverse to \(S\)]], then \(f^{-1}(S)\) is an embedded submanifold of \(M\). For every \(x\in f^{-1}(S)\),
\[
T_xf^{-1}(S)=(df_x)^{-1}(T_{f(x)}S),
\]
and
\[
\operatorname{codim}_M f^{-1}(S)=\operatorname{codim}_N S.
\]
Thus the inverse image has the codimension predicted by the normal directions to \(S\).

## Proof idea

Choose local coordinates on \(N\) in which \(S\) is the zero set of a submersion \(h\) to \(\mathbb R^k\), where \(k=\operatorname{codim}_N S\). Transversality says that \(d(h\circ f)_x\) is surjective along \(f^{-1}(S)\). The regular-level-set theorem applied to \(h\circ f\) gives the claimed smooth structure, codimension, and tangent-space kernel. See [Hirsch, Chapter 3](https://doi.org/10.1007/978-1-4684-9449-5).

## Special cases and examples

When \(S=\{y\}\), transversality is exactly the assertion that \(y\) is a [[fiber-bundles/regular-value|regular value]], so this theorem recovers the regular-value theorem. Every submersion is transverse to every embedded submanifold; hence the inverse image of \(S\) under a submersion has the same codimension as \(S\).

A constant map whose value lies in a positive-codimension \(S\) is not transverse, and the theorem makes no regularity claim about its inverse image.

## Scope

If \(f^{-1}(S)\) is empty, it is an embedded submanifold and the tangent statement is vacuous. Manifolds with boundary or corners need additional conditions controlling boundary strata. The theorem also does not assert that an arbitrary nontransverse inverse image is singular; it says only that transversality is a sufficient regularity hypothesis.

## References

1. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 3, transversality and inverse images.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, the transversality theorem.
