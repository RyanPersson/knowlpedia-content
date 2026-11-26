+++
id = "proofs/grh/reduction-main/theorem-a-index"
title = "Theorem A (b): images of integral source forms have small index"
kind = "theorem"
summary = "A finite family of target forms s p(phi), with s in a set t of translates and phi integral ramified source forms, has index at most #t · dim(source) · 2 f a log^3 b in the target lattice."
aliases = ["Theorem A (b)", "indexLe_normalizedPoincare"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.indexLe_normalizedPoincare", "New.Data.indexLe_of_mem_image_normalizedPoincare", "New.Data.normalizedPoincare_mem_integralVectors", "New.Data.finrank_sourceForm_le_two_mul"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
proof_status = "full"
+++

**Theorem A (b) (index).** Let \(D\) be [[proofs/grh/reduction-main/data|data]], with source \(\mathcal S\), integral forms \(\mathcal S^{\mathrm{int}}\), group \(\bar G\) and [[proofs/grh/reduction-main/normalized-poincare|normalised Poincaré maps \(s\mathfrak p\)]]. Let \(t\subseteq\bar G\) be a finite set and \(y_1,\dots,y_n\in\mathcal T\) target forms such that each \(y_i\) lies in \(s\mathfrak p(\mathcal S^{\mathrm{int}})\) for some \(s\in t\). Then \(y\) has [[proofs/grh/reduction-main/index-bound|index at most]]
\[
\#t\cdot\dim_{\mathbb C}\mathcal S\cdot2\,f\,a\,(\log b)^3
\]
in the [[proofs/grh/reduction-main/target-lattice|target lattice]].

## Proof

Complete relative to: property (d) of the errors in [[proofs/grh/reduction-main/gain-normalisation|the gain normalisation]] (divisibility of the composite lift); the seesaw identity (property (2) of the normalised Poincaré maps); [[?lean:New.Data.goodProjTranslate_mem_integralForms|integrality of the good part]]: if \(c\,\iota_\vartheta z\) is integral at \(\iota\) then so is \(c\,\Theta_\vartheta(\#\bar Ge_0sz)\); and [[?lean:New.Data.le_finrank_ramifiedSourceForms|the dimension of the ramified forms]], \(\dim\mathcal S\ge(1-f/(N-1))D_X\), with [[?lean:New.Data.f_div_N_sub_one_le|\(f/(N-1)\le b^{-8}\)]].

**Step 1: integrality criterion.** Let \(\iota\mid\ell\), \(s\in\bar G\), \(\varphi\in\mathcal S\), and suppose that for every twist \(\vartheta\) with modulus prime to \(\ell\) and every chain datum \(\Psi\) of \(\vartheta\) the values of \(B_{\vartheta,\Psi}\varphi\) have gauge at most \(\ell^{\operatorname{err}_\ell-\operatorname{gain}_\ell}\). Then \(s\mathfrak p\varphi\) is an integral vector at \(\iota\). Indeed let \(\vartheta\) be an \(m\)-fold twist allowed at \(\ell\) and \(z=c_{ss}^{-1}\mathcal P\varphi\). By the seesaw identity \(\iota_\vartheta z=B_{\vartheta,\Psi}\varphi\) for a chain datum \(\Psi\). As \(g_\ell\le\operatorname{gain}_\ell-\operatorname{err}_\ell\), the form \(\ell^{-g_\ell}B_{\vartheta,\Psi}\varphi\) is integral at \(\iota\); and \(\lvert c_B\rvert_\iota=\lvert\ell^{-g_\ell}\rvert_\iota\), so \(c_B\,\iota_\vartheta z\) is integral at \(\iota\). Hence \(\Theta_\vartheta(s\mathfrak p\varphi)=c_B\Theta_\vartheta(\#\bar Ge_0sz)\) is integral at \(\iota\).

**Step 2: one translate.** Fix \(s\) and let all \(y_i\in s\mathfrak p(\mathcal S^{\mathrm{int}})\). Put \(e_\ell=D_X\operatorname{err}_\ell\ge0\); then \(\sum_{\ell\in U}e_\ell\log\ell\le D_X\,fa\log^3b\le\dim\mathcal S\cdot2fa\log^3b\), since \(D_X\le2\dim\mathcal S\) (from \(f/(N-1)\le b^{-8}\le\tfrac12\)). Fix \(\iota\mid\ell\) and take \(j\le e_\ell\) and \(S\) as in property (d); let \(M\) be the \(\mathcal O_\iota\)-module of \(\varphi\in\mathcal S\) integral at \(\iota\), and \(A=s\mathfrak p\) viewed as \(\mathcal O_\iota\)-linear. By Step 1, every \(\varphi\in M\cap S\) has \(A\varphi\in L_\iota\). The preimage rule of [[proofs/grh/reduction-main/colength-calculus|the calculus of colengths]] (for the inclusion \(\mathcal S\subseteq\mathcal S_X\)) gives \(\operatorname{colen}(M,A^{-1}(L_\iota))\mid\ell^{\,j}\), and the image rule (for \(A\)) gives \(\operatorname{colen}(A(M),L_\iota)\mid\ell^{\,j}\). All \(y_i\) lie in \(A(\mathcal S^{\mathrm{int}})\subseteq A(M)\). By rule (3) of [[proofs/grh/reduction-main/index-calculus|the calculus of indices]], \(y\) has index at most \(\dim\mathcal S\cdot2fa\log^3b\).

**Step 3: several translates.** Apply rule (5) of the calculus of indices to the sets \(A_s=s\mathfrak p(\mathcal S^{\mathrm{int}})\), \(s\in t\).

## References

1. Lean: `New.Data.indexLe_normalizedPoincare`, `New.Data.indexLe_of_mem_image_normalizedPoincare`, `New.Data.normalizedPoincare_mem_integralVectors`, `New.Data.finrank_sourceForm_le_two_mul` in `src/New/Reduction/ShortAndEnough.lean`.
