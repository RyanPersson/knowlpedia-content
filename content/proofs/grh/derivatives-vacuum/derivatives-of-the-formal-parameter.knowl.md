+++
id = "proofs/grh/derivatives-vacuum/derivatives-of-the-formal-parameter"
title = "Derivatives of the formal parameter at powers of the prime norm"
kind = "lemma"
summary = "If n+1 is a power of the norm q_p of a prime of K above p, the coefficient of z^(n+1) of the formal parameter has valuation -n rho_p, and so the greatest norm of (n+1)-st derivatives is at least p^(-n gamma_p)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.norm_coeff_formalParam_of_eq_primeNorm_pow", "New.CMLattice.pow_le_maxDerivNorm_of_eq_primeNorm_pow", "New.CMLattice.norm_eq_one_of_piPrimeInt_dvd_sub_one", "New.rpow_pow_le_norm_factorial_succ"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives|the definition of \(c_C\)]]. Let \(q_p\) be the [[?lean:New.primeNorm|norm of a prime of \(K\) above \(p\)]], \(\rho_p=1/(e(q_p-1))\) the [[?lean:New.varpiValuation|valuation threshold]] (\(e\) the ramification index of \(p\) in \(K\)), \(\gamma_p=1/(p-1)-\rho_p\) the [[?lean:New.gammaPrime|rate]], and \(\Upsilon\) the [[?lean:New.CMLattice.formalParam|formal parameter]] of \(C\) (the part of \(y\) in degrees \(\equiv1\bmod q_p-1\)).

**Lemma.** If \(n+1=q_p^{\,j}\) for some \(j\ge0\), then

1. \(\lvert[z^{n+1}]\Upsilon\rvert_p=p^{\,n\rho_p}\);
2. \(c_C(n+1)\ge p^{-n\gamma_p}\).

## Proof

1. By a result of the formal-group chapter ([[?lean:New.CMLattice.exists_scaled_formalParam|the scaled formal parameter]]; asserted here) there are \(\varpi\in\mathbb{C}_p\) with \(\lvert\varpi\rvert_p=p^{-\rho_p}\) and an integral series \(Y\) with \(\Upsilon(\varpi z)=\varpi\,Y(z)\), whose coefficient of \(z^{k}\) is \(\equiv1\) modulo \(\pi_p\) when \(k\) is a power of \(q_p\) (\(\pi_p=\sqrt{-d}\) if \(p=d\), \(\pi_p=p\) otherwise; \(\lvert\pi_p\rvert_p<1\)). An integer of \(\mathbb{C}_p\) congruent to \(1\) modulo \(\pi_p\) has absolute value \(1\). Comparing coefficients of \(z^{n+1}\): \(\varpi^{n+1}[z^{n+1}]\Upsilon=\varpi\,[z^{n+1}]Y\), so \(\lvert[z^{n+1}]\Upsilon\rvert_p=\lvert\varpi\rvert_p^{-n}\).

2. By Legendre's formula, \(v_p((n+1)!)\le n/(p-1)\), i.e. \(\lvert(n+1)!\rvert_p\ge p^{-n/(p-1)}\). With 1, \(\lvert(n+1)!\,[z^{n+1}]\Upsilon\rvert_p\ge p^{-n/(p-1)+n\rho_p}=p^{-n\gamma_p}\). And \(\Upsilon\in\mathcal{O}[\![y]\!]\) (it is another generator; Lean `isSeriesGenerator_formalParam`), so the left side is \(\le c_C(n+1)\).

## References

1. Lean: `New.CMLattice.norm_coeff_formalParam_of_eq_primeNorm_pow`, `New.CMLattice.pow_le_maxDerivNorm_of_eq_primeNorm_pow`, `New.CMLattice.norm_eq_one_of_piPrimeInt_dvd_sub_one`, `New.rpow_pow_le_norm_factorial_succ` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
