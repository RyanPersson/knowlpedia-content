+++
id = "proofs/grh/derivatives-divisibility/normal-form-substitution"
title = "Substitution into a series with the normal form"
kind = "lemma"
summary = "If F has the normal form and the Z_x are integral series without constant term, then F(varpi Z) is an integral series times exp(c Xi(Z))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasNormalForm.exists_subst_eq_mul_expSubst", "New.subst_expSubst"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
proof_status = "full"
+++

**Lemma.** Let \(F\) have the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with the data \((S,\operatorname{pr},\varpi,\lambda)\), in the variables \(z_x\), \(x\in\Phi\times c\). Let \(Z_x\), \(x\in\Phi\times c\), be integral power series without constant term in variables indexed by any set. Then there is an integral series \(W'\) in the new variables with
\[
F\bigl((\varpi Z_x)_x\bigr)=W'\cdot\exp\Bigl(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda}\bigl((Z_x)_x\bigr)\Bigr),\qquad c_\varpi=\varpi^{p+1}/p .
\]

## Proof

Write \(F(\varpi z)=W\exp(c_\varpi\Xi)\) with \(W\) integral and \(\Xi=\Xi_{S,\operatorname{pr},\lambda}\). [[algebra-rings/substitution-of-formal-power-series|Substitutions]] of series without constant term compose, so substituting \(z_x\mapsto Z_x\) in \(F(\varpi z)\) gives \(F(\varpi Z)\). Substitution is a ring homomorphism and commutes with the exponential: \(\exp(h)(Z)=\exp(h(Z))\) when \(h(0)=0\), again because substitutions compose. Hence
\[
F(\varpi Z)=W(Z)\cdot\exp\bigl(c_\varpi\,\Xi(Z)\bigr),
\]
and \(W'=W(Z)\) is integral, since \(W\) and the \(Z_x\) are. (Here \(\Xi(0)=0\) by the properties of the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]].) \(\blacksquare\)

## References

1. Lean: `New.HasNormalForm.exists_subst_eq_mul_expSubst`, `New.subst_expSubst` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
