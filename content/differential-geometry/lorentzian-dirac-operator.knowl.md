+++
id = "differential-geometry/lorentzian-dirac-operator"
title = "Lorentzian Dirac operator"
kind = "definition"
summary = "The first-order hyperbolic-type operator obtained by Clifford contraction of the Lorentzian spin connection."
aliases = ["spacetime Dirac operator", "pseudo-Riemannian spin Dirac operator"]
domains = ["differential-geometry", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/lorentzian-spinor-bundle", "fiber-bundles/spin-connection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,g)\) be a Lorentzian spin manifold, \(S\to M\) its
[[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor bundle]],
and \(\nabla^S\) its [[fiber-bundles/spin-connection|spin connection]]. The **Lorentzian Dirac operator** is
Clifford contraction of the covariant derivative:
\[
D_g=c\circ\nabla^S:
\Gamma^\infty(S)\longrightarrow\Gamma^\infty(S).
\]
If \((e_a)\) is a local pseudo-orthonormal frame and
\(\varepsilon_a=g(e_a,e_a)\in\{-1,+1\}\), then
\[
D_g\psi=\sum_a\varepsilon_a\,c(e_a)\nabla^S_{e_a}\psi.
\]
This formula is independent of the chosen pseudo-orthonormal frame.

## Principal symbol

Ignoring the conventional factor of \(i\) used in some symbol conventions,
the principal symbol at a covector \(\xi\) is
\[
\sigma_1(D_g)(x,\xi)=c(\xi^\sharp).
\]
With \(c(v)^2=-g(v,v)\), it satisfies
\[
\sigma_1(D_g)(x,\xi)^2
=-g_x^{-1}(\xi,\xi)\operatorname{id}_{S_x}.
\]
Thus \(D_g\) is nonelliptic: its nonzero characteristic covectors are exactly
the null covectors. Its square has the principal symbol of a
[[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic
operator]].

## Cauchy problem

On a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]], compactly supported initial spinor data on
a smooth spacelike [[differential-geometry/cauchy-hypersurface|Cauchy hypersurface]] determine a unique solution with
finite propagation speed. This is the
[[mathematical-physics/cauchy-problem-for-the-lorentzian-dirac-operator|Cauchy
theorem for the Lorentzian Dirac operator]].

## Scope

The Lorentzian Dirac operator is the signature-\((1,n-1)\) counterpart of the
Riemannian spin [[noncommutative-geometry/dirac-operator|Dirac operator]], but
their analytic theories differ. The flat model is the
[[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]].
Choices of invariant spinor pairing and [[differential-geometry/time-orientation|time orientation]] are required before
formulating formal-adjoint or Hilbert-space statements.

## References

1. Helga Baum, *Spin-Strukturen und Dirac-Operatoren über
   pseudoriemannschen Mannigfaltigkeiten*, Teubner, 1981. [Bibliographic
   record](https://zbmath.org/0476.53047). Relevant: Chapters 2–3.
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on
   Lorentzian Manifolds and Quantization*, European Mathematical Society,
   2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.3
   and 3.4.
