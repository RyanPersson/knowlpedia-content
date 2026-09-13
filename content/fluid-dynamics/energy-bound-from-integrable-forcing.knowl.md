+++
id = "fluid-dynamics/energy-bound-from-integrable-forcing"
title = "Energy bound from a time-integrable L2 force"
kind = "theorem"
summary = "The accumulated L2 size of the force bounds velocity and total dissipation without dividing by a possibly zero norm."
aliases = ["L1 time L2 force energy estimate"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/kinetic-energy-identity", "convex-analysis/holder-inequality-integrals", "real-analysis/nonnegative-square-root", "measure-theory/monotone-convergence-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose a solution satisfies the [[fluid-dynamics/kinetic-energy-identity|energy identity]] on \([0,T)\), and \(F(t)=\int_0^t\|f(r)\|_2\,dr\) is finite. Then
\[
\|u(t)\|_2\le\|u(0)\|_2+F(t),
\]
and
\[
\|u(t)\|_2^2+2\nu\int_0^t\|\nabla u(r)\|_2^2\,dr
\le\bigl(\|u(0)\|_2+F(t)\bigr)^2.
\]
If \(F(T)<\infty\), these give uniform energy and finite total dissipation up to the possibly excluded endpoint.

## Regularizing a vanishing norm

Set \(Y_\delta(t)=(\|u(t)\|_2^2+\delta^2)^{1/2}\). Drop dissipation in the differential identity and use Cauchy–Schwarz to obtain \(Y_\delta'\le\|f\|_2\). Integration and \(\delta\downarrow0\) prove the first bound. Insert it into the integrated energy identity: the work is at most \(\int_0^t F'(r)(\|u(0)\|_2+F(r))\,dr\). This gives the squared bound. Monotone convergence handles total dissipation as \(t\uparrow T\), without assuming regularity at \(T\).
