+++
id = "proofs/grh/spanning-frames-b/form-constant-real"
title = "Normalising constant of the forms at a real place"
kind = "definition"
summary = "The constant vol U(k) / vol U(r) / (lambda |I|)^2 by which the forms of a cut Bessel function are normalised."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IsCutBessel.formConst"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(F\colon G_1\to\mathbb{C}^I\) be a [[proofs/grh/spanning-frames-b/cut-bessel-function-real|cut Bessel function]]. Its **form constant** is the positive real number
\[
c_{\mathrm{form}}=\frac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}\cdot\frac{1}{(\lambda\,\lvert I\rvert)^2},
\]
where \(\lambda\) is the Haar ratio of the place datum at \(\mathbb{C}\) (so that the group measure is \(\lambda\) times the Haar measure of \(G_1\)). A *normalised* integral over positions is an integral against the group measure times the head density \(\kappa_j(p,q)\) and \(c_{\mathrm{form}}\).

## References

1. Lean: `New.Floors.IsCutBessel.formConst` in `src/New/Spanning/Frames/RealShells.lean`.
