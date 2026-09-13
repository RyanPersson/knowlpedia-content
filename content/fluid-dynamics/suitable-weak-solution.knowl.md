+++
id = "fluid-dynamics/suitable-weak-solution"
title = "Suitable weak solution"
kind = "definition"
summary = "A local energy-class Navier–Stokes pair satisfying the local energy inequality."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/weak-navier-stokes-solution", "fluid-dynamics/local-energy-inequality", "fluid-dynamics/navier-stokes-energy-class", "measure-theory/mixed-lebesgue-norm", "functional-analysis/local-sobolev-space", "measure-theory/locally-integrable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On an open cylinder \(Q\subset\mathbb R^3\times\mathbb R\), a **suitable weak solution** is a [[fluid-dynamics/weak-navier-stokes-solution|weak Navier–Stokes pair]] with local [[fluid-dynamics/navier-stokes-energy-class|energy bounds]]
\[
u\in L^\infty_{t,\rm loc}L^2_{x,\rm loc}\cap L^2_{t,\rm loc}H^1_{x,\rm loc},
\qquad p\in L^{3/2}_{\rm loc}(Q),
\]
that obeys the [[fluid-dynamics/local-energy-inequality|local energy inequality]]. Here the bounds hold on every smaller cylinder compactly contained in \(Q\). For this definition take \(f\in L^2_{\rm loc}(Q)\); more general forces are allowed when the weak equation and the product \(f\cdot u\) are well defined and the particular theorem permits them.

The notation uses [[measure-theory/mixed-lebesgue-norm|mixed Lebesgue norms]] and [[functional-analysis/local-sobolev-space|local Sobolev spaces]]; the pressure has the specified [[measure-theory/locally-integrable-function|local integrability]] power.

## Local integrability of the energy flux

The three-dimensional Sobolev inequality and interpolation give \(u\in L^{10/3}_{\rm loc}(Q)\), hence \(u\in L^3_{\rm loc}(Q)\). Hölder's inequality makes \(pu\), \(|u|^2u\), and \(f\cdot u\) locally integrable. Suitability is a local condition; a global initial-value statement may also impose the Leray–Hopf conditions.

## References

- [Caffarelli, Kohn and Nirenberg, Partial regularity of suitable weak solutions (1982)](https://doi.org/10.1002/cpa.3160350604).
