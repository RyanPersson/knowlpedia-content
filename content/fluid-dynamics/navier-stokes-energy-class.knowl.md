+++
id = "fluid-dynamics/navier-stokes-energy-class"
title = "Navier–Stokes energy class"
kind = "definition"
summary = "Velocity with essentially bounded kinetic energy and finite integrated squared spatial gradient."
aliases = ["energy space for Navier–Stokes"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["measure-theory/mixed-lebesgue-norm", "functional-analysis/weak-derivative", "functional-analysis/sobolev-space", "fluid-dynamics/kinetic-energy", "measure-theory/lp-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On \(\mathbb R^n\times(0,T)\), the **Navier–Stokes energy class** is
\[
u\in L^\infty(0,T;L^2(\mathbb R^n)),\qquad
\nabla u\in L^2(\mathbb R^n\times(0,T)),
\]
where \(\nabla u\) is the [[functional-analysis/weak-derivative|weak spatial gradient]] and the time-space norms are [[measure-theory/mixed-lebesgue-norm|mixed Lebesgue norms]]. For finite \(T\) this equals \(L^\infty_tL^2_x\cap L^2_tH^1_x\), with \(H^1=W^{1,2}\) the [[functional-analysis/sobolev-space|Sobolev space]]. It bounds [[fluid-dynamics/kinetic-energy|kinetic energy]] and integrated dissipation.

Here spatial \(L^2\) is the usual [[measure-theory/lp-space|Lebesgue space]] of square-integrable velocity components.

## What membership supplies

Membership is a function-space condition. It does not by itself assert the equation, a representative at every time, an initial trace, or an energy inequality. On an infinite interval the analogous local-in-time definition is imposed on each finite interval; global integrated dissipation is an additional requirement.
