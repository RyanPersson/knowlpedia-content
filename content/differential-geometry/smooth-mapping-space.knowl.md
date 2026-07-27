+++
id = "differential-geometry/smooth-mapping-space"
title = "Space of smooth maps"
kind = "definition"
summary = "The space of smooth maps from one smooth manifold to another, with topology and smooth structure specified by the chosen mapping-space framework."
aliases = ["smooth mapping space", "C-infinity mapping space", "C∞(M,N)"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] \(M\) and \(N\), the [[fiber-bundles/smooth-map|smooth maps]] from \(M\) to \(N\) form the **space of smooth maps**
\[
C^\infty(M,N)=\{f:M\to N\mid f\text{ is smooth}\}.
\]
As a set, it is the morphism set \(\operatorname{Hom}_{\mathbf{Man}}(M,N)\) in the [[differential-geometry/category-of-smooth-manifolds|smooth-manifold category]]. When \(M\) is compact, the standard mapping-space convention equips it with the compact-open \(C^\infty\) topology and an infinite-dimensional smooth-manifold structure; near \(f\), charts are modeled on smooth sections of \(f^*TN\). For noncompact \(M\), the phrase “mapping space” does not determine a unique topology or calculus without further conventions.

## Local model and tangent space

Choose a local addition on \(N\), such as one obtained from a Riemannian exponential map. It identifies maps near \(f\) with sections near the [[fiber-bundles/zero-section|zero section]] of the pullback [[fiber-bundles/tangent-bundle|tangent bundle]] \(f^*TN\). For compact \(M\), the tangent space at \(f\) is therefore
\[
T_fC^\infty(M,N)\cong\Gamma(M,f^*TN).
\]
If \(N=\mathbb R^q\), the mapping space is the [[functional-analysis/frechet-space|Fréchet space]] \(C^\infty(M,\mathbb R^q)\).

## Evaluation and composition

In the convenient smooth structure, evaluation
\[
\operatorname{ev}:C^\infty(M,N)\times M\to N,\qquad(f,x)\mapsto f(x),
\]
is smooth, and composition of [[fiber-bundles/smooth-map|smooth maps]] is smooth as a map between the corresponding mapping spaces. This cartesian-closed behavior is one reason to retain the infinite-dimensional smooth structure rather than only the underlying set [Kriegl and Michor, Chapter IX](https://doi.org/10.1090/surv/053).

## Topology and scope

For noncompact source manifolds, compact-open \(C^\infty\), weak Whitney, strong Whitney, and convenient mapping-space constructions can lead to different topological or manifold structures. Claims about continuity, tangent spaces, or smooth composition must therefore name the framework and hypotheses. The bare notation \(C^\infty(M,N)\) safely denotes only the set of smooth maps.

## References

1. Andreas Kriegl and Peter W. Michor, *The Convenient Setting of Global Analysis*, Mathematical Surveys and Monographs 53, AMS, 1997. [AMS record](https://bookstore.ams.org/surv-53/). Relevant: Chapter IX, manifolds of mappings.
2. Peter W. Michor, *Manifolds of Differentiable Mappings*, Shiva Mathematics Series 3, Shiva Publishing, 1980. [Author record](https://www.mat.univie.ac.at/~michor/listpubl.html). Relevant: mapping-space topologies and smooth structures.
