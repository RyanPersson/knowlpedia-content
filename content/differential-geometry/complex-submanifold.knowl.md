+++
id = "differential-geometry/complex-submanifold"
title = "Complex submanifold"
kind = "definition"
summary = "A subset of a complex manifold that is locally a complex coordinate subspace."
aliases = ["holomorphic submanifold", "complex analytic submanifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] of complex dimension \(n\). A subset \(Y\subseteq X\) is a **complex submanifold of complex dimension \(k\)** if every \(p\in Y\) has a [[differential-geometry/complex-coordinate-chart|complex chart]] \((U,\varphi)\) of \(X\), with \(\varphi(p)=0\), such that
\[
\varphi(U\cap Y)=\varphi(U)\cap(\mathbb C^k\times\{0\}) .
\]
The induced charts make \(Y\) a complex manifold, and its inclusion into \(X\) is [[differential-geometry/holomorphic-map|holomorphic]]. In particular, \(Y\) is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of the underlying [[fiber-bundles/smooth-manifold|smooth manifold]], of real dimension \(2k\) and real codimension \(2(n-k)\).

## Equivalent formulation

An injective holomorphic immersion \(i:Y\to X\) whose underlying map is a topological embedding identifies \(Y\) biholomorphically with a complex submanifold of \(X\). Conversely, every complex submanifold inclusion has these properties. The local coordinate form follows from the holomorphic constant-rank theorem [Wells, Chapter I, §3](https://doi.org/10.1007/978-0-387-73892-5).

## Tangent spaces and local equations

For \(p\in Y\), the inclusion identifies the [[differential-geometry/tangent-space|tangent space]] \(T_pY\) with a complex-linear subspace of \(T_pX\). Locally, a codimension-\(r\) complex submanifold is the common zero set of \(r\) holomorphic functions whose complex differentials are linearly independent along that zero set.

## Examples and non-examples

A complex linear subspace of \(\mathbb C^n\) and the graph of a holomorphic map are complex submanifolds. The real line \(\mathbb R\subset\mathbb C\) is a smooth embedded submanifold but not a complex submanifold: its real tangent line is not preserved by multiplication by \(i\).

## Conventions and scope

A complex analytic subset may have singular points and therefore need not be a complex submanifold. “Complex analytic submanifold” in the alias list refers only to the nonsingular, locally coordinate-linear notion defined here.

## References

1. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §3, holomorphic maps and submanifolds.
2. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Springer DOI record](https://doi.org/10.1007/b137952). Relevant: §2.1, complex manifolds and holomorphic submanifolds.
