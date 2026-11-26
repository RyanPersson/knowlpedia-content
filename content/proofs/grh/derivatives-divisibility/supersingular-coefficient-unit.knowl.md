+++
id = "proofs/grh/derivatives-divisibility/supersingular-coefficient-unit"
title = "The coefficient of z^(p-1) in x at an inert prime"
kind = "proposition"
summary = "At a prime p inert in K, the coefficient of z^(p-1) in the Taylor series of x(z) = wp(z+t) - wp(t) is a p-adic unit."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.norm_coeff_taylorVia_translatedX_eq_one", "New.CMLattice.norm_coeff_pow_taylorVia_translatedX_recursion_lt_one", "New.CMLattice.norm_coeff_pow_taylorVia_translatedX_lt_one", "New.CMLattice.derivative_pow_mul_derivative_taylorVia_translatedX", "New.CMLattice.derivative_taylorVia_translatedX_sq", "New.CMLattice.derivative_derivative_taylorVia_translatedX", "New.CMLattice.coeff_two_mul_taylorVia_translatedX_pow"]
lean_files = ["src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean"]
proof_status = "full"
+++

**Proposition.** Let \(d\equiv 7\pmod 8\) be a prime, \(C\) a CM lattice for \(K=\mathbb{Q}(\sqrt{-d})\), and \(p\) a prime inert in \(K\) (\(\chi_K(p)=-1\)), with a \(p\)-adic place \(\iota_p\). Let \(x\in\mathbb{C}_p[[z]]\) be the Taylor series of \(\wp(z+t)-\wp(t)\) (notation of the [[proofs/grh/derivatives-divisibility/cm-curve-setting|CM lattice]]). Then the coefficient of \(z^{p-1}\) in \(x\) has norm \(1\).

## Proof

From \(x'=2y+a_1x\), \(y'=1+3x^2-a_1y\) and the curve equation \(y^2+a_1xy=x^3+x\) one gets
\[
x'^2=4x^3+a_1^2x^2+4x,\qquad x''=6x^2+a_1^2x+2,
\]
and therefore, for \(n\ge0\),
\[
(x^nx')'=nx^{n-1}x'^2+x^nx''=(4n+6)\,x^{n+2}+(n+1)a_1^2\,x^{n+1}+(4n+2)\,x^n .
\]
Let \(h_n\) be the coefficient of \(z^{p-1}\) in \(x^n\). The coefficient of \(z^{p-1}\) in \((x^nx')'\) is \(p\) times the coefficient of \(z^p\) in \(x^nx'\). The latter series lies in \(\mathcal{O}[[y]]\) (facts 1 of the setting) and \(p<p^2=q_p\), so that coefficient is integral (fact 2). Hence
\[
\bigl\lvert(4n+6)h_{n+2}+(n+1)a_1^2h_{n+1}+(4n+2)h_n\bigr\rvert\le p^{-1}<1 .\tag{*}
\]
The prime \(p\) is odd; write \(p=2m+1\). By fact 2, \(\lvert h_1\rvert\le 1\). Suppose \(\lvert h_1\rvert<1\). We show \(\lvert h_n\rvert<1\) for all \(n\le m\) by induction: \(h_0=0\) since \(p-1>0\); and if \(n+2\le m\), then \(4n+6=2(2n+3)\) with \(0<2n+3<p\) is a unit, \(\lvert a_1\rvert\le 1\), so \((*)\) and the ultrametric inequality give \(\lvert h_{n+2}\rvert<1\) from \(\lvert h_{n+1}\rvert,\lvert h_n\rvert<1\). But \(x=z^2+\cdots\), so \(h_m\), the coefficient of \(z^{2m}\) in \(x^m\), equals \(1\): a contradiction. Thus \(\lvert h_1\rvert=1\). \(\blacksquare\)

## Remarks

This is independent of the [[proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta|Frobenius congruence]]. It is used to show that the number \(\lambda\) in the [[proofs/grh/derivatives-divisibility/exponent-on-one-curve|exponent on one curve]] is a unit.

## References

1. Lean: `New.CMLattice.norm_coeff_taylorVia_translatedX_eq_one` in `src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean`.
