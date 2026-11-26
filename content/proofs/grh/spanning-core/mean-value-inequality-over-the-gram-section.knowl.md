+++
id = "proofs/grh/spanning-core/mean-value-inequality-over-the-gram-section"
title = "The mean value inequality over the Gram matrix of two frames"
kind = "theorem"
summary = "The integral of f(s' gamma_Z s) over the fixer of the frame twice and over Z in the open cell, with density c_G g(Z)^(k-1), is at most the Haar integral of f."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.lintegral_gramSection_le", "New.RealPlace.leGramFibre_gramSectionMeasure", "New.RealPlace.gramSectionMeasure", "New.RealPlace.enorm_det_pow_mul_sphereMass", "New.RealPlace.setLIntegral_openCell_frame_coords_le"]
lean_files = ["src/New/Spanning/Bessel/MeanValue.lean"]
proof_status = "outline"
+++

**Theorem (mean value inequality).** Let \(G_1\) be the real unitary group of a [[?lean:New.Shape|shape]] with Haar measure \(d\gamma\) ([[?lean:New.haarU|the volume of \(G_1\)]]), \(R^\circ\) the fixer of the frame with its measure \(ds\) (see [[proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix|coordinates on frames]]), \(\Omega\) the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]] with Lebesgue measure \(dZ\), \(\gamma_Z\) the [[proofs/grh/spanning-core/gram-section|Gram section]], \(\mathsf g\) the real [[proofs/grh/spanning-core/frame-discriminant|frame discriminant]], \(k=\lvert\kappa\rvert\) and \(c_G\) the [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|open cell constant]]. For every measurable \(f\colon G_1\to[0,\infty]\),
\[
\int_\Omega c_G\,\mathsf g(Z)^{k-1}\int_{R^\circ}\!\int_{R^\circ}f\bigl(s'\gamma_Zs\bigr)\,ds\,ds'\,dZ\ \le\ \int_{G_1}f(\gamma)\,d\gamma .
\]

## Proof

*Outline.* Let \(\lambda\) be the **Gram section measure** on \(G_1\): the image under \((Z,s)\mapsto s\gamma_Z\) of the measure \(\frac{2\pi^k}{(k-1)!}\,2^{-(\varrho+1)}\,\mathsf g(Z)^{k-1}\,dZ\,ds\) on \(\Omega\times R^\circ\).

*Step 1: \(\lambda\) is at most the fibre measure of the Gram map.* The notion [[?lean:New.LeGramFibre|`LeGramFibre`]] (library) says, for a measure \(l\) on tuples \(Y\): if \(K\ge0\) is lower semicontinuous and \(\int_{T(Y)\in S}K\,dY\le C\operatorname{vol}(S)\) for all open sets \(S\) of Gram coordinates inside some neighbourhood of the Gram matrix \(T_0\) of the frame, then \(\int K\,dl\le C\). We claim this for the image \(l\) of \(\lambda\) under \(g\mapsto gF\). Parametrise tuples by \((t,Z,s)\mapsto s\,y(T')\,Z\), \(T'=(Z^{-1})^*T(t)Z^{-1}\), with weight \(w(t,Z)=\lvert\det Z\rvert^{2(k-1)}2^{-\varrho}\sigma_k(1+T'_{\varrho+1,\varrho+1})\). By [[proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix|the coordinate lemma]] (2), for each \(Z\in\Omega\) the integral of \(w\cdot K\) over \((t,s)\) equals \(\int K(JFZ+Rp)\,dp\); and \((Z,p)\mapsto JFZ+Rp\) is a measure preserving bijection onto all tuples (library statement `New.measurePreserving_mul_mul_add_mul`), so integrating over \(Z\in\Omega\) gives at most \(\int K(Y)\,dY\). Where \(w\ne0\) the tuple has Gram coordinates \(t\). At \(t=t_0\) (the coordinates of \(T_0\)) the tuple is \(s\gamma_ZF\) and, since \(\lvert\det Z\rvert^{2(k-1)}\sigma_k(\nu(Z)^2)=\frac{\pi^k}{(k-1)!}\mathsf g(Z)^{k-1}\), the weight is the density of \(\lambda\); and both are continuous in \(t\) at \(t_0\) for \(Z\in\Omega\). The library criterion `New.LeFibreMeasure.of_coordinates` turns exactly these facts into the claim. (The passage from the inequality for all \(t\) to the fibre over \(t_0\) is inside that criterion and is not reproduced here.)

*Step 2.* The library theorem `New.LeGramFibre.mconv_fixerHaar_le` states that a measure on \(G_1\) whose image on frames is at most the fibre measure has convolution with \(ds\) on the right at most \(\dfrac{\operatorname{vol}U(r)}{\operatorname{vol}U(k)\,2^{\varrho+1}}\) times Haar measure. Applying it to \(\lambda\):
\[
\int_\Omega\frac{2\pi^k}{(k-1)!\,2^{\varrho+1}}\mathsf g(Z)^{k-1}\int\!\!\int f(s'\gamma_Zs)\,ds\,ds'\,dZ=\int f\,d(\lambda*ds)\le\frac{\operatorname{vol}U(r)}{\operatorname{vol}U(k)2^{\varrho+1}}\int f\,d\gamma ,
\]
and dividing by the constant on the right gives the theorem, since \(c_G=\frac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}\cdot\frac{2\pi^k}{(k-1)!}\). \(\blacksquare\)

## Remarks

The Lean file head compares the fibre measures of the Gram map with Siegel, Über die analytische Theorie der quadratischen Formen, Ann. of Math. 36 (1935).

## References

1. Lean: `New.RealPlace.lintegral_gramSection_le`, `New.RealPlace.leGramFibre_gramSectionMeasure`, `New.RealPlace.gramSectionMeasure` in `src/New/Spanning/Bessel/MeanValue.lean`.
