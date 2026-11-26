+++
id = "proofs/grh/derivatives-divisibility/partner-of-a-place"
title = "Partner of an infinite place"
kind = "definition"
summary = "The partner of an infinite place tau of E for the prime p and exponent e is the place -p^e tau; modulo pi_p, the p^e-th power at tau is complex conjugation at the partner."
aliases = ["partner", "partner of a place", "partner rule of E"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.partner", "New.Parameters.norm_pow_sub_conj_partner_le", "New.Parameters.norm_conj_pow_sub_partner_le", "New.piPrimeInt_dvd_iff"]
lean_files = ["src/New/Derivatives/FormalGroup/ThetaProducts.lean"]
proof_status = "full"
+++

**Definition (partner).** Let \(E=K(\zeta)\) with its group \(\Phi\) of infinite places (see the [[proofs/grh/derivatives-divisibility/field-setting|field \(E\)]]), \(p\) a prime and \(e\ge0\). The **partner** of \(\tau\in\Phi\) for \(p\) and \(e\) is
\[
\operatorname{pr}_e\tau=\nu_{-p^e}\cdot\tau\in\Phi ,
\]
where \(\nu_{-p^e}\) is the place named by the integer \(-p^e\) (the class of \(-p^e\) in \((\mathbb{Z}/q_1)^\times\) if \(p\nmid q_1\), the identity otherwise). The map \((e,\tau)\mapsto\operatorname{pr}_e\tau\) is the partner rule used for the [[proofs/grh/derivatives-divisibility/coupling|couplings]] of \(E\).

**Lemma (powers and conjugation at partners).** Let \(p\) be a prime with a \(p\)-adic place \(\iota_p\), let \(e\in I_p^\circ\) (so \(\chi_K(p)\neq1\); see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]), \(\tau\in\Phi\) and \(\tau'=\operatorname{pr}_e\tau\). Then, modulo \(\pi_p\) in \(\mathcal{O}\):

1. \(\iota_p\bigl(\Phi_\tau(\alpha)\bigr)^{p^e}\equiv\iota_p\bigl(\overline{\Phi_{\tau'}(\alpha)}\bigr)\) for every \(\alpha\in\mathcal{O}_E\);
2. \(\iota_p\bigl(\overline{\Phi_\tau(y)}\bigr)^{p^e}\equiv\iota_p\bigl(\Phi_{\tau'}(y)\bigr)\) for every \(y\in E\) [[proofs/grh/derivatives-divisibility/integral-above-p|integral above \(p\)]].

## Proof

1. Since every prime dividing \(q_1\) splits in \(K\), \(p\nmid q_1\). Let \(R=\mathcal{O}/\pi_p\mathcal{O}\), a ring of characteristic \(p\), and \(\varphi\colon\mathcal{O}_E\to R\) the reduction of \(\iota_p\circ\Phi_\tau\). With \(u=\nu_{-p^e}\) we have \(\overline{\Phi_{\tau'}(\alpha)}=\Phi_{\tau'}(\bar\alpha)=\Phi_\tau(\sigma_u\bar\alpha)\), so the claim is \(\varphi(\sigma_u(\bar\alpha))=\varphi(\alpha)^{p^e}\) for all \(\alpha\); replacing \(\alpha\) by \(\bar\alpha\), it is \(\varphi(\sigma_u x)=\varphi(\bar x)^{p^e}\) for all \(x\). By the [[proofs/grh/derivatives-divisibility/frobenius-on-generators|criterion on generators]] (with complex conjugation, sign \(-1\), and \(n=e\)) this holds if and only if \(\varphi(\sigma_u\zeta)=\varphi(\sigma_{\nu_{-p^e}}\zeta)\), which is trivial, and
\[
\chi_K(p)^e\cdot(-1)\cdot\varphi(\sqrt{-d})=\varphi(\sqrt{-d}).
\]
If \(p=d\), then \(\Phi_\tau(\sqrt{-d})=\sqrt{-d}=\pi_p\) and \(\varphi(\sqrt{-d})=0\). If \(p\) is inert, \(e\) is odd and \(\chi_K(p)^e(-1)=1\).

2. Write \(Ny=\alpha\) with \(N\) prime to \(p\) and \(\alpha\in\mathcal{O}_E\). Put \(a=\iota_p(\overline{\Phi_\tau(y)})\) and \(b=\iota_p(\Phi_{\tau'}(y))\); both are integral. Part 1 for \(\bar\alpha\) reads \((Na)^{p^e}\equiv Nb\). By Fermat's little theorem \(N^{p^e}\equiv N\pmod p\), and \(\pi_p\mid p\). Hence \(N^{p^e}(a^{p^e}-b)=\bigl((Na)^{p^e}-Nb\bigr)-(N^{p^e}-N)b\equiv0\), and \(N\) is a unit of \(\mathcal{O}\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.partner`, `New.Parameters.norm_pow_sub_conj_partner_le`, `New.Parameters.norm_conj_pow_sub_partner_le` in `src/New/Derivatives/FormalGroup/ThetaProducts.lean`.
