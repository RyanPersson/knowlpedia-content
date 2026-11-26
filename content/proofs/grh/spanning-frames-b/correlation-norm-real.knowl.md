+++
id = "proofs/grh/spanning-frames-b/correlation-norm-real"
title = "The norm of the correlation of a cut Bessel function"
kind = "lemma"
summary = "The squared norm of the correlation of a cut Bessel function is at most lambda^2 |I|."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IsCutBessel.pairingNormSq_le"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
proof_status = "full"
+++

**Lemma.** In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(F\colon G_1\to\mathbb{C}^I\), \(I\ne\emptyset\), be a [[proofs/grh/spanning-frames-b/cut-bessel-function-real|cut Bessel function]]. Then
\[
\lVert F\rVert^2_{\mathrm{corr}}=\iint\lvert\langle F(x),F(y)\rangle\rvert^2\,d\vartheta(y)\,d\vartheta(x)\le\lambda^2\,\lvert I\rvert ,
\]
where \(\vartheta\) is the convolution of all floor measures of the place datum at \(\mathbb{C}\) and \(\lambda\) its Haar ratio.

## Proof

For a measurable function \(f\ge0\) on \(G_1\) that is invariant under left translation by \(U\), \(\int f\,d\vartheta=\lambda\int_{U\backslash G_1}f\). Since \(F(uy)=\psi(\sigma_0(u))F(y)\) with \(\lvert\psi\rvert=1\), the functions \(\lVert F\rVert^2\) and \(\lvert\langle v,F(\cdot)\rangle\rvert^2\) (\(v\in\mathbb{C}^I\) fixed) are of this kind. By the definition of a cut pair, \(\int_{U\backslash G_1}\lVert F\rVert^2\le\lvert I\rvert\), and by [[?lean:New.IsCutPair.lintegral_sq_inner_cut_le|the orthogonality relation for the cut function]], which uses the irreducibility of \(\mathrm{rep}\),
\[
\int_{U\backslash G_1}\lvert\langle v,F(y)\rangle\rvert^2\,dy\le\lVert v\rVert^2\qquad(v\in\mathbb{C}^I).
\]
Hence, taking \(v=F(x)\),
\[
\lVert F\rVert^2_{\mathrm{corr}}\le\int\lambda\lVert F(x)\rVert^2\,d\vartheta(x)=\lambda\cdot\lambda\int_{U\backslash G_1}\lVert F\rVert^2\le\lambda^2\lvert I\rvert .
\]

## References

1. Lean: `New.Floors.IsCutBessel.pairingNormSq_le` in `src/New/Spanning/Frames/RealShells.lean`.
