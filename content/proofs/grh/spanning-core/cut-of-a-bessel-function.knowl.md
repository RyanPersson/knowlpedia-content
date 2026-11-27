+++
id = "proofs/grh/spanning-core/cut-of-a-bessel-function"
title = "Cut of a Bessel function"
kind = "construction"
summary = "The product of a continuous Bessel function with a cutoff in the Bessel length at radius b^(6n+2)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.besselCutoff", "New.besselCut", "New.besselCutoff_mem_Icc", "New.besselCutoff_eq_one", "New.besselCutoff_eq_zero", "New.enorm_besselCut_le", "New.enorm_besselCut_sub_le", "New.inCut_of_besselCut_ne_zero", "New.lt_besselLength_of_besselCut_ne", "New.IsBesselFunction.besselCut", "New.IsBesselFunction.smul_of_invariant", "New.IsDecayMajorant.lintegral_sq_besselCut_sub_le"]
lean_files = ["src/New/Spanning/Bessel/CutTailBound.lean"]
+++

For \(R>0\) the **cutoff** of radius \(R\) is \(\chi_R(t)=\max(0,\min(1,2-2t/R))\): it is \(1\) for \(t\le R/2\), \(0\) for \(t\ge R\), linear in between, with values in \([0,1]\). For a continuous \(F\colon G_1\to\mathbb{C}^I\) and \(b>0\), the **cut** of \(F\) is
\[
F^\flat(y)=\chi_{b^{6n+2}}\bigl(\ell(y)\bigr)\,F(y),\qquad n=\varrho+1,
\]
with \(\ell\) the [[proofs/grh/spanning-core/bessel-length|Bessel length]] (continuous and left \(S\)-invariant).

## Properties

1. \(\lVert F^\flat(y)\rVert\le\lVert F(y)\rVert\) and \(\lVert F^\flat(y)-F(y)\rVert\le\lVert F(y)\rVert\).
2. \(F^\flat(y)\neq0\Rightarrow\ell(y)\le b^{6n+2}\); \(F^\flat(y)\ne F(y)\Rightarrow\ell(y)>\tfrac12b^{6n+2}\).
3. If \(F\) is a [[?lean:New.IsBesselFunction|Bessel function of type \(\mathrm{rep}\)]], so is \(F^\flat\) (more generally \(a\cdot F\) for any bounded continuous real \(a\) that is left \(S\)-invariant).
4. If \((F,F^\flat)\) has a [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|decay majorant]] \((w,a)\) for \((b,f)\) with \(b\ge2\), \(r\ge100\), \(f\ne0\), then \(\int\lVert F^\flat-F\rVert^2d\mu\le b^{-2r^3f}\lvert I\rvert\) (\(\mu\) the measure of \(\mathsf U\backslash G_1\)).

## Proof

(1)–(3) are immediate from \(0\le\chi\le1\) and the invariance of \(\ell\). (4) Where \(F^\flat(y)\ne F(y)\), \(\ell(y)>\frac12b^{6n+2}\), so the scaled length is \(\ge b\) and \(b^{3r^3f}\lVert F^\flat(y)-F(y)\rVert\le b^{3r^3f}\lVert F(y)\rVert\le w(y)\le a\). Hence \(b^{6r^3f}\lVert F^\flat-F\rVert^2\le a\,w\) everywhere, and integrating, \(b^{6r^3f}\int\lVert F^\flat-F\rVert^2d\mu\le a\int w\,d\mu\le b^{400r^2}\lvert I\rvert\le b^{4r^3f}\lvert I\rvert\), because \(100r^2\le r^3\le r^3f\). \(\blacksquare\)

## References

1. Lean: `New.besselCutoff`, `New.besselCut`, `New.IsBesselFunction.besselCut`, `New.IsDecayMajorant.lintegral_sq_besselCut_sub_le` in `src/New/Spanning/Bessel/CutTailBound.lean`.
