+++
id = "differential-geometry/smooth-map-of-manifolds-with-boundary"
title = "Smooth map between manifolds with boundary"
kind = "definition"
summary = "A smooth map between manifolds with boundary has coordinate representatives that extend smoothly across the bounding hyperplanes."
aliases = ["boundary-smooth map", "smooth map on manifolds with boundary"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[differential-geometry/manifold-with-boundary|smooth manifolds with boundary]] of dimensions \(m\) and \(n\). A map \(F:M\to N\) is **smooth** if, for every \(p\in M\), there are [[differential-geometry/boundary-chart|boundary charts]] \((U,\varphi)\) at \(p\) and \((V,\psi)\) at \(F(p)\), with \(F(U)\subseteq V\), such that
\[
\psi\circ F\circ\varphi^{-1}:\varphi(U)\longrightarrow\psi(V)
\]
locally extends around \(\varphi(p)\) to a smooth map between open subsets of \(\mathbb R^m\) and \(\mathbb R^n\). This condition is independent of the chosen charts. It is the boundary analogue of a [[fiber-bundles/smooth-map|smooth map]] between manifolds without boundary.

## Equivalent local tests

It suffices to verify the extension condition in one pair of compatible charts around each point: smooth transition maps and their local Euclidean extensions transfer it to every other pair. Equivalently, each component of the coordinate representative is the restriction of an ordinary smooth real-valued function near every point of its half-space domain.

For real-valued functions on \(M\), no target boundary is involved: a function is smooth precisely when its expression in every boundary chart extends smoothly across the hyperplane \(x^m=0\).

## Structure and consequences

Identity maps are smooth, and composites of smooth maps between manifolds with boundary are smooth. Consequently these objects and maps form a category. The differential \(dF_p:T_pM\to T_{F(p)}N\) is defined using an extension and is independent of that extension. At a [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]], \(T_pM\) is still an \(m\)-dimensional [[linear-algebra/vector-space|vector space]] rather than a half-space.

Smoothness alone imposes no boundary-preservation condition. A smooth map may send an interior point to the boundary or a boundary point to the interior.

## Examples and non-examples

The inclusion \([0,\infty)\hookrightarrow\mathbb R\), \(x\mapsto x\), and the function \([0,\infty)\to\mathbb R\), \(x\mapsto\sqrt{1+x}\), are smooth because they extend across \(0\).

The function \(x\mapsto\sqrt{x}\) on \([0,\infty)\) is continuous and smooth on the interior, but it is not smooth as a map of manifolds with boundary: no smooth Euclidean extension near \(0\) can have its unbounded one-sided derivative.

## Conventions and scope

**Warning.** Some authors reserve “map of manifolds with boundary” for maps satisfying extra conditions such as \(F(\partial M)\subseteq\partial N\). Those are additional geometric requirements, not part of smoothness here. Manifolds with corners require compatible extensions from orthants and are outside this half-space definition.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 2, “Smooth Maps,” and the section on manifolds with boundary.
2. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [Publisher record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1, differentiable manifolds and maps on half-spaces.
