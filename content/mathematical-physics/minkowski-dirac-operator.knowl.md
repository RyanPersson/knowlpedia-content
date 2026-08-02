+++
id = "mathematical-physics/minkowski-dirac-operator"
title = "Minkowski Dirac operator"
kind = "definition"
summary = "The flat Lorentzian first-order operator obtained by Clifford contraction of ordinary differentiation."
aliases = ["flat Lorentzian Dirac operator", "free Dirac operator", "slash partial"]
domains = ["mathematical-physics", "differential-geometry"]
section_mode = "progressive"
+++

On four-dimensional [[mathematical-physics/minkowski-spacetime|Minkowski spacetime]], choose a constant [[differential-geometry/dirac-spinor|complex spinor]] module \(S\) and [[mathematical-physics/gamma-matrices|gamma matrices]] \(\gamma^\mu=c(dx^\mu)\) satisfying
\[
\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=-2\eta^{\mu\nu}I,
\qquad \eta=\operatorname{diag}(-1,1,1,1).
\]
The **Minkowski Dirac operator** is
\[
D_{\mathrm M}=c\circ d=\gamma^\mu\partial_\mu
\]
on smooth spinor fields \(\psi:\mathbb R^{1,3}\to S\).

## Square and symbol

Because the matrices are constant and partial derivatives commute,
\[
D_{\mathrm M}^{\,2}
=-\eta^{\mu\nu}\partial_\mu\partial_\nu
=\Box_\eta.
\]
Its [[differential-geometry/principal-symbol|principal symbol]] is \(c(\zeta)\), and
\[
c(\zeta)^2=-\eta^{-1}(\zeta,\zeta)I.
\]
It is invertible away from the null cone but singular at nonzero null covectors. Thus this Lorentzian operator is not elliptic; its square is [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic]].

## Relation to gamma-matrix conventions

With the metric convention above, the matrices \(\gamma^\mu=c(dx^\mu)\) square to \(+I\) in the time direction and \(-I\) in spatial directions. This is the same matrix relation often written with the mostly-minus metric \(-\eta\). Switching metric or Clifford sign conventions changes the displayed anticommutator and may insert factors of \(i\).

## Curved analogue

On a [[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor bundle]], ordinary differentiation is replaced by the [[fiber-bundles/spin-connection|spin connection]] and \(D_g=c\circ\nabla^S\). Squaring then produces curvature terms. By contrast, the Riemannian [[noncommutative-geometry/dirac-operator|spin Dirac operator]] is elliptic and belongs to a different analytic theory.

## References

1. Helga Baum, *Spin-Strukturen und Dirac-Operatoren über pseudoriemannschen Mannigfaltigkeiten*, Teubner, 1981. [Bibliographic record](https://zbmath.org/0476.53047). Relevant: Chapter 3.
2. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley, 1995. [Publisher record](https://doi.org/10.1201/9780429503559). Relevant: Chapters 3–4.
