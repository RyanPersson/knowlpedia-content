+++
id = "fiber-bundles/gauge-transformation"
title = "Gauge transformation"
kind = "knowl"
summary = "A principal bundle automorphism that covers the identity map on the base manifold."
aliases = ["gauge-transformation", "Gauge transformation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/gauge-transformation.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. A **gauge transformation** of \(P\) is a [[fiber-bundles/principal-bundle-automorphism|principal bundle automorphism]] covering \(\operatorname{id}_M\): a smooth diffeomorphism \(\Phi:P\to P\) satisfying
\[
\pi\circ\Phi=\pi,
\qquad
\Phi(p\cdot g)=\Phi(p)\cdot g
\]
for every \(p\in P\) and \(g\in G\).

Every gauge transformation can be written uniquely in the form
\[
\Phi(p)=p\cdot u(p)
\]
for a smooth map \(u:P\to G\) satisfying the conjugation-equivariance condition
\[
u(p\cdot g)=g^{-1}u(p)g.
\]
Such maps \(u\) are the same data as smooth sections of the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]] \(\mathrm{Ad}(P)\) (often described explicitly in [[fiber-bundles/section-of-ad|sections of Ad(P)]]).

## Examples
1. **Trivial bundle.** For \(P=M\times G\), any smooth map \(g:M\to G\) defines a gauge transformation by
   \[
   \Phi(x,h)=(x,\,g(x)\,h).
   \]
2. **Abelian structure group.** If \(G\) is abelian (e.g. \(U(1)\)), the conjugation condition on \(u\) becomes \(u(p\cdot g)=u(p)\), so gauge transformations correspond to smooth \(G\)-valued functions on \(M\).
3. **Frames of a vector bundle.** For the frame bundle of a rank-\(n\) vector bundle \(E\to M\), gauge transformations correspond to bundle automorphisms of \(E\) covering \(\mathrm{id}_M\) (locally given by \(GL(n)\)-valued functions acting on frames).
