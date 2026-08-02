+++
id = "differential-geometry/smooth-fiber-product"
title = "Smooth fiber product"
kind = "definition"
summary = "The manifold of pairs having the same image under two transverse smooth maps."
aliases = ["fiber product of smooth manifolds", "transverse pullback manifold"]
domains = ["differential-geometry", "algebra-category-theory"]
section_mode = "progressive"
+++

Let \(f:M\to P\) and \(g:N\to P\) be
[[fiber-bundles/smooth-map|smooth maps]] between finite-dimensional
[[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary. If \(f\)
and \(g\) are
[[differential-geometry/transverse-smooth-maps|transverse]], their **smooth
fiber product** is
\[
M\times_PN=\{(x,y)\in M\times N:f(x)=g(y)\},
\]
equipped with the unique smooth structure for which it is the corresponding
[[differential-geometry/embedded-submanifold|embedded submanifold]] of the
[[differential-geometry/product-manifold|product manifold]] \(M\times N\).
The coordinate projections restrict to smooth maps
\(\pi_M:M\times_PN\to M\) and \(\pi_N:M\times_PN\to N\), and satisfy
\(f\pi_M=g\pi_N\).

## Tangent space and dimension

At \((x,y)\in M\times_PN\), with common image \(z\), its
[[differential-geometry/tangent-space|tangent space]] is the linear pullback
\[
T_{(x,y)}(M\times_PN)
=\{(v,w)\in T_xM\oplus T_yN:df_x(v)=dg_y(w)\}.
\]
Transversality makes the difference map
\((v,w)\mapsto df_x(v)-dg_y(w)\) surjective. The regular-level-set theorem
therefore gives
\[
\dim(M\times_PN)=\dim M+\dim N-\dim P.
\]

## Universal property

The square formed by the two projections is a
[[algebra-category-theory/pullback|categorical pullback]] in the category of
smooth manifolds: if smooth maps \(a:Q\to M\) and \(b:Q\to N\) obey
\(fa=gb\), there is a unique smooth map
\[
q\longmapsto(a(q),b(q))
\]
from \(Q\) to \(M\times_PN\) through which both maps factor. Thus the
set-theoretic equality condition and the smooth universal property agree once
the transverse submanifold structure exists.

## Examples and scope

If \(P\) is a point, the fiber product is the ordinary product \(M\times N\).
If \(g:N\hookrightarrow P\) is an embedded submanifold and \(f\) is transverse
to \(N\), then \(M\times_PN\) identifies with the inverse-image submanifold
\(f^{-1}(N)\).

**Warning.** Arbitrary pairs of smooth maps need not have a fiber product in
the category of manifolds. Manifolds with boundary or corners require
additional boundary-stratum transversality and depend on the chosen category.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6 on submanifolds, transversality, and fiber products.
2. Dominic Joyce, “On manifolds with corners,” in *Advances in Geometric Analysis*, Advanced Lectures in Mathematics 21, 2012, 225–258. [Preprint record](https://arxiv.org/abs/0910.3518). Relevant: §6 on transverse fiber products in a category of manifolds with corners.
