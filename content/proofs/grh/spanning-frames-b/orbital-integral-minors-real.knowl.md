+++
id = "proofs/grh/spanning-frames-b/orbital-integral-minors-real"
title = "A nonzero orbital integral bounds the leading minors"
kind = "theorem"
summary = "If the orbital integral of a cut Bessel function at gamma is nonzero, the leading minors of the frame Gram matrix of gamma are at most rho^(9n)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IsCutBessel.norm_leadingMinor_le_of_besselOrbitalIntegral_ne_zero"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
proof_status = "full"
+++

**Theorem.** In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(F\) be a [[proofs/grh/spanning-frames-b/cut-bessel-function-real|cut Bessel function]] of box radius \(\rho\), and let \(\gamma\in G_1\) be such that the [[?lean:New.besselOrbitalIntegral|orbital integral]]
\[
J(\gamma)=\int_{G_1}F(y)\otimes\overline{F(\gamma^{-1}y)}\,dy\ \in\mathbb{C}^{I\times I}
\]
(Haar measure; coordinates \(\int F_i(y)\overline{F_{i'}(\gamma^{-1}y)}\,dy\)) is not zero. Then for every \(0\le j\le n\) the leading \(j\times j\) minor of the [[?lean:New.realFrameGram|frame Gram matrix]] \(Z(\gamma)=\bigl(h(f_a,\gamma f_b)\bigr)_{a,b}\) of the frame \(f=(e_0,\dots,e_{\varrho-1},z)\) satisfies
\[
\lvert\det Z(\gamma)_{<j,<j}\rvert\le\rho^{9n}.
\]

## Proof

\(F\) is a cut Bessel function for the place datum at \(\mathbb{C}\). The general statement [[?lean:New.Floors.Gauge.leadingMinor_mem_ofSize_of_besselOrbitalIntegral_ne_zero|a nonzero orbital integral bounds the size of the leading minors]], applied to the gauge \(\Gamma_\rho\) of size \(\rho\), says that each leading minor has size \(9n\) for \(\Gamma_\rho\), which by the definition of that gauge is the inequality \(\lvert\cdot\rvert\le\rho^{9n}\). (The general statement holds because \(J(\gamma)\ne0\) gives a point \(y\) with \(F(y)\ne0\ne F(\gamma^{-1}y)\); both points are then near at every floor, and the minors are computed from two elements of the box.)

## References

1. Lean: `New.Floors.IsCutBessel.norm_leadingMinor_le_of_besselOrbitalIntegral_ne_zero` in `src/New/Spanning/Frames/RealShells.lean`.
