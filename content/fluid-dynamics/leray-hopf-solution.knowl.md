+++
id = "fluid-dynamics/leray-hopf-solution"
title = "Leray–Hopf solution"
kind = "definition"
summary = "An energy-class weak solution with weak time continuity, strong initial trace, and the global energy inequality."
aliases = ["Leray solution", "Leray–Hopf weak solution"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/weak-navier-stokes-solution", "fluid-dynamics/navier-stokes-energy-class", "functional-analysis/weakly-continuous-path", "fluid-dynamics/kinetic-energy-inequality", "partial-differential-equations/initial-datum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Fix \(T<\infty\), divergence-free [[partial-differential-equations/initial-datum|initial velocity]] \(u_0\in L^2(\mathbb R^3)\), and \(f\in L^1(0,T;L^2)\). A **Leray–Hopf solution** here is a [[fluid-dynamics/weak-navier-stokes-solution|weak Navier–Stokes velocity]] in the [[fluid-dynamics/navier-stokes-energy-class|energy class]] with [[functional-analysis/weakly-continuous-path|weak time continuity]] \(u\in C_w([0,T];L^2)\), \(u(t)\to u_0\) strongly in \(L^2\) as \(t\downarrow0\), and the [[fluid-dynamics/kinetic-energy-inequality|energy inequality]]
\[
\frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(\tau)\|_2^2\,d\tau
\leq\frac12\|u(s)\|_2^2+\int_s^t\!\int f\cdot u
\]
for \(s=0\), and for almost every \(s\in(0,T)\), for every \(t\in[s,T]\).

## Conventions and forcing

Some authors use “Leray solution” with only the inequality starting at zero. The time convention must be read in the particular statement. Other force classes are possible with a suitable dual pairing. An energy inequality does not assert uniqueness. Albritton, Brué and Colombo constructed distinct suitable Leray solutions with the same zero initial velocity and a force in \(L^1_tL^2_x\); their forcing has singular behavior at the initial endpoint. This result does not change the forcing hypotheses in a different problem.

## References

- [Albritton, Brué and Colombo, Non-uniqueness of Leray solutions of the forced Navier–Stokes equations](https://arxiv.org/abs/2112.03116).
