+++
id = "proofs/grh/upper-elementary-divisors/defect-weight-bounds"
title = "Bounds on the defect weights"
kind = "lemma"
summary = "The defect weight rises from X_s to Y_s by an amount in [0, 3/2], and the defect of a monomial of degree at most d in each letter is at most 2d in absolute value."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.defectWeight_sub_mem_Icc", "New.FrobeniusCycle.abs_weight_defectWeight_le", "New.FrobeniusCycle.sum_P_pow_le", "New.FrobeniusCycle.five_mul_P_pow_le_q"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\), and let \(\omega=\omega_{i,a,a'}\) be a [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect weight]].

1. If \(a\neq a'\), then \(0\le\omega(Y_s)-\omega(X_s)\le\tfrac32\) for every letter \(s\).
2. Let \(d\ge 0\) be real and let \(\alpha\) be an exponent on the variables \(x_{b,s}\) with \(\sum_b\alpha(b,s)\le d\) for every \(s\). Then \(\lvert\operatorname{def}_{i,a,a'}(\alpha)\rvert\le 2d\) (here \(a=a'\) is allowed).

## Proof

Let \(e(s)=N\) if \(s=i\) and \(e(s)=[s-i]\) otherwise, so that \(\omega(Y_s)=P^{e(s)}/(q-1)\) and \(\omega(X_s)=-P^{[s-i]}/(q-1)\). Since \(P\ge5\) and \([s-i]\le N-1\), we have \(5P^{[s-i]}\le P^{N}=q\), and \(q\ge 5\).

(1) \(\omega(Y_s)-\omega(X_s)=(P^{e(s)}+P^{[s-i]})/(q-1)\ge0\), and \(P^{e(s)}+P^{[s-i]}\le q+q/5\le\tfrac32(q-1)\) because \(q\ge5\).

(2) For every variable \(x=x_{b,s}\), \(\lvert\omega(x)\rvert\le P^{e(s)}/(q-1)\), since the numerator of \(\omega(x)\) is a difference of two numbers in \([0,P^{e(s)}]\) (note \([s-i]\le e(s)\)). Hence
\[
\lvert\operatorname{def}(\alpha)\rvert\le\sum_s\Bigl(\sum_b\alpha(b,s)\Bigr)\frac{P^{e(s)}}{q-1}\le \frac{d}{q-1}\sum_{s}P^{e(s)}.
\]
As \(s\) runs over the letters, \(e(s)\) runs over \(1,\dots,N\). With \(S=1+P+\dots+P^{N-1}\) the sum is both \(PS\) and \(S+(q-1)\); from \(5S\le PS=S+(q-1)\) we get \(S\le(q-1)/4\) and so \(\sum_sP^{e(s)}\le 2(q-1)\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.defectWeight_sub_mem_Icc`, `New.FrobeniusCycle.abs_weight_defectWeight_le`, `New.FrobeniusCycle.sum_P_pow_le`, `New.FrobeniusCycle.five_mul_P_pow_le_q` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.
