+++
id = "proofs/grh/derivatives-divisibility/normal-form-valuation"
title = "The normal form depends only on the valuation of varpi"
kind = "lemma"
summary = "The normal form is kept under scaling the variables by an integral number, and its existence depends only on the absolute value of varpi."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasNormalForm.rescale", "New.HasNormalForm.exists_of_norm_eq"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
proof_status = "full"
+++

**Lemma.** Let \(F\) have the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with the data \((S,\operatorname{pr},\varpi,\lambda)\).

1. (*Scaling.*) For \(\alpha\in\mathcal{O}\), the series \(F(\alpha z)\) has the normal form with the data \((S,\operatorname{pr},\varpi,\lambda')\), where \(\lambda'_{e,j}=\alpha^{(p^e+1)p^j}\lambda_{e,j}\).
2. (*Change of \(\varpi\).*) If \(\varpi\ne 0\) and \(\varpi'\in\mathbb{C}_p\) has \(\lvert\varpi'\rvert=\lvert\varpi\rvert\), then there is a family \(\lambda''\) in \(\mathcal{O}\) such that \(F\) has the normal form with the data \((S,\operatorname{pr},\varpi',\lambda'')\).

## Proof

1. The series \(F(\alpha z)\) evaluated at \(\varpi z\) is \(F(\varpi Z)\) with \(Z_x=\alpha z_x\), integral without constant term. By [[proofs/grh/derivatives-divisibility/normal-form-substitution|substitution into the normal form]] it is an integral series times \(\exp(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda}(\alpha z))\), and \(\Xi_{S,\operatorname{pr},\lambda}(\alpha z)=\Xi_{S,\operatorname{pr},\lambda'}(z)\) by the scaling property of the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]].

2. Then \(\varpi'\neq0\), and \(\alpha=\varpi'/\varpi\), \(\beta=\varpi/\varpi'\) lie in \(\mathcal{O}\). By 1 there is an integral \(W\) with
\[
F(\varpi' z)=F(\alpha\cdot\varpi z)=W\cdot\exp\bigl(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda'}\bigr),\qquad \lambda'_{e,j}=\alpha^{(p^e+1)p^j}\lambda_{e,j}.
\]
Since \(c_\varpi=c_{\varpi'}\beta^{p+1}\) and the coupling sum is linear in its coefficients, \(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda'}=c_{\varpi'}\,\Xi_{S,\operatorname{pr},\lambda''}\) with \(\lambda''_{e,j}=\beta^{p+1}\lambda'_{e,j}\in\mathcal{O}\). \(\blacksquare\)

## References

1. Lean: `New.HasNormalForm.rescale`, `New.HasNormalForm.exists_of_norm_eq` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
