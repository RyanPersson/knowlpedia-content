+++
id = "differential-geometry/complex-coordinate-chart"
title = "Complex coordinate chart"
kind = "definition"
summary = "A homeomorphism from an open manifold neighborhood to an open subset of complex Euclidean space."
aliases = ["holomorphic chart", "complex chart", "complex coordinate system"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[topology/topological-manifold|topological manifold]] of real dimension \(2n\). A **complex coordinate chart** on \(M\) is a pair \((U,\varphi)\) in which \(U\subseteq M\) is open and
\[
\varphi=(z^1,\ldots,z^n):U\longrightarrow \varphi(U)\subseteq\mathbb C^n
\]
is a [[topology/homeomorphism|homeomorphism]] onto an open subset. The functions \(z^j\) are the complex coordinates of the chart. A single complex chart supplies local complex coordinates but not a complex structure on all of \(M\); that requires an atlas of such charts whose overlap maps are holomorphic.

## Compatibility of charts

Two complex charts \((U,\varphi)\) and \((V,\psi)\) are compatible when the transition map
\[
\psi\circ\varphi^{-1}:\varphi(U\cap V)\longrightarrow\psi(U\cap V)
\]
is [[differential-geometry/holomorphic-map|holomorphic]]. Its inverse is then holomorphic as well, so compatibility is symmetric. A maximal compatible atlas defines a [[differential-geometry/complex-manifold|complex manifold]]; the atlas, rather than any preferred coordinate system, is the intrinsic structure [Huybrechts, Chapter 2, §2.1](https://doi.org/10.1007/b137952).

## Coordinate expressions

A map between complex manifolds is holomorphic precisely when its coordinate representative is holomorphic for charts about each source point and its image. Because transition maps are biholomorphic, this test is independent of the selected compatible charts. Coordinate vector fields and differentials transform by complex-linear [[real-analysis/jacobian-matrix|Jacobian matrices]].

## Conventions and scope

Complex dimension \(n\) corresponds to real dimension \(2n\). Some authors call only members of a specified [[differential-geometry/complex-atlas|complex atlas]] “holomorphic charts”; here that phrase is an alias for a complex coordinate chart understood in the context of a compatible atlas.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Springer DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 2, §2.1, complex manifolds, charts, and holomorphic maps.
2. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §1.
