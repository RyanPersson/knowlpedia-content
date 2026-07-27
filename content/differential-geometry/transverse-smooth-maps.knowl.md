+++
id = "differential-geometry/transverse-smooth-maps"
title = "Transverse smooth maps"
kind = "definition"
summary = "Smooth maps to a common target whose differentials jointly span the target tangent space over every coincidence."
aliases = ["transverse maps", "maps transverse to each other"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f:M\to P\) and \(g:N\to P\) be [[fiber-bundles/smooth-map|smooth maps]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary. The maps \(f\) and \(g\) are **transverse**, written \(f\pitchfork g\), if for every pair \((x,y)\in M\times N\) with \(f(x)=g(y)=z\),
\[
df_x(T_xM)+dg_y(T_yN)=T_zP,
\]
where \(df_x\) and \(dg_y\) are their [[fiber-bundles/differential-of-a-smooth-map|differentials]]. The two differential images may overlap; only their sum must fill the target tangent space. If the images of \(f\) and \(g\) are disjoint, the condition holds vacuously.

## Equivalent diagonal formulation

Define \((f,g):M\times N\to P\times P\) on the [[differential-geometry/product-manifold|product manifold]]. Then \(f\pitchfork g\) exactly when \((f,g)\) is transverse to the diagonal submanifold \(\Delta_P\subset P\times P\). The difference-map formulation in tangent spaces is the differential of this diagonal condition.

## Fiber-product consequence

When \(f\pitchfork g\), the fiber product
\[
M\times_PN=\{(x,y)\in M\times N:f(x)=g(y)\}
\]
is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of \(M\times N\) of dimension \(\dim M+\dim N-\dim P\). Its [[differential-geometry/tangent-space|tangent space]] consists of pairs \((v,w)\) satisfying \(df_x(v)=dg_y(w)\) [Hirsch, Chapter 3](https://doi.org/10.1007/978-1-4684-9449-5).

## Examples and non-examples

If \(f\) is a submersion, then \(f\pitchfork g\) for every smooth \(g\), because \(df_x\) is surjective. Two constant maps with the same value in a positive-dimensional target are not transverse: both differential images are zero.

## Conventions and scope

For manifolds with boundary or corners, extra hypotheses are needed to control the boundaries and corners of the fiber product. The boundaryless setting in the core avoids silently asserting those stronger conclusions.

## References

1. M. W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 3, transversality and inverse images.
2. V. Guillemin and A. Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [AMS DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 2, transversality.
