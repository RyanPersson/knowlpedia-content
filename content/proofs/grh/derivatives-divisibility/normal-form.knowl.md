+++
id = "proofs/grh/derivatives-divisibility/normal-form"
title = "Normal form of a power series"
kind = "definition"
summary = "A series F has the normal form if F(varpi z) is an integral series times the exponential of varpi^(p+1)/p times a coupling sum."
aliases = ["normal form", "has the normal form"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasNormalForm"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
+++

**Definition (normal form).** Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\), \(\Phi\) and \(c\) finite sets, \(\operatorname{pr}\) a partner rule on \(\Phi\), \(S\subseteq\mathbb{N}\), \(\varpi\in\mathbb{C}_p\) and \(\lambda=(\lambda_{e,j})\) a family in \(\mathcal{O}\). A power series \(F\in\mathbb{C}_p[[z_x:x\in\Phi\times c]]\) **has the normal form** with the data \((S,\operatorname{pr},\varpi,\lambda)\) if there is an integral series \(W\in\mathcal{O}[[z]]\) with
\[
F(\varpi z)=W(z)\cdot\exp\bigl(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda}(z)\bigr),\qquad c_\varpi=\frac{\varpi^{p+1}}{p},
\]
where \(F(\varpi z)\) is \(F\) with every variable multiplied by \(\varpi\), \(\Xi_{S,\operatorname{pr},\lambda}=\sum_{e\in S}\sum_{j\ge0}\lambda_{e,j}\Gamma_e^{p^j}\) is the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]], and \(\exp\) is the exponential of a series without constant term (see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]).

## Remarks

The exponential factor is in general not integral: \(c_\varpi\) has valuation \((p+1)v(\varpi)-1\), which is negative for the \(\varpi\) of valuation \(\rho_p\) used in the application. The normal form isolates this single obstruction to the integrality of \(F(\varpi z)\). It is established for products of theta functions in [[proofs/grh/derivatives-divisibility/normal-form-of-theta-products|the normal form of theta products]] and exploited in [[proofs/grh/derivatives-divisibility/the-count|the count]].

## References

1. Lean: `New.HasNormalForm` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
