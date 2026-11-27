+++
id = "proofs/grh/derivatives-divisibility/normal-form-modulo-pi"
title = "The exponent of a normal form need only be known modulo pi"
kind = "lemma"
summary = "If F(varpi z) = W exp(c Xi) with W, Xi integral and Xi congruent to a coupling sum modulo a pi with |c pi| at most p^(-1/(p-1)), then F has the normal form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasNormalForm.of_dvd_sub", "New.norm_coeff_expSubst_smul_le_one"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
proof_status = "full"
+++

**Lemma.** In the notation of the [[proofs/grh/derivatives-divisibility/normal-form|normal form]], let \(\pi\in\mathcal{O}\) satisfy \(\lvert c_\varpi\pi\rvert\le p^{-1/(p-1)}\), where \(c_\varpi=\varpi^{p+1}/p\). Let \(W,\Xi\in\mathcal{O}[\![z]\!]\) with \(\Xi(0)=0\),
\[
\Xi\equiv\Xi_{S,\operatorname{pr},\lambda}\pmod{\pi}\qquad\text{and}\qquad F(\varpi z)=W\cdot\exp(c_\varpi\,\Xi).
\]
Then \(F\) has the normal form with the data \((S,\operatorname{pr},\varpi,\lambda)\).

The proof rests on the following bound.

**Lemma (exponential of a divisible series).** Let \(a\in\mathbb{C}_p\) and \(\pi\in\mathcal{O}\) with \(\lvert a\pi\rvert\le p^{-1/(p-1)}\), let \(G\) be an integral series without constant term, in any variables, and let \(B\ge 0\). If \(\pi\) divides the coefficients of \(G\) in all degrees \(\le B\), then the coefficients of \(\exp(aG)\) in the degrees \(\le B\) have norm at most \(1\).

## Proof

*Exponential of a divisible series.* In the degrees \(\le B\) the coefficients of \(aG\) have norm at most \(\lvert a\rvert\lvert\pi\rvert\le p^{-1/(p-1)}\). The claim is then [[?lean:New.norm_coeff_expSubst_le_one|the integrality of the exponential in low degrees]]: if \(h(0)=0\) and the coefficients of \(h\) in the degrees \(\le B\) have valuation at least \(1/(p-1)\), then \(\exp(h)=\sum_j h^j/j!\) is integral in these degrees, by the bound \(v(j!)\le j/(p-1)\) from [[?c:Legendre's formula|Legendre's formula]].

*The lemma.* Put \(G=\Xi-\Xi_{S,\operatorname{pr},\lambda}\). It is integral, has no constant term (neither \(\Xi\) nor the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]] has one), and \(\pi\) divides all its coefficients. By the bound, applied in every degree, \(V=\exp(c_\varpi G)\) is an integral series. Since \(\exp(g+h)=\exp(g)\exp(h)\) for series without constant term,
\[
\exp(c_\varpi\Xi)=V\cdot\exp(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda}),\qquad\text{so}\qquad F(\varpi z)=(WV)\cdot\exp(c_\varpi\,\Xi_{S,\operatorname{pr},\lambda})
\]
with \(WV\) integral. \(\blacksquare\)

## References

1. Lean: `New.HasNormalForm.of_dvd_sub`, `New.norm_coeff_expSubst_smul_le_one` in `src/New/Derivatives/Divisibility/NormalForm.lean`; `New.norm_coeff_expSubst_le_one` in `src/Lib/General/Algebra/SeriesBounds.lean`.
