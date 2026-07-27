+++
id = "differential-geometry/tangent-space"
title = "Tangent Space"
kind = "knowl"
summary = "The vector space of derivations at a point of a smooth manifold."
aliases = ["tangent-space", "Tangent Space"]
domains = ["differential-geometry"]
legacy_source_path = "differential-geometry/tangent-space.md"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], \(p\in M\), and \(C^\infty_p(M)\) the algebra of germs of smooth real-valued functions at \(p\). The **tangent space** \(T_pM\) is the [[linear-algebra/vector-space|vector space]] of linear maps
\[
v: C^\infty_p(M)\to \mathbb{R}
\]
that satisfy the Leibniz rule
\[
v(fg)=v(f)\,g(p)+f(p)\,v(g).
\]
Such maps are called derivations, or tangent vectors at \(p\).

## Coordinate description
Given a chart \((U,x)\) with \(p\in U\) and \(x=(x^1,\dots,x^n)\), there are distinguished tangent vectors \(\left.\frac{\partial}{\partial x^i}\right|_p\) defined by
\[
\left.\frac{\partial}{\partial x^i}\right|_p(f)=\frac{\partial (f\circ x^{-1})}{\partial u^i}\Big|_{u=x(p)}.
\]
These form a [[algebra-modules/basis-module|basis]] of \(T_pM\), so \(\dim T_pM = \dim M\).

## Curve viewpoint
Equivalently, \(T_pM\) can be described using equivalence classes of smooth curves \(\gamma:(-\epsilon,\epsilon)\to M\) with \(\gamma(0)=p\), where \(\gamma_1\sim\gamma_2\) if they have the same first derivative in any (hence every) chart.

## Examples
If \(M=\mathbb{R}^n\), then \(T_p\mathbb{R}^n\cong \mathbb{R}^n\) canonically, and derivations correspond to directional derivatives (see [[real-analysis/derivative|derivative]]).
