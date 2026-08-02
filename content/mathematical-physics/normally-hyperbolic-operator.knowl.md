+++
id = "mathematical-physics/normally-hyperbolic-operator"
title = "Normally hyperbolic operator"
kind = "definition"
summary = "A second-order operator whose principal symbol is the negative Lorentzian inverse metric times the identity."
aliases = ["normally hyperbolic differential operator", "wave operator on a vector bundle"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] and \(E\to M\) a smooth vector bundle. A second-order differential operator
\[
P:\Gamma^\infty(E)\longrightarrow\Gamma^\infty(E)
\]
is **normally hyperbolic** in the convention used here if its [[differential-geometry/principal-symbol|principal symbol]] is
\[
\sigma_2(P)(x,\xi)=-g_x^{-1}(\xi,\xi)\operatorname{id}_{E_x}.
\]
Equivalently, in local coordinates its second-order part is \(-g^{\mu\nu}\partial_\mu\partial_\nu\) times the identity.

The principal-symbol condition is local. It implies the [[mathematical-physics/connection-form-of-a-normally-hyperbolic-operator|unique connection form]] of \(P\), but global existence and causal support require additional hypotheses. On a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]] they are supplied by the [[mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators|Cauchy theorem]] and the [[mathematical-physics/existence-of-advanced-and-retarded-green-operators|Green-operator existence theorem]].

## Examples

The scalar [[mathematical-physics/dalembert-operator|d’Alembert operator]] is normally hyperbolic. Adding a mass term or any smooth endomorphism preserves normal hyperbolicity, so the [[mathematical-physics/klein-gordon-operator|Klein–Gordon operator]] is another example. The square of a Lorentzian [[noncommutative-geometry/dirac-type-operator|Dirac-type operator]] is normally hyperbolic up to the convention-dependent overall sign.

## Distinction from ellipticity

The symbol fails to be invertible on every nonzero null covector. A normally hyperbolic operator is therefore not [[differential-geometry/elliptic-differential-operator|elliptic]] on a Lorentzian manifold of dimension at least two. Elliptic boundary-value theory and hyperbolic initial-value theory are different analytic settings.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.5 and 3.2–3.4.
2. Nicolas Ginoux, *The Dirac Spectrum*, Springer, 2009. [Publisher record](https://doi.org/10.1007/978-3-642-01570-0). Relevant: Appendix A.
