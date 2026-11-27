+++
id = "proofs/grh/spanning-unfolding-a/block-sums-under-unipotent-reductions"
title = "Blocks transform by the unipotent character and vanish unless s agrees"
kind = "theorem"
summary = "The block at u-bar s u-bar'^-1 is psi(u)^-1 psi(u') times the block at s, for integral unipotent u, u'; hence the block of a stable set vanishes unless s agrees with the unipotent character."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.amplitudeSum_besselU_mul", "New.Filling.amplitudeSum_eq_zero_of_not_agrees", "New.Filling.besselKernel_besselU_mul", "New.Filling.besselFn_mul_of_mem_classUnipotent", "New.Filling.isStable_besselS"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(T\) a [[?lean:New.Filling.IsStable|stable]] set of rational [[?c:Isometry of a hermitian space|isometries]], \(\tau\) a side, \(c,c'\) classes and \(s\) an element of the [[?lean:New.Filling.ResidueGL|residue group]]. Let \(\psi\) be the [[?lean:New.Filling.unipotentChar|unipotent character]] \(\psi(u)=\psi_f\bigl(-\sigma(u)/(M\varpi)\bigr)\) on the finite adelic group, \(\sigma(u)\) being the sum of the entries of \(u\) just above the diagonal on the frame.

1. Let \(u,u'\) be elements of the integral subgroup \(K\) ([[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]) lying in the finite adelic unipotent group \(\mathsf U\), with reductions \(\bar u,\bar u'\) at the chosen places. Then
\[
A^{\tau}_T\bigl(c,\ \bar u\,s\,\bar u'^{-1},\ c'\bigr)=\psi(u)^{-1}\psi(u')\;A^{\tau}_T(c,s,c').
\]
2. If \(s\) does not [[?lean:New.Filling.Agrees|agree]] — that is, there are such \(u,u'\) with \(\bar u s=s\bar u'\) and \(\psi(u)\ne\psi(u')\) — then \(A^{\tau}_T(c,s,c')=0\).

## Proof

*Kernel under rational unipotent elements.* For rational \(x,x'\in\mathsf U\), \(\mathcal K^{\tau}_{x\gamma x'^{-1}}(xy)=\psi(x)^{-1}\psi(x')\,\mathcal K^{\tau}_\gamma(y)\) (with \(\psi\) evaluated at the finite images). Indeed \((x\gamma x'^{-1})^{-1}xy=x'\gamma^{-1}y\), the Bessel function satisfies \(W(xy)=\psi(x)^{-1}W(y)\) ([[?lean:New.Filling.besselFn_ratToInf_mul|transformation of the Bessel function]]), and in the second tensor factor the complex conjugate of \(\psi(x')^{-1}\) is \(\psi(x')\), as \(\lvert\psi\rvert=1\).

*1.* By approximation ([[?lean:New.Filling.exists_rat_approx_unipotentChar_eq|rational approximation of unipotent elements]]) there is a rational \(x\in\mathsf U\) with \(h_c^{-1}xh_c\in u\,K(M)\) and \(\psi(x)=\psi(u)\); thus \(x\) is a term over \((c,\bar u,c)\). Likewise \(x'\) for \(u'\) and \(c'\), a term over \((c',\bar u',c')\). Since \(T\) is stable, \(\gamma\in T\iff x\gamma x'^{-1}\in T\). Apply the proposition on [[proofs/grh/spanning-unfolding-a/moving-a-block-by-the-bessel-subgroup|moving a block]] with \(\sigma=x\), \(\sigma'=x'\) (the unipotent group lies in the Bessel subgroup) and \(L\) the multiplication by \(\psi(x)^{-1}\psi(x')\).

*2.* If \(\bar us=s\bar u'\) then \(\bar us\bar u'^{-1}=s\), so by 1 the vector \(A=A^{\tau}_T(c,s,c')\) satisfies \(A=\psi(u)^{-1}\psi(u')A\). If \(A\ne0\) this forces \(\psi(u)=\psi(u')\) for all such pairs, i.e. \(s\) agrees.

## Remarks

The set of rational points of the Bessel subgroup is stable, since it contains the rational points of \(\mathsf U\).

## References

1. Lean: `New.Filling.amplitudeSum_besselU_mul` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.amplitudeSum_eq_zero_of_not_agrees` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.besselKernel_besselU_mul` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
4. Lean: `New.Filling.besselFn_mul_of_mem_classUnipotent` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
5. Lean: `New.Filling.isStable_besselS` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
