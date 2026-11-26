+++
id = "proofs/grh/derivatives-vacuum/properties-of-resolution-forms"
title = "Properties of the resolution forms of a tight frame of length M"
kind = "lemma"
summary = "For a tight frame of length M the resolution vectors are a resolution of the identity, the resolution forms are p-integral, and at primes not dividing q1 M, in particular at non-split primes, the Taylor scale is a unit and the resolution vectors are integral above p; the complex period scale has squared modulus M/Omega."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.isResolution_resolutionVectors", "New.Data.resolutionForms_eq_smul", "New.Data.norm_resolutionForms_le_one", "New.Data.not_dvd_q₁_mul_M", "New.Data.isIntegralAbove_resolutionVectors", "New.Data.norm_taylorScale_eq_one_of_not_dvd", "New.Data.norm_taylorScale", "New.Data.norm_conj_piMBar_mul_jetScale_sq", "New.isIntegralAbove_of_isIntegral_mul", "New.CMLattice.thetaProd_smul"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame|the definition of resolution forms]].

**Lemma.** Let \((w_i)\) with multiplicities \((c_i)\) be a [[?lean:New.IsTightFrame|tight frame]] of length \(M\).

1. \((u_i,c_i)\) is a [[?lean:New.IsResolution|resolution of the identity]] on \(E^1\).
2. \(\lvert\mu_{i,\tau}\rvert_p\le1\) for all \(i,\tau\) and every prime \(p\).
3. A prime \(p\) with \(\chi_K(p)\ne1\) does not divide \(q_1M\).
4. If \(p\nmid q_1M\), then \(\lvert\mathfrak{s}\rvert_p=1\).
5. If \(\chi_K(p)\ne1\), every \(u_i\) is integral at all places of \(E\) above \(p\).
6. \(\lvert\pi_M\lambda\rvert^2=M/\Omega\), where \(\lambda\) is the [[proofs/grh/derivatives-vacuum/jet-scale|jet scale]] and \(\Omega\) [[?lean:New.Parameters.bigOmega|the constant \(\Omega\)]].
7. For linear forms \(\mu\) and a scalar \(s\), the theta product of the forms \(s\mu\) is \(\Theta(sz)\).

## Proof

1. \(\sum_ic_i\Phi_\sigma(u_i)\overline{\Phi_\tau(u_i)}=\frac{1}{\bar\pi_M\pi_M}\sum_ic_i\Phi_\sigma(w_i)\overline{\Phi_\tau(w_i)}=\delta_{\sigma\tau}\) (the \(\Phi_\tau\) are the identity on \(K\)).

2. The \(w_i\) lie in \(\mathfrak{a}_0\); apply [[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|part 2 of the size of the period factor]].

3. Primes dividing \(q_1\) split in \(K\), and the level primes are \(\equiv1\) modulo a multiple of \(d\), hence split ([[?lean:New.Parameters.chiK_eq_one_of_modEq_one|\(\chi_K=1\) at primes \(\equiv1\)]]).

4. \(\lvert\iota_p\varpi\rvert_p=1\) as \(p\nmid q_1\) ([[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|part 3]]). \(\pi_M\) and \(\bar\pi_M\) are algebraic integers with product \(M\), a \(p\)-adic unit, so both are \(p\)-adic units.

5. \(q_1M\,u_i=(q_1w_i)\,\pi_M\). Here \(q_1w_i\) is an algebraic integer because \(q_1\alpha\) is an integral adele and \(\alpha^{-1}w_i\) is integral. Since \(p\nmid q_1M\) by 3, \(u_i\) is integral above \(p\).

6. \(\lvert\pi_M\rvert^2=M\) and \(\lvert\lambda\rvert^2=\Omega^{-1}\) by [[proofs/grh/derivatives-vacuum/modulus-of-jet-scale|the modulus of the jet scale]].

7. \(\theta((s\mu_j)(z))=\theta(\mu_j(sz))\).

## References

1. Lean: `New.Data.isResolution_resolutionVectors`, `New.Data.resolutionForms_eq_smul`, `New.Data.norm_resolutionForms_le_one`, `New.Data.not_dvd_q₁_mul_M`, `New.Data.isIntegralAbove_resolutionVectors`, `New.Data.norm_taylorScale_eq_one_of_not_dvd`, `New.Data.norm_taylorScale`, `New.Data.norm_conj_piMBar_mul_jetScale_sq`, `New.isIntegralAbove_of_isIntegral_mul`, `New.CMLattice.thetaProd_smul` in `src/New/Derivatives/Sharpness/Cases.lean`.
