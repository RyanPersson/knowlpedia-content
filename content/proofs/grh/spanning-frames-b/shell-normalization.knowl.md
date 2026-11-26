+++
id = "proofs/grh/spanning-frames-b/shell-normalization"
title = "Normalization of integrals over positions"
kind = "definition"
summary = "The unit in which integrals over positions are measured: floor moduli of the level, a power of the kernel bound, and the squared norm of the correlation."
aliases = ["shell normalization"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.PlaceData.shellNormalization"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], let \(F\) be a place datum with level \(M\) and let \(W\colon G\to\mathbb{C}^I\) be a function. The **shell normalization** of \(W\) is the element of \([0,\infty]\)
\[
\mathsf{c}_F(W)\;=\;\Bigl(\prod_{l=0}^{\varrho-1}\lvert M\rvert_A^{\,k+1+2(\varrho-l-1)+\frac12}\Bigr)\cdot c_A^{\,\operatorname{rk}(X')\cdot\varrho}\cdot\lVert W\rVert_{\mathrm{corr}}^2 ,
\]
where the factors of the product are the [[?lean:New.Floors.PlaceData.floorModulus|floor moduli]] of the level, \(c_A\) is the kernel bound of the [[?lean:New.Floors.Place|place]], \(\operatorname{rk}(X')=\lvert\iota\rvert-2(2m+2)\) is the number of free orthonormal vectors, and
\[
\lVert W\rVert_{\mathrm{corr}}^2=\iint\bigl\lvert\langle W(x),W(y)\rangle\bigr\rvert^2\,d\vartheta(x)\,d\vartheta(y)
\]
is the [[?lean:New.Floors.PlaceData.pairingNormSq|squared norm of the correlation]] of \(W\), \(\vartheta\) being the convolution of all floor measures (which stands for integration over \(U\backslash G\)).

## Remarks

At the finite places the product of the floor moduli is the volume of the congruence subgroup of level \(M\) of the unipotent group. The normalization is the right-hand side, up to powers of the loss, of the bound for one frame, [[?lean:New.Floors.Gauge.headDensity_mul_lintegral_le_mul_pairingNormSq|the gain on a position ball]].

## References

1. Lean: `New.Floors.PlaceData.shellNormalization` in `src/New/Spanning/Frames/Shells.lean`.
