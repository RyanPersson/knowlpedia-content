+++
id = "proofs/grh/spanning-frames-b/real-place-setting"
title = "Standing notation at a real place"
kind = "notation"
summary = "The group G1, the place datum and the gauges of size L at the place C, with the numerical hypotheses on the box radius and the ranks."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = []
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
+++

**Standing notation (the real place).** The place is \(A=\mathbb{C}\) with complex conjugation ([[?lean:New.Floors.complexPlace|the place \(\mathbb{C}\)]]): modulus \(\lvert x\rvert_A=\lvert x\rvert^2\), character \(\psi(x)=e^{x-\bar x}\), kernel bound \(c_A=\pi^2\). It lies over a real place of the totally real subfield and is called a *real place*. In the [[proofs/grh/spanning-frames-b/frames-setting|general notation]] the following choices are made.

* \(G_1\) is the [[?lean:New.Shape.G₁|unitary group]] over \(\mathbb{C}\) of the hermitian form made of \(\varrho\) hyperbolic planes \(\langle e_a,e_a^*\rangle\), a positive definite space \(X_0\) with orthonormal basis \((x_i)_{i\in\kappa}\), \(k=\lvert\kappa\rvert\), and a vector \(z\) with \(h(z,z)=-1\). Its rank is \(r=2\varrho+k+1\), and \(n=\varrho+1\). Norms of matrices are operator norms for the Euclidean norm in which this basis is orthonormal.
* The [[?lean:New.Floors.RealPlaceSizes|numerical hypotheses]] on a box radius \(\rho\), an exponent \(s\) and a base \(b\) are:
\[
\rho=b^{6n+2}\ge 8r,\qquad b\ge2,\qquad k=s+3n+6\ge n^7,\qquad s>10^9n^3,\qquad \varrho\ge10^8 .
\]
In particular \(\rho\ge4\).
* The [[?lean:New.Floors.RealPlaceSizes.complexData|place datum at \(\mathbb{C}\)]] has level \(M=1\), box \(K=\{x\in G_1:\lVert x\rVert\le\rho\}\), all of \(G_1\) as positions, close pairs \(\{(\omega_1,\omega_2):\lvert\omega_1\rvert^2+\lvert\omega_2\rvert^2<1\}\), \(m=0\) further hyperbolic pairs and the orthonormal vectors \(x_i\), \(i\ne k_0\). Its volume exponent is \(s\) and \(\operatorname{rk}X'=k-5\). Its group measure is \(\mathsf{M}=\lambda\cdot dy\) for the Haar measure \(dy\) of \(G_1\) and a constant \(0<\lambda<\infty\), the [[?lean:New.Floors.RealPlaceSizes.haarRatio|Haar ratio]], with \(\lambda\le\operatorname{vol}U(r)/\operatorname{vol}U(k)\); and for measurable left \(U\)-invariant \(f\ge0\), \(\int f\,d\vartheta=\lambda\int_{U\backslash G_1}f\) where \(\vartheta\) is the convolution of all floor measures and the right side is the integral against the [[?lean:New.besselQuotMeasure|measure of \(U\backslash G_1\)]] ([[?lean:New.Floors.RealPlaceSizes.haarRatio_ne_zero_and_groupMeasure_eq_smul|comparison with Haar measure]]).
* For \(L\ge\rho\), the [[?lean:New.Floors.RealPlaceSizes.gauge|gauge of size \(L\)]] \(\Gamma_L\): a number \(x\in\mathbb{C}\) has size \(i\) if \(\lvert x\rvert\le L^i\); its loss is \(\Lambda=L^2\). A sequence \(p\) of nonzero complex numbers is a head of length \(j\) for \(\Gamma_L\) if and only if \(\lvert p_0\cdots p_{l-1}\rvert^{-1}\le L\) for all \(l\le j\).
* The depth at \(\mathbb{C}\) is \(\mathrm{depth}_a(y,x)=d_a(y,yx)/\pi\), where the [[?lean:New.Floors.realDepth|real depth]] \(d_a(g,g')\) is the infimum of \(\lvert\zeta\rvert_g^2+\lvert\zeta\rvert_{g'}^2\) over the vectors \(\zeta\) orthogonal to \(e_b\) (\(b<a\)) with \(h(e_a,\zeta)=1\); here \(\lvert\zeta\rvert_g\) is the infimum of the Euclidean lengths of \(g^{-1}\zeta'\) over \(\zeta'\equiv\zeta\) modulo the span of the \(e_b\), \(b<a\). The set of [[?lean:New.Floors.PlaceData.stableProducts|stable products]] is the disc \(\mathfrak{d}_a=\{c:\lvert c\rvert^2d_a(y,yx)<1\}\) ([[?lean:New.Floors.RealPlaceSizes.stableProducts_eq|Lean]], [[?lean:New.Floors.RealPlaceSizes.depth_eq|Lean]]).
* \(\operatorname{vol}U(j)=\prod_{i=1}^{j}2\pi^{i}/(i-1)!\) is the [[?lean:New.volU|volume of the compact unitary group]], and \(\Theta=\pi^{(2\varrho+1)k}\operatorname{vol}U(k)/\operatorname{vol}U(r)\) the [[?lean:New.Shape.scaledVolumeRatio|scaled volume ratio]].
* For a sequence \(p\) of nonzero complex numbers, \(R\in\mathbb{R}\) and integers \(K,j\ge0\), the [[?lean:New.headWeight|head weight]] is
\[
\mathrm{w}_{R,K,j}(p)=\prod_{l<j}\begin{cases}\max(1,\lvert\delta_l\rvert^{-1})^{K}&\lvert\delta_l\rvert\le R\\ 0&\text{otherwise}\end{cases},\qquad\delta_l=p_0p_1\cdots p_l ,
\]
and the [[?lean:New.dampedPower|damped power]] is \(\mathrm{D}_K(u)=u^{K}\min(1,u)^6\).

## References

1. Lean: head of `src/New/Spanning/Frames/RealShells.lean`; definitions in `src/New/Spanning/Frames/RealPlaceGauge.lean`, `src/New/Spanning/MainTerm/SieveSystem.lean`, `src/New/Spanning/Bessel/Basic.lean`.
