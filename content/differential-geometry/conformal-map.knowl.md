+++
id = "differential-geometry/conformal-map"
title = "Conformal map"
kind = "definition"
summary = "A smooth map that pulls the target Riemannian metric back to a positive pointwise multiple of the source metric."
aliases = ["conformal mapping", "conformal immersion", "angle-preserving map"]
domains = ["differential-geometry", "complex-analysis"]
section_mode = "progressive"
+++

Let \((M,g)\) and \((N,h)\) be [[differential-geometry/riemannian-manifold|Riemannian manifolds]]. A **conformal map** in the convention used here is a smooth map \(f:M\to N\) for which there is a smooth positive function \(\lambda:M\to(0,\infty)\) satisfying
\[
f^*h=\lambda^2g.
\]
Equivalently, every tangent map \(df_p\) multiplies all lengths by the same factor \(\lambda(p)\), and therefore preserves angles. Positive-definiteness forces \(df_p\) to be injective, so such a map is a smooth immersion and \(\dim M\leq\dim N\).

## Equal dimensions and isometries

When \(\dim M=\dim N\), a conformal map is a local diffeomorphism. If it is globally a diffeomorphism, it is a **conformal diffeomorphism** or **conformal transformation**. The special case \(\lambda=1\) is a [[differential-geometry/riemannian-isometric-immersion|Riemannian isometric immersion]].

Some authors use “conformal map” only for equal-dimensional local diffeomorphisms or homeomorphisms and call the general pullback-preserving map above a **conformal immersion**. The displayed metric equation is the house convention; it makes the dimension and rank requirements unambiguous.

## Oriented surfaces and holomorphic maps

An orientation and Riemannian metric on a real surface determine the complex structure whose multiplication by \(i\) rotates tangent vectors through \(+\pi/2\). Conversely, a [[differential-geometry/riemann-surface|Riemann surface]] determines an oriented conformal class of Riemannian metrics.

For maps between oriented Riemannian surfaces, a conformal local diffeomorphism is orientation-preserving exactly when it is [[differential-geometry/holomorphic-map|holomorphic]] for the associated Riemann-surface structures. It is orientation-reversing exactly when it is antiholomorphic. Thus “conformal” alone does not encode orientation.

A nonconstant holomorphic map may have critical points. It is conformal in the strict positive-factor sense away from those points, but at a critical point its pullback metric has zero scale factor. Such a map is often called **weakly conformal** rather than conformal everywhere.

## Classical complex-analysis examples

The [[complex-analysis/riemann-mapping-theorem|Riemann mapping theorem]] produces a biholomorphic—and hence orientation-preserving conformal—diffeomorphism from every nonempty proper [[topology/simply-connected-space|simply connected]] plane domain to the unit disc. Every [[complex-analysis/mobius-transformation|Möbius transformation]] is an orientation-preserving conformal diffeomorphism of the [[complex-analysis/riemann-sphere|Riemann sphere]]. In fact, the [[complex-analysis/mobius-transformation-group|Möbius group]] is the full orientation-preserving conformal diffeomorphism group of the round sphere; adjoining anti-Möbius maps gives the orientation-reversing component.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Riemannian metrics, pullbacks, and conformal changes.
2. Otto Forster, *Lectures on Riemann Surfaces*, Graduate Texts in Mathematics 81, Springer, 1981. [DOI record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: §§1–2, holomorphic maps and conformal structures on surfaces.
3. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapters 3–4, conformal maps, Möbius transformations, and the Riemann mapping theorem.
