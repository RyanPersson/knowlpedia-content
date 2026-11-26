+++
id = "proofs/grh/upper-objects/chains-kill-ramified-source-forms"
title = "A chain with data fixed by a scaling above N annihilates ramified source forms"
kind = "theorem"
summary = "The characters of the lifts X_j to X_{j+1} are unramified above N, scalings at a prime dividing pi_N pass through every lift, and a chain one of whose data is fixed by such a scaling kills the ramified source forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.tensorChainLift_eq_zero_of_ramified", "New.Data.tensorChainLift_sub_scaling_eq_zero", "New.Data.charUnramifiedAt_rankTwist_of_N_mem", "New.Data.spaceChar_rankTwist", "New.Data.liftKernel_omega_scaling", "New.Data.liftKernel_lift_scaling", "New.Data.liftKernel_lift_sub_scaling", "New.Data.liftKernel_lift_sub_scaling_eq_zero", "New.Data.doubleLiftChain_eq_zero_of_ramified"]
lean_files = ["src/New/UpperBound/Objects/CharactersAtLevel.lean"]
proof_status = "full"
+++

Let \(D\) be admissible data, \(\vartheta\) a tame character, \(k_j(\vartheta)\) the [[proofs/grh/upper-objects/lift-kernels-of-the-chain|kernels of the lifts \(X_j\to X_{j+1}\)]] with characters built from \(\nu_i=\mu^0_i\vartheta^i\), and \(w\) a prime of \(E\) dividing \(\pi_N\). A [[?lean:New.Data.IsScalingAt|scaling at \(w\)]] is a finite adele \(z\) of norm one, integral, equal to \(1\) away from \(w\) and \(\bar w\); it acts on forms on \(X_j\) by right translation by the scalar matrix \(z\). The [[?lean:New.Data.ramifiedSourceForms|ramified source forms]] are the source forms \(\varphi\) with \(\sum_{0\le e<N-1}R(z_v^e)\varphi=0\) for every prime \(v\mid\pi_N\), \(z_v\) the chosen scaling at \(v\) (of order \(N-1\) modulo \(v\)).

**Theorem.**

1. For a finite index set \(n\) and a place \(w\) above \(N\), the base change of the rank twist of \(\nu_j\) is unramified at \(w\). Since the rank of \(X_j\) is even, the rank twist of \(\nu_i\) for \(X_j\) has [[?lean:New.AutChar.spaceChar|space character]] equal to the base change \(x\mapsto\nu_i(x/\bar x)\).
2. For a scaling \(z\) at \(w\): \(\omega_j(z\cdot1,z\cdot1)=1\) on the data of \(k_j(\vartheta)\). Hence each lift commutes with the scaling, and maps \(\psi-R(z)\psi\) to \(\chi-R(z)\chi\) with \(\chi\) the lift of \(\psi\); and if the datum \(\Phi\) is fixed by \(\omega_j(1,z)\), the lift with datum \(\Phi\) annihilates \(\psi-R(z)\psi\).
3. Let \(t\in\mathcal S_{m-1}\otimes\dots\otimes\mathcal S_0\) be a tensor of data and \(j<m\). If \(\omega_j(1,z)\) acting on factor \(j\) alone fixes \(t\), then \(\operatorname{chain}_m(t)(\psi-R(z)\psi)=0\) for every form \(\psi\) on \(X_0\).
4. If this holds for \(z=z_w\), then \(\operatorname{chain}_m(t)\varphi=0\) for every ramified source form \(\varphi\). The same holds for chains of double lifts when \(\omega(1,z_w)\) on the second factor of some double datum fixes it.

## Proof

*1.* A character with a weight whose tame part is trivial at \(w\) and at \(\bar w\) has base change unramified at \(w\) (Lean: `New.AutChar.HasWeight.charUnramifiedAt`, cited). The tame part of \(\nu_j\) is trivial at the places above \(N\): they are neither chosen places nor places of \(Q\) (a place of \(Q\) or its conjugate does not divide \(N\)). The second claim is the Lean statement `New.Exchange.spaceChar_rankTwist` (cited): for even rank \(n\), the space character of the rank twist of \(\nu\) in rank \(n\) is the base change of \(\nu\).

*2.* For scalars \(\nu,\nu'\) of norm one, \(\omega_{a,b}(\nu\cdot1,\nu'\cdot1)\) is the value of the pair of characters at this pair times \(\omega_{1,1}(1,(\nu'/\nu)\cdot1)\): on \(\operatorname{Hom}(X_j,X_{j+1})\) both pairs of scalars act by the scalar \(\nu'/\nu\) (Lean: `New.Seesaw.pairWeilFinite_scalarFin`, in the file of the composite lift). For \(\nu=\nu'=z\) the second factor is trivial, and the character value is \(1\), because the characters are unramified at \(w\) by 1, \(w\) is split, and \(z\cdot1\) lies in the maximal compact subgroup at \(w\) and is trivial elsewhere (Lean: `CharUnramifiedAt.det_maxCompactAt_eq_one`, cited). The equivariance of the lift, \(\operatorname{lift}(\omega(a,b)\Phi)(R(a)\psi)=R(b)\operatorname{lift}(\Phi)\psi\), then gives \(\operatorname{lift}(\Phi)R(z)=R(z)\operatorname{lift}(\Phi)\); and if \(\omega(1,z)\Phi=\Phi\) then \(R(z)\operatorname{lift}(\Phi)\psi=\operatorname{lift}(\Phi)\psi\), so the lift kills \(\psi-R(z)\psi\).

*3.* This is part 3 of the [[proofs/grh/upper-objects/chain-equivariance|equivariance of chains]] with \(z_i=z\cdot1\) for all \(i\), whose hypothesis is 2: \(\operatorname{chain}_m(t)(R(z)\psi)=\operatorname{chain}_m(t)\psi\).

*4.* Every ramified source form is \(\varphi=\psi-R(z_w)\psi\) for a source form \(\psi\) (Lean: `New.Data.exists_eq_sub_scalingGenerator`, in the area on short source forms). One may take \(\psi=-\tfrac1{N-1}\sum_{0\le e<N-1}e\,R(z_w^{e})\varphi\): since \(z_w^{N-1}\) lies in the level, \(R(z_w)^{N-1}\varphi=\varphi\), and with \(\sum_{e<N-1}R(z_w^e)\varphi=0\) one computes \(\psi-R(z_w)\psi=-\tfrac1{N-1}\big(\sum_{1\le e\le N-2}R(z_w^e)\varphi-(N-2)\varphi\big)=\varphi\). Then apply 3. For chains of double lifts, regroup the \(p\) double data into \(2p\) single factors: \(\omega(1,z_w)\) on the single factor \(2i+1\) fixes the regrouped tensor, and \(2i+1<2p\). \(\square\)

## References

1. Lean: `New.Data.tensorChainLift_eq_zero_of_ramified`, `New.Data.liftKernel_omega_scaling`, `New.Data.spaceChar_rankTwist` in `src/New/UpperBound/Objects/CharactersAtLevel.lean`.
