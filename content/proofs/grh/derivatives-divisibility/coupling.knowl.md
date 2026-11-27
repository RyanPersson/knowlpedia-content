+++
id = "proofs/grh/derivatives-divisibility/coupling"
title = "Coupling of places with their partners"
kind = "definition"
summary = "The power series Gamma_e, the sum of z_x to the power p^e times the variable at the partner of x."
aliases = ["coupling", "couplings", "coupling Gamma_e"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.coupling", "New.subst_coupling", "New.rescale_coupling", "New.le_order_coupling"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
+++

**Definition (coupling).** Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\) (see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]), \(\Phi\) and \(c\) finite sets, and \(\operatorname{pr}\colon\mathbb{N}\times\Phi\to\Phi\) any map, called a **partner rule**: \(\operatorname{pr}_e\tau\) is the partner of the *place* \(\tau\in\Phi\) for the exponent \(e\). In the variables \(z_x\) indexed by the pairs \(x=(\tau,i)\in\Phi\times c\), the **coupling** for the exponent \(e\ge 0\) is the polynomial
\[
\Gamma_e=\sum_{(\tau,i)\in\Phi\times c} z_{(\tau,i)}^{\,p^e}\; z_{(\operatorname{pr}_e\tau,\;i)}\;\in\;\mathcal{O}[\![z]\!] .
\]

## Properties

1. \(\Gamma_e\) is homogeneous of degree \(p^e+1\): \(\Gamma_e(\alpha z)=\alpha^{p^e+1}\Gamma_e(z)\) for \(\alpha\in\mathcal{O}\). In particular its order is at least \(p^e+1\).
2. For series \(Z_x\) without constant term, in any variables, the [[algebra-rings/substitution-of-formal-power-series|substitution]] gives \(\Gamma_e(Z)=\sum_{(\tau,i)}Z_{(\tau,i)}^{\,p^e}Z_{(\operatorname{pr}_e\tau,i)}\), because substitution is a ring homomorphism.

## Remarks

No property of the partner rule is assumed. In the application \(\Phi\) is the group of infinite places of the field \(E\) and the partner is the [[proofs/grh/derivatives-divisibility/partner-of-a-place|place \(-p^e\tau\)]].

## References

1. Lean: `New.coupling`, `New.subst_coupling`, `New.rescale_coupling`, `New.le_order_coupling` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
