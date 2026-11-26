+++
id = "proofs/grh/upper-elementary-divisors/substitution-operator-conjugation"
title = "Conjugating the factors conjugates the substitution operator"
kind = "lemma"
summary = "For block diagonal h, conjugating every factor of the letter s by the image of h under the s-th map conjugates the substitution operator by the twisted representation of h."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.substitutionOperator_map_eq_conj", "New.FrobeniusCycle.substitutionLetterMatrix_map", "New.FrobeniusCycle.letterMatrix_mul_parityCofactor_letterConj_mul", "New.mul_adjugate_conj_mul", "New.FrobeniusCycle.letterMatrix_inv_apply_eq_zero", "New.FrobeniusCycle.parityCofactor_map"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
proof_status = "full"
+++

**Lemma.** In the setting of the [[proofs/grh/upper-elementary-divisors/substitution-operator|substitution operator]], let \(\chi\colon R\to O\) be a ring homomorphism and let \(h\in\mathrm{GL}_k(W)\) be block diagonal for the blocks \(\{b<r\}\), \(\{b\ge r\}\). Then for all factors \(\psi\),
\[
\chi\bigl(\mathcal{S}(r,\ell,n;\psi)\bigr)=\rho_n(h^{-1})\;\mathcal{S}\bigl(r,\ell,n;\ (\operatorname{conj}_{h,s}\chi(\psi_{s,d}))_{s,d}\bigr)\;\rho_n(h),
\]
where \(\rho_n\) is the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted representation]] and \(\chi\) is applied entrywise.

## Proof

It suffices to prove for each letter \(\chi(\Sigma_s(\psi))=h_s^{-1}\,\Sigma_s(\psi')\,h_s\) with \(\psi'_{s,d}=\operatorname{conj}_{h,s}\chi(\psi_{s,d})\) and \(h_s\) the matrix of \(h\) on the letter \(s\); then apply \(\operatorname{Sym}^n\) and the Kronecker product, which are multiplicative and commute with \(\chi\).

Let \(A=\iota_s(h)\), \(B=\iota_s(h^{-1})\). For any \(M\in M_k(O)\): \(h_s^{-1}\operatorname{pc}_s(AMB)\,h_s=\operatorname{pc}_s(M)\). For even \(s\) this is \(B(AMB)A=M\). For odd \(s\), \(h_s={}^tB\), \(h_s^{-1}={}^tA\), and \({}^tA\,{}^t\!\operatorname{adj}(AMB)\,{}^tB={}^t\bigl(B\operatorname{adj}(AMB)A\bigr)={}^t\!\operatorname{adj}(M)\), because \(\operatorname{adj}(AMB)=\operatorname{adj}(B)\operatorname{adj}(M)\operatorname{adj}(A)\) and \(B\operatorname{adj}(B)=\det B\), \(\operatorname{adj}(A)A=\det A\), \(\det A\det B=1\). Since conjugation is multiplicative, for each \(m\), \(\chi\bigl(\operatorname{pc}_s(\psi_{s,m-1}\cdots\psi_{s,0})\bigr)=h_s^{-1}\operatorname{pc}_s(\psi'_{s,m-1}\cdots\psi'_{s,0})h_s\).

Row \(b\) of \(\Sigma_s\) uses \(m=\ell+\delta_r(b,s)\). As \(h\) is block diagonal, \((h_s^{-1})_{b,x}=0\) unless \(b,x\) are in the same block, i.e. unless \(\delta_r(b,s)=\delta_r(x,s)\). Hence row \(b\) of \(h_s^{-1}\Sigma_s(\psi')\) only involves rows \(x\) of \(\Sigma_s(\psi')\) built with the same \(m\), and equals row \(b\) of \(h_s^{-1}\operatorname{pc}_s(\psi'_{s,m-1}\cdots\psi'_{s,0})\). Multiplying by \(h_s\) on the right gives row \(b\) of \(\chi(\Sigma_s(\psi))\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.substitutionOperator_map_eq_conj`, `New.FrobeniusCycle.substitutionLetterMatrix_map`, `New.FrobeniusCycle.letterMatrix_mul_parityCofactor_letterConj_mul`, `New.mul_adjugate_conj_mul`, `New.FrobeniusCycle.letterMatrix_inv_apply_eq_zero`, `New.FrobeniusCycle.parityCofactor_map` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.
