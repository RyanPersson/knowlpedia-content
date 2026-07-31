+++
id = "differential-geometry/diagonal-transversality-criterion"
title = "Diagonal transversality criterion"
kind = "theorem"
summary = "Two smooth maps are transverse exactly when their product map is transverse to the diagonal."
aliases = ["transversality via the diagonal", "fiber product diagonal criterion"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f:M\to P\) and \(g:N\to P\) be [[fiber-bundles/smooth-map|smooth maps]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary. Using the [[differential-geometry/product-manifold|product manifolds]], form the map
\[
f\times g:M\times N\longrightarrow P\times P,\qquad (x,y)\longmapsto(f(x),g(y)).
\]
Then \(f\) and \(g\) are [[differential-geometry/transverse-smooth-maps|transverse smooth maps]] if and only if \(f\times g\) is transverse to the [[differential-geometry/embedded-submanifold|diagonal submanifold]]
\[
\Delta_P=\{(z,z):z\in P\}.
\]
Moreover, \((f\times g)^{-1}(\Delta_P)\) is the set-theoretic fiber product \(M\times_PN\).

## Tangent-space calculation

At \((z,z)\in\Delta_P\),
\[
T_{(z,z)}\Delta_P=\{(u,u):u\in T_zP\}.
\]
The quotient of \(T_zP\oplus T_zP\) by this diagonal subspace is identified with \(T_zP\) by \((u,v)\mapsto u-v\). Consequently, transversality of \(f\times g\) to \(\Delta_P\) is equivalent to surjectivity of
\[
(v,w)\longmapsto df_x(v)-dg_y(w),
\]
which is exactly the condition \(df_x(T_xM)+dg_y(T_yN)=T_zP\).

## Fiber-product consequence

When the equivalent conditions hold, the [[differential-geometry/transverse-preimage-theorem|transverse preimage theorem]] makes \(M\times_PN\) an embedded submanifold of \(M\times N\). Its [[differential-geometry/tangent-space|tangent space]] is
\[
\{(v,w):df_x(v)=dg_y(w)\},
\]
and its dimension is \(\dim M+\dim N-\dim P\). This is the [[differential-geometry/smooth-fiber-product|smooth fiber product]] construction.

## Scope

The criterion is a reformulation, not an additional hypothesis. It is especially useful because coincidence equations become a single inverse-image problem. Versions for manifolds with boundary or corners require a notion of transversality compatible with the relevant strata.

## References

1. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 2, diagonal formulation of transversality.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 3, transverse maps and inverse images.
