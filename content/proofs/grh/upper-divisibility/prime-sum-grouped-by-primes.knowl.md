+++
id = "proofs/grh/upper-divisibility/prime-sum-grouped-by-primes"
title = "The von Mangoldt sum grouped prime by prime"
kind = "proposition"
summary = "For orders at most a, the prime sum is the sum over primes below x_1 of 2 log p times the local prime sum; the gain vanishes at split primes and at primes at least x_1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.primeSum_eq_sum_localPrimeSum", "New.Data.localPrimeSum_eq_tsum", "New.Data.localPrimeSum_eq_zero", "New.Data.gain_eq_zero", "New.Data.sum_localPrimeSumTotal_mul_log_le", "New.Data.localPrimeSumTotal_nonneg", "New.Data.posPart_div_sub_weight_eq_zero", "New.Data.smallNonsplitPrimes"]
lean_files = ["src/New/UpperBound/Size/Estimates.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\Phi\) the group of infinite places of \(E\), \(w\) the [[?lean:New.Data.weight|weight]], \(u(\nu)\) the place named by an integer \(\nu\), \(\chi_K\) the Legendre symbol modulo \(d\), \(\Lambda\) the [[?c:Von Mangoldt function|von Mangoldt function]], and
\[
S(y,\sigma)=\sum_{1\le\nu\le a}\Lambda(\nu)\bigl(1-\chi_K(\nu)\bigr)\Bigl(\frac y\nu-w\bigl(u(-\nu)\sigma\bigr)\Bigr)^{+}
\]
the [[?lean:New.Data.primeSum|prime sum]]. Let \(s_p\), \(F(p)\) be the [[proofs/grh/upper-divisibility/local-prime-sum|local prime sum]] and its total.

**Proposition.**

1. For a prime \(p\): \(s_p(y,\sigma)=\sum_{e\ge1}\tfrac12\bigl(1-\chi_K(p^{e})\bigr)\bigl(y/p^{e}-w(u(-p^{e})\sigma)\bigr)^{+}\).
2. If \(y\le a\) and \(t\ge x_1\) then \((y/t-w(\tau))^{+}=0\) for every \(\tau\). Hence \(s_p(y,\sigma)=0\) for natural \(p\ge x_1\) and \(y\le a\).
3. The [[proofs/grh/upper-divisibility/gain|gain]] at \(p\) is \(0\) if \(\chi_K(p)=1\) or \(p\ge x_1\).
4. For \(y\le a\), \(\sigma\in\Phi\) and every natural number \(U\ge\lceil x_1\rceil\):
\[
S(y,\sigma)=\sum_{p<U,\ p\ \mathrm{prime}}2\,s_p(y,\sigma)\log p .
\]
5. \(F(p)\ge0\), and for every finite set \(T\) of primes, \(\displaystyle\sum_{p\in T}2F(p)\log p\le\sum_{\tau\in\Phi}S\bigl(w(\tau),\tau\bigr)\).

## Proof

(1) By definition \(s_p=v(\pi_p)\sum_{e\in I_p}(\cdots)^{+}\). For a prime \(p\) one has \(\tfrac12(1-\chi_K(p^{e}))=v(\pi_p)\) if \(e\in I_p\) and \(0\) otherwise, for \(e\ge1\): if \(p=d\) then \(\chi_K(p^e)=0\) and \(v(\pi_p)=\tfrac12\); if \(\chi_K(p)=-1\) then \(\chi_K(p^{e})=(-1)^{e}\), giving \(1\) for odd \(e\) and \(0\) for even \(e\); if \(\chi_K(p)=1\) the factor is \(0\) and \(I_p=\emptyset\) (Lean: [[?lean:New.one_sub_chiK_pow_div_two|`one_sub_chiK_pow_div_two`]]).

(2) Every weight is at least \(a/x_1\), so \(y/t\le a/x_1\le w(\tau)\). For \(p\ge x_1\) (in particular \(p\ge1\)) and \(e\ge1\) we have \(p^{e}\ge x_1\).

(3) If \(\chi_K(p)=1\) then \(I_p=\emptyset\); if \(p\ge x_1\) use (2) with \(y=a\) and with \(y=w(\sigma)\le a\).

(4) Let \(G(\nu)\) be the summand. \(G\) is supported on prime powers (as \(\Lambda\) is), vanishes for \(\nu\ge x_1\) by (2), and \(\lceil x_1\rceil\le a\); so \(S(y,\sigma)=\sum_{\nu\ge1}G(\nu)=\sum_p\sum_{e\ge1}G(p^{e})\), and only primes \(p<U\) contribute. Since \(\Lambda(p^{e})=\log p\), (1) gives \(\sum_{e\ge1}G(p^{e})=2s_p(y,\sigma)\log p\).

(5) Nonnegativity is clear from the definition. Choose \(U\) larger than \(x_1\) and than all elements of \(T\); by nonnegativity the sum over \(T\) is at most the sum over all primes below \(U\), which by (4) with \(y=w(\tau)\le a\), summed over \(\tau\), equals the right-hand side. \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Size/Estimates.lean`.
