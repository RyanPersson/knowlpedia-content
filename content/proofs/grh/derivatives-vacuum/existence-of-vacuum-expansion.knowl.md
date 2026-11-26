+++
id = "proofs/grh/derivatives-vacuum/existence-of-vacuum-expansion"
title = "Existence of vacuum expansions"
kind = "theorem"
summary = "At every prime p the integral vacuum of a standard space has an expansion along a tight frame of length b^2 with b prime to p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_isVacuumExpansion", "New.Parameters.exists_intVacuum_eq_sum_of_isThetaFunction", "New.Parameters.intVacuum_eq_sum_smul_vacElem", "New.Parameters.exists_finHeisenbergOp_rho_eq_smul"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(V\) be a standard space over \(E\) with finite index set \(n\), \(p\) a prime and \(\iota_p\) a \(p\)-adic place. Then a [[proofs/grh/derivatives-vacuum/vacuum-expansion|vacuum expansion]] \((b,w,F,y,a)\) at \(p\) exists.

## Proof

*Frame and \(F\).* Take \(b\) prime to \(p\) and a tight frame \(w\) of length \(b^2\) by [[proofs/grh/derivatives-vacuum/tight-frame-of-square-length-prime-to-p|the lemma on square lengths]]. Apply [[proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame|the existence of resolution products]] with \(\delta=b\), \(N=M=b^2\), all exponents \((1,0,0)\), \(C=\mathcal{E}\), \(a=\Omega_0\) (the area of \(\Omega_0\mathcal{O}_K\) is \(\lvert\Omega_0\rvert^2\sqrt d/2\)): we get \(F\) in the finite part, a resolution product of copies of \(\theta_{\mathcal{E}}\) along \(w\) at scale \(\Omega_0/b\), with \(\Theta_F\) a theta function for \(b\,\mathfrak{a}_0^{\,n}\). Taking \(\gamma=0\) in the formula for theta values gives \(\theta(F)=\theta_{\mathcal{E}}(0)^{\lvert I\times n\rvert}=1\). Condition 6 is [[proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets|the jet series of translates]] at scale \(c\,c_A/\Omega_0\): the linear form has coefficient \((\Omega_0/b)(1/c_A)(c\,c_A/\Omega_0)\overline{\Phi_\tau(w_i)}=c\,\overline{\Phi_\tau(w_i)}/b\), and the shift is \(t_{i,k}(\gamma)\).

*Expansion of the vacuum.* Finite Fourier inversion ([[?lean:New.Space.exists_fourier_coefficients|Fourier coefficients of a theta function]]; asserted) gives finite sets \(Y,\Gamma\), points \(\mathrm{pt}_i\in b^{-1}\mathfrak{a}_0^{\,n}\) (\(i\in Y\)), periods \(\mathrm{per}_j\in\mathfrak{a}_0^{\,n}\) (\(j\in\Gamma\)) and coefficients \(c_i\in\mathbb{C}\) such that
\[ c_i\,\mathrm{vac}=\sum_{j\in\Gamma}h(\mathrm{per}_j)\varrho(-\mathrm{pt}_i)F,\qquad \sum_{i\in Y}c_i\,\varrho(\mathrm{pt}_i)\mathrm{vac}=M\,F,\quad M=(b^2)^{f\lvert n\rvert} \]
(translations by the finite images). Applying \(\theta\) to the second identity, with \(\theta(\varrho(x)g)=g(x)\) and \(\theta(F)=1\): \(\sum_ic_i\,\mathrm{vac}(\mathrm{pt}_i)=M\). Multiply by \(M^{-1}\theta^\circ\) and use that \(\theta^\circ\) is a scalar multiple of \(\mathrm{vac}\), so \(\mathrm{vac}(x)\theta^\circ=\theta^\circ(x)\mathrm{vac}\):
\[ \theta^\circ=\sum_{i\in Y}M^{-1}\theta^\circ(\mathrm{pt}_i)\;c_i\,\mathrm{vac}=\sum_{i\in Y}a_i\sum_{j\in\Gamma}h(\mathrm{per}_j)\varrho(-\mathrm{pt}_i)F,\qquad a_i=M^{-1}\theta^\circ(\mathrm{pt}_i). \]
The \(a_i\) are \(p\)-integral: the values of \(\theta^\circ\) are ([[proofs/grh/derivatives-vacuum/integral-vacuum-values|values of the integral vacuum]]) and \(M\) is a power of \(b\), a \(p\)-adic unit. Finally \(h(x)\varrho(y)F=r\,\varrho(x+y)F\) with \(r\) a value of the self-dual additive character (a root of unity, so \(r\in R_p\)). This gives 5 with index set \(Y\times\Gamma\), points \(y_{(i,j)}=\alpha^{-1}(\mathrm{per}_j-\mathrm{pt}_i)\) and coefficients \(a_ir_{(i,j)}\); and \(b\,y_{(i,j)}\) is integral because \(b(\mathrm{per}_j-\mathrm{pt}_i)\in\mathfrak{a}_0^{\,n}\).

## References

1. Lean: `New.Parameters.exists_isVacuumExpansion`, `New.Parameters.exists_intVacuum_eq_sum_of_isThetaFunction`, `New.Parameters.intVacuum_eq_sum_smul_vacElem`, `New.Parameters.exists_finHeisenbergOp_rho_eq_smul` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
