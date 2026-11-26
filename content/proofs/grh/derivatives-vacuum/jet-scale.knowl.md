+++
id = "proofs/grh/derivatives-vacuum/jet-scale"
title = "The scale of theta Taylor series"
kind = "definition"
summary = "The area scale, the period factor and their combination, the jet scale, at whose multiples Taylor series of theta functions are taken."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.areaScale", "New.Parameters.periodFactor", "New.Parameters.jetScale"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]] with prime \(d\), let \(s\in\mathbb{N}\), and let \(E\) be the CM field \(K(\zeta)\) of \((P,s)\), with \(f\) infinite places. Let \(s_0\) be the [[?lean:New.Parameters.vacuumRoot|vacuum root]] (the principal \(f\)-th root of \(\chi_{\mathrm{fin}}(\alpha)^{-1}\)), \(u\) the [[proofs/grh/derivatives-vacuum/chowla-selberg-unit|Chowla–Selberg unit]] and \(\Omega_0\) the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|period of \(K\)]].

* The **area scale** is the positive real number \(c_A=\sqrt{2\pi/\sqrt d}\).
* The **period factor** is \(\varpi=s_0/u\in\mathbb{C}\).
* The **jet scale** is
\[ \lambda=\frac{\varpi\,c_A}{\Omega_0}=\frac{s_0}{u}\cdot\frac{\sqrt{2\pi/\sqrt d}}{\Omega_0}\in\mathbb{C}. \]

## Remarks

The area scale is the factor by which an element of \(E\) is multiplied at each infinite place when it is written in Fock coordinates: the real image of \(\gamma\in E^n\) has coordinate \(c_A\,\Phi_\tau(\gamma_k)\) at \((\tau,k)\). Since \(u\) is a unit at every \(p\)-adic place, \(\varpi\) and \(s_0\) have the same absolute value there; see [[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|the \(p\)-adic size of the period factor]].

## References

1. Lean: `New.Parameters.areaScale`, `New.Parameters.periodFactor`, `New.Parameters.jetScale` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
