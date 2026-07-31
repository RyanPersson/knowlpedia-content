+++
id = "differential-geometry/tubular-neighborhood"
title = "Tubular neighborhood"
kind = "definition"
summary = "A neighborhood of an embedded submanifold modeled by a neighborhood of the zero section in its normal bundle."
aliases = ["tubular neighborhood embedding", "normal neighborhood"]
domains = ["differential-geometry", "fiber-bundles"]
section_mode = "progressive"
+++

Let \(i:S\hookrightarrow M\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]] with [[differential-geometry/normal-bundle|normal bundle]] \(\nu\to S\). A **tubular neighborhood** of \(S\) in \(M\) consists of an open neighborhood \(U\subseteq\nu\) of the [[fiber-bundles/zero-section|zero section]] and a [[fiber-bundles/smooth-embedding|smooth embedding]] \(\Phi:U\to M\) such that \(\Phi(0_p)=i(p)\) for every \(p\in S\), and \(\Phi(U)\) is open in \(M\). Hence \(\Phi\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]] from \(U\) onto an open neighborhood of \(S\). Its differential in each normal fiber must induce the canonical normal direction modulo \(T_pS\).

## Construction from a metric

After choosing a Riemannian metric on \(M\), the normal bundle may be represented by the [[linear-algebra/orthogonal-complement|orthogonal complements]] \(T_pS^\perp\). The Riemannian [[fiber-bundles/exponential-map|exponential map]] sends sufficiently small normal vectors to \(M\) and restricts, with a radius allowed to vary over \(S\), to a tubular-neighborhood embedding [Lee, Chapter 10]. The resulting model depends on choices, although its germ has strong uniqueness properties.

## Geometric uses

Fiberwise scalar multiplication in \(\nu\) transports through \(\Phi\) to a smooth deformation retraction of \(\Phi(U)\) onto \(S\), after shrinking to a fiberwise star-shaped neighborhood if necessary. Tubular neighborhoods also make extension of sections, construction of [[fiber-bundles/thom-class|Thom classes]], and comparison of nearby submanifolds local problems on a [[fiber-bundles/vector-bundle|vector bundle]].

## Examples and scope

For the standard inclusion \(\mathbb R^k\subset\mathbb R^n\), the normal bundle is \(\mathbb R^k\times\mathbb R^{n-k}\), and addition gives a global tubular model. A tubular neighborhood is more than an arbitrary open neighborhood of \(S\): it includes a specified identification with normal-bundle data and must agree with the inclusion along the zero section.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, normal bundles and tubular neighborhoods.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, vector bundles and tubular neighborhoods.
