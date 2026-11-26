+++
id = "proofs/grh/derivatives-divisibility/chosen-places-and-characters"
title = "Chosen places, their residue characters, and characters of given weight"
kind = "construction"
summary = "The chosen places of E are the primes dividing pi_M; they carry residue characters omega_w of order q2; characters chi_0 of weight -w_0 and chi_M of weight 0 and tame part omega of U(1) exist."
aliases = ["chosen place", "chosen places", "residue character omega", "character chi_0", "character chi_M"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsChosen", "New.Data.ChosenPlace", "New.Data.piM", "New.Data.piM_mul_star", "New.Data.exists_levelPrime_mem_of_isChosen", "New.Data.isChosen_iff", "New.Data.q_eq_levelPrime", "New.Data.finite_isChosen", "New.Data.chiMLocalRoot", "New.Data.chiMLocal", "New.Data.orderOf_chiMLocal", "New.Data.chiMLocal_apply_eq_one_of_pow_q₁_eq_one", "New.Data.chiMLocal_zpow_mul_pow_eq_one", "New.Data.exists_char_hasWeight", "New.Data.chiZero", "New.Data.chiM", "New.Data.chiZero_hasWeight", "New.Data.chiM_hasWeight", "New.Data.exists_zeta_pow_eq_of_isIntegral", "New.Data.prod_phi_zeta_pow_pow_liftWeight_zero_eq_one", "New.Data.exists_piM_mul_star_eq_levelPrime_mul_coprime", "New.Data.exists_mulChar_orderOf_eq_sq_of_isChosen"]
lean_files = ["src/New/Derivatives/Field/ChosenPlaces.lean"]
proof_status = "full"
+++

**Setting.** Let \(D\) be [[?lean:New.Data|admissible data]] for the parameters, with level \(s\) and field \(E=K(\zeta)\) (see the [[proofs/grh/derivatives-divisibility/field-setting|field \(E\)]]). Among its components are two distinct primes \(p_0,p_1\) with \(p_i\equiv1\pmod{q_1d}\) and \(q_2^2\mid p_i-1\), where \(q_2=(q_0d)^{s+6}\), and an integer \(\bar\pi_M\in\mathcal{O}_K\) with \(\bar\pi_M\pi_M=M:=p_0p_1\), where \(\pi_M\in\mathcal{O}_E\) denotes the complex conjugate of (the image of) \(\bar\pi_M\).

**Definition (chosen place).** A finite place \(w\) of \(E\) is **chosen** if \(\pi_M\in w\).

**Construction (residue characters).** For a chosen place \(w\) fix a complex [[?c:multiplicative character of a finite field|multiplicative character]] \(T_w\) of order \(q_2^2\) of the residue field \(k_w=\mathcal{O}_E/w\), and put \(\omega_w=T_w^{\,q_2}\); for a place \(w\) that is not chosen put \(\omega_w=1\).

**Construction (characters of \(U(1)\)).** Let \(w_0(v)=\kappa(v)+r^8\) be the [[?lean:New.Data.liftWeight|weight of lift \(0\)]] at the infinite place \(v\), where \(q_1\mid\kappa(v)\). For natural numbers \(a,n\) there is an [[?lean:New.AutChar|automorphic character]] \(\mu\) of \(U(1)\) (a continuous character of the norm-one adeles of \(E\), trivial on the norm-one elements of \(E\)) of [[?lean:New.AutChar.HasWeight|weight]] \(v\mapsto-a\,w_0(v)\) and tame part \((\omega_w^n)_w\), that is,
\[
\mu(u)=\prod_vu_v^{-a\,w_0(v)}\cdot\prod_w\omega_w(u\bmod w)^n\qquad\text{for all } u\text{ with integral finite part.}
\]
One fixes \(\chi_0\) with \((a,n)=(1,0)\) (weight \(-w_0\), trivial tame part) and \(\chi_M\) with \((a,n)=(0,1)\) (weight \(0\), tame part \(\omega\)).

## Properties

1. A chosen place lies above \(p_0\) or \(p_1\); every place above \(p_i\) has norm \(p_i\); there are finitely many chosen places. For each \(i\), \(\pi_M\bar\pi_M=p_i\cdot p_{1-i}\) with \(p_{1-i}\) prime to \(p_i\), so the [[proofs/grh/derivatives-divisibility/places-above-split-primes|proposition on places above split primes]] applies to \(a=\pi_M\).
2. For chosen \(w\), \(\omega_w\) has order \(q_2\). For every \(w\) and \(x\in k_w\) with \(x^{q_1}=1\), \(\omega_w(x)=1\).

## Proof

1. If \(\pi_M\in w\), then \(p_0p_1=\pi_M\bar\pi_M\in w\), so \(p_0\in w\) or \(p_1\in w\). The norm is \(p_i\) because \(p_i\equiv1\pmod{q_1d}\) ([[proofs/grh/derivatives-divisibility/decomposition-of-primes-in-e|decomposition of primes]]). The chosen places are the prime divisors of the nonzero ideal \((\pi_M)\).

*Existence of \(T_w\).* \(k_w^\times\) is cyclic of order \(p_i-1\), which is divisible by \(q_2^2\).

2. \(T_w^{q_2}\) has order \(q_2^2/q_2\). Since \(q_1\mid q_1d\mid q_2\), \(x^{q_1}=1\) gives \(x^{q_2}=1\) and \(\omega_w(x)=T_w(x^{q_2})=1\).

*Existence of \(\mu\).* By the [[?lean:New.AutChar.exists_hasWeight_of_prod_eq_one|existence criterion for characters of given weight]], it suffices that the formula gives \(1\) at every \(\gamma\in\mathcal{O}_E\) with \(\gamma\bar\gamma=1\). Such \(\gamma\) has absolute value \(1\) at every infinite place, so it is a root of unity, hence \(\gamma=\zeta^k\) and \(\gamma^{q_1}=1\). At infinity: \(w_0(v)\equiv r^8\pmod{q_1}\), so \(\prod_v\Phi_v(\gamma)^{w_0(v)}=\prod_v\Phi_v(\gamma^{r^8})=N_{E/K}(\gamma^{r^8})=1\), as \(N_{E/K}(\zeta)=1\). At a finite place the residue of \(\gamma\) is a \(q_1\)-th root of unity, on which \(\omega_w\) is trivial by 2. \(\blacksquare\)

## References

1. Lean: `New.Data.IsChosen`, `New.Data.chiMLocal`, `New.Data.exists_char_hasWeight`, `New.Data.chiZero`, `New.Data.chiM` in `src/New/Derivatives/Field/ChosenPlaces.lean`; `New.AutChar.HasWeight`, `New.AutChar.exists_hasWeight_of_prod_eq_one` in `src/Lib/ClassField/HeckeCharacter/Basic.lean`.
