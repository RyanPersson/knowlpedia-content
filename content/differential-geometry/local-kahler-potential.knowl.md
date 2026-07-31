+++
id = "differential-geometry/local-kahler-potential"
title = "Local Kähler potential"
kind = "definition"
summary = "A real smooth function whose complex Hessian is a given Kähler form on a coordinate neighborhood."
aliases = ["Kähler potential", "local potential for a Kähler form"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(\omega\) be a [[differential-geometry/kahler-form|Kähler form]] on a [[differential-geometry/complex-manifold|complex manifold]] \(X\), and let \(U\subseteq X\) be open. A **local Kähler potential** for \(\omega\) on \(U\) is a real-valued smooth function \(\varphi:U\to\mathbb R\) satisfying
\[
\omega|_U=i\partial\bar\partial\varphi.
\]
Equivalently, using the [[differential-geometry/d-c-operator|\(d^c\)-operator]] convention \(d^c=i(\bar\partial-\partial)\), one has \(\omega|_U=\tfrac12dd^c\varphi\). The complex Hessian \((\partial^2\varphi/\partial z^j\partial\bar z^k)\) must be positive definite. Every Kähler form admits such potentials on sufficiently small coordinate neighborhoods.

## Nonuniqueness

If \(\varphi\) and \(\psi\) are potentials for the same form on \(U\), then
\[
\partial\bar\partial(\varphi-\psi)=0.
\]
Thus their difference is pluriharmonic. On a simply connected coordinate neighborhood, it is locally the real part of a holomorphic function. Adding a constant or the real part of a holomorphic function therefore leaves the Kähler form unchanged. Potentials are local scalar descriptions, not canonical global functions.

## Examples

On \(\mathbb C^n\),
\[
\varphi(z)=\sum_{j=1}^n|z^j|^2
\]
is a potential for the standard form \(i\sum_j dz^j\wedge d\bar z^j\). On the affine chart of [[algebraic-geometry-foundations/projective-space|complex projective space]], \(\log(1+|z|^2)\) is a potential for the Fubini–Study form, up to the normalization chosen for that form.

## Local versus global

A global Kähler potential is much stronger than local existence. A positive-dimensional compact [[differential-geometry/kahler-manifold|Kähler manifold]] cannot satisfy \(\omega=i\partial\bar\partial\varphi\) globally, because \(\omega\) would be exact and [[differential-geometry/stokes-theorem|Stokes' theorem]] would force \(\int_X\omega^n=0\). Local potentials nonetheless glue up to pluriharmonic differences and encode the [[differential-geometry/kahler-metric|metric]] by
\[
g_{j\bar k}=\frac{\partial^2\varphi}{\partial z^j\partial\bar z^k}.
\]

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: §3.1, local potentials for Kähler metrics.
2. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §4, especially Example 4.4 and Theorem 4.8.
