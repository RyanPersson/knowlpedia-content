+++
id = "proofs/grh/upper-divisibility/local-prime-sum"
title = "Local prime sum"
kind = "definition"
summary = "The exponent of a prime p asked of a derivative of order y at an infinite place: a sum of positive parts over the partner exponents of p."
aliases = ["local prime sum", "prime sum at p", "total local prime sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.localPrimeSum", "New.Data.localPrimeSumTotal"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] for the parameters \((q_0,d)\), let \(\Phi\cong(\mathbb{Z}/q_1)^\times\) be the group of [[?c:Infinite place of a number field|infinite places]] of \(E=K(\zeta)\), let \(w\colon\Phi\to\mathbb{R}\) be the [[?lean:New.Data.weight|weight]] (\(w=b\) on the b-places and \(w=a/x_1\) elsewhere), and for an integer \(\nu\) let \(u(\nu)\in\Phi\) be the [[?lean:New.Data.placeOfInt|place named by \(\nu\)]] (the class of \(\nu\) if \(\nu\) is prime to \(q_1\), the identity otherwise). For a natural number \(p\), a real number \(y\) and \(\sigma\in\Phi\), the **local prime sum** is
\[
s_p(y,\sigma)\;=\;v(\pi_p)\sum_{e\in I_p}\Bigl(\frac{y}{p^{e}}-w\bigl(u(-p^{e})\,\sigma\bigr)\Bigr)^{+},
\]
where \(t^{+}=\max(t,0)\), where \(v(\pi_p)\) is the [[?lean:New.piPrimeValuation|valuation of the prime element]] (\(\tfrac12\) if \(p=d\), and \(1\) otherwise), and where \(I_p\) is the set of [[?lean:New.positivePartnerExponents|positive partner exponents]] of \(p\): all \(e\ge 1\) if \(p=d\); the odd \(e\ge1\) if \(\chi_K(p)=-1\); and no \(e\) otherwise. Here \(\chi_K\) is the [[?lean:New.chiK|quadratic character]] of \(K=\mathbb{Q}(\sqrt{-d})\).

The **total local prime sum** is
\[
F(p)\;=\;\sum_{\sigma\in\Phi}s_p\bigl(w(\sigma),\sigma\bigr).
\]

## Remarks

The sum over \(e\) is a sum of nonnegative terms that vanish as soon as \(p^{e}>y/\min w\) (for \(p\ge2\)), so it is finite. For a prime \(p\) that splits in \(K\) the set \(I_p\) is empty and \(s_p=0\). For \(y\le a\), the sum of \(2\log p\cdot s_p(y,\sigma)\) over the primes \(p\) (only primes below \(x_1\) contribute) is the [[?lean:New.Data.primeSum|prime sum]] at the order \(y\) and the place \(\sigma\); see [[proofs/grh/upper-divisibility/prime-sum-grouped-by-primes|the prime sum grouped by primes]]. The hypothesis \(y\le a\) is needed: the prime sum stops at \(\nu=a\), while the local sums run over all prime powers.

## References

1. Lean: `New.Data.localPrimeSum`, `New.Data.localPrimeSumTotal` in `src/New/UpperBound/Size/ShortColumns.lean`.
