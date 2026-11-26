+++
id = "proofs/grh/upper-divisibility/allowed-loss"
title = "Allowed loss at a prime and its total"
kind = "proposition"
summary = "The allowed loss is twice the loss at small non-split primes and 2mfb at N; weighted by log p it sums to at most the error unit."
aliases = ["allowed loss"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.allowedLoss", "New.Data.sum_allowedLoss_mul_log_le", "New.Data.exists_mul_sub_one_eq_or_mul_add_one_eq", "New.Data.allowedLoss_nonneg"]
lean_files = ["src/New/UpperBound/Size/Estimates.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. The **allowed loss** at a natural number \(p\) is
\[
\operatorname{al}(p)=\begin{cases}2\operatorname{loss}(p)&p\text{ prime},\ p<x_1,\ \chi_K(p)\ne1\\ 2mfb&\text{otherwise, if }p=N\\ 0&\text{otherwise,}\end{cases}
\]
where \(\operatorname{loss}(p)=f(\log b)^2\,\dfrac ap\,\varepsilon_p\) is the [[proofs/grh/upper-divisibility/classes-of-primes|loss]] (\(\varepsilon_p=m\) if \(p\equiv\pm1\bmod m\), else \(1\)).

**Proposition.** \(\operatorname{al}(p)\ge0\), and for every finite set \(U\) of natural numbers
\[
\sum_{p\in U}\operatorname{al}(p)\log p\;\le\;f\,a\,(\log b)^{3}=\mathrm{err},
\]
the [[?lean:New.Data.errorUnit|error unit]].

## Proof

Put \(T=4fa(\log b)^2\log x_1\). We show that each term is at most \(T/c\) for some integer \(1\le c\le x_1\), in such a way that each \(c\) is used by at most four values of \(p\), namely \(N\), \(mc-1\), \(c\), \(mc+1\).

*A non-split prime \(p<x_1\), \(p\not\equiv\pm1\bmod m\).* Take \(c=p\): \(2\operatorname{loss}(p)\log p\le 2f(\log b)^2(a/p)\log x_1\le T/p\).

*A non-split prime \(p<x_1\), \(p\equiv\pm1\bmod m\).* Then \(p=mc\mp1\) with \(1\le c\le p\) and \(mc\le p+1\le2p\), so \(m\le2p/c\) and \(2\operatorname{loss}(p)\log p\le2f(\log b)^2\,\dfrac ap\cdot\dfrac{2p}{c}\log x_1=T/c\).

*\(p=N\) (not a small non-split prime).* \(2mfb\log N\le T\) is a size comparison of the data (quoted); take \(c=1\).

Summing, and using \(\sum_{c\le x_1}1/c\le1+\log x_1\),
\[
\sum_{p\in U}\operatorname{al}(p)\log p\le4T\sum_{1\le c\le x_1}\frac1c\le4T(1+\log x_1)\le\mathrm{err},
\]
the last step being the comparison \(16fa(\log b)^2\log x_1(1+\log x_1)\le fa(\log b)^3\), which holds since \((\log x_1)^6\le\log b\) (quoted from [[?lean:New.Data.le_of_hasLogBound|`le_of_hasLogBound`]] with [[?lean:New.Data.scale_inequalities|the scale inequalities]]). \(\blacksquare\)

## References

1. Lean: `New.Data.allowedLoss`, `New.Data.sum_allowedLoss_mul_log_le` in `src/New/UpperBound/Size/Estimates.lean`.
