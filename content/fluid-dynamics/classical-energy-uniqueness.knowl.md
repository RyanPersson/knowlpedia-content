+++
id = "fluid-dynamics/classical-energy-uniqueness"
title = "Classical uniqueness from difference energy"
kind = "theorem"
summary = "An integrable reference gradient controls the squared L2 difference of regular solutions with common forcing."
aliases = ["smooth Navier–Stokes uniqueness", "periodic Navier–Stokes uniqueness"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-difference-equation", "fluid-dynamics/solenoidal-integration-cancellation", "functional-analysis/sobolev-embedding-bounded-derivatives", "differential-equations/gronwall-inequality", "fluid-dynamics/pressure-gradient-identification", "functional-analysis/fourier-sobolev-space", "fluid-dynamics/relative-kinetic-energy", "topology/flat-torus"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For two smooth periodic incompressible Navier–Stokes solutions with common force and viscosity, or smooth whole-space solutions \(u,v\in C([0,T];H^3(\mathbb R^3))\) with common \(f\in C([0,T];L^2)\), let \(w=v-u\). Then
\[
\|w(t)\|_2^2\le\|w(0)\|_2^2
\exp\!\left(2\int_0^t\|\nabla u(s)\|_\infty\,ds\right).
\]
In particular, the same initial velocity gives the same velocity on \([0,T]\). This is the **classical difference-energy uniqueness estimate** obtained from [[differential-equations/gronwall-inequality|Gronwall's inequality]].

## Energy calculation

The difference equation and integration cancellations give
\[
\frac12\frac d{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int(w\cdot\nabla)u\cdot w
\le\|\nabla u\|_\infty\|w\|_2^2.
\]
On the torus, smoothness and periodicity justify the integration. In the whole-space case, \(H^3\) controls \(u,\nabla u,v,\nabla v\) in \(L^\infty\); the quadratic tensor lies in \(L^2\), and the identified canonical pressure lies in \(L^2\). Smooth approximation and expanding cutoffs justify the pairing and cancellation. The reference gradient is bounded on the compact time interval, so Gronwall applies. Equality of velocities determines pressure only up to a function of time.
