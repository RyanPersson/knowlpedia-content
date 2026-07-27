+++
id = "fiber-bundles/convention-principal-bundles-use-a-right-g-action-on-p"
title = "Convention: principal bundles use a right G-action on P"
kind = "knowl"
summary = "A principal G-bundle is written with a right action of G on the total space, matching standard connection and equivariance formulas."
aliases = ["convention-principal-bundles-use-a-right-g-action-on-p", "Convention: principal bundles use a right G-action on P"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/convention-principal-bundles-use-a-right-g-action-on-p.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]]. In this convention, a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] is a fiber bundle \(\pi:P\to M\) equipped with a **right** smooth action
\[
R: P\times G\to P,\qquad (p,g)\mapsto p\cdot g,
\]
which is free and transitive on each fiber, with \(M\cong P/G\).

## Consequences for formulas

All equivariance conditions are written with respect to this right action. In particular, for a [[fiber-bundles/principal-connection|principal connection]] \(1\)-form \(\omega\in\Omega^1(P;\mathfrak g)\) and \(g\in G\), the convention is
\[
(R_g)^*\omega=\mathrm{Ad}(g^{-1})\,\omega,
\]
and the induced vertical identification uses fundamental vector fields defined from the right action (see [[fiber-bundles/convention-fundamental-vector-field-x-is-defined-using-the-right-action|fundamental vector field convention]]).

This convention fixes the sign choices appearing in curvature and covariant differentiation identities.

## Examples
1. **Frame bundle.** For a rank-\(n\) vector bundle \(E\to M\), the frame bundle \(P=\operatorname{Fr}(E)\) carries a natural right \(\operatorname{GL}(n,\mathbb R)\)-action by postcomposition: \((u,g)\mapsto u\circ g\).

2. **Transition functions from local sections.** If \(s_i,s_j:U\to P\) are local sections, the transition map \(g_{ij}:U\to G\) is defined by \(s_j=s_i\cdot g_{ij}\).

3. **Gauge transformations.** A gauge transformation \(\Phi:P\to P\) satisfies \(\Phi(p\cdot g)=\Phi(p)\cdot g\).
