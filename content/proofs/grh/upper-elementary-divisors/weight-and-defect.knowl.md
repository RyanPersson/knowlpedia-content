+++
id = "proofs/grh/upper-elementary-divisors/weight-and-defect"
title = "Weight of a monomial in the copies against the defect of a row"
kind = "theorem"
summary = "In the substitution operator at the conjugated Frobenius factors, a monomial whose coefficient in row beta is not divisible by w^c has copy weight within 3kc of the defect of beta."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.abs_defect_sub_copyWeight_le", "New.FrobeniusCycle.substitutionOperator_conj_mem_gaussFiltration", "New.FrobeniusCycle.mul_defectWeight_eq_indexWeight_mul", "New.FrobeniusCycle.abs_defect_sub_mul_le_one", "New.FrobeniusCycle.abs_scaledIndexWeight_sub_scaledIndexWeight_sub_entryWeight_le"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
proof_status = "full"
+++

**Theorem.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\). Let \(a,a'\) be indices below \(k\) with \(a'=a+1\), let \(\ell,n\ge0\) with \(\ell\le N\) and \(N\,n\,k\,(\ell+2)\le P^{\ell}\), let \(h\in\mathrm{GL}_k(W)\) and \(i\in\mathbb{Z}/N\). Let \(\mathcal{S}=\mathcal{S}(a',\ell,n;\Psi^{h})\) be the [[proofs/grh/upper-elementary-divisors/substitution-operator|substitution operator]] with cut \(r=a'\) at the conjugated Frobenius factors. If \(c\in\mathbb{N}\) and the coefficient of \(X^{\nu}\) in the entry \(\mathcal{S}_{\beta,\gamma}\) is not divisible by \(w^{c}\), then
\[
\bigl\lvert\operatorname{def}_{i+\ell,a,a'}(\beta)-\operatorname{cw}_i(\nu)\bigr\rvert\le c^{*}=3kc,
\]
where \(\operatorname{def}\) is the [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]] and \(\operatorname{cw}_i\) the [[proofs/grh/upper-elementary-divisors/copy-weight|copy weight]].

## Proof

*Levels.* Let \(\lvert\varepsilon\rvert\le\tfrac12\), \(\omega=\varepsilon\,\epsilon_i\) (entry weights), \(u=\tfrac12P^{-\ell}\). Then \(\lvert\omega\rvert\le P^{-\ell}\le P^{-d}\) for \(d\le\ell\), so by [[proofs/grh/upper-elementary-divisors/conjugated-frobenius-factors-level|the level of the factors]], \((\Psi^{h}_{s,d})_{b,c}\) has Gauss level \(P^{d}\omega(X_{s-d,b,c})\). Define potentials \(\alpha_{s,d}(b)=\varepsilon\,\varsigma_{d+[s-d-i]}(b)\); they sum to \(0\) over \(b\) and \(\lvert\alpha_{s,0}\rvert\le u\). For \(d\le N\),
\[
\bigl\lvert\varsigma_{d+1+[s-d-1-i]}(b)-\varsigma_{d+[s-d-i]}(c)-P^{d}\epsilon_i(X_{s-d,b,c})\bigr\rvert\le P^{-\ell}:
\]
indeed \(\varsigma_{d+m}=P^{d}\varsigma_m\) and \(1+[s-d-1-i]\) equals \([s-d-i]\) if \(s-d\ne i\) and \(N\) if \(s-d=i\); in the first case the difference is exactly \(P^{d}\epsilon_i\), in the second \(P^{d}\varsigma_N(b)=P^{d}\epsilon_i(X_{i,b,c})\) and only \(\varsigma_{d}(c)\), of size \(\le P^{-\ell}\), is left. Hence \(\alpha_{s,d+1}(b)-\alpha_{s,d}(c)-u\le P^{d}\omega(X_{s-d,b,c})\) for \(d\le\ell\). The last potentials are, for both parities,
\[
\pm\alpha_{s,\ell+\delta_{a'}(b,s)}(b)=\varepsilon\bigl(1-\tfrac1q\bigr)\,\omega_{i+\ell,a,a'}(x_{b,s}),
\]
a case check on \(b\in\{a,a'\}\) and the parity of \(s\) (exactly one of \(x_{a,s},x_{a',s}\) is deep for the cut \(a'\), which produces the two exponents in the defect weight; e.g. for even \(s\) and \(b=a'\): \(\varsigma_{\ell+1+[s-1-(i+\ell)]}(a')=P^{1+[s-1-(i+\ell)]}/q\)). By [[proofs/grh/upper-elementary-divisors/levels-of-substitution-operator|the level lemma]], \(\mathcal{S}_{\beta,\gamma}\) lies in the Gauss level \(\varepsilon E-L\) for \((F^{w},\varepsilon\epsilon_i)\), where \(E=(1-\tfrac1q)\Delta\), \(\Delta=\operatorname{def}_{i+\ell,a,a'}(\beta)\), \(L=Nnk(\ell+2)/(2P^{\ell})\le\tfrac12\).

*Conclusion.* With \(D=\operatorname{cw}_i(\nu)\), the coefficient at \(\nu\) is divisible by \(w^{\lceil\varepsilon(E-D)-L\rceil_+}\); as it is not divisible by \(w^{c}\), \(\varepsilon(E-D)\le c+\tfrac12\). Taking \(\varepsilon=\pm\tfrac12\): \(\lvert E-D\rvert\le2c+1\). Since \(2n\le Nnk(\ell+2)\le P^{\ell}\le q\), the [[proofs/grh/upper-elementary-divisors/defect-weight-bounds|bound]] \(\lvert\Delta\rvert\le2n\) gives \(\lvert\Delta-E\rvert=\lvert\Delta\rvert/q\le1\). So \(\lvert\Delta-D\rvert\le2c+2\le3kc\), because \(k\ge2\) (\(a<a'<k\)) and \(c\ge1\) (\(w^{0}\) divides everything). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.abs_defect_sub_copyWeight_le`, `New.FrobeniusCycle.substitutionOperator_conj_mem_gaussFiltration`, `New.FrobeniusCycle.mul_defectWeight_eq_indexWeight_mul`, `New.FrobeniusCycle.abs_defect_sub_mul_le_one`, `New.FrobeniusCycle.abs_scaledIndexWeight_sub_scaledIndexWeight_sub_entryWeight_le` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.
